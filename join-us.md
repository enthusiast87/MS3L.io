---
layout: default
title: Join Us
---
{% assign join = site.data.lab.join_us %}
{% assign contact = site.data.lab.contact %}
{% assign primary_email = contact.emails | first %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ join.title }}</h1>
      <p>{{ join.body }}</p>
    </div>

    <section class="profile-section">
      <h2 class="section-title section-title-sm">{{ join.work.title }}</h2>
      <p class="section-lead">{{ join.work.lead }}</p>
      <div class="card-grid three">
        {% for item in join.work.items %}
        <div class="card">
          <h3>{{ item.title }}</h3>
          <p>{{ item.summary }}</p>
          {% if item.detail %}
          <p class="joinus-grounding">{{ item.detail }}</p>
          {% endif %}
        </div>
        {% endfor %}
      </div>
    </section>

    <section class="profile-section">
      <h2 class="section-title section-title-sm">{{ join.positions.title }}</h2>
      <div class="card-grid three">
        {% for item in join.positions.items %}
        <div class="card">
          <h3>{{ item.title }}</h3>
          <p>{{ item.summary }}</p>
        </div>
        {% endfor %}
      </div>
    </section>

    <section class="profile-section">
      <h2 class="section-title section-title-sm">How to reach out</h2>
      <div class="card-grid two">
        <div class="card">
          <h3>Start with a short email</h3>
          <p>{{ contact.position_inquiry_note }}</p>
          <ol class="joinus-steps">
            {% for item in contact.position_inquiry_items %}
            <li><span class="joinus-step-num">{{ forloop.index }}</span><span>{{ item }}</span></li>
            {% endfor %}
          </ol>
        </div>
        <div class="card">
          <h3>Where to send it</h3>
          <p><strong>Jihoon Kim</strong> | Principal Investigator<br>{{ site.data.lab.institution }}, Daejeon</p>
          <p><a class="inline-link" href="mailto:{{ primary_email }}">{{ primary_email }}</a></p>
          <p><a class="btn btn-primary" href="mailto:{{ primary_email }}">Email the PI</a></p>
        </div>
      </div>
    </section>
  </div>
</div>
