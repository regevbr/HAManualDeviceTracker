A Home Assistant custom integration for manually updated device tracker.

Device should be updated via automations only

# Installation:

Copy the manual_device_tracker folder and all of its contents into your Home Assistant's custom_components folder. This is often located inside of your /config folder. If you are running Hass.io, use SAMBA to copy the folder over. If you are running Home Assistant Supervised, the custom_components folder might be located at /usr/share/hassio/homeassistant. It is possible that your custom_components folder does not exist. If that is the case, create the folder in the proper location, and then copy the manual_device_tracker folder and all of its contents inside the newly created custom_components folder.

Alternatively, you can install manual_device_tracker through HACS by adding this repository.

# Configuration:

Add the proper entry to your configuration.yaml file. Make sure to save when you are finished editing configuration.yaml.

```yaml
device_tracker:
  - platform: manual_device_tracker
    new_device_defaults:
      track_new_devices: true
```

Restart Home Assistant when finished editing.

# Usage:

Use the [device_Tracker.see service](https://www.home-assistant.io/integrations/device_tracker/#device_trackersee-service) to update the tracker