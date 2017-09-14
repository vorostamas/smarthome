# Jinja Helpers and Sample Scripts to get you started

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

### Here is the sample output of the above script:

```
-------------------------------------------------- ------------------------------
Entity ID                                          Name                          
-------------------------------------------------- ------------------------------
input_boolean.do_not_disturb                       Do Not Disturb
input_boolean.home_assistant_restart               Home Assistant
light.dinette                                      Kitchen Light
light.family_room                                  Family Room Lights
light.master_bedroom                               Master Bedroom Lights
light.tradfri_bulb_e26_ws_opal_980lm               Office Room Light
switch.wemobackyardlightswitch                     Backyard Lights
switch.wemofrontporchlightswitch                   Front Porch Lights
switch.wemoswitch1                                 Front Room Light
-------------------------------------------------- ------------------------------
```

## To generate template sensors based on the device_trackers,  run the following script and copy the output and use it in your code

Copy the output of the code in your dev-templates, and use it in your code directly

```
- platform: template
  sensors:
{% for state in states.device_tracker -%}
  {% if loop.first %}{% elif loop.last %}
{% else %}
{% endif %}    {{state.entity_id|replace("device_tracker.","") -}}_template:
      value_template: {{ '"{% if is_state' }}('{{-state.entity_id -}}', 'home') {{'%}online{% else %}offline{% endif %}"'}}
      friendly_name: "{{ state.attributes.friendly_name|title|replace("_"," ",) if state.attributes.friendly_name is defined else state.name|title|replace("_"," ",) }}"
      icon_template: {{ '"{% if is_state' }}('{{-state.entity_id -}}', 'home') {{'%}mdi:check-circle{% else %}mdi:alert-circle{% endif %}"'}}
{% endfor %}
```

### Here is the sample output of the above script:

```
    suresh_suresh_template:
      value_template: "{% if is_state('device_tracker.suresh_suresh', 'home') %}online{% else %}offline{% endif %}"
      friendly_name: "Suresh"
      icon_template: "{% if is_state('device_tracker.suresh_suresh', 'home') %}mdi:check-circle{% else %}mdi:alert-circle{% endif %}"

    srinika_srinika_template:
      value_template: "{% if is_state('device_tracker.srinika_srinika', 'home') %}online{% else %}offline{% endif %}"
      friendly_name: "Srinika"
      icon_template: "{% if is_state('device_tracker.srinika_srinika', 'home') %}mdi:check-circle{% else %}mdi:alert-circle{% endif %}"

    ...more entries!    
```

## Group Management:

To see the list of `groups`,  and the entities that belong to the group, run this script

```
{% for group in states.group%}
Group Name: {{ group.name }}, Entity ID: {{ group.entity_id }}
{{ "-".ljust(50, '-') }} {{ "-".ljust(30, '-') }}
{% for entity in group.attributes.entity_id|list() %}
{{- entity }}
{% endfor %}
{% endfor %}
```

### Here is the sample output of the above script:

```
Group Name: Date Time, Entity ID: group.date_time
-------------------------------------------------- ------------------------------
sensor.time
sensor.date
binary_sensor.workday_sensor
sensor.ha_installed_version
sensor.ha_current_version
sensor.ha_last_restart


Group Name: Door Sensors, Entity ID: group.door_sensors
-------------------------------------------------- ------------------------------
binary_sensor.ecolink_door_sensor_sensor
binary_sensor.ecolink_door_sensor_sensor_2

...more entries!
```

## To see all the Entities and corresponding attributes all in one place, run this script:

```
{{ "_".ljust(90, "_") }}
{{ "Entity ID".ljust(50) }}{{ "Entity Name" }}
  {{ "Attribute Name".ljust(50) }}{{ "Attribute Value" }}

{% for item in states %}
{{ "_".ljust(90, "_") }}
{{ item.entity_id.ljust(50) }}
  {{ "State".ljust(50) }}: {{ item.state}}
  {{ "Domain".ljust(50) }}: {{ item.domain}}
  {{ "Object ID".ljust(50) }}: {{ item.object_id}}
  {{ "Last Updated".ljust(50) }}: {{ item.last_updated}}
  {{ "Last Changed".ljust(50) }}: {{ item.last_changed}}
{%- for attrib in item.attributes|sort() %}
{%- if attrib is defined %} 
  {{attrib.ljust(50)}}: {{ item.attributes[attrib] }} 
{%- endif %}
{%- endfor %}
{%- endfor %}
```

### The following is the sample output of the above script:

```
__________________________________________________________________________________________
automation.alert_low_battery_level_of_sensors     
  State                                             : on
  Domain                                            : automation
  Object ID                                         : alert_low_battery_level_of_sensors
  Last Updated                                      : 2017-09-14 00:19:00.697024+00:00
  Last Changed                                      : 2017-09-14 00:19:00.697024+00:00 
  friendly_name                                     : Alert Low Battery Level of Sensors 
  icon                                              : mdi:arrow-right-drop-circle 
  last_triggered                                    : None
__________________________________________________________________________________________
automation.alert_super_heavy_winds                
  State                                             : on
  Domain                                            : automation
  Object ID                                         : alert_super_heavy_winds
  Last Updated                                      : 2017-09-14 00:19:00.739659+00:00
  Last Changed                                      : 2017-09-14 00:19:00.739659+00:00 
  friendly_name                                     : Alert Super Heavy Winds 
  hidden                                            : True 
  icon                                              : mdi:arrow-right-drop-circle 
  last_triggered                                    : None

  ...more entries!
```

## Temperature Conversion

Sample code that uses macros to convert temperature from Fahrenheit to Centigrade and vice versa

```
{%- macro F2C(temperature) -%}
{% set tmp =(((temperature - 32) *5)/9) %}
{{- " %0.2f" % tmp }}
{%- endmacro -%}

{%- macro C2F(temperature) -%}
{% set tmp =(((temperature *9) /5) + 32) %}
{{- " %0.2f" % tmp -}}
{%- endmacro -%}

75.00 degrees of Fahrenheit is equal to: {{- F2C(75.00) }} Centigrade
23.89 degrees of Centigrade is equal to: {{- C2F(23.89) }} Fahrenheit
```

### Here is the output of the above script:

```
75.00 degrees of Fahrenheit is equal to: 23.89 Centigrade
23.89 degrees of Centigrade is equal to: 75.00 Fahrenheit
```

