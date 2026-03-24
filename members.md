---
layout: default
title: Members
---

# Members

{% for m in site.data.members %}
## {{ m.name }}
- Position: {{ m.position }}
- Email: {{ m.email }}
- Research: {{ m.research }}
{% endfor %}
