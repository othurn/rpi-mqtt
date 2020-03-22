import paho.mqtt.client as mqtt
# Server (broker) settings
broker = "localhost" #hostname
port = 1883 #port
# Callback when we connect to the broker
def on_connect(client, userdata, flags, rc):
    topic = "/dif/topic2"
    topic1 = "/dif/topic1"
    if rc == 0:
        print("Successfully Connected As SUBSCRIBER. Listening...")
        client.subscribe([(topic, 0),(topic1, 0)])

# Callback whenever we receive a message from the broker

def on_topic1(client, userdata, msg):
    rec = msg.payload.decode()
    
    message = "From: /dif/topic1 , Hello"
    print("/dif/topic1")
    print(rec)
    
    # the retain tells the broker to keep this message around for the next time the subscriber is available.
    ret = client.publish("/publisher/topic1", message, qos=0, retain=True)
    
def on_publish(client, userdata, results):
    print("dif published")
    
def on_message(client, userdata, msg):
    received = msg.payload.decode()
    print(received)
    
    
# Connect to the broker and loop forever
client = mqtt.Client("SUBSCRIBER")
client.connect(broker, port)
client.on_connect = on_connect
client.message_callback_add("/dif/topic2", on_message) # specific topic
client.message_callback_add("/dif/topic1", on_topic1)

# client.on_message = on_message # all topics / messages
client.loop_forever()

# Subscriber and publisher ... has 2 different topics is is subscribes to and then publishes back to the pub_client. 
# you can treat the on_whatever callbacks as the main operations and then loop for ever. 