---
layout: default
title: Invited Talks
---
{% assign talks = site.data.lab.invited_talks %}
{% assign now_ts = site.time | date: '%s' | plus: 0 %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ talks.title }}</h1>
      <p>{{ talks.lead }}</p>
    </div>

    <div class="news-feed">
      {% for item in talks.items %}
      {% assign talk_ts = item.date | date: '%s' | plus: 0 %}
      <article class="news-card news-card-text-only">
        <div class="news-card-body">
          <div class="talk-meta">
            <span class="list-meta">{{ item.date_label | default: item.date }}</span>
            {% if item.tag %}<span class="talk-tag">{{ item.tag }}</span>{% endif %}
            {% if talk_ts > now_ts %}<span class="talk-upcoming">Upcoming</span>{% endif %}
          </div>
          <h2 class="news-card-title">{{ item.title }}</h2>
          <p class="talk-event">
            <strong>{{ item.event }}</strong>{% if item.session %} &middot; {{ item.session }}{% endif %}
          </p>
          {% if item.location %}<p class="talk-location">{{ item.location }}</p>{% endif %}
          {% if item.note %}<p class="talk-note">{{ item.note }}</p>{% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</div>
