---
layout: default
title: Technology Transfer
---
{% assign experiences = site.data.lab.experiences %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>Technology Transfer</h1>
      <p>Translation of research outcomes toward practical implementation and industrial deployment.</p>
    </div>

    <div class="content-feed">
      {% for item in experiences.items %}
        {% if item.title == "Technology transfer to Lotte Chemical" or item.title == "Know-how consultancy to Evonik Industries" %}
        <article class="content-item-card impact-item-card">
          <h2 class="content-item-title">{{ item.title }}</h2>
          <p>{{ item.summary }}</p>
          <p class="content-item-detail">{{ item.detail }}</p>
        </article>
        {% endif %}
      {% endfor %}
    </div>
  </div>
</div>
