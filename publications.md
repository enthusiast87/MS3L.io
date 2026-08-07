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

    <div class="content-feed">
      {% for item in site.data.publications %}
      <article class="content-item-card publication-entry">
        <div class="list-meta">{{ item.venue }} · {{ item.year }}</div>
        {% if item.url %}
        <h2 class="content-item-title"><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></h2>
        {% else %}
        <h2 class="content-item-title">{{ item.title }}</h2>
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
      </article>
      {% endfor %}
    </div>
  </div>
</div>
