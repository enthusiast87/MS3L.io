---
layout: default
title: Industrial Collaboration
---
{% assign impact = site.data.lab.technology_impact %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>Industrial Collaboration</h1>
      <p>
        Collaboration and consulting on membrane separation systems and sustainable chemical engineering.
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
      <strong>Know-how consultancy to Evonik Industries</strong>
      <p>Roll-to-roll robust membrane fabrication and module preparation.</p>
      <p class="publication-doi">2020-07 to 2020-12, 8,000 GBP, 100% contribution.</p>
    </div>
  </div>
</div>
