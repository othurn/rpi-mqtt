# Unique manager for A plus rpi 

import paho.mqtt.client as mqtt
import re
import json

# Server (broker) settings

broker = "192.168.0.19"  # rpi
# broker = "localhost"
port = 1883  # port

sub_topics =['/3A/test']
pub_topics = ['/base/test']

def cust_on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe('/3A/test')

def cust_on_message(client, userdata, msg):
    print('3A recieved message:')
    print('Topic: ', msg.topic)
    print('Message: ', msg.payload.decode())

def cust_on_publish(client, userdata, msg):
    print('3A published')

client = mqtt.Client("3-A-Plus")
client.connect(broker, port)

client.on_connect = cust_on_connect
client.on_message = cust_on_message
client.on_publish = cust_on_publish

message = 'The lights are on - 3A'
client.publish('/base/test', message, 0)

client.loop_forever()
 
