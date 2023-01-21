# This example only works with Grove RGB Backlight i2c LCD Displays

from i2c_lcd import RGBDisplay
from machine import I2C

i2c = I2C(0)

d = RGBDisplay(i2c)

d.home()
d.write('Hello World')

def color_cycle():
	rgbColour = [0,0,0]

	while True:
		for x in range(0,255,1):
			d.color(x,0,0)

		for x in range(0,255,1):
			d.color(0,x,0)

		for x in range(0,255,1):
			d.color(0,0,x)

color_cycle()
