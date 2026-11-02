---
layout: default
title: Publications
---
{% assign lab = site.data.lab %}

<div class="page-wrap">
  <div class="container publications-page">
    <div class="page-card">
      <h1>{{ lab.publications.title }}</h1>
      <p>{{ lab.publications.lead }}</p>
    </div>

    {% assign featured = site.data.publications | where: "featured", true %}
    {% if featured.size > 0 %}
    <details class="publication-featured-section">
      <summary class="featured-toggle">
        <h2 class="section-title section-title-sm">Featured <span class="featured-count">{{ featured.size }}</span><svg class="featured-chevron" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></h2>
      </summary>
      <div class="card-grid three featured-grid">
        {% for item in featured %}
        <article class="card publication-featured">
          <div class="publication-badge">{{ item.venue }} &middot; {{ item.year }}</div>
          {% if item.url %}
          <h3><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></h3>
          {% else %}
          <h3>{{ item.title }}</h3>
          {% endif %}
          {% if item.authors %}<p class="publication-authors">{% include highlight-members.html text=item.authors %}</p>{% endif %}
          {% if item.summary %}<p>{{ item.summary }}</p>{% endif %}
        </article>
        {% endfor %}
      </div>
    </details>
    {% endif %}

    <h2 class="section-title section-title-sm all-publications-title">All publications</h2>
    <div class="pub-list">
      {% assign prev_year = "" %}
      {% for item in site.data.publications %}
      <article class="pub-row{% if item.year != prev_year %} pub-year-start{% endif %}">
        <div class="pub-year">{% if item.year != prev_year %}{{ item.year }}{% endif %}</div>
        <div>
          {% if item.url %}
          <h3 class="pub-title"><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></h3>
          {% else %}
          <h3 class="pub-title">{{ item.title }}</h3>
          {% endif %}
          <p class="pub-meta">{{ item.venue }}</p>
          {% if item.authors %}
          <p class="pub-authors">{% include highlight-members.html text=item.authors %}</p>
          {% endif %}
          {% if item.support %}
          <p class="publication-support"><strong>Support:</strong> {{ item.support }}</p>
          {% endif %}
        </div>
      </article>
      {% assign prev_year = item.year %}
      {% endfor %}
    </div>
  </div>
</div>
