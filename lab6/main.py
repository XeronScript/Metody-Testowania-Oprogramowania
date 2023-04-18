#!/usr/bin/env python3

import sys
import re


def calc_param(num):
    old_param = str(num)
    res = ""

    if old_param[0] == '-':
        res += old_param[0]
        old_param = old_param[1:]

    for digit in old_param:
        res += str((int(digit)*9+1) % 10)

    return res


def my_printf(format_string, param):
    new_param = calc_param(param)
    pattern = r"#.Xg"
    print(re.sub(pattern, new_param, format_string))


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
