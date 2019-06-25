def camelcase(s):
    cont = 1
    for letter in s:
        if letter.isupper():
            cont += 1
    return cont

if __name__ == '__main__':
    s = input()

    result = camelcase(s)
    print(result)
