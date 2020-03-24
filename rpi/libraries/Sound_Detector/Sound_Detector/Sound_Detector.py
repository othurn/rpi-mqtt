#! usr/bin/python


class Sound_Detector():
    """
    A class that holds the pins used for the Sound Detector, so that driver scripts can reference them as arguments to the MCP device when reading their values

    :param _gate_pin: the GPIO pin being used for the Gate (binary 0/1)
    :type _gate_pin: int
    :param _envelope_pin: the GPIO pin being used for the Envelope (??)
    :type _envelope_pin: int
    :param _audio_pin: the GPIO pin being used for the Audio (analog 0-1023)
    :type _audio_pin: int

    :example: mySoundDetector = Sound_Detector(17, 22, 27)

    It must be used in conjunction with the MCP300X library, with calls such as:

    :example: gate_value = myMCP.read(mySoundDetector.gate())

    Since the MCP300X library exposes channel aliases, you may wish to increase readability by initializing the sound detector like this. See MCP300X documentation for details.

    :example: mySoundDetector = MCP300X(17, myMCP.CH0, myMCP.CH1)

    """
    def __init__(self,_gate_pin,_envelope_pin,_audio_pin):
        self._gate_pin = _gate_pin
        self._envelope_pin = _envelope_pin
        self._audio_pin = _audio_pin

    def gate(self):
        """
        :return: The GPIO pin connected to the Gate
        """
        return self._gate_pin
    
    def envelope(self):
        """
        :return: The GPIO pin connected to the Envelope
        """
        return self._envelope_pin
        
    def audio(self):
        """
        :return: The GPIO pin connected to the Audio
        """
        return self._audio_pin
