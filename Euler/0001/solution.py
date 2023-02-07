#!/bin/python3

import math
import os
import random
import re
import sys

def find_sum(number,divisor):
    number //= divisor
    return divisor * number * (number + 1) // 2


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(find_sum(n-1, 3) + find_sum(n-1, 5) - find_sum(n-1, 3 * 5))