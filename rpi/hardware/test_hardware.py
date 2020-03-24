import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

#import libraries.SSD1306
#import DHT22
#import MCP300X

from libraries.DHT22 import DHT22
from libraries.MCP300X import MCP300X
from libraries.SSD1306 import SSD1306


dht22_pin = 16

dht22 = DHT22(dht22_pin)

mcp3004 = MCP300X.MCP3004

mcp = MCP300X(mcp3004)

# 128x32 display with hardware I2C:
disp = SSD1306.SSD1306_128_32()

# 128x64 display with hardware I2C:
# disp = SSD1306.SSD1306_128_64(rst=RST)

# Note you can change the I2C address by passing an i2c_address parameter like:
# disp = SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)

# Alternatively you can specify an explicit I2C bus number, for example
# with the 128x32 display you would use:
# disp = SSD1306.SSD1306_128_32(rst=RST, i2c_bus=2)


# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )

    humidity, temperature = dht22.get_temperature_and_humidity()
    temperature_str = "Temperature: " + str(round(temperature,3)) + " \xb0C"
    humidity_str = "Humidity: " + str(round(humidity,3)) + " %"

    lighting = mcp.read(mcp.CH2)
    lighting_str = "Ambient Light: " + str(lighting)

    #cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.2f%%\", $3,$2,$3*100/$2 }'"
    #MemUsage = subprocess.check_output(cmd, shell = True )
    #cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'"
    #Disk = subprocess.check_output(cmd, shell = True )

    # Write two lines of text.

    draw.text((x, top),       "IP: " + str(IP),  font=font, fill=255)
    #draw.text((x, top+8),     str(CPU), font=font, fill=255)
    draw.text((x, top+8),    str(temperature_str),  font=font, fill=255)
    draw.text((x, top+16),    str(humidity_str),  font=font, fill=255)
    draw.text((x, top+25),    str(lighting_str),  font=font, fill=255)

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(.1)
