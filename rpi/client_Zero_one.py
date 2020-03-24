# Unique manager for Zero One rpi
from hardware.libraries.DHT22 import DHT22

import paho.mqtt.client as mqtt
import re
import json
import RPi.GPIO as GPIO
import time
# Server (broker) settings

broker = "192.168.0.19"  # rpi
# broker = "localhost"
port = 1883  # port

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

dht_pin = 16
dht22 = DHT22.DHT22(dht_pin)

sub_topics = ['/Zero_1/test']
pub_topics = ['base/test/z1']


def cust_on_connect(client, userdata, flags, rc):
    if rc == 0:
       # client.subscribe('/Zero_1/test')
       sub_test()


def cust_on_message(client, userdata, msg):
    print('Zero_1 received message:')
    print('Message: ', msg.payload.decode())

def sub_test():
    client.subscribe('/Zero_1/test')
    client.subscribe('/bedroom/client/temp_hum')

def cust_on_publish(client, userdata, msg):
    print('Zero_1 published')

def loop():
    counter = 0
    # while True:
    while counter < 5:
        hum, temp = dht22.get_temperature_and_humidity()
        print('Humidity: %s, Temp: %s', hum, temp)
        data = {
            'humidity': hum, 
            'temperature': temp
        }
        
        client.publish('/bedroom/client', data)
        counter = counter + 1
        time.sleep(5)
        

client = mqtt.Client("Zero-One-24")
client.connect(broker, port)

client.on_connect = cust_on_connect
client.on_message = cust_on_message
client.on_publish = cust_on_publish

loop()
