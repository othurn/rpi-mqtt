import paho.mqtt.client as mqtt
import json
import time
import re

from Comms import Communication
# Server (broker) settings

broker = "192.168.0.24" # rpi
# broker = "localhost"
port = 1883 #port

class LightBulb:
    def __init__(self, client_name, comms):
        self.client_name = client_name
        
        self.comms = comms
        
        self.comms.subscriber.on_message = self.message_handler
        
    
    def message_handler(self, client, userdata, msg):
        
        topic = msg.topic
        msg = str(msg.payload.decode('utf-8', 'ignore'))
        
        if re.match('/class_topic', topic):
            print(msg)
            
    def loop(self):
        self.comms.subscribe_all()
        while True:
            self.comms.publish_all()
            time.sleep(4)
            

def main():
    
    comms = Communication('test_light_1')
    light = LightBulb('light_1', comms)
    
    light.loop()
    
if __name__ == "__main__":
    main()
    
    
    