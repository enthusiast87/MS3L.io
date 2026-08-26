---
layout: default
title: Scale-up
---
{% assign scale = site.data.lab.scale_up %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>Scale-up</h1>
      <p>{{ scale.lead }}</p>
      {% if scale.focus %}
      <h2>What we work on</h2>
      <ul>
        {% for item in scale.focus %}
        <li>{{ item }}</li>
        {% endfor %}
      </ul>
      {% endif %}
    </div>

    <section class="profile-section">
      <h2 class="section-title section-title-sm">Plant and pilot-scale work</h2>
      <div class="card-grid two impact-grid">
        {% for item in scale.items %}
        <article class="card impact-experience-card">
          <h3>{{ item.title }}</h3>
          <p>{{ item.summary }}</p>
          {% if item.detail %}<p class="impact-experience-detail">{{ item.detail }}</p>{% endif %}
        </article>
        {% endfor %}
      </div>
    </section>
  </div>
</div>
