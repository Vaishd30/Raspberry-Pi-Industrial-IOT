import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import Adafruit_DHT
from pushbullet import Pushbullet
from time import sleep
import thingspeak
import csv
from datetime import datetime

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
                sleep(2)

        else:
            dev = pb.get_device('Motorola Moto g(9)')
            push = dev.push_note("Invalid RFID!", "Intruder Alert!!")
            
            # Keep the LED and buzzer high for 5 seconds
            GPIO.output(led, GPIO.HIGH)
            GPIO.output(buzzer, GPIO.HIGH)
            global timer
            timer = 0
            while timer < 5:  # Wait for 5 seconds
                sleep(1)
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
            print(f'Date={date} Time={time} Temp={Temperature:0.1f}*C Humidity={Humidity:0.1f}%')
            
            # Append data as a dictionary
            data_list.append({'Date': date, 'Time': time, 'Temperature': Temperature, 'Humidity': Humidity})
            
            sleep(2)  # Delay between updates
            
        # Write to ThingSpeak
            response = channel.update({1: Temperature, 2: Humidity})
            
        # Read from ThingSpeak
            read = channel.get({})
            print("Read:", read)
            break
        
        # write data to CSV file
        with open("sensor_data.csv", "a", newline="") as file:
            fieldnames = ['Date', 'Time', 'Temperature', 'Humidity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # If the file is empty, write the header
            if file.tell() == 0:
                writer.writeheader()
            
            # Write data
            writer.writerows(data_list)

    except Exception as e:
        print("Error in measure:", e)

if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write)
    while True:
        print("Place your RFID card")
        rfid = SimpleMFRC522()
        func1()
        sleep(2)
