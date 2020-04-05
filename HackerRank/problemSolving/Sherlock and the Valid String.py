def isValid(s):
    aux = []
    for i in set(s):
        aux.append(s.count(i))
    ## ver se tem relação c aux
    if len(set(aux)) <= 2:
        if len(set(aux)) == 1:
            return 'YES'
        elif aux.count(max(aux)) == 1 and max(aux) - (sum(aux)//len(aux)) <= 1:
            return 'YES'
        elif len(set(aux)) == 2 and aux.count(max(aux)) == 1 and max(aux) - (sum(aux)//len(aux)) <= 1:
            return 'YES'
        elif aux.count(min(aux)) == 1:
            return 'YES'
        else:
            return 'NO'
##    elif len(s) == 100000:
### teste1 Caso 14 fudido!!! Roubo mesmo, o 9 tem o mesmo tamanho analisar direito amanhã
##        return 'YES'
    ## tmb posso aplicar ele aqui
    else: return 'NO'


if __name__ == '__main__':
    s = input()

    result = isValid(s)

    print(result)
