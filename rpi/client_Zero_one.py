# Unique manager for Zero One rpi

import paho.mqtt.client as mqtt
import re
import json

# Server (broker) settings

broker = "192.168.0.19"  # rpi
# broker = "localhost"
port = 1883  # port

sub_topics = ['/Zero_1/test']
pub_topics = ['base/test/z1']


def cust_on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe('/Zero_1/test')


def cust_on_message(client, userdata, msg):
    print('Zero_1 received message:')
    print('Message: ', msg.payload.decode())
    

def cust_on_publish(client, userdata, msg):
    print('Zero_1 published')


client = mqtt.Client("Zero-One-24")
client.connect(broker, port)

client.on_connect = cust_on_connect
client.on_message = cust_on_message
client.on_publish = cust_on_publish

message = 'Sounds like the TV is on - Zero_1'
client.publish('/base/test', message, 0)
client.loop_forever()
