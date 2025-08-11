# This example works with both Multiple i2c LCD Displays, including the following from Seeed Studio:
# - Grove LCD RGB Backlight
# - Grove LCD 16x2 (single color backlight)

import i2c_lcd
from machine import I2C

i2c = I2C(0)
d = i2c_lcd.Display(i2c)

d.home()
d.write('Hello, World!')
d.move(0,1)
d.write('How are you?')
