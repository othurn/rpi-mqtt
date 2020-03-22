import paho.mqtt.client as mqtt
import json

class Communication:
    
    def __init__(self, client_name):
        self.client_name = client_name
        
        self.publisher = mqtt.Client(f'{client_name}_publisher')
        self.subscriber = mqtt.Client(f'{client_name}_subscriber')
        
        self.publisher.connect('192.168.0.24')
        self.subscriber.connect('192.168.0.24')
        self.publisher.loop_start()
        self.subscriber.loop_start()
        
        
    def subscribe_all(self):
        
        self.subscriber.subscribe('/class_topic')
        
    
    def publish_all(self):
        
        self.publish_test()
        
        
    def publish_test(self):
        data = {'client' : self.client_name, 'msg' : 'publishing data'}
        data = json.dumps(data)
        self.publisher.publish('/light_bulb', data)
        