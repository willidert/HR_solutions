n = int(input())
s = set(map(int, input().split()))
k = int(input())
for i in range(k):
    op = input().split()
    if len(op) == 2:
        if op[1] in s:
            print(s)
            getattr(s, op[0])(op[1])
    else:
        print(s)
        getattr(s, op[0])

    
print(sum(s))
