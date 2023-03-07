#!/usr/bin/env python3

import sys

def my_printf(format_string, param):
    shouldDo = True

    for i in range(len(format_string)):
        if shouldDo:

            if format_string[i] == '#' and format_string[i+1] == 'k':
                param = param.swapcase()
                print(param,end="")
                shouldDo=False

            elif i+3 < len(format_string) and format_string[i] == '#' and format_string[i+1] == '.' and format_string[i+3] == 'k':
                str_lim = int(format_string[i+2])
                print(param[:str_lim], end="")
                shouldDo = False

            else:
                print(format_string[i], end="")
        else:
            shouldDo=True
    print("")

data = sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
