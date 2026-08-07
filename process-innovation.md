---
layout: default
title: Process Innovation
---
{% assign experiences = site.data.lab.experiences %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>Process Innovation</h1>
      <p>Development of low-energy, circular, and intensified separation processes for real-world applications.</p>
    </div>

    <div class="content-feed">
      {% for item in experiences.items %}
        {% if item.title == "National Research and Development Excellence Achievements 100 Case (2023)" or item.title == "Principal Investigator" %}
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
