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
      {% assign authors_rendered = item.authors %}
      {% for member in site.data.members %}
        {% assign member_tag = "<span class='author-highlight'>" | append: member.name | append: "</span>" %}
        {% assign authors_rendered = authors_rendered | replace: member.name, member_tag %}
        {% if member.aliases %}
          {% for alias in member.aliases %}
            {% assign alias_tag = "<span class='author-highlight'>" | append: alias | append: "</span>" %}
            {% assign authors_rendered = authors_rendered | replace: alias, alias_tag %}
          {% endfor %}
        {% endif %}
      {% endfor %}
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
