if __name__ == '__main__':
    n = int(input())
    estudantes = {}
    for i in range(n):
        aluno = input()
        nota = float(input())
        estudantes[nota] = aluno
    sorted(estudantes.keys())
    notas = list(estudantes.keys())
    menor = notas[0]
    for j in estudantes.keys():
        if j == menor:
            print(estudantes[j])
            print(j)
