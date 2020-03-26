# Broker for Model 2B rpi
from mqtt.Comms import Communication

import Adafruit_DHT
import paho.mqtt.client as mqtt
import re
import json
import requests

# Server (broker) settings

# broker = "192.168.0.19"  # rpi
broker = "localhost"
port = 1883  # port

sub_topics = ['/base/test', '/bedroom/client', '/livingroom/client']
pub_topics = ['/Zero_1/test', '/3A/test']

client_name = 'BROKER'

def post_to_livingroom(payload):
    # data = {'title': 'fake title', 'author': 'fake author'}
    print("post to rest")
    data = json.dumps(payload)
    requests.post('http://localhost:7070/bedroom', data=data)


def post_to_bedroom(payload):
    data = json.dumps(payload)
    requests.post('http://localhost:7070/livingroom', data=data)
    

comms = Communication(client_name, sub_topics, pub_topics)

def cust_comms_on_message(client, userdata, msg):
    print(msg.topic)
    
comms.subscriber.on_message = cust_comms_on_message

comms.subscribe_all()