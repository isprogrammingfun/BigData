#!/usr/bin/python3
import sys
from datetime import datetime, date

def get_day(date):
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    day = date.weekday()
    return days[day]

a = list()
with open (sys.argv[1], "rt") as fp:
  for line in fp:
    str_arr = line.split(",")
    arr = str_arr[1].split("/")
    s = str_arr[0] + "," + get_day(date(int(arr[2]), int(arr[0]), int(arr[1]))) + " " + str(str_arr[2]) + "," + str(str_arr[3])
    a.append(s)


with open (sys.argv[2], "wt") as fp:
  for i in a:
    fp.write(i)
