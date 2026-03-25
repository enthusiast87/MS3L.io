---
layout: default
title: Patents
---
{% assign experiences = site.data.lab.experiences.items %}
{% assign impact = site.data.lab.technology_impact %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ impact.title }}</h1>
      <p>{{ impact.lead }}</p>
    </div>

    <div class="card-grid three">
      {% for item in impact.pages %}
      <a class="card" href="{{ item.slug | prepend: '/' | relative_url }}">
        <h3>{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
      </a>
      {% endfor %}
    </div>

    <section class="member-note">
      <div class="page-card">
        <h2>Representative experiences</h2>
        {% for item in experiences %}
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
