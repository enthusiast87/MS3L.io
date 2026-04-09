---
layout: default
title: News
---
{% assign lab = site.data.lab %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ lab.news_page.title }}</h1>
      <p>{{ lab.news_page.lead }}</p>
    </div>

    {% for item in site.data.news %}
    <div class="list-card">
      <div class="list-meta">{{ item.date | date: "%B %Y" }}</div>
      {% if item.url %}
      <strong><a class="publication-link" href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>
      {% else %}
      <strong>{{ item.title }}</strong>
      {% endif %}
      {% if item.summary %}<p>{{ item.summary }}</p>{% endif %}
    </div>
    {% endfor %}

    <section class="member-note">
      <div class="page-card">
        <h2>News and updates</h2>
        <p>
          News migration is in progress. The entries above already include migrated highlights from publications, awards, and patent milestones, and more archived items will be added chronologically.
        </p>
      </div>
    </section>
  </div>
</div>
