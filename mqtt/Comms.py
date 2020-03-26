import paho.mqtt.client as mqtt
import json

BROKER = '192.168.0.24'
PORT = 1883

class Communication:
    
    def __init__(self, client_name, sub_topics:list, pub_topics:list):
        self.client_name = client_name
        self.sub_topics = sub_topics
        self.pub_topics = pub_topics
        
        self.publisher = mqtt.Client(f'{client_name}_publisher')
        self.subscriber = mqtt.Client(f'{client_name}_subscriber')
        self.publisher.connect(BROKER, PORT)
        self.subscriber.connect(BROKER, PORT)
        self.publisher.loop_start()
        self.subscriber.loop_start()
        
        
    def subscribe_all(self): 
        self.subscriber.subscribe('/class_topic')
        
        for sub in self.sub_topics:
            self.subscriber.subscribe(sub, 0)   
            print(self.client_name + " subscribed to " + sub) 
    
    def publish_all(self):
        self.publish_test()
        
        
    def publish_to_topic(self, topic, payload):
        self.publisher.publish(topic, payload, 0)
        
        
    def publish_test(self):
        data = {'client' : self.client_name, 'msg' : 'publishing data'}
        data = json.dumps(data)
        self.publisher.publish('/light_bulb', data)
        
