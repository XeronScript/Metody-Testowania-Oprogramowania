#!/usr/bin/env python3

import sys
import re


def split_float(num: str) -> tuple[int, int]:
    p, s = num.split(".")
    return (int(p), int(s))


def convert_prefix(prefix: str) -> str:
    if not prefix.isdigit() or len(prefix) != 1:
        return ""

    prefix_int = int(prefix)
    if prefix_int < 0 or prefix_int > 9:
        return ""

    return chr(ord("a") + prefix_int)


def calculate_suffix(param: int) -> int:
    return (param + 5) % 10


def my_printf(format_string, param):
    pattern = r"#.(\d+)h"
    search = re.search(pattern, format_string)

    if search is not None:
        l = int(search.group(1))

        prefix, suffix = split_float(param)
        conv_prefix = convert_prefix(str(prefix))
        conv_suffix = str(calculate_suffix(suffix))
        new_param = ".".join([conv_prefix, conv_suffix])

        if l > len(conv_suffix):
            for _ in range(l - len(conv_suffix)):
                new_param += "0"
            print(re.sub(pattern, new_param, format_string))
        elif l == 0:
            print(re.sub(pattern, conv_prefix, format_string))
        elif l < len(conv_suffix):
            new_param = ".".join([conv_prefix, conv_suffix[:l]])
            print(re.sub(pattern, new_param, format_string))
        else:
            print(re.sub(pattern, new_param, format_string))
    else:
        print(format_string)


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
