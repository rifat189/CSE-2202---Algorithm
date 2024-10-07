#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure, d):
    # notifications = 0
    global n
    i = n
    arr = []
    while i>=0:
        arr.append(expenditure[d-i])
        i-=1
    # n = n+1
    print(arr)
    arr.sort()
    print(arr)
    # print(arr[n//2])
    if n%2!=0:
        median = (arr[n//2] + arr[(n//2)+1]) / 2
    else:
        median = arr[n//2]
    print(median)
    # global notifications

    d += 1
    if d<len(expenditure):
        print(f"expenditure: {expenditure[d]}")

        if expenditure[d] >= 2 * median:
            global notifications
            notifications += 1
            print("ok")
        activityNotifications(expenditure, d)
    return notifications

expenditure = []
t = int(input())
d = int(input())
while t>0:
     expenditure.append(int(input()))
     t-=1
n = d-1
notifications = 0
print(expenditure)
count = activityNotifications(expenditure, d-1)
print(count)

