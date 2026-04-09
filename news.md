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

    <div class="news-feed">
      {% for item in site.data.news %}
      <article class="news-card">
        {% if item.image %}
        <div class="news-card-media">
          <img src="{{ item.image }}" alt="{{ item.image_alt | default: item.title }}">
        </div>
        {% endif %}

        <div class="news-card-body">
          <div class="list-meta">{{ item.date | date: "%B %-d, %Y" }}</div>

          {% if item.url %}
          <h2 class="news-card-title"><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></h2>
          {% else %}
          <h2 class="news-card-title">{{ item.title }}</h2>
          {% endif %}

          {% if item.summary %}<p>{{ item.summary }}</p>{% endif %}
          {% if item.note %}<p class="news-note">{{ item.note }}</p>{% endif %}

          {% if item.links %}
          <div class="news-links">
            <span class="news-links-label">Related links</span>
            {% for link in item.links %}
            <a class="publication-link" href="{{ link.url }}">{{ link.label }}</a>{% unless forloop.last %}<span class="news-links-sep">/</span>{% endunless %}
            {% endfor %}
          </div>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</div>
