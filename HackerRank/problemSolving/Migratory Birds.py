def migratoryBirds(arr):
    moreSee = 0
    qtdvistos = 0
    for i in range(1, 6):
        if arr.count(i) > qtdvistos:
            qtdvistos = arr.count(i)
            moreSee = i
    return moreSee

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
