A Home Assistant custom integration for manually updated device tracker.

Device should be updated via automations only

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