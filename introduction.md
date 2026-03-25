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
      <h2>Jihoon Kim</h2>
      <p><strong>{{ lab.introduction.principal_investigator.current_role }}</strong></p>
      <p>{{ lab.introduction.principal_investigator.current_affiliation }}</p>
      <ul>
        {% for item in lab.introduction.principal_investigator.previous_positions %}
        <li>{{ item }}</li>
        {% endfor %}
      </ul>
    </div>
  </div>
</div>
