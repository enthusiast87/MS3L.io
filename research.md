---
layout: default
title: Research
---

# Research Themes

{% for item in site.data.research %}
## {{ item.title }}
{{ item.summary }}

{% if item.topics %}
<ul>
  {% for t in item.topics %}
  <li>{{ t }}</li>
  {% endfor %}
</ul>
{% endif %}
{% endfor %}
