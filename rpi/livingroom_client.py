from mqtt.Comms import Communication
import Adafruit_DHT

import json
import time

BASE = "192.168.0.19"
COMP = "192.168.0.10"
broker = BASE  # device
# broker = "localhost"
port = 1883  # port

dht_pin = 16
dht22 = Adafruit_DHT.DHT22

client_name = 'livingroom'

sub_topics = ['/livingroom/client1']
pub_topics = ['base/test/z1', '/livingroom/client']

def cust_on_message(client, userdata, msg):
    
    topic = msg.topic
    
    if topic == "/livingroom/client1":
        print('Message: ' + msg.payload.decode())
        print('send to rest')

comms = Communication(client_name, sub_topics, pub_topics)
comms.subscriber.on_message = cust_on_message

hum, temp = Adafruit_DHT.read_retry(dht22, dht_pin)

comms.subscribe_all()

comms.publish_to_topic(pub_topics[1], {'test':'topic'})


