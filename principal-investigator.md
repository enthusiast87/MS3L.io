---
layout: default
title: Principal Investigator
---
{% assign pi = site.data.lab.introduction.principal_investigator %}
{% assign member_pi = site.data.members | where: "role_group", "Principal Investigator" | first %}

<div class="page-wrap">
  <div class="container">
    <div class="profile-card pi-profile-card">
      <div class="profile-photo pi-profile-photo">
        {% if member_pi.image_url %}
        <img src="{{ member_pi.image_url | relative_url }}" alt="{{ member_pi.name }} profile photo" loading="lazy">
        {% endif %}
      </div>
      <div class="profile-body">
        <div class="profile-label">Principal Investigator</div>
        <h2>{{ member_pi.name }}</h2>
        <p class="profile-role">{{ pi.current_role }}</p>
        <p class="profile-affiliation">{{ pi.current_affiliation }}</p>
        <p><strong>Research focus:</strong> {{ member_pi.research }}</p>

        <h3>Career</h3>
        <ul>
          {% for item in pi.previous_positions %}
          <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
    </div>

    <div class="pi-details">
      {% if pi.biography %}
      <section class="page-card pi-detail-card">
        <h2>Short Biography</h2>
        {% for paragraph in pi.biography %}
        <p>{{ paragraph }}</p>
        {% endfor %}
      </section>
      {% endif %}

      {% if pi.research_interests %}
      <section class="page-card pi-detail-card">
        <h2>Research Interests</h2>
        {% for paragraph in pi.research_interests %}
        <p>{{ paragraph }}</p>
        {% endfor %}
      </section>
      {% endif %}
    </div>
  </div>
</div>
