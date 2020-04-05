import math
import os
import random
import re
import sys


def repeatedString(s, n):
    aux = s
    i = 0
    while len(aux) < n:
        if i > len(s) - 1:
            i = 0
        aux += s[i]
        i += 1
    return aux.count('a')


if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(result)
