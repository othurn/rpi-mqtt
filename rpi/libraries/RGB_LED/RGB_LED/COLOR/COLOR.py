#! /usr/bin/python

class Color():
    """
    Setters and getters for an RGB color, used as a utility for the RGB_LED library.
    """
    def __init__(self):
        self._color=(0, 0, 0)
        #self._red = 0
        #self._green = 0
        #self._blue = 0

    def set_color(self, red, green, blue):
        """
        Sets the color via ints.

        :param red: value 0-255 representing intensity of red
        :param green: value 0-255 representing intensity of green
        :param blue: value 0-255 representing intensity of blue

        :example: myColor.set_color(255, 0, 255)

        """
        self._color = (red, green, blue)
        #self._red = red
        #self._green = green
        #self._blue = blue

    def set_color_string(self, color):
        """
        Sets the color by parsing a hex color code into RGB values.

        :param color: A string with 6 hex digits, e.g. "FFFFFF"

        :example: myColor.set_color_string("0F0F0F")

        """
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        self._color = (r, g, b)

    def get_color(self):
        """
        :return: a triplet representing each color channel

        :example: (red, green, blue) = myColor.getColor()

        """
        return self._color
        #return (self._red, self._green, self._blue)

    def get_red(self):
        """
        :return: Numeric value in the red channel
        """
        return self._color[0]
        #return self._red;

    def get_green(self):
        """
        :return: Numeric value in the green channel
        """
        return self._color[1]
        #return self._green;

    def get_blue(self):
        """
        :return: Numeric value in the blue channel
        """
        return self._color[2]
        #return self._blue;
