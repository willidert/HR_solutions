def countingSort(arr):
    counter = [0] * 100
    for i in arr:
        counter[i] += 1
    arr.clear()
    for _ in range(100):
        if counter[_] != 0:
            arr.append((str(_)+' ')*counter[_])
    return arr
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
#MuitaAtençãoAqui!!!ResolviDeUmJeitoÉpico!
#EuRetireiOEspaçoDoJoin!!!
    print(''.join(map(str,countingSort(arr))))
