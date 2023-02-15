#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        x, y = 1, 1
        total = 0
        while x <= n:
            if x % 2 == 0:
                total += x
            x, y = y, x + y
        print(total)
