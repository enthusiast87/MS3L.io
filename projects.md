---
layout: default
title: Projects
---
{% assign lab = site.data.lab %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ lab.projects.title }}</h1>
      <p>{{ lab.projects.lead }}</p>
    </div>

    <div class="card-grid three">
      {% for item in lab.projects.items %}
      <div class="card">
        <h3>{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
        {% if item.trl %}
        <p><strong>{{ item.trl }}</strong></p>
        {% endif %}
      </div>
      {% endfor %}
    </div>
  </div>
</div>
