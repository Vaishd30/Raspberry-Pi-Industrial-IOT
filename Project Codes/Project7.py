import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import Adafruit_DHT
from pushbullet import Pushbullet
import time 
import thingspeak
import csv
from datetime import datetime
import Adafruit_BMP.BMP085 as BMP085
import board
import adafruit_bh1750

bmp=BMP085.BMP085()

i2c = board.I2C()
gy30 = adafruit_bh1750.BH1750(i2c)
led = 21
buzzer = 20
# Set sensor type: Options are DHT11, DHT22, or AM2302
sensor = Adafruit_DHT.DHT11
# Set GPIO sensor is connected to
dht = 26

channel_id = 2304287  # PUT CHANNEL ID HERE
write = 'D521YTSHB1OK6QHG'  # PUT YOUR WRITE KEY HERE
read_key = 'DT1ILWEXVZU6YWH9'  # PUT YOUR READ KEY HERE

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)

pb = Pushbullet("o.czMZdJSTdkbbT83gm5LWf4Mlkhdmlji5")
print(pb.devices)

rfid = SimpleMFRC522()

# Initialize the timer
timer = 0

def func1():
    try:
        id, text = rfid.read()
        print(id)
        if id == 1042427819006:
            dev = pb.get_device('Motorola Moto g(9)')
            push = dev.push_note("Valid RFID!", "Employee given access")
            sleep(1)
            for _ in range(5):
                measure(channel)
                # free account has an API limit of 15 sec
                time.sleep(2)

        else:
            dev = pb.get_device('Motorola Moto g(9)')
            push = dev.push_note("Invalid RFID!", "Intruder Alert!!")
            
            # Keep the LED and buzzer high for 5 seconds
            GPIO.output(led, GPIO.HIGH)
            GPIO.output(buzzer, GPIO.HIGH)
            ultrasonic()
            global timer
            timer = 0
            while timer < 5:  # Wait for 5 seconds
                time.sleep(1)
                timer += 1
            GPIO.output(led, GPIO.LOW)
            GPIO.output(buzzer, GPIO.LOW)
            return

    except:
        print("Connection failed")

def measure(channel):
    data_list = []  # List to store data for CSV
    try:
        for _ in range(5):
            Humidity, Temperature = Adafruit_DHT.read_retry(sensor, dht)
            timestamp = datetime.now()
            date = timestamp.strftime("%Y-%m-%d")
            time = timestamp.strftime("%H:%M:%S")
            Pressure=bmp.read_pressure()
            Altitude=bmp.read_altitude()
            SeaLevelPressure=bmp.read_sealevel_pressure()
            AmbientLight=gy30.lux
            print(f'Date={date} Time={time} Temp={Temperature:0.1f}*C Humidity={Humidity:0.1f}% Pressure={Pressure} Pa Altitude={Altitude} m SeaLevelPressure={SeaLevelPressure} Pa AmbientLight={AmbientLight} Lux')
             # Append data as a dictionary
            data_list.append({'Date': date, 'Time': time, 'Temperature': Temperature, 'Humidity': Humidity,'Pressure':Pressure , 'Altitude':Altitude, 'SeaLevelPressure':SeaLevelPressure,'AmbientLight':AmbientLight})
            
            time.sleep(2)  # Delay between updates
            
        # Write to ThingSpeak
            response = channel.update({1: Temperature, 2: Humidity,3: Pressure , 4:Altitude, 5:SeaLevelPressure, 6: AmbientLight})
            
        # Read from ThingSpeak
            read = channel.get({})
            print("Read:", read)
            break
        
        # write data to CSV file
        with open("sensor_data.csv", "a", newline="") as file:
            fieldnames = ['Date', 'Time', 'Temperature', 'Humidity','Pressure','Altitude','SeaLevelPressure','AmbientLight']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # If the file is empty, write the header
            if file.tell() == 0:
                writer.writeheader()
            
            # Write data
            writer.writerows(data_list)

    except Exception as e:
        print("Error in measure:", e)

def ultrasonic():
    try:
        PIN_TRIGGER = 4
        PIN_ECHO = 17

        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        print ("Waiting for ultrasonic sensor to settle")
        time.sleep(2)
        print ("Calculating distance of intruder")

        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)

        while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        print ("Distance of intruder from RFID Reader:",distance,"cm")

        dev = pb.get_device('Motorola Moto g(9)')
        push = dev.push_note("Invalid RFID!", "Intruder is" + distance + "away from RFID")

    except Exception as e:
        print("Error in distance measure:", e)

if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write)
    while True:
        print("Place your RFID card")
        rfid = SimpleMFRC522()
        func1()
        time.sleep(2)