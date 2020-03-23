# Unique manager for A plus rpi 

import paho.mqtt.client as mqtt
import re
import json

# Server (broker) settings

broker = "192.168.0.19"  # rpi
# broker = "localhost"
port = 1883  # port

sub_topics = []
pub_topics = []

def cust_on_connect(client, userdata, flags, rc):
    pass

def cust_on_message(client, userdata, msg):
    pass

def cust_on_publish(client, userdata, msg):
    pass

client = mqtt.Client("3-A-Plus")
client.connect(broker, port)

client.on_connect = cust_on_connect
client.on_message = cust_on_message
client.on_publish = cust_on_publish

client.loop_forever()
    