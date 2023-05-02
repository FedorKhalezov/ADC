import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
comp = 4
troyka = 17

gpio.setup(dac, gpio.OUT, initial=gpio.LOW)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def decimal2binary(a):
    return [int(bit) for bit in bin(a)[2:].zfill(bits)]


def adc():
    l = 0
    r = 256
    while (l + 1 < r):
        m = (l + r) // 2
        b = decimal2binary(m)
        gpio.output(dac, b)
        time.sleep(0.07)
        c = gpio.input(comp)
        if (c == 1):
            r = m
        else:
            l = m
    if (c == 1):
        return l
    else:
        return r

    '''
    for i in range(256):
        b = decimal2binary(i)
        gpio.output(dac, b)
        c = gpio.input(comp)
        #print(c)
        time.sleep(0.07)
        if (c == 0):
            return i
    #'''

try:
    while True:
        a = adc()
        print(a)
        print(a, '{:.2f}v'.format(3.3 * a / 256))
        #print(a, 'a')
        #if (a != 0):
            
finally:
    gpio.output(dac, 0)
    gpio.cleanup()