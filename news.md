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
          <img src="{{ item.image | relative_url }}" alt="{{ item.image_alt | default: item.title }}" loading="lazy">
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

          <div class="detail-actions">
            <button class="btn btn-secondary btn-compact" type="button" data-modal-open="news-{{ forloop.index }}">Details</button>
            {% if item.url %}
            <a class="btn btn-primary btn-compact" href="{{ item.url }}">Read more</a>
            {% endif %}
          </div>
        </div>
      </article>

      <div class="content-modal" id="news-{{ forloop.index }}" hidden>
        <div class="content-modal-panel" role="dialog" aria-modal="true" aria-labelledby="news-title-{{ forloop.index }}">
          <button class="modal-close" type="button" data-modal-close aria-label="Close details">Close</button>
          <div class="modal-layout">
            {% if item.image %}
            <div class="modal-media">
              <img src="{{ item.image | relative_url }}" alt="{{ item.image_alt | default: item.title }}" loading="lazy">
            </div>
            {% endif %}
            <div class="modal-body">
              <div class="list-meta">{{ item.date | date: "%B %-d, %Y" }}</div>
              <h2 id="news-title-{{ forloop.index }}">{{ item.title }}</h2>
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
          </div>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</div>
