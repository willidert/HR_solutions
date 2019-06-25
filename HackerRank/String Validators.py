if __name__ == '__main__':
    s = list(input())
    testes = [[] for _ in range(5)]
    for i in range(len(s)):
        testes[0].append(s[i].isalnum())
        testes[1].append(s[i].isalpha())
        testes[2].append(s[i].isdigit())
        testes[3].append(s[i].islower())
        testes[4].append(s[i].isupper())

    for i in testes:
        print(any(i))

