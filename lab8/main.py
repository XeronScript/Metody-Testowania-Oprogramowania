#!/usr/bin/env python3

import sys
import re


def convert_to_hex(param: str) -> str:
    res = ""

    for c in param:
        if ord(c) >= "a" and ord(c) <= "f":
            res += chr(ord(c) + 6)
        else:
            res += c


def my_printf(format_string, param):
    pattern = r"#.(\d+)j"
    search = re.search(pattern, format_string)

    if search is not None:
        l = int(search.group(1))
        new_param = convert_to_hex(str(hex(int(param)))[2:])

        if l <= len(new_param):
            print(re.sub(pattern, new_param, format_string))
        else:
            padded_param = "".join([0 for i in range(len(new_param - l))])
            padded_param += new_param
            print(re.sub(pattern, padded_param, format_string))

    else:
        print(format_string)


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
