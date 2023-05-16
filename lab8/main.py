#!/usr/bin/env python3

import sys

def convert_letters(param):
    res = ''
    num = str(param)
    
    for i in num:
        if ord(i) >= 'a' and ord(i) <= 'f':
            res += chr(ord(i) + 6)


def my_printf(format_string, param):
    #print(format_string)
    shouldDo=True
    for idx in range(0,len(format_string)):
        if shouldDo:
            if format_string[idx] == '#' and format_string[idx+1] == 'k':
                print(param,end="")
                shouldDo=False
            else:
                print(format_string[idx],end="")
        else:
            shouldDo=True
    print("")


data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
