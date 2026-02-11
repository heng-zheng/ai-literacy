# AI Watchlist

Not required reading. A lightweight stream of items I’m currently following.  
Sorted by **date added** (newest first).

---

## Latest

{% for x in watchlist_latest(12) %}
### [{{ x.title or "Untitled" }}]({{ x.url }})

<small>
Added {{ x.added or "????-??-??" }}{% if x.type %} · {{ (x.type or "item")|capitalize }}{% endif %}{% if x.published %} · Published {{ x.published }}{% endif %}{% if x.source %} · {{ x.source }}{% endif %}
</small>

{% if x.why %}
{{ x.why }}
{% endif %}

{% if not loop.last %}
---
{% endif %}

{% endfor %}

## By Category

{% for t in watchlist_types() %}
### {{ t|capitalize }}

{% for x in watchlist_by_type(t) %}
- **[{{ x.title or "Untitled" }}]({{ x.url }})**{% if x.source %} · {{ x.source }}{% endif %}{% if x.published %} · {{ x.published }}{% endif %}{% if x.why %}  
  <small>{{ x.why }}</small>{% endif %}
{% endfor %}

---
{% endfor %}
