'''VCC - 3.3V - Pin 1
GND - GND - Pin 6
SCL - Pin 5
SDA - Pin 3
ADDR - GND - Pin 6/14'''
import board
import adafruit_bh1750
 
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

print("%.2f Lux" % sensor.lux)