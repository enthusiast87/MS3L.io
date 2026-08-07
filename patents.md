---
layout: default
title: Patents
---
{% assign impact = site.data.lab.technology_impact %}
{% assign patents = site.data.patents %}
{% assign patent_page = impact.pages | where: "slug", "patents" | first %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ patent_page.title }}</h1>
      <p>{{ patent_page.summary }}</p>
    </div>

    <div class="news-feed">
      {% for patent in patents %}
      <article class="news-card news-card-text-only publication-entry">
        <div class="news-card-body">
          <div class="list-meta">{% if patent.date %}{{ patent.date | date: "%Y" }}{% else %}N/A{% endif %} · {{ patent.country | default: "Korea (KR)" }}</div>
          <h2 class="news-card-title">{{ patent.title }}</h2>
          <p class="publication-authors">{% include highlight-members.html text=patent.inventors %}</p>
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
      </article>
      {% endfor %}
    </div>
  </div>
</div>
