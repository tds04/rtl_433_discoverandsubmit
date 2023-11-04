import logging
import json
from mqtt_client import publish_to_topic
from config_loader import load_device_mappings
logging.basicConfig(filename='rtl_433_discoverandsubmit.log', encoding='utf-8', level=logging.DEBUG)

NAMING_KEYS = ["brand", "model", "subtype", "channel", "id"]
DEVICE_MAPPINGS = load_device_mappings()


def sanitize(string):
    """Sanitize a string to be used as a topic component."""
    return string.lower().replace(" ", "_")

def rtl_433_device_topic(data):
    """
    Return rtl_433 device topic to subscribe to for a data element.

    :param data: Device data.
    :return: Formatted topic.
    """
    path_elements = []
    for key in NAMING_KEYS:
        if key in data:
            element = sanitize(str(data[key]))
            path_elements.append(element)
    return '/'.join(path_elements)


def publish_ha_config(client, data, retain=False):
    """
    Publish Home Assistant configuration for a device.

    :param client: MQTT client instance.
    :param data: Device data.
    :param retain: Whether to retain the message on the broker or not.
    """
    # Get model and instance details
    model = data.get("model")
    id= data.get("original_id")
    uid = data.get("id")



    logging.info(f"Model: {model}")
    instance = rtl_433_device_topic(data)
    logging.info(f"Instance: {instance}")
    topicprefix = data.get("topicprefix")

    # Iterate through the mappings and publish configuration for each attribute
    for attribute, mapping in DEVICE_MAPPINGS.items():

        if attribute in data:
            # Construct the topic and payload based on the mapping
            #path = f"homeassistant/{mapping['device_type']}/{instance}/{mapping['object_suffix']}/config"

            path = f"homeassistant/{mapping['device_type']}/{uid}/config"

            logging.debug(f"Path: {path}")
            config = mapping["config"].copy()
            config["name"] = None
            if (data.get("type") is not None):
                type = data.get("type")
                config["state_topic"] = f"{topicprefix}/devices/{type}/{model}/{id}/{attribute}"
            else:
                config["state_topic"] = f"{topicprefix}/devices/{model}/{id}/{attribute}"
            config["unique_id"] = f"rtl_433_{uid}"
            config["device"] = {
                "identifiers": instance,
                "name": uid,
                "model": model,
                "manufacturer": "rtl_433"
            }
            logging.debug(f"Config: {config}")
            # Publish the configuration
            publish_to_topic(client, path, json.dumps(config), retain=retain)


