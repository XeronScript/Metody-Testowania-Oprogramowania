#!/usr/bin/env python3

import sys


def convert_prefix(prefix: str):
    if not prefix.isdigit() or len(prefix) != 1:
        return None

    prefix_int = int(prefix)
    if prefix_int < 0 or prefix_int > 9:
        return None

    return chr(ord("a") + prefix_int)


def calculate_postfix(param: str):
    return (int(param) + 5) % 10


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
