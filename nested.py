#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "mprodhan/yabamov"

import sys

nested_dict = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
    '*)': '(*'
}

def is_nested(line):
    count = 0
    nested_list = []
    while line:
        token = line[0]
        if line.startswith("(*"):
            token = "(*"
        if line.startswith("*)"):
            token = "*)"
        count += 1
        if token in nested_dict.values():
            nested_list.append(token)
        elif token in nested_dict.keys():
            a = nested_dict[token]
            b = nested_list.pop()
            if a != b:
                return "NO " + str(count)
        line = line[len(token):]
    if nested_list:
        return "NO " + str(count)
    else:
        return "YES"


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    with open('input.txt', 'r') as f:
        with open('output.txt', 'w') as w:
            for line in f:
                result = is_nested(line)
                w.write(result+'\n')

if __name__ == '__main__':
    main(sys.argv[1:])
