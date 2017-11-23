import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

from pyA20.gpio import gpio
from pyA20.gpio import port

class RGBControl:
    def __init__(self, red, green, blue):
        self.rPin = red
        self.gPin = green
        self.bPin = blue

        gpio.init()
        gpio.setcfg(self.rPin, gpio.OUTPUT)
        gpio.setcfg(self.gPin, gpio.OUTPUT)
        gpio.setcfg(self.bPin, gpio.OUTPUT)

    def r(self, type="on"):
        if(type == "on"):
            gpio.output(self.rPin, 0)
        else:
            gpio.output(self.rPin, 1)

    def g(self, type="on"):
        if(type == "on"):
            gpio.output(self.gPin, 0)
        else:
            gpio.output(self.gPin, 1)

    def b(self, type="on"):
        if(type == "on"):
            gpio.output(self.bPin, 0)
        else:
            gpio.output(self.bPin, 1)

    def off(self):
        self.r("off")
        self.g("off")
        self.b("off")

    def white(self):
        self.r("on")
        self.g("on")
        self.b("on")

    def red(self):
        self.r("on")
        self.g("off")
        self.b("off")

    def green(self):
        self.r("off")
        self.g("on")
        self.b("off")

    def blue(self):
        self.r("off")
        self.g("off")
        self.b("on")

    def yellow(self):
        self.r("on")
        self.g("on")
        self.b("off")

    def magenta(self):
        self.r("on")
        self.g("off")
        self.b("on")

    def cyan(self):
        self.r("off")
        self.g("on")
        self.b("on")
