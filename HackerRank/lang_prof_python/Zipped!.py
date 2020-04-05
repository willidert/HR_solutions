n, x = [int(num) for num in input().split()]
subject = []

for _ in range(x):
    subject.append(list(map(float,input().split())))
for _ in zip(*subject):
    print(sum(_)/len(_))
