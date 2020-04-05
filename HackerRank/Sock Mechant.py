import math
import os
import random
import re
import sys


def sockMerchant(n, ar):
    colors = sorted(set(ar))
    pares = 0
    for i in colors:
        if ar.count(i) % 2 != 0:
            pares += ar.count(i) - 1
        else: pares += ar.count(i)
    return pares//2

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

