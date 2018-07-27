# -*- coding: utf-8 -*-
import time

debug = False
try:
    # noinspection PyUnresolvedReferences
    import RPi.GPIO as GPIO
except:
    print("Could not import GPIO, using debug method")
    debug = True


def setup(out_pins, in_pins):
    if debug:
        print("Setting to output:", out_pins)
        print("Setting to input:", in_pins)
        return

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    for out_pin in out_pins:
        GPIO.setup(out_pin, GPIO.OUT)
    for in_pin in in_pins:
        GPIO.setup(in_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def set_on(pin):
    if debug:
        print("Enabling output on", pin)
        return

    GPIO.output(pin, GPIO.HIGH)


def set_off(pin):
    if debug:
        print("Disabling output on", pin)
        return

    GPIO.output(pin, GPIO.LOW)


def wait_on(pin):
    if debug:
        print("Waiting for rising edge on pin", pin)
        input("Press enter to continue: ")
        return

    GPIO.wait_for_edge(pin, GPIO.RISING)


def wait_off(pin):
    if debug:
        print("Waiting for falling edge on pin", pin)
        input("Press enter to continue: ")
        return

    GPIO.wait_for_edge(pin, GPIO.FALLING)


def wait_toggle(pin, min_time=1000):
    while True:
        wait_on(pin)
        start = time.time()
        wait_off(pin)
        end = time.time()

        if (end - start) * 1000 >= min_time:
            break


def clean():
    if not debug:
        GPIO.cleanup()
