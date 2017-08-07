# -*- coding: utf-8 -*-
import time
import random
import gpio_wrapper

# Maximale Anzahl aktivierter Kanäle (inklusive immer an)
MAX_ENABLED = 3

# Button-Pin
INPUT_PIN = 7

# Pins welche immer aktiv sein sollen, wenn die Sequenz läuft
ALWAYS_ON_CHANNELS = [29]

# Random-Kanäle
CHANNELS = [
    {"pin": 40, "minOnTime": 1000, "maxOnTime": 5000},
    {"pin": 38, "minOnTime": 1000, "maxOnTime": 5000},
    {"pin": 37, "minOnTime": 1000, "maxOnTime": 5000},
    {"pin": 36, "minOnTime": 1000, "maxOnTime": 5000},
    {"pin": 35, "minOnTime": 1000, "maxOnTime": 5000},
    {"pin": 33, "minOnTime": 1000, "maxOnTime": 5000},
    {"pin": 32, "minOnTime": 1000, "maxOnTime": 5000},
    {"pin": 31, "minOnTime": 1000, "maxOnTime": 5000},
]

VIDEO_LENGTH_SECONDS = 10

# Setup GPIO mode & pins
gpio_wrapper.setup(ALWAYS_ON_CHANNELS + [it["pin"] for it in CHANNELS], [INPUT_PIN])


def reset_channels():
    for channel in CHANNELS:
        channel["state"] = False
        channel["counter"] = 0


def active_channel_count():
    return len(ALWAYS_ON_CHANNELS) + len(list(filter(lambda x: x["state"], CHANNELS)))


def find_any_off_channel():
    off_channels = [x for x in CHANNELS if not x["state"]]
    return off_channels[random.randint(0, len(off_channels) - 1)]


def toggle_channel_random(channel):
    if channel["state"]:
        gpio_wrapper.set_off(channel["pin"])
    else:
        gpio_wrapper.set_on(channel["pin"])
        channel["counter"] = random.randint(channel["minOnTime"], channel["maxOnTime"])
    channel["state"] = not channel["state"]


def update_channels(time_step):
    for channel in CHANNELS:
        before_state = channel["state"]
        channel["counter"] -= time_step

        new_state = channel["counter"] > 0

        if before_state == new_state:
            continue

        channel["state"] = new_state
        if new_state:
            gpio_wrapper.set_on(channel["pin"])
        else:
            gpio_wrapper.set_off(channel["pin"])


while True:
    reset_channels()
    gpio_wrapper.wait_on(INPUT_PIN)
    # TODO play video
    for channel in ALWAYS_ON_CHANNELS:
        gpio_wrapper.set_on(channel)

    time_ms = 0
    time_step_ms = 10
    while time_ms < VIDEO_LENGTH_SECONDS * 1000:
        if active_channel_count() < MAX_ENABLED:
            toggle_channel_random(find_any_off_channel())

        time.sleep(0.01)
        time_ms += time_step_ms
        update_channels(time_step_ms)

    for pin in ALWAYS_ON_CHANNELS + [channel["pin"] for channel in CHANNELS]:
        gpio_wrapper.set_off(pin)
