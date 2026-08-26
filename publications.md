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
    <section class="publication-featured-section">
      <h2 class="section-title section-title-sm">Featured</h2>
      <div class="card-grid two">
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
    </section>
    {% endif %}

    <h2 class="section-title section-title-sm all-publications-title">All publications</h2>
    <div class="news-feed">
      {% for item in site.data.publications %}
      <article class="news-card news-card-text-only publication-entry">
        <div class="news-card-body">
          <div class="list-meta">{{ item.venue }} · {{ item.year }}</div>
          {% if item.url %}
          <h2 class="news-card-title"><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></h2>
          {% else %}
          <h2 class="news-card-title">{{ item.title }}</h2>
          {% endif %}
          {% if item.authors %}
          <p class="publication-authors">{% include highlight-members.html text=item.authors %}</p>
          {% endif %}
          {% if item.summary %}
          <p>{{ item.summary }}</p>
          {% endif %}
          {% if item.doi %}
          <p class="publication-doi">DOI: <a class="inline-link" href="{{ item.url }}">{{ item.doi }}</a></p>
          {% endif %}
          {% if item.support %}
          <p class="publication-support"><strong>Support:</strong> {{ item.support }}</p>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</div>
