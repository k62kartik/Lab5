#!/usr/bin/env python3
# Author ID: k62

def add(number1, number2):
    """Attempts to add two numbers; returns an error message if the addition fails."""
    try:
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    """Attempts to read a file and return its contents; returns an error message if reading fails."""
    try:
        with open(filename, 'r') as file_obj:
            return file_obj.readlines()
    except (FileNotFoundError, OSError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                        # should print 15
    print(add('10', 5))                      # should print 15
    print(add('abc', 5))                     # should print error message
    print(read_file('seneca2.txt'))          # reads file successfully if exists
    print(read_file('file10000.txt'))        # should print error message if file does not exist
