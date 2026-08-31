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

    <div class="card-grid two research-theme-grid">
      {% for item in site.data.research %}
      <article class="research-card">
        <button class="research-card-figure" type="button" data-modal-open="research-figure-{{ forloop.index }}" aria-label="Enlarge the {{ item.title }} figure">
          <img src="{{ item.image | relative_url }}" alt="{{ item.image_alt | default: item.title }}" loading="lazy">
          <span class="research-figure-expand">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 3h6v6"></path><path d="M9 21H3v-6"></path><path d="M21 3l-7 7"></path><path d="M3 21l7-7"></path></svg>
            Enlarge
          </span>
        </button>

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
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</div>

{% comment %}
  One lightbox per figure, driven by the modal handlers already in the default
  layout, so no page-specific script is needed.
{% endcomment %}
{% for item in site.data.research %}
<div class="content-modal" id="research-figure-{{ forloop.index }}" hidden>
  <div class="content-modal-panel research-figure-panel">
    <button class="modal-close" type="button" data-modal-close>Close</button>
    <img src="{{ item.image | relative_url }}" alt="{{ item.image_alt | default: item.title }}">
    {% if item.visual_caption %}
    <p class="research-figure-caption">{{ item.visual_caption }}</p>
    {% endif %}
  </div>
</div>
{% endfor %}
