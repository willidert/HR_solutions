def marsExploration(s):
    cont = 0
    conj = []
    st, end = 0, 3
    for i in range(len(s)//3):
        conj.append(s[st:end])
        st = end
        end += 3
    msg = list('SOS')
    for comb in conj:
        if comb != msg:
            for i in range(3):
                if msg[i] != comb[i]:
                    cont += 1
    return cont


if __name__ == '__main__':
    s = input()

    result = marsExploration(s)

    print(result)
