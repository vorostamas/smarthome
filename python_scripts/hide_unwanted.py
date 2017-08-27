'''
@Author         :       Mahasri Kalavala
@Date           :       08/27/2017
@Description    :       This python script hides all the sensors that are Online, so that 
                        ONLY the Offline sensors are visible in the UI
'''

offlineCount = 0
for entity_id in hass.states.entity_ids('sensor'):
    entity_state_object = hass.states.get(entity_id)
    if entity_state_object.state == 'Online':
        attributes = entity_state_object.attributes.copy()
        attributes['hidden'] = True
        hass.states.set(entity_id, entity_state_object.state, attributes=attributes)
        offlineCount = offlineCount + 1

logger.info("{} sensors are marked hidden.".format(offlineCount))