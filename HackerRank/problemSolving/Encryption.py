import math


def encryption(s):
    row = math.floor(math.sqrt(len(s)))
    col = math.ceil(math.sqrt(len(s)))
    if row*col < len(s):
        row += 1
    msg = [[' ' for _ in range(col)] for _ in range(row)]


    iterator = 0
    for i in range(row):
        for j in range(col):
            msg[i][j] = s[iterator]
            iterator += 1
            if iterator == len(s):
                break
    cMsg = ''
    for j in range(col):
        for i in range(row):
            cMsg += msg[i][j]
            if cMsg[-1] == ' ':
                cMsg = cMsg.rstrip()
        cMsg += ' '

    return cMsg.rstrip()

if __name__ == '__main__':
    s = input()
    print(encryption(s))
