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

    <div class="pub-list">
      {% assign prev_year = "" %}
      {% for patent in patents %}
      {% assign year = patent.date | date: "%Y" | default: "N/A" %}
      {% capture countries %}{{ patent.country | default: "KR" }}{% for reg in patent.foreign %}, {{ reg.country }}{% endfor %}{% endcapture %}
      <article class="pub-row{% if year != prev_year %} pub-year-start{% endif %}">
        <div class="pub-year">{% if year != prev_year %}{{ year }}{% endif %}</div>
        <div>
          <h3 class="pub-title">{{ patent.title }}</h3>
          <p class="pub-meta">{{ countries }}</p>
          <p class="pub-authors">{% include highlight-members.html text=patent.inventors %}</p>
          <p class="publication-doi">{{ patent.registration }}{% if patent.date %}<span class="patent-reg-date"> · registered {{ patent.date | date: "%Y-%m-%d" }}</span>{% endif %}</p>
          {% for reg in patent.foreign %}
          <p class="publication-doi">{{ reg.registration }}{% if reg.date %}<span class="patent-reg-date"> · registered {{ reg.date | date: "%Y-%m-%d" }}</span>{% endif %}</p>
          {% endfor %}
          {% if patent.pct %}
          <p class="publication-doi">PCT: {{ patent.pct }}</p>
          {% endif %}
        </div>
      </article>
      {% assign prev_year = year %}
      {% endfor %}
    </div>
  </div>
</div>
