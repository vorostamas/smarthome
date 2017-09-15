"""
@ Author      : Suresh Kalavala
@ Date        : 09/14/2017
@ Description : Global String Variable - We can now have global variable
                that holds "String" datatype values

@ Notes:        Copy this file and services.yaml files and place it in your 
                "Home Assistant Config folder\custom_components\" folder

                To use the component, have the following in your .yaml file:
                The 'value' is optional, by default, it is set to 0 

global_variable_string:
  some_string1:
    name: Some String 1 
    icon: mdi:alphabetical

  some_string2:
    name: Some String 2
    value: 'Hello, Home Assistant!'
    icon: mdi:alphabetical

"""

"""
Component to provide global variables for use.

For more details about this component, please refer to the documentation
at https://home-assistant.io/components/global_variable_string/
"""
import asyncio
import logging
import os

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.config import load_yaml_config_file
from homeassistant.const import (ATTR_ENTITY_ID, CONF_ICON, CONF_NAME)
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity
from homeassistant.helpers.entity_component import EntityComponent
from homeassistant.helpers.restore_state import async_get_last_state
from homeassistant.loader import bind_hass

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'global_variable_string'
ENTITY_ID_FORMAT = DOMAIN + '.{}'

ATTR_VALUE   = "value"
DEFAULT_INITIAL = ""

SERVICE_SETVALUE = 'set_value'

SERVICE_SCHEMA = vol.Schema({
    vol.Optional(ATTR_ENTITY_ID): cv.entity_ids,
    vol.Optional(ATTR_VALUE): cv.string,
})

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        cv.slug: vol.Any({
            vol.Optional(CONF_ICON): cv.icon,
            vol.Optional(ATTR_VALUE, default=DEFAULT_INITIAL): cv.string,
            vol.Optional(CONF_NAME): cv.string,
        }, None)
    })
}, extra=vol.ALLOW_EXTRA)

@bind_hass
def set_value(hass, entity_id, value):
    hass.add_job(async_set_value, hass, entity_id, value)

@callback
@bind_hass
def async_set_value(hass, entity_id, value):
    hass.async_add_job(hass.services.async_call(
        DOMAIN, SERVICE_SETVALUE, {ATTR_ENTITY_ID: entity_id, ATTR_VALUE: value }))

@asyncio.coroutine
def async_setup(hass, config):
    """Set up a global_variable_string."""
    component = EntityComponent(_LOGGER, DOMAIN, hass)

    entities = []

    for object_id, cfg in config[DOMAIN].items():
        if not cfg:
            cfg = {}

        name = cfg.get(CONF_NAME)
        value = cfg.get(ATTR_VALUE)
        icon = cfg.get(CONF_ICON)

        entities.append(GlobalVariableString(object_id, name, value, icon))

    if not entities:
        return False

    @asyncio.coroutine
    def async_handler_service(service):
        """Handle a call to the global_variable_string services."""
        target_global_variables = component.async_extract_from_service(service)

        if service.service == SERVICE_SETVALUE:
            attr = 'async_set_value'

        tasks = [getattr(global_variable, attr)(service.data[ATTR_VALUE]) 
                  for global_variable in target_global_variables]
        if tasks:
            yield from asyncio.wait(tasks, loop=hass.loop)

    descriptions = yield from hass.async_add_job(
        load_yaml_config_file, os.path.join(
            os.path.dirname(__file__), 'services.yaml')
    )

    hass.services.async_register(
        DOMAIN, SERVICE_SETVALUE, async_handler_service,
        descriptions[DOMAIN][SERVICE_SETVALUE], SERVICE_SCHEMA)

    yield from component.async_add_entities(entities)
    return True


class GlobalVariableString(Entity):
    """Representation of a global_variable_string."""

    def __init__(self, object_id, name, value, icon):
        """Initialize a global_variable_string."""
        self.entity_id = ENTITY_ID_FORMAT.format(object_id)
        self._name = name
        self._state = value
        self._icon = icon
 
    @property
    def should_poll(self):
        """If entity should be polled."""
        return False

    @property
    def name(self):
        """Return name of the global_variable_string."""
        return self._name

    @property
    def icon(self):
        """Return the icon to be used for this entity."""
        return self._icon

    @property
    def state(self):
        """Return the current value of the global_variable_string."""
        return self._state

    @property
    def state_attributes(self):
        """Return the state attributes."""
        return {
            ATTR_VALUE: self._state,
        }

    @asyncio.coroutine
    def async_added_to_hass(self):
        """Call when entity about to be added to Home Assistant."""
        # If not None, we got an initial value.
        if self._state is not None:
            return

        state = yield from async_get_last_state(self.hass, self.entity_id)
        self._state = state and state.state == state

    @asyncio.coroutine
    def async_set_value(self, value):
        self._state = value
        yield from self.async_update_ha_state()
