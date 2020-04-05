import itertools

def alternate(s):
    maior = 0
    valido = True
    if len(set(s)) - 2 == 0:
        return len(set(s))
    elif len(set(s)) - 2 < 0:
        return maior
    else:
        conjU = itertools.combinations(set(s), len(set(s)) - 2)
    for conj in conjU:
        string = s
        for elemento in range(len(set(s)) - 2):
            string = string.replace(conj[elemento], '')
        valido = True
        for i in range(1, len(string)):
            if string[i] == string[i - 1]:
                valido = False
                break
        if valido and len(string) > maior:
            maior = len(string)
    return maior


if __name__ == '__main__':
    l = int(input().strip())

    s = input()

    result = alternate(s)
    
    print(result)
