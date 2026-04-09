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

    <section class="profile-section">
      <h2 class="section-title section-title-sm">Ongoing projects</h2>
      <div class="card-grid two">
        {% for item in lab.projects.ongoing %}
        <div class="card">
          <h3>{{ item.title }}</h3>
          <p><strong>{{ item.period }}</strong></p>
          <p>{{ item.sponsor }}</p>
        </div>
        {% endfor %}
      </div>
    </section>

    <section class="profile-section">
      <h2 class="section-title section-title-sm">Previous projects</h2>
      <div class="card-grid two">
        {% for item in lab.projects.previous %}
        <div class="card">
          <h3>{{ item.title }}</h3>
          <p><strong>{{ item.period }}</strong></p>
          <p>{{ item.sponsor }}</p>
        </div>
        {% endfor %}
      </div>
    </section>
  </div>
</div>
