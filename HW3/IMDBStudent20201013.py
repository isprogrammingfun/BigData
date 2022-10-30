#!/usr/bin/python3
import sys

cate = dict()
print(sys.argv[2])
with open (sys.argv[2], "rt") as fp:
  for line in fp:
    str_arr = line.split("::")
    if str_arr[4].find("|") is True:
      arr = str_arr[4].split("|")
      for i in arr:
          if i not in cate:
            cate[i] = 1
          else:
            cate[i] += 1  
    else:  
      if str_arr[4] not in cate:
        cate[str_arr[4]] = 1
      else:
        cate[str_arr[4]] += 1


with open (sys.argv[3], "wt") as fp:
  for key, value in cate.items():
    print(key,value)
    fp.write(key, value)
