def permutationEquation(p):
    p.insert(0, 0)
    res = []
    for i in range(1, len(p)):
        res.append(p.index(p.index(i)))
    return res

if __name__ == '__main__':

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print(result)
