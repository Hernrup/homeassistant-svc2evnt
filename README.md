svc2evnt
==========
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![action 1 badge](https://github.com/Hernrup/homeassistant-svc2evnt/workflows/Semantic%20Release/badge.svg)
[![action 2 badge](https://github.com/Hernrup/homeassistant-svc2evnt/workflows/Validate%20with%20hassfest/badge.svg)
[![badge](https://img.shields.io/github/issues/Hernrup/homeassistant-svc2evnt)
[![badge](https://img.shields.io/github/license/Hernrup/homeassistant-svc2evnt)

A Home Assistant integration that implements a simple way of triggering a generic event through a service call.

### Installation
The integration can be installed from `HACS` or by copying the files under `custom_components` into the config directory.

### Configuration

To use the component you will need to add the following to your
`configuration.yaml` file.

The component has no configuration options.

```
svc2evnt:
```
### Usage

| Name | Type | Requried | Supported options | Description |
| ----------------- | ------ | -------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `action` | string | yes | call-service | Action to perform |
| `service` | string | yes | svc2evnt.fire_event | Service to call |
| `service_data` | string | yes | Se below |  |

#### Service data

| Name | Type | Requried | Supported options | Description |
| ----------------- | ------ | -------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `event_type` | string | yes | Any event type, ex `custom_event`| Event type |
| `data` | string | yes |  | Any data to send with event |

#### Example
This example uses the custom component ["button-card"](https://github.com/custom-cards/button-card/blob/master/README.md) 

Send a custom event with event type `custom_event` and with data `domain: media` and `id: playpause`.


```yaml
  type: 'custom:button-card'
  tap_action:
    action: call-service
    service: svc2evnt.fire_event
    service_data:
      event_type: custom_event
      data:
        domain: media
        id: playpause
  show_icon: true
  icon: 'mdi:play-pause'
```
