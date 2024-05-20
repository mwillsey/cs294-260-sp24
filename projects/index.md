---
layout: default
---

# Final Projects
<ul>
{% for p in site.pages %}
{% if p.layout == 'project' %}
<li markdown="1">
 <a href="{{ p.url | relative_url }}">{{ p.title }}</a>
 <br> by
 {{ p | map: 'authors' | join: ', ' }}
</li>
{% endif %}
{% endfor %}
</ul>