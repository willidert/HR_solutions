def countingValleys(n, s):
    cont = 0
    x = 0
    for i in range(n):
        if s[i] == 'D':
            x -= 1
        else:
            x += 1
        if x == 0 and s[i] == 'U':
            cont += 1
    return cont 

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(result)
