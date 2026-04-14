---
layout: default
title: Technology Transfer
---
{% assign impact = site.data.lab.technology_impact %}
{% assign experiences = site.data.lab.experiences %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>Technology Transfer</h1>
      <p>
        Translation of research outcomes toward practical implementation and industrial deployment.
      </p>
    </div>

    <section class="member-note">
      <div class="page-card">
        <h2>Selected Experiences</h2>
        <div class="card-grid two">
          {% for item in experiences.items %}
          <div class="card impact-experience-card">
            <h3>{{ item.title }}</h3>
            <p>{{ item.summary }}</p>
            <p class="impact-experience-detail">{{ item.detail }}</p>
          </div>
          {% endfor %}
        </div>
      </div>
    </section>

    <div class="list-card publication-entry">
      <strong>Technology transfer to Lotte Chemical</strong>
      <p>Continuous waste polystyrene catalytic depolymerization and separation.</p>
      <p class="publication-doi">2022-07-11, 396,000 USD, 10% contribution.</p>
    </div>
  </div>
</div>
