#!/usr/bin/env python3
# Author ID: k62

def read_file_string(file_name):
    """Returns the entire content of a file as a single string."""
    with open(file_name, 'r') as file_obj:
        content = file_obj.read()
    return content

def read_file_list(file_name):
    """Returns the entire content of a file as a list of lines without new-line characters."""
    with open(file_name, 'r') as file_obj:
        lines = file_obj.read().splitlines()
    return lines

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
