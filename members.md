---
layout: default
title: Members
---
{% assign members = site.data.members %}
{% assign lab = site.data.lab %}
{% assign postdocs = members | where: "role_group", "Postdoctoral Researcher" %}
{% assign interns = members | where: "role_group", "Internship Master Researcher" %}
{% assign students = members | where_exp: "item", "item.role_group contains 'Student'" %}
{% assign alumni = site.data.alumni %}

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

    {% if interns.size > 0 %}
    <section class="profile-section">
      <h2 class="section-title section-title-sm">Internship Master Researchers</h2>
      <div class="member-grid">
        {% for member in interns %}
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

    {% if alumni.size > 0 %}
    <section class="profile-section">
      <h2 class="section-title section-title-sm">Alumni</h2>
      <p class="section-lead alumni-lead">Degrees completed in MS<sup>3</sup>L. Members who stayed on in the lab are also listed above.</p>
      <div class="alumni-grid">
        {% for person in alumni %}
        <article class="alumni-card">
          <h3>{{ person.name }}</h3>
          <p class="alumni-degree">{{ person.degree }}<span class="alumni-period">{{ person.period }}</span></p>
          {% if person.institution %}<p class="alumni-institution">{{ person.institution }}</p>{% endif %}
          {% if person.research %}<p class="alumni-research">{{ person.research }}</p>{% endif %}
          {% if person.now %}<p class="alumni-now"><span>Now</span>{{ person.now }}</p>{% endif %}
        </article>
        {% endfor %}
      </div>
    </section>
    {% endif %}
  </div>
</div>
