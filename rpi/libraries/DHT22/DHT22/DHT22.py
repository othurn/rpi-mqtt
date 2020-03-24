#! usr/bin/python

import Adafruit_DHT

class DHT22():
	"""
	A wrapper class that uses Adafruit's DHT library. Stores the GPIO pin and can retrieve temperature in Celsius, humidity in percent.
	"""

	def __init__(self,_pin):
		self._pin = _pin
		self._sensor = Adafruit_DHT.DHT22        

	def get_temperature_and_humidity(self):
		"""
    	:return: humidity, temperature. In that order. Must be received into two variables by the driver script.

    	:example: myHumidity, myTemperature = myDHT22.get_temperature_and_humidity()
    	
    	"""

		return Adafruit_DHT.read_retry(self._sensor, self._pin)

	def get_temperature(self):
		"""
    	:return: temperature in celsius, to two decimal places.
    	"""

		return self.get_temperature_and_humidity()[1]

	def get_humidity(self):
		"""
    	:return: humidity in percent, to two decimal places.
    	"""

		return self.get_temperature_and_humidity()[0]


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
