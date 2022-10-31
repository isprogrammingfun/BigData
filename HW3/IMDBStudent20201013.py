#!/usr/bin/python3
import sys

cate = dict()

with open (sys.argv[1], "rt") as fp:
  for line in fp:
    str_arr = line.split("::")
    if "|" in str_arr[2]:
      arr = str_arr[2].split("|")
      for i in arr:
        if "\n" in i:
          i = i.replace("\n", "")
        if i not in cate:
          cate[i] = 1
        else:
          cate[i] += 1
    else:
      if "\n" in str_arr[2]:
        str_arr[2] = str_arr[2].replace("\n", "")
        if str_arr[2] not in cate:
          cate[str_arr[2]] = 1
        else:
          cate[str_arr[2]] += 1


with open (sys.argv[2], "wt") as fp:
  for key, value in cate.items():
    fp.write(f'{key } {value}\n')
