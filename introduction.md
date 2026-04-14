---
layout: default
title: Introduction
---
{% assign lab = site.data.lab %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ lab.introduction.title }}</h1>
      {% for paragraph in lab.introduction.overview %}
      <p>{{ paragraph }}</p>
      {% endfor %}

      <h2>Research Priorities</h2>
      <ul>
        {% for item in lab.introduction.priorities %}
        <li>{{ item }}</li>
        {% endfor %}
      </ul>

      <h2>{{ lab.approach.title }}</h2>
      <p>{{ lab.approach.lead }}</p>

      <div class="card-grid two">
        {% for area in lab.approach.areas %}
        <div class="card">
          <h3>{{ area.title }}</h3>
          <p>{{ area.summary }}</p>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</div>
