## a rafa resolveu com um for e dois if : ( 

def jumpingOnClouds(c, k):
    e = 100
    me = 0
    while e >= 0 and (me+k) % len(c) >= k:
##        print((me+k) % len(c) >= k)
##        print(me, e)
        if c[(me + k) % len(c)] == 1:
            e -= 2
        e -= 1
        me = ((me + k) % len(c))
    if c[(me + k) % len(c)] == 1:
            e -= 2
    return e - 1
        

if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0]) ## number of clouds

    k = int(nk[1]) ## jump's range

    c = list(map(int, input().rstrip().split())) ## clouds

    result = jumpingOnClouds(c, k)

    print(result)
