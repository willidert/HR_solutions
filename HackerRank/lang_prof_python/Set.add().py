n = int(input())
stamp = set()
for i in range(n):
    country = input().rstrip()
    stamp.add(country)
print(len(stamp))
    
