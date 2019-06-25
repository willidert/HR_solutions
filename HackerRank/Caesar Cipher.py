import string


def caesarCipher(s, k):
    if k > 26:
        k = k%26
    alpha = list(string.ascii_lowercase)
##    print(alpha)
    alphaMod = alpha[k:] + alpha[:k]
##    print(alphaMod)
    Alpha = list(string.ascii_uppercase)
##    print(Alpha)
    AlphaMod = Alpha[k:] + Alpha[:k]
##    print(AlphaMod)
    letras = list(s)
    for char in range(len(letras)):
        if letras[char] in alpha:
            letras[char] = alphaMod[alpha.index(letras[char])]
        elif letras[char] in Alpha:
            letras[char] = AlphaMod[Alpha.index(letras[char])]
    return ''.join(letras)


if __name__ == '__main__':
    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result)
