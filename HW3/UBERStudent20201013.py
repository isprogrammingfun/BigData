#!/usr/bin/python3
import sys
from datetime import datetime, date

def get_day(date):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.weekday()
    return days[day]

a = list()

with open (sys.argv[1], "rt") as fp:
  for line in fp:
    str_arr = line.split(",")
    arr = str_arr[1].split("/")
    key = str_arr[0] + "," + get_day(date(int(arr[2]), int(arr[0]), int(arr[1])))
    str_arr[3] = str_arr[3].replace("\n", "")
    value = str(str_arr[2]) + "," + str(str_arr[3])
    a.append(key + " " + value)

print(a)
with open (sys.argv[2], "wt") as fp:
    for i in a:
        fp.write(i + "\n")
