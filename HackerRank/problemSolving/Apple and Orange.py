import math
import os
import random
import re
import sys


def countApplesAndOranges(s, t, a, b, apples, oranges):
    cont_a = 0
    cont_o = 0
    for i in apples:
## só conto as maçãs c chance de cair perto da casa i > 0
        if i > 0 and (i + a >= s and i + a <= t):
            cont_a +=1
    for i in oranges:
## i < 0
        if i < 0 and (b + i >= s and b + i <= t):
            cont_o += 1
    print(cont_a)
    print(cont_o)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
