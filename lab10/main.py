#!/usr/bin/env python3

import sys

def calculate_param_expression(param):
    return int( (param*2) / len(str(param)) )
    

def my_printf(format_string, param):
    pass
    

data=sys.stdin.readlines()

for i in range(0,len(data),2):
    my_printf(data[i].rstrip(),data[i+1].rstrip())
