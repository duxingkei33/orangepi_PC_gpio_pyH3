from rgbControlClass import RGBControl

# 7 -> like port.PA7
# 8 -> like port.PA8
# 9 -> like port.PA9
rgb = RGBControl(7, 8, 9)

rgb.r("on") # red led is on from rgb
rgb.r("off") # red led is off from rgb

rgb.g("on") # green led is on from rgb
rgb.g("off") # green led is off from rgb

rgb.b("on") # blue led is on from rgb
rgb.b("off") # blue led is off from rgb

rgb.off() # it turns off rgb led

rgb.white() # red green and blue lights mix for white light

rgb.red() # for red light

rgb.green() # for green light

rgb.blue() # red green and blue lights mix for white light

rgb.yellow() # red and green lights mix for white light

rgb.magenta() # red and blue lights mix for white light

rgb.cyan() # green and blue lights mix for white light
