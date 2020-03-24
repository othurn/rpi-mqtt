#! usr/bin/python

import MCP300X
import time

#num_channels = 4 # Using MCP3004
num_channels = 8 # Using MCP3008

mcp = MCP300X.MCP300X(num_channels)

print('Reading MCP300{} values, press Ctrl-C to quit...'.format(num_channels))

# Print nice channel column headers.
if num_channels is 4:
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} |'.format(*range(num_channels)))
    print('-' * 29)
else:
    print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(num_channels)))
    print('-' * 57)

# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*num_channels
    for i in range(num_channels):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read(i)
        # Print the ADC values.
    if num_channels is 4:
        print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} |'.format(*values))
    else:
        print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))

    # Pause for half a second.
    time.sleep(0.1)

