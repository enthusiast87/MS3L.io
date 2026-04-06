---
layout: default
title: Home
---
{% assign lab = site.data.lab %}

<section class="hero">
  <div class="container hero-grid">
    <div class="hero-copy">
      <div class="eyebrow">{{ lab.subtitle }}</div>
      <h1>{{ lab.hero.title }}</h1>
      <p>{{ lab.hero.body }}</p>

      <div class="hero-actions">
        <a class="btn btn-primary" href="{{ lab.hero.primary_cta_url | relative_url }}">{{ lab.hero.primary_cta_label }}</a>
        <a class="btn btn-secondary" href="{{ lab.hero.secondary_cta_url | relative_url }}">{{ lab.hero.secondary_cta_label }}</a>
      </div>

      <div class="hero-metrics">
        {% for metric in lab.hero.metrics %}
        <div class="metric-card">
          <div class="metric-label">{{ metric.label }}</div>
          <strong>{{ metric.value }}</strong>
        </div>
        {% endfor %}
      </div>
    </div>

    <div class="hero-card">
      <div class="hero-card-photo"></div>
      <h3>{{ lab.principal_investigator.name }}</h3>
      <div class="role">{{ lab.principal_investigator.role }}</div>
      <div class="hero-card-affiliation">{{ lab.principal_investigator.affiliation }}</div>
      <p>{{ lab.principal_investigator.summary }}</p>
      <div class="hero-card-links">
        {% for link in lab.principal_investigator.links %}
        <a href="{{ link.url | relative_url }}">{{ link.label }}</a>
        {% endfor %}
      </div>
    </div>
  </div>
</section>

<section class="credibility-strip">
  <div class="container credibility-grid">
    {% for item in lab.hero.credibility %}
    <div class="credibility-item">
      <div class="credibility-label">{{ item.label }}</div>
      <strong>{{ item.value }}</strong>
    </div>
    {% endfor %}
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">{{ lab.research.title }}</h2>
    <p class="section-lead">{{ lab.research.lead }}</p>

    <div class="card-grid four">
      {% for item in site.data.research %}
      <div class="card">
        <h3>{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
        {% if item.topics %}
        <ul class="topic-list">
          {% for topic in item.topics limit: 3 %}
          <li>{{ topic }}</li>
          {% endfor %}
        </ul>
        {% endif %}
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="container split-grid">
    <div>
      <h2 class="section-title">{{ lab.featured_outputs.title }}</h2>
      <p class="section-lead">{{ lab.featured_outputs.lead }}</p>

      {% assign featured_publications = site.data.publications | where: "featured", true %}
      {% for item in featured_publications %}
      <div class="list-card">
        <div class="list-meta">{{ item.venue }} | {{ item.year }}</div>
        {% if item.url %}
        <strong><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></strong>
        {% else %}
        <strong>{{ item.title }}</strong>
        {% endif %}
        {% if item.doi %}
        <p>DOI: <a class="inline-link" href="{{ item.url }}">{{ item.doi }}</a></p>
        {% endif %}
      </div>
      {% endfor %}
    </div>

    <div>
      <h2 class="section-title">{{ lab.news.title }}</h2>
      <p class="section-lead">{{ lab.news.lead }}</p>

      {% for item in site.data.news limit: 3 %}
      <div class="list-card">
        <div class="list-meta">{{ item.date }}</div>
        <strong>{{ item.title }}</strong>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">{{ lab.projects.title }}</h2>
    <p class="section-lead">{{ lab.projects.lead }}</p>

    <div class="card-grid four">
      {% for item in lab.projects.items %}
      <div class="card">
        <h3>{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
        <p class="trl-badge">{{ item.trl }}</p>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">{{ lab.approach.title }}</h2>
    <p class="section-lead">{{ lab.approach.lead }}</p>

    <div class="card-grid three">
      {% for item in lab.approach.areas %}
      <div class="card">
        <h3>{{ item.title }}</h3>
        <p>{{ item.summary }}</p>
      </div>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container split-grid">
    <div>
      <h2 class="section-title">{{ lab.experiences.title }}</h2>
      <p class="section-lead">Selected translation and commercialization highlights from the original MS3L website.</p>
      {% for item in lab.experiences.items %}
      <div class="list-card">
        <strong>{{ item.title }}</strong>
        <p>{{ item.summary }}</p>
        <p class="publication-doi">{{ item.detail }}</p>
      </div>
      {% endfor %}
    </div>
    <div>
      <h2 class="section-title">{{ lab.contact.title }}</h2>
      <p class="section-lead">{{ lab.contact.note }}</p>
      <div class="page-card contact-summary">
        <p><strong>Address</strong><br>{{ lab.contact.address }}</p>
        <p><strong>Email</strong><br>
          {% for item in lab.contact.emails %}
          <a class="inline-link" href="mailto:{{ item }}">{{ item }}</a>{% unless forloop.last %}<br>{% endunless %}
          {% endfor %}
        </p>
        <p><strong>Phone</strong><br>{{ lab.contact.phone }}</p>
        <a class="btn btn-primary" href="{{ '/contact' | relative_url }}">Get in touch</a>
      </div>
    </div>
  </div>
</section>

<section class="section section-emphasis">
  <div class="container cta-panel">
    <div>
      <h2 class="section-title">{{ lab.join.title }}</h2>
      <p class="section-lead">{{ lab.join.body }}</p>
    </div>
    <div class="cta-actions">
      {% for item in lab.join.actions %}
      <a class="btn {% if forloop.first %}btn-primary{% else %}btn-secondary{% endif %}" href="{{ item.url | relative_url }}">{{ item.label }}</a>
      {% endfor %}
    </div>
  </div>
</section>
