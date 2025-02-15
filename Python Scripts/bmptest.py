import Adafruit_BMP.BMP085 as BMP085
bmp=BMP085.BMP085()
print('Temperature = {0:0.2f} *C'.format(bmp.read_temperature()))
print('Pressure = {0:0.2f} Pa'.format(bmp.read_pressure()))
print('Altitude = {0:0.2f} m'.format(bmp.read_altitude()))
print('Sealevel Pressure = {0:0.2f} Pa'.format(bmp.read_sealevel_pressure()))