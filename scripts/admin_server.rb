#!/usr/bin/env ruby
# frozen_string_literal: true

require 'cgi'
require 'date'
require 'fileutils'
require 'json'
require 'time'
require 'webrick'
require 'yaml'

ROOT = File.expand_path('..', __dir__)
DATA_FILES = {
  'news' => File.join(ROOT, '_data', 'news.yml'),
  'member' => File.join(ROOT, '_data', 'members.yml'),
  'research_image' => File.join(ROOT, '_data', 'research.yml')
}.freeze

def load_yaml_array(path)
  return [] unless File.exist?(path)

  YAML.safe_load_file(path, permitted_classes: [Date, Time], aliases: true) || []
rescue Psych::SyntaxError => e
  raise "Could not parse #{path}: #{e.message}"
end

def write_yaml_draft(path, data)
  draft_path = "#{path}.draft"
  yaml = YAML.dump(data)
  File.write(draft_path, yaml, encoding: 'UTF-8')
  draft_path
end

def clean(value)
  value.to_s.strip
end

def present_hash(hash)
  hash.reject { |_key, value| value.nil? || value == '' || value == [] }
end

def line_list(value)
  clean(value).split(/\r?\n/).map(&:strip).reject(&:empty?)
end

def link_list(value)
  line_list(value).filter_map do |line|
    label, url = line.split('|', 2).map { |part| clean(part) }
    next if label.empty? || url.empty?

    { 'label' => label, 'url' => url }
  end
end

def build_news(data)
  present_hash(
    'date' => clean(data['date']),
    'title' => clean(data['title']),
    'summary' => clean(data['summary']),
    'note' => clean(data['note']),
    'image' => clean(data['image']),
    'image_alt' => clean(data['image_alt']),
    'url' => clean(data['url']),
    'links' => link_list(data['links'])
  )
end

def build_member(data)
  present_hash(
    'name' => clean(data['name']),
    'aliases' => line_list(data['aliases']),
    'role_group' => clean(data['role_group']),
    'position' => clean(data['position']),
    'affiliation' => clean(data['affiliation']),
    'email' => clean(data['email']),
    'research' => clean(data['research']),
    'bio' => clean(data['bio']),
    'image_url' => clean(data['image_url']),
    'achievements' => line_list(data['achievements'])
  )
end

def build_research_image(data)
  present_hash(
    'title' => clean(data['title']),
    'image' => clean(data['image']),
    'image_alt' => clean(data['image_alt'])
  )
end

def apply_entry(type, data)
  path = DATA_FILES.fetch(type)
  collection = load_yaml_array(path)

  case type
  when 'news'
    entry = build_news(data)
    raise 'News title is required.' if entry['title'].to_s.empty?
    raise 'News date is required.' if entry['date'].to_s.empty?

    collection.unshift(entry)
  when 'member'
    entry = build_member(data)
    raise 'Member name is required.' if entry['name'].to_s.empty?
    raise 'Member role group is required.' if entry['role_group'].to_s.empty?

    collection << entry
  when 'research_image'
    entry = build_research_image(data)
    raise 'Research title is required.' if entry['title'].to_s.empty?
    raise 'Image path is required.' if entry['image'].to_s.empty?

    existing = collection.find { |item| item['title'].to_s.casecmp(entry['title']).zero? }
    if existing
      existing['image'] = entry['image']
      existing['image_alt'] = entry['image_alt'] unless entry['image_alt'].to_s.empty?
    else
      collection << {
        'title' => entry['title'],
        'summary' => '',
        'one_liner' => '',
        'why_it_matters' => '',
        'image' => entry['image']
      }
    end
  else
    raise 'Unknown draft type.'
  end

  draft_path = write_yaml_draft(path, collection)
  { type: type, draft_path: draft_path.sub("#{ROOT}/", '').sub("#{ROOT}\\", '') }
end

def json_response(response, status, payload)
  response.status = status
  response['Content-Type'] = 'application/json; charset=utf-8'
  response.body = JSON.pretty_generate(payload)
end

def admin_html
  today = Date.today.iso8601
  <<~HTML
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>MS3L Local Admin</title>
        <style>
          :root {
            --ink: #102a43;
            --muted: #52677a;
            --line: #c8d7e6;
            --blue: #0050a4;
            --cyan: #0096d6;
            --green: #009e73;
            --bg: #eef4f9;
            --surface: #ffffff;
          }
          * { box-sizing: border-box; }
          body {
            margin: 0;
            font-family: Inter, "Noto Sans KR", Arial, sans-serif;
            color: var(--ink);
            background: var(--bg);
          }
          main {
            width: min(1080px, calc(100% - 40px));
            margin: 0 auto;
            padding: 40px 0 64px;
          }
          header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
            padding: 24px 0;
          }
          h1, h2, p { margin-top: 0; }
          h1 { font-size: 2rem; letter-spacing: 0; }
          p { color: var(--muted); }
          .actions {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 16px;
          }
          .admin-card {
            border: 1px solid var(--line);
            border-radius: 8px;
            background: var(--surface);
            padding: 22px;
            box-shadow: 0 14px 32px rgba(16, 42, 67, 0.08);
          }
          button {
            min-height: 44px;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 10px 14px;
            background: #fff;
            color: var(--ink);
            font: inherit;
            font-weight: 700;
            cursor: pointer;
          }
          .primary {
            color: #fff;
            border-color: var(--blue);
            background: linear-gradient(135deg, var(--blue), var(--cyan));
          }
          .result {
            margin-top: 22px;
            border-left: 4px solid var(--green);
            background: #fff;
            padding: 16px;
            white-space: pre-wrap;
          }
          dialog {
            width: min(720px, calc(100% - 32px));
            border: 1px solid var(--line);
            border-radius: 10px;
            padding: 0;
            box-shadow: 0 24px 72px rgba(16, 42, 67, 0.24);
          }
          dialog::backdrop { background: rgba(16, 42, 67, 0.42); }
          form {
            display: grid;
            gap: 14px;
            padding: 24px;
          }
          label {
            display: grid;
            gap: 6px;
            font-weight: 700;
          }
          input, textarea, select {
            width: 100%;
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 10px 12px;
            font: inherit;
            color: var(--ink);
            background: #fff;
          }
          textarea { min-height: 92px; resize: vertical; }
          .form-grid {
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
          }
          .dialog-head, .dialog-actions {
            display: flex;
            justify-content: space-between;
            gap: 12px;
            align-items: center;
          }
          .dialog-actions { margin-top: 4px; }
          .muted { color: var(--muted); font-size: 0.92rem; }
          [hidden] { display: none !important; }
          @media (max-width: 760px) {
            header, .dialog-head, .dialog-actions { align-items: stretch; flex-direction: column; }
            .actions, .form-grid { grid-template-columns: 1fr; }
          }
        </style>
      </head>
      <body>
        <main>
          <header>
            <div>
              <h1>MS3L Local Admin</h1>
              <p>Create reviewed YAML drafts for lab website updates.</p>
            </div>
            <button class="primary" type="button" data-open="news">Add News</button>
          </header>

          <section class="actions">
            <article class="admin-card">
              <h2>Add News</h2>
              <p>Prepare a new item for <code>_data/news.yml.draft</code>.</p>
              <button type="button" data-open="news">Add News</button>
            </article>
            <article class="admin-card">
              <h2>Add Member</h2>
              <p>Prepare a new profile for <code>_data/members.yml.draft</code>.</p>
              <button type="button" data-open="member">Add Member</button>
            </article>
            <article class="admin-card">
              <h2>Add Research Image</h2>
              <p>Prepare an image-path update for <code>_data/research.yml.draft</code>.</p>
              <button type="button" data-open="research_image">Add Research Image</button>
            </article>
          </section>

          <pre class="result" id="result" hidden></pre>
        </main>

        <dialog id="draft-dialog">
          <form id="draft-form">
            <div class="dialog-head">
              <div>
                <h2 id="dialog-title">Create Draft</h2>
                <p class="muted">Drafts are written next to the source YAML file and are not applied automatically.</p>
              </div>
              <button type="button" data-close>Close</button>
            </div>
            <input type="hidden" name="type" id="draft-type">

            <div data-fields="news">
              <div class="form-grid">
                <label>Title <input name="title" required></label>
                <label>Date <input name="date" type="date" value="#{today}" required></label>
              </div>
              <label>Summary <textarea name="summary"></textarea></label>
              <label>Note <textarea name="note"></textarea></label>
              <div class="form-grid">
                <label>Image path <input name="image" placeholder="/assets/images/news/example.jpg"></label>
                <label>Image alt <input name="image_alt"></label>
              </div>
              <label>Primary URL <input name="url" type="url"></label>
              <label>Related links <textarea name="links" placeholder="KBS|https://example.com"></textarea></label>
            </div>

            <div data-fields="member" hidden>
              <div class="form-grid">
                <label>Name <input name="name" required></label>
                <label>Role group <input name="role_group" placeholder="Master Student" required></label>
              </div>
              <label>Position <input name="position"></label>
              <label>Affiliation <input name="affiliation"></label>
              <div class="form-grid">
                <label>Email <input name="email" type="email"></label>
                <label>Image path <input name="image_url" placeholder="/assets/images/members/name.jpg"></label>
              </div>
              <label>Research <textarea name="research"></textarea></label>
              <label>Bio <textarea name="bio"></textarea></label>
              <label>Aliases <textarea name="aliases"></textarea></label>
              <label>Achievements <textarea name="achievements"></textarea></label>
            </div>

            <div data-fields="research_image" hidden>
              <label>Research title <input name="title" placeholder="Biorefinery" required></label>
              <label>Image path <input name="image" placeholder="/assets/images/research/biorefinery.jpg" required></label>
              <label>Image alt <input name="image_alt"></label>
            </div>

            <div class="dialog-actions">
              <button class="primary" type="submit">Create Draft</button>
              <button type="button" data-close>Cancel</button>
            </div>
          </form>
        </dialog>

        <script>
          const dialog = document.querySelector('#draft-dialog');
          const form = document.querySelector('#draft-form');
          const result = document.querySelector('#result');
          const draftType = document.querySelector('#draft-type');
          const title = document.querySelector('#dialog-title');
          const labels = {
            news: 'Add News',
            member: 'Add Member',
            research_image: 'Add Research Image'
          };

          function setType(type) {
            draftType.value = type;
            title.textContent = labels[type];
            document.querySelectorAll('[data-fields]').forEach((section) => {
              section.hidden = section.dataset.fields !== type;
              section.querySelectorAll('input, textarea, select').forEach((input) => {
                input.disabled = section.hidden;
              });
            });
          }

          document.querySelectorAll('[data-open]').forEach((button) => {
            button.addEventListener('click', () => {
              form.reset();
              setType(button.dataset.open);
              dialog.showModal();
            });
          });

          document.querySelectorAll('[data-close]').forEach((button) => {
            button.addEventListener('click', () => dialog.close());
          });

          form.addEventListener('submit', async (event) => {
            event.preventDefault();
            const formData = new FormData(form);
            const payload = { type: draftType.value, data: Object.fromEntries(formData.entries()) };
            const response = await fetch('/draft', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(payload)
            });
            const body = await response.json();
            result.hidden = false;
            result.textContent = JSON.stringify(body, null, 2);
            if (response.ok) dialog.close();
          });

          setType('news');
        </script>
      </body>
    </html>
  HTML
end

port = Integer(ENV.fetch('MS3L_ADMIN_PORT', '4567'))
server = WEBrick::HTTPServer.new(Port: port, DocumentRoot: ROOT, AccessLog: [])

server.mount_proc('/') do |_request, response|
  response['Content-Type'] = 'text/html; charset=utf-8'
  response.body = admin_html
end

server.mount_proc('/draft') do |request, response|
  unless request.request_method == 'POST'
    json_response(response, 405, error: 'POST required')
    next
  end

  begin
    payload = JSON.parse(request.body.to_s)
    result = apply_entry(payload.fetch('type'), payload.fetch('data'))
    json_response(response, 200, ok: true, **result)
  rescue StandardError => e
    json_response(response, 422, ok: false, error: e.message)
  end
end

trap('INT') { server.shutdown }

puts "MS3L local admin running at http://localhost:#{port}/"
server.start
