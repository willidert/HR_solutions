def breakingRecords(scores):
    menor = scores[0]
    maior = scores[0]
    contm = 0
    contn = 0
    for i in range(1, len(scores)):
        if i > maior:
            contm += 1
            maior = i
        elif i < menor:
            contn += 1
            menor = i
    return contm, contn
n = int(input())
scores = list(map(int, input().split()))
result = breakingRecords(scores)
