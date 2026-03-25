---
layout: default
title: Join Us
---
{% assign join = site.data.lab.join_us %}

<div class="page-wrap">
  <div class="container">
    <div class="page-card">
      <h1>{{ join.title }}</h1>
      <p>{{ join.body }}</p>
      <p><a class="btn btn-primary" href="{{ join.cta_url | relative_url }}">{{ join.cta_label }}</a></p>
    </div>
  </div>
</div>
