#!/usr/bin/env python3

import sys
import re


def calc_param(num: int, fill: str):
    old_param = str(num)
    res = ""

    if old_param[0] == '-':
        res += old_param[0]
        old_param = old_param[1:]

    f = int(fill)
    rng = range(f - len(old_param))

    if f > len(old_param):
        for i in rng:
            res += "0"
            f -= 1

    for digit in old_param:
        res += str((int(digit)*9+1) % 10)

    return res


def my_printf(format_string, param):
    pattern = r"#.[0-9]+g"
    fill_search = re.search(pattern, format_string)

    if (fill_search is not None):
        fill_span = fill_search.span()
        fill = format_string[fill_span[0]+2: fill_span[1]-1]

        new_param = calc_param(param, fill)
        print(re.sub(pattern, new_param, format_string))
    else:
        print(format_string)


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
