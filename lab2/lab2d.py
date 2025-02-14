#!/usr/bin/env python3

import sys

# Check if exactly two arguments are provided
if len(sys.argv) != 3:
    print("Usage:", sys.argv[0], "name age")
    sys.exit()

# Assign arguments to variables
name = sys.argv[1]
age = sys.argv[2]

# Print the output
print("Hi " + name + ", you are " + age + " years old.")
