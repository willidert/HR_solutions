a = set(map(int, input().split()))
n = int(input())

def check_superset(n, a):
    subset = True
    for i in range(n):
        b = set(map(int, input().split()))
        if a.issuperset(b):
            subset = False
            return subset
    return subset

print(check_superset(n, a))


a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))
## elegant broo!
