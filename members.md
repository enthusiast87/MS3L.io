---
layout: default
title: Members
---
{% assign members = site.data.members %}
{% assign lab = site.data.lab %}
{% assign pi = members | where: "role_group", "Principal Investigator" %}
{% assign postdocs = members | where: "role_group", "Postdoctoral Researcher" %}
{% assign students = members | where_exp: "item", "item.role_group contains 'Student'" %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ lab.members.title }}</h1>
      <p>{{ lab.members.lead }}</p>
    </div>

{% for member in members %}
    <section class="profile-section">
      <div class="profile-card">
        <div class="profile-photo">
          {% if member.image_url %}
          <img src="{{ member.image_url }}" alt="{{ member.name }} profile photo">
          {% endif %}
        </div>
        <div class="profile-body">
          <div class="profile-label">{{ member.role_group }}</div>
          <h2>{{ member.name }}</h2>
          <p class="profile-role">{{ member.position }}</p>
          {% if member.affiliation %}
          <p class="profile-affiliation">{{ member.affiliation }}</p>
          {% endif %}
          {% if member.bio %}
          <p>{{ member.bio }}</p>
          {% endif %}
          {% if member.research %}
          <p><strong>Research focus:</strong> {{ member.research }}</p>
          {% endif %}
          {% if member.achievements %}
          <p><strong>Highlights:</strong></p>
          <ul>
            {% for item in member.achievements %}
            <li>{{ item }}</li>
            {% endfor %}
          </ul>
          {% endif %}
          {% if member.email %}
          <p><strong>Email:</strong> <a class="inline-link" href="mailto:{{ member.email }}">{{ member.email }}</a></p>
          {% endif %}
        </div>
      </article>
      {% endfor %}
    </section>
    {% endif %}

    {% if postdocs.size > 0 %}
    <section class="profile-section">
      <h2 class="section-title section-title-sm">Postdoctoral Researchers</h2>
      <div class="member-grid">
        {% for member in postdocs %}
        <article class="member-card-compact">
          <div class="profile-photo">
            {% if member.image_url %}
            <img src="{{ member.image_url }}" alt="{{ member.name }} profile photo">
            {% endif %}
          </div>
          <div class="profile-body">
            <div class="profile-label">{{ member.role_group }}</div>
            <h3>{{ member.name }}</h3>
            <p class="profile-role">{{ member.position }}</p>
            {% if member.research %}<p><strong>Research:</strong> {{ member.research }}</p>{% endif %}
          </div>
        </article>
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
            <img src="{{ member.image_url }}" alt="{{ member.name }} profile photo">
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
          </div>
        </article>
        {% endfor %}
      </div>
    </section>
    {% endif %}

    <section class="member-note">
      <div class="page-card">
        <h2>Team updates</h2>
        <p>
          This member list is migrated from the current Google Site structure and includes PI, graduate students, and postdoctoral researchers.
        </p>
      </div>
    </section>
  </div>
</div>
