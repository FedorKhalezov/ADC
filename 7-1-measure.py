import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17