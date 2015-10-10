#!/usr/bin/env python
"""Read button.

Make gpio input and enable pull-up resistor.
"""

import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import connector
from pyA20.gpio import port

__author__ = "Stefan Mavrodiev"
__copyright__ = "Copyright 2014, Olimex LTD"
__credits__ = ["Stefan Mavrodiev"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "support@olimex.com"

led = connector.gpio1p38    # This is the same as port.PH2
button = connector.gpio1p40  #CHOW

"""Init gpio module"""
gpio.init()

"""Set directions"""
gpio.setcfg(led, gpio.OUTPUT)
gpio.setcfg(button, gpio.INPUT)

"""Enable pullup resistor"""
gpio.pullup(button, gpio.PULLUP)
#gpio.pullup(button, gpio.PULLDOWN)     # Optionally you can use pull-down resistor
state =1
value_out = 1
try:
    print ("Press CTRL+C to exit")
    while True:
	"""Since we use pull-up the logic will be inverted"""
        gpio.output(led,  value_out)
	print "led out value is %d"%value_out
	if value_out == 1:	value_out = 0
	else :	value_out = 1
	sleep(1)
        state = gpio.input(button)      # Read button state
	print "get button state is %d"%state
        sleep(2)
        
       

except KeyboardInterrupt:
    print ("Goodbye.")
