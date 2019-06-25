n = int(input())
agenda = {}
for i in range(n):
    contato = input().split()
    agenda[contato[0]] = contato[1]
for i in range(n):
    busca = input()
    if busca in agenda:
        for j in agenda.keys():
            if j == busca:
                print(j+"="+agenda[j])
    else:
        print("Not Found")

n = int(input())
agenda = {}
for i in range(n):
    contato = input().split()
    agenda[contato[0]] = contato[1]
busca = []
for i in range(n):
    busca.append(input())
print(busca)
for nome in busca:
    if nome in agenda:
        for j in agenda.keys():
            if j == nome:
                print(j+"="+agenda[j])
    else:
        print("Not found")
