# -*- coding: utf-8 -*-

try:
    import time
    import random

    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing GPIO.lib")

# Nummerierung der PIN statt GPIO Nummer benutzen
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Pins auf Output setzen

GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

# Pin 7 (GPIO4) als Input definieren, Variablenname Taste
GPIO.setup(7, GPIO.IN)
Taste = 7

# Testdurchgang 40
GPIO.output(40, GPIO.HIGH)
time.sleep(1.5 * random.random())
GPIO.output(40, GPIO.LOW)
# Testdurchgang 38
GPIO.output(38, GPIO.HIGH)
time.sleep(1.5 * random.random())
GPIO.output(38, GPIO.LOW)
# Testdurchgang 36
GPIO.output(36, GPIO.HIGH)
time.sleep(1.5 * random.random())
GPIO.output(36, GPIO.LOW)

time.sleep(1.5 * random.random())

# Random Blinken lassen
count = 0

while count < 66:
    GPIO.output(40, GPIO.HIGH)
    time.sleep(0.15 * random.random())

    GPIO.output(38, GPIO.HIGH)
    time.sleep(0.15 * random.random())

    GPIO.output(40, GPIO.LOW)
    GPIO.output(38, GPIO.LOW)
    GPIO.output(36, GPIO.HIGH)
    time.sleep(0.15 * random.random())

    GPIO.output(38, GPIO.HIGH)
    GPIO.output(36, GPIO.LOW)
    time.sleep(0.15 * random.random())

    GPIO.output(40, GPIO.HIGH)
    time.sleep(0.15 * random.random())

    GPIO.output(38, GPIO.LOW)
    time.sleep(0.15 * random.random())
    count = count + 1

GPIO.cleanup()
