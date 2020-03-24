import time

import RPi.GPIO as GPIO

from libraries.MCP300X import MCP300X
from libraries.Sound_Detector import Sound_Detector

GPIO.setmode(GPIO.BCM)

mcp3004 = MCP300X.MCP3004

mcp = MCP300X(mcp3004)

# use for revised circuit
# gate_pin = 26
# envelope_pin = MCP300X.CH1
# audio_pin = MCP300X.CH2

# use of og circuit
gate_pin = 26
envelope_pin = MCP300X.CH4
audio_pin = MCP300X.CH5

sound = Sound_Detector(gate_pin, envelope_pin, audio_pin)
GPIO.setup(sound.gate(), GPIO.IN)


while True:
    gate = GPIO.input(sound.gate())
    print(gate)
    envelope, audio = mcp.read(sound.envelope()), mcp.read(sound.audio())

    print("(gate,envelope,audio)=({},{},{})".format(gate,envelope,audio))

    time.sleep(0.1)
