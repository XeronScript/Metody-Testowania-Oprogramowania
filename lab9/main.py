#!/usr/bin/env python3

import sys
import re


def split_float(num: str):
    p, s = num.split(".")
    return (int(p), int(s))


def convert_prefix(prefix: str):
    if not prefix.isdigit() or len(prefix) != 1:
        return None

    prefix_int = int(prefix)
    if prefix_int < 0 or prefix_int > 9:
        return None

    return chr(ord("a") + prefix_int)


def calculate_suffix(param: str):
    return (int(param) + 5) % 10


def my_printf(format_string, param):
    pattern = r"#.(\d+)h"
    search = re.search(pattern, format_string)

    if search is not None:
        l = search.group(1)
        prefix, suffix = split_float(l)


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
