import string


def minimumNumber(n, password):
    cont = 0
    conj = set(password)
    conja = set(string.ascii_lowercase)
    conjA = set(string.ascii_uppercase)
    conjN = set(string.digits)
    conjS = set(list("!@#$%^&*()-+"))
    
    if conj.isdisjoint(conja):
        cont += 1
    if conj.isdisjoint(conjA):
        cont += 1
    if conj.isdisjoint(conjN):
        cont += 1
    if conj.isdisjoint(conjS):
        cont += 1

    while 6 - len(password) > cont:
        cont += 1
        
    return cont

if __name__ == '__main__':
    n = int(input())

    password = input()

    answer = minimumNumber(n, password)
    print(answer)
