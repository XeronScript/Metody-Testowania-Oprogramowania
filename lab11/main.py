#!/usr/bin/env python3

import sys
import re


def convert_to_special_binary(param: str) -> str:
    param = int(param)
    binary = bin(param).replace('-0b', '').replace('0b', '')
    new_param = ''
    possible_characters = 'abcdefghij'

    for i, value in enumerate(binary[::-1]):
        if value == '0':
            new_param += '0'
        else:
            new_param += possible_characters[i % 10]
    
    return new_param.__reversed__()


def my_printf(format_string: str, param: str) -> None:
    pattern = '#b'
    search = re.search(pattern, format_string)

    if search is not None:
        new_param = convert_to_special_binary(param)

    else:
        print(format_string)


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
