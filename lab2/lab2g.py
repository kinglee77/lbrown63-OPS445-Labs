#!/usr/bin/env python3

import sys

# Set default timer if no argument is provided
if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
