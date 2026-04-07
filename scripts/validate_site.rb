#!/usr/bin/env ruby
require 'yaml'
require 'uri'
require 'date'

ROOT = File.expand_path('..', __dir__)

DATA_FILES = {
  lab: File.join(ROOT, '_data', 'lab.yml'),
  members: File.join(ROOT, '_data', 'members.yml'),
  research: File.join(ROOT, '_data', 'research.yml'),
  publications: File.join(ROOT, '_data', 'publications.yml'),
  news: File.join(ROOT, '_data', 'news.yml'),
  patents: File.join(ROOT, '_data', 'patents.yml')
}.freeze

errors = []

def valid_url?(value)
  return true if value.nil? || value.to_s.strip.empty?
  uri = URI.parse(value)
  uri.is_a?(URI::HTTP) || uri.is_a?(URI::HTTPS)
rescue URI::InvalidURIError
  false
end

def valid_doi?(value)
  return true if value.nil? || value.to_s.strip.empty?
  value.to_s.match?(%r{^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$})
end

loaded = {}
DATA_FILES.each do |name, path|
  unless File.exist?(path)
    errors << "Missing file: #{path}"
    next
  end
  loaded[name] = YAML.safe_load_file(path, permitted_classes: [Date], aliases: true)
end

Array(loaded[:members]).each_with_index do |m, i|
  %w[name role_group].each do |k|
    errors << "members[#{i}].#{k} is required" if m[k].to_s.strip.empty?
  end
  if m['email'] && m['email'] !~ /@/
    errors << "members[#{i}].email is invalid: #{m['email']}"
  end
  if m['image_url'] && !valid_url?(m['image_url'])
    errors << "members[#{i}].image_url is invalid URL"
  end
end

Array(loaded[:publications]).each_with_index do |p, i|
  %w[title venue year].each do |k|
    errors << "publications[#{i}].#{k} is required" if p[k].to_s.strip.empty?
  end
  if p['year'] && p['year'].to_s !~ /^\d{4}$/
    errors << "publications[#{i}].year must be 4 digits"
  end
  errors << "publications[#{i}].doi invalid format" unless valid_doi?(p['doi'])
  errors << "publications[#{i}].url invalid URL" unless valid_url?(p['url'])
end

Array(loaded[:patents]).each_with_index do |p, i|
  %w[title registration].each do |k|
    errors << "patents[#{i}].#{k} is required" if p[k].to_s.strip.empty?
  end
end

if errors.empty?
  puts 'Validation passed: YAML syntax and key fields are valid.'
  exit 0
else
  puts 'Validation failed:'
  errors.each { |e| puts "- #{e}" }
  exit 1
end
