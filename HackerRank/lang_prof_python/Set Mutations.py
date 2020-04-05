nA = int(input())

a = set(map(int, input().split()))

set_aux  = set()

for i in range(int(input())):
    op, set_aux = input().split()[0], map(int, input().split())
    getattr(a, op)(set_aux)
    ## funciona como o map, mas é mais interessante pq posso aplicar
    ## um método sem conhce-lo previamente
        
print(sum(a))
