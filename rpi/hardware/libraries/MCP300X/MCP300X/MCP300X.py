#! usr/bin/python

import spidev

_MAX_SPEED_HZ=1000000

class MCP300X():
    """
    A library for using an MCP300 ADC. Currently supports MCP3004 and MCP3008

    :param num_channels: the device being used (opt.), defaults to (int) 8 for the MCP3008 device
    :param _MAX_SPEED_HZ: the max frequency permitted, used for configuring the IC, defaults to 10000000 hZ

    :example: myMCP3008 = MCP300X()

    :example: myMCP3004 = MCP300X(4)

    Channel member variables exist to provide an abstraction for driver scripts, so that they can assign sensor pins to channels instead of directly to pins. It increases readability.

    :example: light_dependent_resistor = myMCP3008.CH2

    In this example, the circuit is set so that the value of the ldr is plugged in to channel 2 of the MCP device. Channels CH0 through CH7 are available, though only CH0-CH3 are meaningful when using an MCP3004 device.
    """

    MCP3004 = 4
    MCP3008 = 8
    
    CH0 = 0
    CH1 = 1
    CH2 = 2
    CH3 = 3
    CH4 = 4
    CH5 = 5
    CH6 = 6
    CH7 = 7

    def __init__(self, num_channels=MCP3008,_MAX_SPEED_HZ=_MAX_SPEED_HZ):
        self.num_channels=num_channels

        self.spi = spidev.SpiDev()
        
        self._MAX_SPEED_HZ=_MAX_SPEED_HZ

        self._initialize_spi()

    ''' Helper function for object instantiation '''
    def _initialize_spi(self):
        self.spi.open(0,0)
        self.spi.max_speed_hz=self._MAX_SPEED_HZ

    def read(self,channel):
        """
        Read from the specified channel of the MCP device

        :param channel: the channel to read from (0 ... num_channels - 1)
        :type channel: int
        :return: analog value read from that pin of the chip
        :rtype: int ranging 0-1023
        """
        raw_data = self.spi.xfer([1, 8 + channel << 4, 0])
        #print("raw_data = ", raw_data)
        #print(raw_data[1]&3 << 8)
        adc_reading = ((raw_data[1] & 3) << 8) + raw_data[2]
        #print("adc_reading = ", adc_reading)

        return adc_reading
