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
      <p><strong>Institution:</strong> {{ contact.institution }}</p>
      <p><strong>Address:</strong> {{ contact.address }}</p>

      {% if contact.position_inquiry_note %}
      <h2>Position inquiries</h2>
      <p>{{ contact.position_inquiry_note }}</p>
      {% if contact.position_inquiry_items %}
      <ul>
        {% for item in contact.position_inquiry_items %}
        <li>{{ item }}</li>
        {% endfor %}
      </ul>
      {% endif %}
      {% endif %}

      <p><strong>Email:</strong></p>
      <ul>
        {% for item in contact.emails %}
        <li><a class="inline-link" href="mailto:{{ item }}">{{ item }}</a></li>
        {% endfor %}
      </ul>
      <p><strong>Phone:</strong> {{ contact.phone }}</p>
    </div>
  </div>
</div>
