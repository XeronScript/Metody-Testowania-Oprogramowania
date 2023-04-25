#!/usr/bin/env python3

import sys
import re

def convertToHex(decimal: str) -> str:
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    res = ''
    
    for c in decimal:
        if c in nums:
            res += c
        else:
            res += chr(ord(c) + 6)
            
    return res


def my_printf(format_string, param):
    pattern = r'#j'
    search = re.search(pattern, format_string)
    
    if search is not None:
        span = search.span()
        arg = format_string[span[0]+1 : span[1]-1]
        
    else:
        print(format_string)


data=sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
