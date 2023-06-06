#!/usr/bin/env python3

import sys
import re


def convert_to_special_binary(param: str) -> str:
    binary = bin(int(param)).replace('-0b', '').replace('0b', '')


def my_printf(format_string,param):
    pattern = '#b'
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
