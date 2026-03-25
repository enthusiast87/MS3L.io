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

    <section class="member-note">
      <div class="page-card">
        <h2>{{ lab.experiences.title }}</h2>
        {% for item in lab.experiences.items %}
        <div class="list-card publication-entry">
          <strong>{{ item.title }}</strong>
          <p>{{ item.summary }}</p>
          <p class="publication-doi">{{ item.detail }}</p>
        </div>
        {% endfor %}
      </div>
    </section>
  </div>
</div>
