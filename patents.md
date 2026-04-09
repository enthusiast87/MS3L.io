---
layout: default
title: Patents
---
{% assign impact = site.data.lab.technology_impact %}
{% assign patents = site.data.patents %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ impact.title }}</h1>
      <p>{{ impact.lead }}</p>
    </div>

    <section class="member-note">
      <div class="page-card">
        <h2>Registered patents</h2>
        {% for patent in patents %}
        <div class="list-card publication-entry">
          <strong>{{ patent.title }}</strong>
          <p class="publication-authors">{% include highlight-members.html text=patent.inventors %}</p>
          <div class="list-meta">{% if patent.date %}{{ patent.date | date: "%Y" }}{% else %}N/A{% endif %} · {{ patent.country | default: "Korea (KR)" }}</div>
          <p class="publication-doi">{{ patent.registration }}</p>
          {% if patent.pct %}
          <p class="publication-doi">PCT: {{ patent.pct }}</p>
          {% endif %}
          {% if patent.us_patent %}
          <p class="publication-doi">{{ patent.us_patent }}</p>
          {% endif %}
          {% if patent.china_patent %}
          <p class="publication-doi">{{ patent.china_patent }}</p>
          {% endif %}
        </div>
        {% endfor %}
      </div>
    </section>
  </div>
</div>
