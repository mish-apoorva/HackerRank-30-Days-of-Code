#!/bin/python

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):


    # Write your calculation code here
    tip = (tip_percent/100)* meal_cost # calculate tip
    tax = (tax_percent/100)* meal_cost# caclulate tax

    # cast the result of the rounding operation to an int and save it as total_cost 
    total_cost = round(meal_cost+tip+tax)
    print(total_cost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)