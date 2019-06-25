n = int(input())

for i in range(n):
    _ = int(input())
    a = set(map(int, input().split()))
    _b = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))
