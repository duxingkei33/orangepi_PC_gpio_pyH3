#!/usr/bin/env python
"""Basic blinking led example.

The led on A20-OLinuXino-MICRO  blinks with rate of 1Hz like "heartbeat".
"""

import os
import sys

if not os.getegid() == 0:
    sys.exit('Script must be run as root')


from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
#//BY CHOW
from pyA20.gpio import connector

__author__ = "Stefan Mavrodiev"
__copyright__ = "Copyright 2014, Olimex LTD"
__credits__ = ["Stefan Mavrodiev"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = __author__
__email__ = "support@olimex.com"


# 
"""
*/  {"LED",
        {
            {   "POWER_LED",  SUNXI_GPL(10),  1   },
            {   "STATUS_LED",  SUNXI_GPA(15),  2   },
"""
#led = connector.LEDp1    # This is the same as port.POWER_LED
led = connector.LEDp2    # This is the same as port.STATUS_LED
#led = port.POWER_LED
#led = port.STATUS_LED

gpio.init()
gpio.setcfg(led, gpio.OUTPUT)

try:
    print ("Press CTRL+C to exit")
    while True:
        gpio.output(led, 1)
	print "led set 1 \r\n"
        sleep(2)
        gpio.output(led, 0)
	print "led set 0 \r\n"
        sleep(2)
	"""
        gpio.output(led, 1)
        sleep(0.1)
        gpio.output(led, 0)
        sleep(0.1)

        sleep(0.6)
	"""
except KeyboardInterrupt:
    print ("Goodbye.")
