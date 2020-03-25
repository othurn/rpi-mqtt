# Unique manager for Zero One rpi
from libraries.DHT22 import DHT22
import Adafruit_DHT
import paho.mqtt.client as mqtt
import re
import json
import time
# Server (broker) settings

broker = "192.168.0.19"  # rpi
# broker = "localhost"
port = 1883  # port

dht_pin = 16
dht22 = Adafruit_DHT.DHT22

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
       # hum, temp = dht22.get_temperature_and_humidity()
        hum, temp = Adafruit_DHT.read_retry(dht22, dht_pin)
        print('Humidity: %s, Temp: %s', hum, temp)
        data = {
            'humidity': hum, 
            'temperature': temp
        }

        data = json.dumps(data)
        
        client.publish('/bedroom/client', data)
        counter = counter + 1
        time.sleep(5)
        

client = mqtt.Client("Zero-One-24")
client.connect(broker, port)

client.on_connect = cust_on_connect
client.on_message = cust_on_message
client.on_publish = cust_on_publish

loop()
