#!/usr/bin/env python3

import sys
import re


def getHexOrDecimal(param: int) -> str:
    if param % 2 == 0:
        return str(param)
    else:
        return hex(param).replace("0x", "")


def calculate_param_expression(param: int):
    return int((param * 2) / len(str(param)))


def my_printf(format_string, param):
    pattern = r"#a"
    search = re.search(pattern, format_string)

    if search is not None:
        new_param = calculate_param_expression(param)
        hex_or_decimal = getHexOrDecimal(new_param)
        print(re.sub(pattern, hex_or_decimal, format_string))


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
