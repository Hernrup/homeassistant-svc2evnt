"""
The "svc2evnt" custom component.
This component implements a simple way of triggering a generic event through a service call.

Configuration:

To use the hello_word component you will need to add the following to your
configuration.yaml file.
svc2evnt:
"""

__version__ = "0.0.0"

# The domain of your component. Should be equal to the name of your component.
DOMAIN = "svc2evnt"


def setup(hass, config):
    hass.states.set('svc2evnt.initialized', True)

    def handle_hello(call):
        """Handle the service call."""
        data = call.data
        event_id = data['event_id']
        payload = data['data']
        print(data)
        hass.bus.fire(event_id, payload)
        print('sent')


    hass.services.register(DOMAIN, "fire_event", handle_hello)

    # Return boolean to indicate that initialization was successfully.
    return True