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

        <ul class="pi-appointments">
          {% for appointment in pi.current_appointments %}
          <li>
            <span class="pi-appointment-title">{{ appointment.title }}</span>
            <span class="pi-appointment-org">{{ appointment.organization }}</span>
          </li>
          {% endfor %}
        </ul>
        <p class="pi-appointment-period">{{ pi.current_period }}</p>

        <p class="pi-research-focus"><strong>Research focus:</strong> {{ member_pi.research }}</p>

        <h3>Career</h3>
        <ul class="pi-career">
          {% for item in pi.career %}
          <li class="pi-career-item">
            <span class="pi-career-period">{{ item.period }}</span>
            <span class="pi-career-role">
              <span class="pi-career-title">{{ item.title }}</span>
              <span class="pi-career-affiliation">{{ item.affiliation }}{% if item.note %} ({{ item.note }}){% endif %}</span>
            </span>
          </li>
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
