t = int(input().strip())

for i in range(t):
    n = int(input().strip())
    qsoma = sum(list(range(1, n+1)))**2
    somaQ = 0
    somaQ = sum([i**2 for i in range(1, n+1)])
    print(abs(qsoma - somaQ))
