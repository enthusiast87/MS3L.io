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

        <div class="hero-process" aria-hidden="true">
          <div class="hero-process-copy">
            <span>Selective transport</span>
            <strong>From complex mixtures<br>to sustainable solutions.</strong>
          </div>
          <div class="separation-visual">
            <span class="visual-label visual-label-feed">Feed</span>
            <span class="visual-label visual-label-product">Product</span>
            <div class="flow-line flow-line-one"></div>
            <div class="flow-line flow-line-two"></div>
            <div class="membrane-layer">
              <i></i><i></i><i></i><i></i><i></i>
            </div>
            <span class="particle particle-pass particle-cyan particle-one"></span>
            <span class="particle particle-pass particle-green particle-two"></span>
            <span class="particle particle-pass particle-cyan particle-three"></span>
            <span class="particle particle-pass particle-green particle-four"></span>
            <span class="particle particle-reject particle-large particle-five"></span>
            <span class="particle particle-reject particle-large particle-six"></span>
            <span class="particle particle-reject particle-medium particle-seven"></span>
          </div>
        </div>

        <div class="hero-actions">
          <a class="btn btn-primary" href="{{ '/research' | relative_url }}">Research</a>
          <a class="btn btn-secondary" href="{{ '/publications' | relative_url }}">Publications</a>
          <a class="btn btn-secondary" href="{{ '/join-us' | relative_url }}">Join Us</a>
        </div>
      </div>

      <aside class="hero-side" aria-labelledby="hero-news-heading">
        <h2 id="hero-news-heading" class="hero-side-title">Notice / News</h2>
        {% for item in site.data.news limit: 3 %}
        <div class="side-news-item">
          <div class="list-meta">{{ item.date | date: "%b %Y" }}</div>
          {% if item.url %}
          <strong class="side-item-title"><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></strong>
          {% else %}
          <strong class="side-item-title">{{ item.title }}</strong>
          {% endif %}
          {% if item.summary %}<p class="side-item-summary">{{ item.summary }}</p>{% endif %}
        </div>
        {% endfor %}
        <a class="inline-link" href="{{ '/news' | relative_url }}">More news</a>
      </aside>
    </div>
  </div>
</section>

<section class="section">
  <div class="container home-overview-grid">
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
      <p>National R&amp;D and CCU related ongoing projects.</p>
    </a>
    <a class="card card-link" href="{{ '/join-us' | relative_url }}">
      <h3>Join Us</h3>
      <p>Open to students and researchers in membrane science and sustainable separations.</p>
    </a>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <h2 class="section-title">Research Themes</h2>
    <p class="section-lead">{{ lab.research.lead }}</p>
    <div class="card-grid two">
      {% for theme in site.data.research limit: 4 %}
      <a class="card card-link research-theme-card" href="{{ '/research' | relative_url }}">
        <div class="research-theme-thumb">
          {% if theme.image %}
          <img src="{{ theme.image | relative_url }}" alt="{{ theme.image_alt | default: theme.title }}" loading="lazy">
          {% endif %}
        </div>
        <h3>{{ theme.title }}</h3>
        <p class="research-theme-summary">{{ theme.one_liner | default: theme.summary }}</p>
        {% if theme.application_examples %}
        <div class="research-chip-row research-chip-row-compact">
          {% for example in theme.application_examples limit: 2 %}
          <span class="research-chip">{{ example }}</span>
          {% endfor %}
        </div>
        {% endif %}
      </a>
      {% endfor %}
    </div>
    <p class="theme-cta"><a class="inline-link" href="{{ '/research' | relative_url }}">View detailed theme summaries and figures</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <h2 class="section-title">{{ lab.technology_impact.title }}</h2>
    <p class="section-lead">{{ lab.technology_impact.lead }}</p>
    <div class="card-grid four">
      {% for entry in lab.technology_impact.pages %}
      <a class="card card-link impact-card" href="{{ entry.slug | prepend: '/' | relative_url }}">
        <h3>{{ entry.title }}</h3>
        <p>{{ entry.summary }}</p>
      </a>
      {% endfor %}
    </div>
  </div>
</section>

<section class="section section-soft">
  <div class="container">
    <h2 class="section-title">Featured Publications</h2>
    <p class="section-lead">Representative work from the lab, spanning membrane materials, separations, and process design.</p>
    {% assign featured = site.data.publications | where: "featured", true %}
    <div class="card-grid two">
      {% for item in featured %}
      <article class="card publication-featured">
        <div class="publication-badge">{{ item.venue }} &middot; {{ item.year }}</div>
        {% if item.url %}
        <h3><a class="publication-link" href="{{ item.url }}">{{ item.title }}</a></h3>
        {% else %}
        <h3>{{ item.title }}</h3>
        {% endif %}
        {% if item.summary %}<p>{{ item.summary }}</p>{% endif %}
      </article>
      {% endfor %}
    </div>
    <p><a class="inline-link" href="{{ '/publications' | relative_url }}">View full publication list</a></p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="page-card contact-banner">
      <div class="contact-banner-copy">
        <h2>Research Contact</h2>
        <p>
          We welcome inquiries about research collaboration, student opportunities,
          and membrane-enabled separation topics connected to the themes above.
        </p>
      </div>
      <div class="contact-banner-meta">
        <p class="contact-summary-meta"><strong>{{ lab.institution }}</strong></p>
        {% assign primary_email = lab.contact.emails | first %}
        <p class="contact-summary-email">
          <a class="inline-link" href="mailto:{{ primary_email }}">{{ primary_email }}</a>
        </p>
      </div>
      <a class="btn btn-primary" href="{{ '/contact' | relative_url }}">Get in touch</a>
    </div>
  </div>
</section>
