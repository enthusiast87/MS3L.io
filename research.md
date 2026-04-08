---
layout: default
title: Research
---
<div class="page-wrap">
  <div class="container research-page">
    <div class="page-card">
      <h1>Research Themes</h1>
      <p>
        MS3L develops membrane-enabled separations for sustainable chemical processing,
        circular resource systems, and energy-related applications.
      </p>
    </div>

    <div class="research-theme-stack">
      {% for item in site.data.research %}
      <article class="research-detail-card">
        <div class="research-detail-media">
          <img src="{{ item.image }}" alt="{{ item.title }} research visual">
        </div>
        <div class="research-detail-body">
          <div class="profile-label">{{ item.title }}</div>
          <h2>{{ item.one_liner }}</h2>
          <p>{{ item.why_it_matters }}</p>

          {% if item.topics %}
          <h3>Core topics</h3>
          <ul>
            {% for topic in item.topics %}
            <li>{{ topic }}</li>
            {% endfor %}
          </ul>
          {% endif %}

          {% if item.key_methods %}
          <h3>Methods and approach</h3>
          <ul>
            {% for method in item.key_methods %}
            <li>{{ method }}</li>
            {% endfor %}
          </ul>
          {% endif %}

          {% if item.selected_papers %}
          <h3>Selected papers</h3>
          <div class="card-grid two">
            {% for paper in item.selected_papers %}
            <div class="list-card publication-entry">
              <div class="list-meta">{{ paper.year }} · {{ paper.venue }}</div>
              <strong><a class="publication-link" href="{{ paper.url }}">{{ paper.title }}</a></strong>
            </div>
            {% endfor %}
          </div>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </div>
  </div>
</div>
