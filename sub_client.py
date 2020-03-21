import paho.mqtt.client as mqtt
# Server (broker) settings
broker = "localhost" #hostname
port = 1883 #port
# Callback when we connect to the broker

# sub topics
# what to do with <i>?
consensus = "lab5/consensus/pitstop_coordinates/<i>"
start_point = "lab5/consensus/start_coordinates/<i>"

# pub topics
understanding = "lab5/consensus/understanding"
ok_understanding = "lab5/consensus/understanding/ok"


sub_topics = [(consensus, 0), (start_point, 0)]

def on_connect(client, userdata, flags, rc):
    topic = "/demo/topic"
    topic1 = "/something/new"
    topic2 = "/moves"
    if rc == 0:
        print("Successfully Connected As SUBSCRIBER. Listening...")
        client.subscribe([(topic,0),(topic1, 0),(topic2, 0)])

# Callback whenever we receive a message from the broker
def on_message(client, userdata, msg):
    received = msg.payload.decode()
    print(received)
    
    
# Connect to the broker and loop forever
client = mqtt.Client("SUBSCRIBER_2")
client.connect(broker, port)
client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()

# Subscriber and publisher ... has 2 different topics is is subscribes to and then publishes back to the pub_client. 
# you can treat the on_whatever callbacks as the main operations and then loop for ever.
# havent figure out any other loop start or stop functions