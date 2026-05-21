---
layout: default
title: Members
---
{% assign members = site.data.members %}
{% assign lab = site.data.lab %}
{% assign postdocs = members | where: "role_group", "Postdoctoral Researcher" %}
{% assign students = members | where_exp: "item", "item.role_group contains 'Student'" %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ lab.members.title }}</h1>
      <p>{{ lab.members.lead }}</p>
    </div>

        {% if postdocs.size > 0 %}
    <section class="profile-section">
      <h2 class="section-title section-title-sm">Postdoctoral Researchers</h2>
      <div class="member-grid">
        {% for member in postdocs %}
        <article class="member-card-compact">
          <div class="profile-photo">
            {% if member.image_url %}
            <img src="{{ member.image_url | relative_url }}" alt="{{ member.name }} profile photo" loading="lazy">
            {% endif %}
          </div>
          <div class="profile-body">
            <div class="profile-label">{{ member.role_group }}</div>
            <h3>{{ member.name }}</h3>
            <p class="profile-role">{{ member.position }}</p>
            {% if member.research %}<p><strong>Research:</strong> {{ member.research }}</p>{% endif %}
            <button class="btn btn-secondary btn-compact" type="button" data-modal-open="member-{{ member.name | slugify }}">Details</button>
          </div>
        </article>

        <div class="content-modal" id="member-{{ member.name | slugify }}" hidden>
          <div class="content-modal-panel" role="dialog" aria-modal="true" aria-labelledby="member-title-{{ member.name | slugify }}">
            <button class="modal-close" type="button" data-modal-close aria-label="Close details">Close</button>
            <div class="modal-layout">
              <div class="modal-media profile-photo">
                {% if member.image_url %}
                <img src="{{ member.image_url | relative_url }}" alt="{{ member.name }} profile photo" loading="lazy">
                {% endif %}
              </div>
              <div class="modal-body">
                <div class="profile-label">{{ member.role_group }}</div>
                <h2 id="member-title-{{ member.name | slugify }}">{{ member.name }}</h2>
                <p class="profile-role">{{ member.position }}</p>
                {% if member.affiliation %}<p class="profile-affiliation">{{ member.affiliation }}</p>{% endif %}
                {% if member.email %}<p><a class="inline-link" href="mailto:{{ member.email }}">{{ member.email }}</a></p>{% endif %}
                {% if member.research %}<p><strong>Research:</strong> {{ member.research }}</p>{% endif %}
                {% if member.achievements %}
                <h3>Highlights</h3>
                <ul>
                  {% for item in member.achievements %}
                  <li>{{ item }}</li>
                  {% endfor %}
                </ul>
                {% endif %}
              </div>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </section>
    {% endif %}

    {% if students.size > 0 %}
    <section class="profile-section">
      <h2 class="section-title section-title-sm">Students</h2>
      <div class="member-grid">
        {% for member in students %}
        <article class="member-card-compact">
          <div class="profile-photo">
            {% if member.image_url %}
            <img src="{{ member.image_url | relative_url }}" alt="{{ member.name }} profile photo" loading="lazy">
            {% endif %}
          </div>
          <div class="profile-body">
            <div class="profile-label">{{ member.role_group }}</div>
            <h3>{{ member.name }}</h3>
            <p class="profile-role">{{ member.position }}</p>
            {% if member.affiliation %}<p class="profile-affiliation">{{ member.affiliation }}</p>{% endif %}
            {% if member.research %}<p><strong>Research:</strong> {{ member.research }}</p>{% endif %}
            {% if member.achievements %}
            <details class="member-achievements">
              <summary>Highlights</summary>
              <ul>
                {% for item in member.achievements %}
                <li>{{ item }}</li>
                {% endfor %}
              </ul>
            </details>
            {% endif %}
            <button class="btn btn-secondary btn-compact" type="button" data-modal-open="member-{{ member.name | slugify }}">Details</button>
          </div>
        </article>

        <div class="content-modal" id="member-{{ member.name | slugify }}" hidden>
          <div class="content-modal-panel" role="dialog" aria-modal="true" aria-labelledby="member-title-{{ member.name | slugify }}">
            <button class="modal-close" type="button" data-modal-close aria-label="Close details">Close</button>
            <div class="modal-layout">
              <div class="modal-media profile-photo">
                {% if member.image_url %}
                <img src="{{ member.image_url | relative_url }}" alt="{{ member.name }} profile photo" loading="lazy">
                {% endif %}
              </div>
              <div class="modal-body">
                <div class="profile-label">{{ member.role_group }}</div>
                <h2 id="member-title-{{ member.name | slugify }}">{{ member.name }}</h2>
                <p class="profile-role">{{ member.position }}</p>
                {% if member.affiliation %}<p class="profile-affiliation">{{ member.affiliation }}</p>{% endif %}
                {% if member.email %}<p><a class="inline-link" href="mailto:{{ member.email }}">{{ member.email }}</a></p>{% endif %}
                {% if member.research %}<p><strong>Research:</strong> {{ member.research }}</p>{% endif %}
                {% if member.achievements %}
                <h3>Highlights</h3>
                <ul>
                  {% for item in member.achievements %}
                  <li>{{ item }}</li>
                  {% endfor %}
                </ul>
                {% endif %}
              </div>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </section>
    {% endif %}
  </div>
</div>
