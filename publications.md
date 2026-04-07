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
      {% assign authors_rendered = item.authors
        | replace: "Jihoon Kim", "<span class='author-highlight'>Jihoon Kim</span>"
        | replace: "Ji Hoon Kim", "<span class='author-highlight'>Ji Hoon Kim</span>"
        | replace: "Jieun Kang", "<span class='author-highlight'>Jieun Kang</span>"
        | replace: "Suyeon Park", "<span class='author-highlight'>Suyeon Park</span>"
        | replace: "Yourim Noh", "<span class='author-highlight'>Yourim Noh</span>"
        | replace: "Seung Hwan Kim", "<span class='author-highlight'>Seung Hwan Kim</span>"
        | replace: "Khilola Kholmizaeva", "<span class='author-highlight'>Khilola Kholmizaeva</span>"
      %}
      <p class="publication-authors">{{ authors_rendered }}</p>
      {% if item.authors contains "et al." %}
      <p class="publication-note">Full author list is available in the journal record (DOI link).</p>
      {% endif %}
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
