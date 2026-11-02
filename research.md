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
        circular resource systems, and energy-related applications. Select a theme to see its
        figure, core topics, methods, and selected papers.
      </p>
    </div>

    <div class="card-grid two research-theme-grid">
      {% for item in site.data.research %}
      <article class="research-card research-card-clickable" role="button" tabindex="0"
               data-modal-open="research-details-{{ forloop.index }}"
               aria-label="Open {{ item.title }} details">
        <div class="research-card-figure">
          <img src="{{ item.image | relative_url }}" alt="{{ item.image_alt | default: item.title }}" loading="lazy">
        </div>

        <div class="research-card-caption">
          <div class="research-card-label">{{ item.title }}</div>
          <h2>{{ item.one_liner }}</h2>
        </div>

        <div class="research-card-body">
          <p>{{ item.why_it_matters }}</p>
          {% if item.application_examples %}
          <div class="research-chip-row" aria-label="{{ item.title }} application examples">
            {% for example in item.application_examples %}
            <span class="research-chip">{{ example }}</span>
            {% endfor %}
          </div>
          {% endif %}
          <div class="research-card-actions">
            <span class="research-details-button">
              Details
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"></path><path d="M13 6l6 6-6 6"></path></svg>
            </span>
          </div>
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</div>

{% comment %}
  One dialog per theme: the whole card opens it, matching the card-link grammar
  used on the home page. The figure lives inside the dialog with its caption.
{% endcomment %}
{% for item in site.data.research %}
<div class="content-modal" id="research-details-{{ forloop.index }}" hidden>
  <div class="content-modal-panel research-details-panel">
    <button class="modal-close" type="button" data-modal-close>Close</button>

    <div class="research-details-head">
      <div class="research-card-label">{{ item.title }}</div>
      <h2>{{ item.one_liner }}</h2>
      <p>{{ item.why_it_matters }}</p>
    </div>

    <div class="research-figure-stage research-details-figure">
      <img src="{{ item.image | relative_url }}" alt="{{ item.image_alt | default: item.title }}">
    </div>
    {% if item.visual_caption %}
    <p class="research-figure-caption">{{ item.visual_caption }}</p>
    {% endif %}

    {% if item.visual_points %}
    <section class="research-details-section">
      <h3>What the figure shows</h3>
      <ul>
        {% for point in item.visual_points %}
        <li>{{ point }}</li>
        {% endfor %}
      </ul>
    </section>
    {% endif %}

    {% if item.topics or item.key_methods %}
    <div class="research-details-columns">
      {% if item.topics %}
      <section class="research-details-section">
        <h3>Core topics</h3>
        <ul>
          {% for topic in item.topics %}
          <li>{{ topic }}</li>
          {% endfor %}
        </ul>
      </section>
      {% endif %}
      {% if item.key_methods %}
      <section class="research-details-section">
        <h3>Methods and approach</h3>
        <ul>
          {% for method in item.key_methods %}
          <li>{{ method }}</li>
          {% endfor %}
        </ul>
      </section>
      {% endif %}
    </div>
    {% endif %}

    {% if item.selected_papers %}
    <section class="research-details-section">
      <h3>Selected papers</h3>
      <div class="card-grid two">
        {% for paper in item.selected_papers %}
        <div class="list-card publication-entry">
          <div class="list-meta">{{ paper.year }} | {{ paper.venue }}</div>
          <strong><a class="publication-link" href="{{ paper.url }}">{{ paper.title }}</a></strong>
        </div>
        {% endfor %}
      </div>
    </section>
    {% endif %}
  </div>
</div>
{% endfor %}
