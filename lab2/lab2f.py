#!/usr/bin/env python3

import sys

# Get the timer value from command-line argument
timer = int(sys.argv[1])

# Countdown loop
while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
