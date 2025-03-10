#!/usr/bin/env python3
# Author ID: lbrown63

def read_file_string(file_name):
    """Reads the entire contents of a file and returns it as a string"""
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """Reads the contents of a file and returns a list of lines (without new-line characters)"""
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
