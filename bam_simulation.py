import random
import gpio_wrapper

# Maximale Anzahl aktivierter Kanäle (inklusive immer an)
MAX_ENABLED = 5

# Button-Pin
INPUT_PIN = 7

# Pins welche immer aktiv sein sollen, wenn die Sequenz läuft
ALWAYS_ON_PINS = [11]

# Random-Kanäle
CHANNELS = [
    {"pin": 40, "minOnTime": 10, "maxOnTime": 50, "minOffTime": 10, "maxOffTime": 50},
    {"pin": 38, "minOnTime": 10, "maxOnTime": 50, "minOffTime": 10, "maxOffTime": 50},
    {"pin": 37, "minOnTime": 10, "maxOnTime": 50, "minOffTime": 10, "maxOffTime": 50},
    {"pin": 36, "minOnTime": 10, "maxOnTime": 50, "minOffTime": 10, "maxOffTime": 50},
    {"pin": 35, "minOnTime": 10, "maxOnTime": 50, "minOffTime": 10, "maxOffTime": 50},
    {"pin": 33, "minOnTime": 10, "maxOnTime": 50, "minOffTime": 10, "maxOffTime": 50},
    {"pin": 32, "minOnTime": 10, "maxOnTime": 50, "minOffTime": 10, "maxOffTime": 50},
    {"pin": 31, "minOnTime": 10, "maxOnTime": 50, "minOffTime": 10, "maxOffTime": 50},
]

# Add counter and state to all channels
for channel in CHANNELS:
    channel["state"] = False
    channel["counter"] = 0

# Setup GPIO mode & pins
gpio_wrapper.setup(ALWAYS_ON_PINS + [it["pin"] for it in CHANNELS], [INPUT_PIN])


def active_channel_count():
    return len(ALWAYS_ON_PINS) + len(list(filter(lambda x: x["counter"] > 0, CHANNELS)))


while True:
    gpio_wrapper.wait_on(INPUT_PIN)
