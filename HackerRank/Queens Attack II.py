'''
Outra ideia é usar a lista de obstaculos pra achar as casa atacavéis
'''

def queensAttack(n, k, r_q, c_q, obstacles):
    rainha = [r_q, c_q]
    cont = 0
    ## up
    while r_q - 1 >= 1 and [r_q - 1, c_q] not in obstacles:
        r_q -= 1
        cont += 1
    r_q, c_q = rainha
    ## down
    while r_q + 1 <= n and [r_q + 1, c_q] not in obstacles:
        r_q += 1
        cont += 1
    r_q, c_q = rainha
    ## left
    while c_q - 1 >= 1 and [r_q, c_q - 1] not in obstacles:
        c_q -= 1
        cont += 1
    r_q, c_q = rainha
    ## right
    while c_q + 1 <= n and [r_q, c_q + 1] not in obstacles:
        c_q += 1
        cont += 1
    r_q, c_q = rainha
    ## direita + baixo
    while r_q + 1 <= n and c_q + 1 <= n and [r_q + 1, c_q + 1] not in obstacles:
        r_q += 1
        c_q += 1
        cont += 1
    r_q, c_q = rainha
    ## esquerda + cima
    while r_q - 1 >= 1 and c_q - 1 >= 1 and [r_q - 1, c_q - 1] not in obstacles:
        r_q -= 1
        c_q -= 1
        cont += 1
    r_q, c_q = rainha
    ## esquerda + baixo
    while r_q + 1 <= n and c_q - 1 >= 1 and [r_q + 1, c_q - 1] not in obstacles:
        r_q += 1
        c_q -= 1
        cont += 1
    r_q, c_q = rainha
    ## direita + cima
    while r_q - 1 >= 1 and c_q + 1 <= n and [r_q - 1, c_q + 1] not in obstacles:
        r_q -= 1
        c_q += 1
        cont += 1

    return cont

if __name__ == '__main__':

    nk = input().split() #tabuleiro nXn, k é o numero de obstaculos

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split() #pos da rainha[i, j]

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = [] # Uma lista de pos dos obstáculos

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
