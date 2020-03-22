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
    print("pub_client")       
    
client = mqtt.Client("Publisher")
client.connect(broker, port)
client.on_publish = on_publish
client.on_connect = on_connect
client.message_callback_add("/publisher/topic1", on_message)

mesage = "topic from publisher"
client.publish('/lights/living_room', mesage, 0)

client.loop_forever()

# This publisher sends out a series of messages to all of its known topics, then goes into a state of waiting for some where else to publish to it. The only way this works is if I loop forever.
# I wonder if we can just react to messages back in forth in different message_callback_add functions. We would control the robot through fucntion calls when certain messages are recieved.
