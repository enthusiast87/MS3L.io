---
layout: default
title: Contact
---
{% assign contact = site.data.lab.contact %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ contact.title }}</h1>
      <p>{{ contact.note }}</p>
      <p><strong>Institution:</strong> {{ site.data.lab.institution }}</p>
      <p><strong>Address:</strong> {{ contact.address }}</p>

      <p><strong>Email:</strong></p>
      <ul>
        {% for item in contact.emails %}
        <li><a class="inline-link" href="mailto:{{ item }}">{{ item }}</a></li>
        {% endfor %}
      </ul>
      <p><strong>Phone:</strong> {{ contact.phone }}</p>

      <p>Interested in joining the lab? See <a class="inline-link" href="{{ '/join-us' | relative_url }}">Join Us</a> for positions and how to reach out.</p>
    </div>
  </div>
</div>
