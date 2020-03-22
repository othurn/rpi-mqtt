import paho.mqtt.client as mqtt
import time

broker = "192.168.0.19"
# broker = "localhost"  # change host name for network connections
port = 1883
topics = ["/demo/topic", "/something/new", "/moves", 
          "/lights/living_room", "/lights/living_room/light1"]

def on_connect(client, userdata, flags, rc):
    topic = "/publisher/topic1"
    if rc == 0:
        print("publish")
        client.subscribe(topic, 0)
    
def on_message(client, userdata, msg):
    rec = msg.payload.decode()
    print("publisher revieced %s" % rec)

# publish callback
def on_publish(client, userdata, results):
    # sending some dummy data
    for topic in topics:
        
        message = "Publisher publised to topic %s" % topic  
    
        # set retain to true if the broker should wait for a subscriber to be listening
        ret = client.publish(topic, message, qos=0, retain=True)
        time.sleep(0.5)
    
    print("fin")        
    
client = mqtt.Client("Publisher")
client.connect(broker, port)
client.on_publish = on_publish
client.on_connect = on_connect
client.message_callback_add("/publisher/topic1", on_message)


client.loop_forever()

# This publisher sends out a series of messages to all of its known topics, then goes into a state of waiting for some where else to publish to it. The only way this works is if I loop forever.
# I wonder if we can just react to messages back in forth in different message_callback_add functions. We would control the robot through fucntion calls when certain messages are recieved.
