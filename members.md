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

    {% assign principal_investigators = members | where: "role_group", "Principal Investigator" %}
    {% for member in principal_investigators %}
    <section class="profile-section">
      <div class="profile-card">
        <div class="profile-photo"></div>
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
          Additional student, researcher, and collaborator profiles can be added as the current MS^3L roster is finalized.
          The page structure is ready for future expansion without redesigning the site again.
        </p>
      </div>
    </section>
  </div>
</div>
