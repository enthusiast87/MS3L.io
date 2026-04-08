---
layout: default
title: News
---
{% assign lab = site.data.lab %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ lab.news_page.title }}</h1>
      <p>{{ lab.news_page.lead }}</p>
    </div>

    {% for item in site.data.news %}
    <div class="list-card">
      <div class="list-meta">{{ item.date }}</div>
      <strong>{{ item.title }}</strong>
      {% if item.summary %}
      <p>{{ item.summary }}</p>
      {% endif %}
    </div>
    {% endfor %}

    <section class="member-note">
      <div class="page-card">
        <h2>News and updates</h2>
        <p>
          The original Google Site frames this page as a place to stay up to date with recent publications, awards, projects, and other activities from MS^3L.
        </p>
      </div>
    </section>
  </div>
</div>
