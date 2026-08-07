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
        {% include member-card.html member=member %}
        {% endfor %}
      </div>
    </section>
    {% endif %}

    {% if students.size > 0 %}
    <section class="profile-section">
      <h2 class="section-title section-title-sm">Students</h2>
      <div class="member-grid">
        {% for member in students %}
        {% include member-card.html member=member %}
        {% endfor %}
      </div>
    </section>
    {% endif %}
  </div>
</div>
