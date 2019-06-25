def jumpingOnClouds(c):
    jumps = 0
    me = 0
    while me < len(c) - 1:
        if me + 2 < len(c) and c[me+2] != 1:
            me += 1
        jumps +=1
        me += 1
    return jumps
    

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)
