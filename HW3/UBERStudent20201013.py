#!/usr/bin/python3
import sys
from datetime import datetime, date

def get_day(date):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day = date.weekday()
    return days[day]

uber = dict()
with open (sys.argv[1], "rt") as fp:
	for line in fp:
		str_arr = line.split(",")
		region = str_arr[0]
		arr = str_arr[1].split("/")
		key = region + "," + get_day(date(int(arr[2]), int(arr[0]), int(arr[1])))
		vehicle = int(str_arr[2])
		trip = int(str_arr[3].replace("\n", ""))

		if key in uber:
			value = uber[key].split(",")
			vehicle += int(value[0])
			trip += int(value[1])
		uber[key] = str(vehicle) + "," + str(trip)


with open (sys.argv[2], "wt") as fp:
  for key, value in uber.items():
    fp.write(f'{key } {value}\n')