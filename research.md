---
layout: default
title: Research
---
<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>Research Themes</h1>
      <p>
        MS3L develops membrane-enabled separations for sustainable chemical processing,
        circular resource systems, and energy-related applications.
      </p>
    </div>

    <div class="card-grid three">
      {% for item in site.data.research %}
      <div class="card">
        <h3>{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
        {% if item.topics %}
        <ul>
          {% for topic in item.topics %}
          <li>{{ topic }}</li>
          {% endfor %}
        </ul>
        {% endif %}
      </div>
      {% endfor %}
    </div>
  </div>
</div>
