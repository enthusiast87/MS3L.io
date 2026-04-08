---
layout: default
title: Home
---
{% assign lab = site.data.lab %}
{% assign pi = site.data.members | where: "role_group", "Principal Investigator" | first %}

<section class="hero hero-clean">
  <div class="container">
    <div class="hero-board">
      <div class="hero-main">
        <div class="eyebrow">{{ lab.subtitle }}</div>
        <h1>{{ lab.hero.title }}</h1>
        <p>{{ lab.hero.body }}</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{{ '/research' | relative_url }}">Research</a>
          <a class="btn btn-secondary" href="{{ '/publications' | relative_url }}">Publications</a>
          <a class="btn btn-secondary" href="{{ '/join-us' | relative_url }}">Join Us</a>
        </div>
      </div>

      <aside class="hero-side">
        <h3>Notice / News</h3>
        {% for item in site.data.news limit: 4 %}
        <div class="side-news-item">
          <div class="list-meta">{{ item.date }}</div>
          <strong>{{ item.title }}</strong>
        </div>
        {% endfor %}
        <a class="inline-link" href="{{ '/news' | relative_url }}">More news →</a>

        <h3 class="hero-side-heading">Upcoming Events</h3>
        {% for event in site.data.events limit: 3 %}
        <div class="side-news-item">
          <div class="list-meta">{{ event.date }}</div>
          <strong>{{ event.title }}</strong>
          <p>{{ event.location }}</p>
        </div>
        {% endfor %}
      </aside>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split-grid">
    <div>
      <h2 class="section-title">Current Projects</h2>
      {% for item in lab.projects.items %}
      <div class="list-card">
        <strong>{{ item.title }}</strong>
        <p>{{ item.summary }}</p>
        <p class="publication-doi">{{ item.trl }}{% if item.period %} · {{ item.period }}{% endif %}</p>
      </div>
      {% endfor %}
      <p><a class="inline-link" href="{{ '/projects' | relative_url }}">View project details →</a></p>
    </div>

    <div>
      <h2 class="section-title">Lab Snapshot</h2>
      <a class="card card-link" href="{{ '/principal-investigator' | relative_url }}">
        <h3>Principal Investigator</h3>
        <p>{{ pi.name }} | {{ pi.position }}</p>
      </a>
      <a class="card card-link" href="{{ '/members' | relative_url }}">
        <h3>Members</h3>
        <p>Graduate students and postdoctoral researchers in MS3L.</p>
      </a>
      <a class="card card-link" href="{{ '/patents' | relative_url }}">
        <h3>Patents & Technology Impact</h3>
        <p>Registered patents, transfer, and industrial collaborations.</p>
      </a>
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container split-grid">
    <div>
      <h2 class="section-title">Research Themes</h2>
      <div class="card-grid two">
        {% for item in site.data.research %}
        <div class="card">
          <h3>{{ item.title }}</h3>
          <p>{{ item.summary }}</p>
        </div>
        {% endfor %}
      </div>
    </div>

    <div>
      <div class="page-card contact-summary">
        <h2>Contact</h2>
        <p><strong>{{ lab.contact.institution }}</strong></p>
        <p>{{ lab.contact.address }}</p>
        <p>
          {% for item in lab.contact.emails %}
          <a class="inline-link" href="mailto:{{ item }}">{{ item }}</a>{% unless forloop.last %}<br>{% endunless %}
          {% endfor %}
        </p>
        <p><strong>TEL.</strong> {{ lab.contact.phone }}</p>
        <a class="btn btn-primary" href="{{ '/contact' | relative_url }}">Contact us</a>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Latest News</h2>
    <div class="card-grid two">
      {% for item in site.data.news limit: 4 %}
      <div class="list-card">
        <div class="list-meta">{{ item.date }}</div>
        <strong>{{ item.title }}</strong>
        {% if item.summary %}
        <p>{{ item.summary }}</p>
        {% endif %}
      </div>
      {% endfor %}
    </div>
    <p><a class="inline-link" href="{{ '/news' | relative_url }}">View all news →</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">Recent Publications</h2>
    <div class="card-grid two">
      {% for item in site.data.publications limit: 6 %}
      <div class="list-card publication-entry">
        <div class="list-meta">{{ item.year }} · {{ item.venue }}</div>
        {% if item.url %}
        <strong><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></strong>
        {% else %}
        <strong>{{ item.title }}</strong>
        {% endif %}
      </div>
      {% endfor %}
    </div>
    <p><a class="inline-link" href="{{ '/publications' | relative_url }}">View full publication list →</a></p>
  </div>
</section>
