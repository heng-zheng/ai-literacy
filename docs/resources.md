# AI Watchlist

Not required reading. A lightweight stream of items I’m currently following.  
Sorted by **date added** (newest first).

---

## Latest

{% for x in watchlist_latest(12) %}
### [{{ x.title or "Untitled" }}]({{ x.url }})

<small>
Added {{ x.added or "????-??-??" }}
{% if x.type %} · {{ (x.type or "item")|capitalize }}{% endif %}
{% if x.published %} · Published {{ x.published }}{% endif %}
{% if x.source %} · {{ x.source }}{% endif %}
</small>

{% if x.why %}
{{ x.why }}
{% endif %}

---
{% endfor %}

## Videos & Podcasts

{% for x in watchlist_by_type("video") %}
- **[{{ x.title or "Untitled" }}]({{ x.url }})**{% if x.source %} · {{ x.source }}{% endif %}{% if x.published %} · {{ x.published }}{% endif %}
{% if x.why %}  \n  <small>{{ x.why }}</small>{% endif %}
{% endfor %}

## News & Non-academic Articles

{% for x in watchlist_by_type("news") %}
- **[{{ x.title or "Untitled" }}]({{ x.url }})**{% if x.source %} · {{ x.source }}{% endif %}{% if x.published %} · {{ x.published }}{% endif %}
{% if x.why %}  \n  <small>{{ x.why }}</small>{% endif %}
{% endfor %}

## Scholarly Articles

{% for x in watchlist_by_type("scholarly") %}
- **[{{ x.title or "Untitled" }}]({{ x.url }})**{% if x.source %} · {{ x.source }}{% endif %}{% if x.published %} · {{ x.published }}{% endif %}
{% if x.why %}  \n  <small>{{ x.why }}</small>{% endif %}
{% endfor %}

## Projects & Platforms

{% for x in watchlist_by_type("project") %}
- **[{{ x.title or "Untitled" }}]({{ x.url }})**{% if x.source %} · {{ x.source }}{% endif %}{% if x.published %} · {{ x.published }}{% endif %}
{% if x.why %}  \n  <small>{{ x.why }}</small>{% endif %}
{% endfor %}

## Courses

{% for x in watchlist_by_type("course") %}
- **[{{ x.title or "Untitled" }}]({{ x.url }})**{% if x.source %} · {{ x.source }}{% endif %}{% if x.published %} · {{ x.published }}{% endif %}
{% if x.why %}  \n  <small>{{ x.why }}</small>{% endif %}
{% endfor %}
