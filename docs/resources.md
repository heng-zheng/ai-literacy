# AI Watchlist

Not required reading. A curated stream of items I’m currently following.

## Latest additions
{% for x in watchlist_latest(8) %}
- **Added:** {{ x.added }} · **Type:** {{ x.type|capitalize }}
  {% if x.published %} · **Published:** {{ x.published }}{% endif %}
  {% if x.source %} · **Source:** {{ x.source }}{% endif %}  
  **{{ x.title }}**  
  {% if x.why %}{{ x.why }}{% endif %}  
  [Link]({{ x.url }})
{% endfor %}

## Videos & Podcasts
{% for x in watchlist_by_type("video") %}
- **Added:** {{ x.added }}{% if x.published %} (Published: {{ x.published }}){% endif %}  
  **{{ x.title }}**{% if x.source %} ({{ x.source }}){% endif %}  
  {% if x.why %}{{ x.why }}{% endif %} [Link]({{ x.url }})
{% endfor %}

## News & Non-academic Articles
{% for x in watchlist_by_type("news") %}
- **Added:** {{ x.added }}{% if x.published %} (Published: {{ x.published }}){% endif %}  
  **{{ x.title }}**{% if x.source %} ({{ x.source }}){% endif %}  
  {% if x.why %}{{ x.why }}{% endif %} [Link]({{ x.url }})
{% endfor %}

## Scholarly Articles
{% for x in watchlist_by_type("scholarly") %}
- **Added:** {{ x.added }}{% if x.published %} (Published: {{ x.published }}){% endif %}  
  **{{ x.title }}**{% if x.source %} ({{ x.source }}){% endif %}  
  {% if x.why %}{{ x.why }}{% endif %} [Link]({{ x.url }})
{% endfor %}
