---
layout: default
title: Publications
---
{% assign lab = site.data.lab %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ lab.publications.title }}</h1>
      <p>{{ lab.publications.lead }}</p>
    </div>

    {% for item in site.data.publications %}
    <div class="list-card publication-entry">
      <div class="list-meta">{{ item.venue }}, {{ item.year }}</div>
      {% if item.url %}
      <strong><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></strong>
      {% else %}
      <strong>{{ item.title }}</strong>
      {% endif %}
      {% if item.authors %}
      {% assign cleaned_authors = item.authors | replace: ' et al.', '' | replace: ' et al', '' %}
      <p class="publication-authors">{% include highlight-members.html text=cleaned_authors %}</p>
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
    {% endfor %}
  </div>
</div>
