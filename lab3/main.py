#!/usr/bin/env python3

import sys
import re

def my_printf(format_string,param):
    #print(format_string)
    shouldDo=True
    skip = 0

    for i in range(0,len(format_string)):
        if shouldDo:
            if i+1 < len(format_string) and format_string[i] == '#' and format_string[i+1] == 'k':
                param = param.swapcase()
                print(param, end="")
                shouldDo=False

            elif format_string[i] == '#' and format_string[i+1] == '.' and format_string[i+2] == 'k':
                skip = 2

            elif i+2 < len(format_string) and format_string[i] == '#' and format_string[i+1] == '.':
                j = i+2
                while j < len(format_string) and re.match("\d", format_string[j]):
                    j += 1
                
                if j < len(format_string) and format_string[j] == 'k':
                    num = 0
                    if j > i+2:
                        num = int(format_string[i+2:j])
                        print(param[0:num], end="")
                        skip = j - i

            elif format_string[i] == '#' and re.match("\d", format_string[i+1]):
                j = i+1
                while j < len(format_string) and re.match("\d", format_string[j]):
                    j += 1

                if j < len(format_string) and format_string[j] == 'k':
                    num = 0
                    if j > i+1:
                        num = int(format_string[i+1:j])
                        print(param[0:num], end="")
                        skip = j - i

            else:
                if skip > 0:
                    skip -= 1
                    # print(param, end="")
                    continue
                print(format_string[i],end="")
            
        else:
            shouldDo=True
    print("")

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
