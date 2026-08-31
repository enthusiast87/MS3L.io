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

    <ul class="talk-list">
      {% for item in talks.items %}
      {% assign talk_ts = item.date | date: '%s' | plus: 0 %}
      <li class="talk-item">
        <div class="talk-when">
          <span class="talk-date">{{ item.date_label | default: item.date }}</span>
          {% if talk_ts > now_ts %}<span class="talk-upcoming">Upcoming</span>{% endif %}
        </div>
        <div class="talk-body">
          <h2>{{ item.title }}</h2>
          <p class="talk-event">
            <strong>{{ item.event }}</strong>{% if item.session %} &middot; {{ item.session }}{% endif %}
          </p>
          {% if item.location %}<p class="talk-location">{{ item.location }}</p>{% endif %}
          {% if item.note %}<p class="talk-note">{{ item.note }}</p>{% endif %}
        </div>
      </li>
      {% endfor %}
    </ul>
  </div>
</div>
