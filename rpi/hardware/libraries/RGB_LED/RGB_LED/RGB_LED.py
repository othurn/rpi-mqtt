#! /usr/bin/python

from GPIO_PWM.GPIO_PWM import GPIO_PWM
from COLOR.COLOR import Color

class RGB_LED():

    """
    A library for interfacing with common anode or common cathode RGB LEDs. The LEDs provided in PiB kits are common anode. Utilizes two helper utilities, COLOR and GPIO_PWM.

    GPIO_PWM abstracts exec commands which use the PiBits ServoBlaster tool (mega props to this convenient, well-documented solution to the problem of Raspberry Pi's only having one PWM pin!) to write to each channel of the LED
    The COLOR utility accepts either a string of the form "FFFFFF" or values between 0 and 255 for each color channel, and is the only type accepted by the RGB_LED when setting a color.

    Example usage in a driver script:

    .. code-block:: python

        red_pin = 22
        green_pin = 27
        blue_pin = 17
        is_common_anode=True

        rgb = RGB_LED(red_pin, green_pin, blue_pin,is_common_anode)

        color = Color()

        color.set_color(0, 255, 0)  # sets color to pure green
        rgb.set_color(color)
    """
    def __init__(self, _red_pin, _green_pin, _blue_pin, _is_common_anode = False):
        self._red_pin = _red_pin
        self._green_pin = _green_pin
        self._blue_pin = _blue_pin

        self._gpio_pins = [self._red_pin, self._green_pin, self._blue_pin]
        
        self._pwm = GPIO_PWM(self._gpio_pins, _is_common_anode)

    def set_color(self, color):
        """
        Sets the LED on hardware to the RGB color stored in the color parameter.

        :param: A color object, which must be set to the desired color before being passed. Upon construction, the color defaults to black, a.k.a., off.
        """
        self._pwm.write(self._red_pin, color.get_red())
        self._pwm.write(self._green_pin, color.get_green())
        self._pwm.write(self._blue_pin, color.get_blue())

        

    

