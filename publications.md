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
