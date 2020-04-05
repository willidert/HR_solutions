import math


def viralAdvertising(n):
    shared = 5
    liked = math.floor(shared/2)
    cont = liked
    for i in range(1, n):
        shared = liked * 3
        liked = math.floor(shared/2)
        cont += liked
    return cont
        

if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)

    print(result)
