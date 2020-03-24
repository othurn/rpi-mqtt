import RGB_LED

import time

from RGB_LED.COLOR import Color

red_pin = 22
green_pin = 27
blue_pin = 17
is_common_anode=True

rgb = RGB_LED.RGB_LED(red_pin, green_pin, blue_pin,is_common_anode)

color = Color()


r = 0
g = 0
b = 0

while r < 256:
    color.set_color(r,0,0)
    rgb.set_color(color)
    time.sleep(0.1)
    r+=32

color.set_color(0,0,0)

while g < 256:
    color.set_color(0,g,0)
    rgb.set_color(color)
    time.sleep(0.1)
    g+=32

color.set_color(0,0,0)

while b < 256:
    color.set_color(0,0,b)
    rgb.set_color(color)
    time.sleep(0.1)
    b+=32

color.set_color(0,0,0)

rgb.set_color(color)
