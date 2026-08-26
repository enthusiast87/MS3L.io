---
layout: default
title: Recognitions
---
{% assign recognitions = site.data.lab.recognitions %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>Recognitions</h1>
      <p>{{ recognitions.lead }}</p>
    </div>

    <div class="card-grid two impact-grid">
      {% for item in recognitions.items %}
      <article class="card impact-experience-card">
        {% if item.year %}<div class="list-meta">{{ item.year }}</div>{% endif %}
        <h3>{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
        {% if item.detail %}<p class="impact-experience-detail">{{ item.detail }}</p>{% endif %}
      </article>
      {% endfor %}
    </div>
  </div>
</div>
