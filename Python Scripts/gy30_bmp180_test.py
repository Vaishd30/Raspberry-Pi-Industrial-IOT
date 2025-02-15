import Adafruit_BMP.BMP085 as BMP085
import board
import adafruit_bh1750

bmp=BMP085.BMP085()
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

print('Temperature = {0:0.2f} *C'.format(bmp.read_temperature()))
print('Pressure = {0:0.2f} Pa'.format(bmp.read_pressure()))
print('Altitude = {0:0.2f} m'.format(bmp.read_altitude()))
print('Sealevel Pressure = {0:0.2f} Pa'.format(bmp.read_sealevel_pressure()))
print("%.2f Lux" % sensor.lux)