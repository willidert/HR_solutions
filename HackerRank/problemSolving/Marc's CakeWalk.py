def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
## Ele quer o correr a menor distância logo ordenar ao inverso :)
    miles = 0
    for i in range(len(calorie)):
        miles += 2**i * calorie[i]
    return miles


if __name__ == '__main__':

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    print(result)
