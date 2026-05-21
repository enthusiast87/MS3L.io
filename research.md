---
layout: default
title: Research
---
<div class="page-wrap">
  <div class="container research-page">
    <div class="page-card">
      <h1>Research Themes</h1>
      <p>
        MS<sup>3</sup>L develops membrane-enabled separations for sustainable chemical processing,
        circular resource systems, and energy-related applications.
      </p>
    </div>

    <div class="research-theme-stack">
      {% for item in site.data.research %}
      <article class="research-detail-card">
        <div class="research-detail-visual">
          <div class="research-detail-media">
            <img src="{{ item.image | relative_url }}" alt="{{ item.image_alt | default: item.title | append: ' research visual' }}" loading="lazy">
          </div>
          {% if item.visual_caption %}
          <div class="research-visual-caption">
            <strong>Visual focus</strong>
            <p>{{ item.visual_caption }}</p>
          </div>
          {% endif %}
        </div>
        <div class="research-detail-body">
          <div class="profile-label">{{ item.title }}</div>
          <h2>{{ item.one_liner }}</h2>
          <p>{{ item.why_it_matters }}</p>

          {% if item.application_examples %}
          <div class="research-chip-row" aria-label="{{ item.title }} application examples">
            {% for example in item.application_examples %}
            <span class="research-chip">{{ example }}</span>
            {% endfor %}
          </div>
          {% endif %}

          {% if item.visual_points %}
          <div class="research-aside-card">
            <h3>What the visual highlights</h3>
            <ul class="research-note-list">
              {% for point in item.visual_points %}
              <li>{{ point }}</li>
              {% endfor %}
            </ul>
          </div>
          {% endif %}

          {% if item.topics %}
          <h3>Core topics</h3>
          <ul>
            {% for topic in item.topics %}
            <li>{{ topic }}</li>
            {% endfor %}
          </ul>
          {% endif %}

          {% if item.key_methods %}
          <h3>Methods and approach</h3>
          <ul>
            {% for method in item.key_methods %}
            <li>{{ method }}</li>
            {% endfor %}
          </ul>
          {% endif %}

          {% if item.selected_papers %}
          <h3>Selected papers</h3>
          <div class="card-grid two">
            {% for paper in item.selected_papers %}
            <div class="list-card publication-entry">
              <div class="list-meta">{{ paper.year }} | {{ paper.venue }}</div>
              <strong><a class="publication-link" href="{{ paper.url }}">{{ paper.title }}</a></strong>
            </div>
            {% endfor %}
          </div>
          {% endif %}

          <div class="detail-actions">
            <button class="btn btn-secondary btn-compact" type="button" data-modal-open="research-{{ item.title | slugify }}">Details</button>
          </div>
        </div>
      </article>

      <div class="content-modal" id="research-{{ item.title | slugify }}" hidden>
        <div class="content-modal-panel" role="dialog" aria-modal="true" aria-labelledby="research-title-{{ item.title | slugify }}">
          <button class="modal-close" type="button" data-modal-close aria-label="Close details">Close</button>
          <div class="modal-layout">
            <div class="modal-media">
              <img src="{{ item.image | relative_url }}" alt="{{ item.image_alt | default: item.title | append: ' research visual' }}" loading="lazy">
            </div>
            <div class="modal-body">
              <div class="profile-label">{{ item.title }}</div>
              <h2 id="research-title-{{ item.title | slugify }}">{{ item.one_liner }}</h2>
              <p>{{ item.why_it_matters }}</p>
              {% if item.visual_caption %}<p><strong>Visual focus:</strong> {{ item.visual_caption }}</p>{% endif %}
              {% if item.application_examples %}
              <div class="research-chip-row">
                {% for example in item.application_examples %}
                <span class="research-chip">{{ example }}</span>
                {% endfor %}
              </div>
              {% endif %}
              {% if item.topics %}
              <h3>Core topics</h3>
              <ul>
                {% for topic in item.topics %}
                <li>{{ topic }}</li>
                {% endfor %}
              </ul>
              {% endif %}
              {% if item.selected_papers %}
              <h3>Selected papers</h3>
              <ul>
                {% for paper in item.selected_papers %}
                <li><a class="publication-link" href="{{ paper.url }}">{{ paper.title }}</a></li>
                {% endfor %}
              </ul>
              {% endif %}
              {% if item.visual_points %}
              <h3>What the visual highlights</h3>
              <ul>
                {% for point in item.visual_points %}
                <li>{{ point }}</li>
                {% endfor %}
              </ul>
              {% endif %}
            </div>
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>
