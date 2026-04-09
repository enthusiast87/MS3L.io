---
layout: default
title: Technology Transfer
---
{% assign impact = site.data.lab.technology_impact %}

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
        <h2>Selected partners and recognition</h2>
        <div class="logo-strip">
          {% for item in impact.logos %}
          <div class="logo-chip">
            <img src="{{ item.image }}" alt="{{ item.alt | default: item.name }}">
            <span>{{ item.name }}</span>
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
