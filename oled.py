from machine import I2C, Pin
from lib.ssd1327 import *

#OLED display
i2c = I2C(0, pins=('P9','P10'))     # create on bus 0; PIN assignments (P9=SDA, P10=SCL)
i2c.init(I2C.MASTER)                # init as a master
print(i2c.scan())
print("I2C Address : " + hex(i2c.scan()[0]).upper())
print("I2C Configuration: " + str(i2c))

display = ssd1327.SH1107_I2C(128, 128, i2c)
display.poweron()
display.fill(0)
display.invert(1)
display.text('Betta fish', 20, 20, 255)
display.show()
#display.poweroff()


# display.fill(0)
#display.invert(1)
# for y in range(0,12):
#     display.text('Hello World', 0, y * 8, 15 - y)
# display.show()


# 'betta', 900x600px
