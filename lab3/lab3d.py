#!/usr/bin/env python3
'''Lab 3 Inv 3: Using subprocess module'''
# Author ID: lbrown63

import subprocess

def free_space():
    process = subprocess.Popen(
        ['df', '-h', '--output=avail', '/'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    output, _ = process.communicate()
    return output.decode('utf-8').strip().split('\n')[1]

if __name__ == '__main__':
    print(free_space())
