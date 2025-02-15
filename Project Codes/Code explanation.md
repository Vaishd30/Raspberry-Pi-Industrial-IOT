Hardware and Sensor Setup: The script begins by importing the necessary Python modules and libraries, making sure that the Raspberry Pi is ready for sensor interaction. It initializes two GPIO pins (21 and 20) to control an LED and a buzzer, respectively. These components are likely used for visual and auditory feedback based on the RFID card read results. The code then sets up several environmental sensors:
DHT11 (humidity and temperature sensor) is connected to GPIO pin 26.

BMP085 (barometric pressure and temperature sensor) is initialized.

BH1750 (ambient light sensor) is set up.

The RFID reader (SimpleMFRC522) is also initialized.


Data Collection and Notification: The script configures communication with external services for data storage and notifications. It specifies a ThingSpeak channel ID and API keys for writing and reading data. ThingSpeak is a platform for IoT data storage and visualization. Pushbullet is configured for sending notifications. Pushbullet is a service that can be used to send notifications to mobile devices and other endpoints.

The code defines a function func1 for handling RFID card access. When a card is presented, the code reads the card's ID and checks if it matches a specific ID (1042427819006). If it's a valid card, a notification is sent via Pushbullet, and then the script collects environmental data using the measure function and updates the ThingSpeak channel with this data.

In the case of an invalid card, the code still sends a notification via Pushbullet, and the LED and buzzer are turned on for 5 seconds as an intruder alert. A timer (timer) is used to keep track of this duration.

Data Measurement and Logging: The measure function is responsible for reading data from the environmental sensors. It takes readings of temperature, humidity, pressure, altitude, and ambient light over a 10-second interval. The data is timestamped with the date and time of the measurement. It then appends this data to a list called data_list.

The code sends the collected data to the ThingSpeak channel using the channel.update method. This enables remote monitoring and storage of environmental data. Additionally, the data is logged to a CSV file named "sensor_data.csv" for local storage and further analysis.

Main Loop: The script's main loop continuously prompts the user to place an RFID card near the reader. When a card is detected, the func1 function is called to handle access control. If the card is valid, it collects and logs environmental data and sends notifications. If the card is invalid, an intruder alert is triggered with the LED and buzzer, and notifications are sent as well. The script then waits for 2 seconds before prompting for another RFID card. This loop continues indefinitely, providing continuous monitoring and access control.




