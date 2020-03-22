import paho.mqtt.client as mqtt
import re
import json

# Server (broker) settings

broker = "192.168.0.19" # rpi
# broker = "localhost"
port = 1883 #port

def on_connect(client, userdata, flags, rc):
    livingroom = '/lights/living_room'
    light_one = '/lights/living_room/light1'
    if rc == 0:
        print('light sub to new topic')  
        client.subscribe([(livingroom, 0), (light_one, 0)])
        

def on_message(client, userdata, msg):
    
    topic = msg.topic
    msg = msg.payload
    print("rec message light") 
    
    if topic == '/lights/living_room':
        print("Living Room lights: ON")    
    elif topic == '/lights/living_room/light1':
        print("Light one: OFF")

        
client = mqtt.Client("Living_Room_Lights")
client.connect(broker, port)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()