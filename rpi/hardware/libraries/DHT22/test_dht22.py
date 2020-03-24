#! usr/bin/python

import DHT22

pin = 16

dht22 = DHT22.DHT22(pin)

humidity, temperature = dht22.get_temperature_and_humidity()

print(humidity,temperature)

#import Adafruit_DHT
'''
class DHT22():
    self.__init__(self,_pin):
        self._pin = _pin
        self._sensor = Adafruit_DHT.DHT22        

    self.get_temperature_and_humidity(self):
        return Adafruit_DHT.read_retry(sensor, pin)

    self.get_temperature():
        return self.get_temperature_and_humidity()[1]
    
    self.get_humidity():
        return self.get_temperature_and_humidity()[0]

'''
'''
# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT22

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
#pin = 23

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    else:
            print('Failed to get reading. Try again!')
'''
