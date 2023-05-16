#!/usr/bin/env python3

import sys


def convert_to_hex(param: str) -> str:
    res = ""

    for c in param:
        if ord(c) >= "a" and ord(c) <= "f":
            res += chr(ord(c) + 6)
        else:
            res += c


def my_printf(format_string, param):
    # print(format_string)
    shouldDo = True
    for idx in range(0, len(format_string)):
        if shouldDo:
            if format_string[idx] == "#" and format_string[idx + 1] == "k":
                print(param, end="")
                shouldDo = False
            else:
                print(format_string[idx], end="")
        else:
            shouldDo = True
    print("")


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
