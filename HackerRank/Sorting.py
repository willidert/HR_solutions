n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swaps = 0
trocou = True

while trocou:
    trocou = False
    for i in range(n-1):
        if a[i]>a[i+1]:
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
            trocou = True
            swaps +=1
print('Array is sorted in {} swaps.'.format(swaps))
print('First Element:',a[0])
print('Last Element:',a[n-1])
