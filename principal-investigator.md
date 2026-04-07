---
layout: default
title: Principal Investigator
---
{% assign pi = site.data.lab.introduction.principal_investigator %}
{% assign member_pi = site.data.members | where: "role_group", "Principal Investigator" | first %}

<div class="page-wrap">
  <div class="container">
    <div class="profile-card">
      <div class="profile-photo">
        {% if member_pi.image_url %}
        <img src="{{ member_pi.image_url }}" alt="{{ member_pi.name }} profile photo">
        {% endif %}
      </div>
      <div class="profile-body">
        <div class="profile-label">Principal Investigator</div>
        <h2>{{ site.data.lab.principal_investigator.name }}</h2>
        <p class="profile-role">{{ pi.current_role }}</p>
        <p class="profile-affiliation">{{ pi.current_affiliation }}</p>
        <p><strong>Research focus:</strong> {{ site.data.lab.principal_investigator.summary }}</p>

        <h3>Career</h3>
        <ul>
          {% for item in pi.previous_positions %}
          <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
    </div>
  </div>
</div>
