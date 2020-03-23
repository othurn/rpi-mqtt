# Unique manager for Model 2B rpi

import paho.mqtt.client as mqtt
import re
import json

# Server (broker) settings

broker = "192.168.0.19"  # rpi
# broker = "localhost"
port = 1883  # port

sub_topics = ['/base/test']
pub_topics = ['/Zero_1/test','/3A/test']


def cust_on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe('/base/test')


def cust_on_message(client, userdata, msg):
    print('Base received message')
    print('Message: ', msg.payload.decode())


def cust_on_publish(client, userdata, msg):
    print('Base published')


client = mqtt.Client("BASE")
client.connect(broker, port)

client.on_connect = cust_on_connect
client.on_message = cust_on_message
client.on_publish = cust_on_publish

message = 'Hey from Base'
for pub in pub_topics:
    client.publish(pub, message, 0)

client.loop_forever()
