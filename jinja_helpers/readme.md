## To see which entities are exposed to your alexa platform, run the following script

The following entities are exposed to Alexa platform via `emulated_hue`:

```
{{ "-".ljust(50, '-') }} {{ "-".ljust(30, '-') }}
{{ "Entity ID".ljust(50, ' ') }} {{ "Name".ljust(30, ' ') }}
{{ "-".ljust(50, '-') }} {{ "-".ljust(30, '-') }}
{%- for item in states-%}
{%- if item.attributes.emulated_hue %}
{{ item.entity_id.ljust(50, ' ') }} {{ item.name }}
{%- endif -%}
{%- endfor %}
{{ "-".ljust(50, '-') }} {{ "-".ljust(30, '-') }}
```
