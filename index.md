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
        <div class="hero-identity">
          <div class="hero-acronym-block" aria-label="{{ lab.full_name | strip_html }}">
            <div class="hero-acronym-line"><span class="hero-initial">M</span>embrane-based</div>
            <div class="hero-acronym-line"><span class="hero-initial">S</span>ustainable</div>
            <div class="hero-acronym-line"><span class="hero-initial">S</span>eparation</div>
            <div class="hero-acronym-line"><span class="hero-initial">S</span>olutions</div>
            <div class="hero-acronym-line"><span class="hero-initial">L</span>aboratory</div>
          </div>
          <div class="hero-identity-copy">
            <h1>MS<sup>3</sup>L</h1>
            <p class="hero-mission">{{ lab.hero.mission }}</p>
            <p class="hero-subcopy">{{ lab.subtitle }}</p>
          </div>
        </div>
        <div class="hero-actions">
          <a class="btn btn-primary" href="{{ '/research' | relative_url }}">Research</a>
          <a class="btn btn-secondary" href="{{ '/publications' | relative_url }}">Publications</a>
          <a class="btn btn-secondary" href="{{ '/join-us' | relative_url }}">Join Us</a>
        </div>
      </div>

      <aside class="hero-side">
        <h3>Notice / News</h3>
        {% for item in site.data.news limit: 3 %}
        <div class="side-news-item">
          <div class="list-meta">{{ item.date | date: "%b %Y" }}</div>
          {% if item.url %}<strong class="side-item-title"><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></strong>{% else %}<strong class="side-item-title">{{ item.title }}</strong>{% endif %}
          {% if item.summary %}<p class="side-item-summary">{{ item.summary }}</p>{% endif %}
        </div>
        {% endfor %}
        <a class="inline-link" href="{{ '/news' | relative_url }}">More news →</a>
      </aside>
    </div>
  </div>
</section>

<section class="section">
  <div class="container card-grid three">
    <a class="card card-link" href="{{ '/principal-investigator' | relative_url }}">
      <h3>Principal Investigator</h3>
      <p>{{ pi.name }} | {{ pi.position }}</p>
    </a>
    <a class="card card-link" href="{{ '/members' | relative_url }}">
      <h3>Members</h3>
      <p>Graduate students and postdoctoral researchers in MS<sup>3</sup>L.</p>
    </a>
    <a class="card card-link" href="{{ '/projects' | relative_url }}">
      <h3>Current Projects</h3>
      <p>National R&D and CCU related ongoing projects.</p>
    </a>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <h2 class="section-title">Research Themes</h2>
    <div class="split-grid">
      <div class="card-grid two">
        {% for item in site.data.research %}
        <div class="card research-theme-card">
          <h3>{{ item.title }}</h3>
          <p>{{ item.summary }}</p>
          {% if item.selected_papers %}
          <div class="theme-paper-inline">
            <div class="list-meta">Key paper</div>
            <a class="publication-link" href="{{ item.selected_papers[0].url }}">{{ item.selected_papers[0].title }}</a>
          </div>
          {% endif %}
        </div>
        {% endfor %}
      </div>

      <div>
        <div class="page-card contact-summary">
          <h2>Research Contact</h2>
          <p>
            We welcome inquiries about research collaboration, student opportunities,
            and membrane-enabled separation topics connected to the themes above.
          </p>
          <p class="contact-summary-meta"><strong>{{ lab.contact.institution }}</strong></p>
          <p class="contact-summary-email">
            <a class="inline-link" href="mailto:{{ lab.contact.email }}">{{ lab.contact.email }}</a>
          </p>
          <a class="btn btn-primary" href="{{ '/contact' | relative_url }}">Get in touch</a>
        </div>
      </div>
    </div>
    <p class="theme-cta"><a class="inline-link" href="{{ '/research' | relative_url }}">View detailed theme summaries and figures →</a></p>
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
        {% if item.url %}<strong><a class="publication-link" href="{{ item.url | relative_url }}">{{ item.title }}</a></strong>{% else %}<strong>{{ item.title }}</strong>{% endif %}
          {% if item.summary %}<p>{{ item.summary }}</p>{% endif %}
        {% endif %}
      </div>
      {% endfor %}
    </div>
    <p><a class="inline-link" href="{{ '/publications' | relative_url }}">View full publication list →</a></p>
  </div>
</section>
