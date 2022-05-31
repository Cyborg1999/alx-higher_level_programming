#!/usr/bin/python3
for num in range(0, 100):
    if num != 99:
        print(f"{num:02d}, ".format(num), end='')
    else:
        print("{num:02d}".format(num))
