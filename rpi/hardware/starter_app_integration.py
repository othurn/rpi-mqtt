import requests
# import the DHT and MCP libraries

# construct the DHT22

# construct the ldr

# the address we will make the request to
# REPLACE WITH YOUR URL
url='http://intro-to-iot-lesson.herokuapp.com/api/data'

# initialize an empty dictionary
packet = {}

# get the temperature and humidity from DHT object

# get the brightness from the ldr object

# fill the packet with data in the format expected by the web API
packet['temperature'] = round(temperature, 3)

# just a debug, comment it out when you know the script works
print(packet)

# submit the post request.
r = requests.post(url,json=packet)
