nA = int(input())
a = set(map(int, input().split()))
nB = int(input())
b = set(map(int, input().split()))

difAB = a.difference(b)
difBA = b.difference(a)
for i in sorted(difBA.union(difAB)):
    print(i)
