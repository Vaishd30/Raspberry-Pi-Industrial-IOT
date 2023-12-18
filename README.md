# Raspberry-Pi-Industrial-IoT
Raspberry Pi Industrial Monitoring, Management, and Data Acquisition System  RFID Reader checks the validity of a RFID Card. If the card is valid, RPi sends an alert to the phone, and then uses sensors to capture and calculate various parameters, and plots them on ThingSpeak

# Requirements
a) Raspberry Pi 3 Model B+

b) RC522 RFID Reader and Card

c) Adafruit DHT11 sensor

d) BH1750 Ambient Light Sensor

e) BMP180 Pressure Sensor

f) LEDs and Buzzers

g) Jumper Wires

h) Pushbullet

i) ThingSpeak

# Raspberry Pi Model 3B+

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/dc1ca68b-92d9-4d9d-a1ec-06024cf8374f)

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/71f31d6b-0bf0-4587-8f48-1c30857fbbd5)

# Raspbian / Raspberry Pi OS

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/464fe22e-26d7-45fb-8cf8-377ecc05156f)

# Adafruit DHT11 sensor

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/79033871-32f8-4447-ba68-388b9f8ff80c)

# RC522 RFID Reader

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/8a87ee3b-a004-4f3b-aef2-c0fc1d6a65da)

# BMP180 Pressure Sensor

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/950e643d-31ca-432c-ac1a-47c20d23318b)

# LEDs and Buzzers

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/4317ee20-2e8c-412c-9443-981bc67b48ac)

# Pushbullet

 https://thingspeak.com/

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/14e1e9b1-f9d2-4c76-b30e-af6a19eaa302)

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/8846f53b-ea09-46f1-8792-bad0c1ed835a)

 # Block Diagram

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/7eb0afd7-f812-48da-b658-598bd7778908)

# Flowchart

 ![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/06fdf5f9-8253-426c-b4c6-e08851a6a82f)

# Circuit Diagram
Connect the Vcc pin of DHT11 Sensor to Pin 2 of Raspberry Pi, Gnd pin of DHT11 Sensor to Pin 6 of Raspberry Pi and the Out pin of DHT11 Sensor to GPIO 26 of the Raspberry Pi. Also connect the + terminal of LED to GPIO 21, + terminal of buzzer to GPIO 20 and connect the ground pins of both to Pin 6 of Raspberry Pi.

Connect the SDA and SCL pins of both BMP180 and BH1750 to Pins 3 and 5 respectively. Connect 3V3 pin to Pin 1, GND and ADDR to Pin 6.

![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/2e4487f1-d064-4950-bc45-a5f56d245150)

![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/af4e40b4-64cf-428e-8d90-43443535deb6)

# Results

ThingSpeak: https://thingspeak.com/channels/2304287

Program output in shell
![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/7675f509-5b3a-4233-ac3b-0176ae6d2451)

# Outputs in ThingSpeak

Temperature and Humidity values plotted against time in ThingSpeak
![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/c879c1fe-b38c-42de-9496-6702db9cdd79)

Temperature and Humidity gauges in ThingSpeak
![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/896630b3-1542-4e90-8130-ca643ef95c4a)

Temperature and Humidity numeric displays in ThingSpeak
![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/9b533646-8726-4065-82cb-ab21d94b8a45)

Correlation between Temperature and Humidity plotted in ThingSpeak
![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/f5794216-eaf3-45c6-a9a2-6dd707ea1469)

Pressure and Altitude values plotted against time in ThingSpeak
![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/ad8a135d-43df-47a9-a662-ae81291596bb)

Sea Level Pressure and Ambient Light values plotted against time in ThingSpeak
![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/00afcc1a-f388-480d-8e0c-1c55234122f6)

Dew Point and Air Density values plotted against time in ThingSpeak
![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/f46d5591-eac4-41a0-9095-b403472386fc)

All sensor parameters stored in a CSV file
![image](https://github.com/Vaishd30/Raspberry-Pi-Industrial-IoT/assets/139155413/234b284e-b9bd-4e4b-9d1b-5cd3bac63d32)

# References

[1] An Internet-Based Interactive Embedded Data Acquisition System for Real-Time Applications by Ali Ziya Alkar and Mehmet Atif Karaca, IEEE Transactions on Instrumentation and Measurement, Vol. 58, No. 3, March 2009.

[2] Wireless SCADA for industrial automation using Raspberry Pi by Avinash V. Ghadage, Dr. S. S. Patil, International Journal of Advanced Research in Innovative Ideas in Education (IJARIIT), Vol. 3, Issue 4, April 2017.

[3] Low-Cost Solutions for Maintenance with a Raspberry Pi by M. V. K. Sivakumar, S. V. Krishna, M. V. N. Srinivas, International Journal of Emerging Technology in Computer Science & Electronics (IJETCSE), Vol. 10, Issue 11, November 2019.

[4] Internet of Things (IoT) based Data Acquisition system using Raspberry Pi by A. S. Patil, D. S. Patil, S. S. Patil, International Journal of Engineering Research & Technology (IJERT), Vol. 3, Issue 5, May 2014.

[5] Raspberry pi based data acquisition system using wireless communication by V. N. Patil, A. S. Patil, International Journal of Recent Engineering Science (IJRES), Vol. 3, No. 2, February 2015.

[6] https://iotdesignpro.com/projects/home-security-system-using-raspberry-pi-and-pir-sensor-with-push-notification-alert

[7] https://iotstarters.com/how-to-send-sensor-data-to-thingspeak-using-raspberry-pi/

[8] https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi/

[9] https://learn.adafruit.com/adafruit-io-basics-digital-output/python-setup

[10] https://github.com/alaub81/rpi_sensor_scripts/tree/main




















