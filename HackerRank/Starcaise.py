def staircase(n):
    l=1 
    caracter='#'  
    c=1  
    floyd = ''
    lista=[' ']*n
    for l in range(1, n+1):
        for c in range(1,l+1):
            floyd += caracter # dá um espaço entre os números
        floyd=floyd.rstrip()   
        print(floyd.rjust(n))
        floyd = ''

if __name__ == '__main__':
    n = int(input())
    staircase(n)
