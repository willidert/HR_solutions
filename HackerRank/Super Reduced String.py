def superReducedString(s):
    conj = sorted(set(s))
    res = ''
    for i in conj:
        cont = s.count(i)
        if cont % 2 != 0:
            res += i
    if len(res) > 0:
        return res
    else:
        return 'Empty String'

if __name__ == '__main__':
    s = input()

    result = superReducedString(s)

    print(result)
