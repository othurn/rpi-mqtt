# Unique manager for Model 2B rpi

import paho.mqtt.client as mqtt
import re
import json
import requests

# Server (broker) settings

# broker = "192.168.0.19"  # rpi
broker = "localhost"
port = 1883  # port

sub_topics = ['/base/test']
pub_topics = ['/Zero_1/test','/3A/test']

def post_to_rest(payload):
    # data = {'title': 'fake title', 'author': 'fake author'}
    data = json.dumps(payload)
    requests.post('http://localhost:7071/bedroom/temp', data=data)
    requests.post('http://localhost:7071/livingroom', data=data)
    


def cust_on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe('/base/test')
        client.subscribe('/bedroom/client', 0)


def cust_on_message(client, userdata, msg):
    print('Message to base: ', msg.payload.decode())
    post_to_rest(msg.payload)
    
    if msg.topic == '/bedroom/client':
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

client.loop_start()
