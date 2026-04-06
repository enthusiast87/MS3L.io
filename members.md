---
layout: default
title: Members
---
{% assign members = site.data.members %}
{% assign lab = site.data.lab %}

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
      </div>
    </section>
    {% endfor %}

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
