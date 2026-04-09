---
layout: default
title: Process Innovation
---
{% assign impact = site.data.lab.technology_impact %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>Process Innovation</h1>
      <p>
        Development of low-energy, circular, and intensified separation processes for real-world applications.
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
      <strong>National Research and Development Excellence Achievements 100 Case (2023)</strong>
      <p>Continuous waste polystyrene catalytic depolymerization and separation.</p>
      <p class="publication-doi">Published by Korea Institute of Science and Technology Evaluation and Planning (KISTEP).</p>
    </div>

    <div class="list-card publication-entry">
      <strong>Principal Investigator</strong>
      <p>National Research Foundation of Korea Basic Science Research Program.</p>
      <p class="publication-doi">2018-09 to 2019-08, developing an innovative and environmentally friendly spraying thin-film composite membrane for interactive separation in organic solvents, 30,000 USD.</p>
    </div>
  </div>
</div>
