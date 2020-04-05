
if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    somas = []

    for i in range(4):
        st = 0
        end = 3
        for x in range(4):
            somas.append(sum(arr[i][st:end]) + arr[i+1][st+1] + sum(arr[i+2][st:end]))
            st += 1
            end += 1

    print(max(somas))
