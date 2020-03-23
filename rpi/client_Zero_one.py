# Unique manager for Zero One rpi

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

def cust_on_publish(client, userdata, msg):
    print('Zero_1 published')

def loop():
    while True:
        if GPIO.input(pin) == GPIO.HIGH:
            message = 'Motion Detected - Zero_1'
            client.publish('/base/test', message, 0)
            time.sleep(1)
        else:
            time.sleep(0.5)

client = mqtt.Client("Zero-One-24")
client.connect(broker, port)

client.on_connect = cust_on_connect
client.on_message = cust_on_message
client.on_publish = cust_on_publish

loop()
