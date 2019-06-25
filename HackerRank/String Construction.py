## momento Rei da Lógica/matemática/porra td
## questão era FÁCIL né animal : (


def stringConstruction(s):
    moves = len(set(s))
    return moves

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        print(result)
