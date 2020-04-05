def fibonacciModified(t1, t2, n):
    fib = [t1, t2]
    i = 0
    while len(fib) < n:
        fib.append(fib[i]+fib[i+1]**2)
        i += 1
    return fib[n-1]

if __name__ == '__main__':
    
    t1T2n = input().split()
## Ele me dá os dois primeiros termos da serie
## Eu preciso só calcular os próximos até o elemento que ele me pede
## note que a pos 0 representa o 1 elemento
## Logo n é a pos n-1 no meu vetor de fibonacci!
    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)
    print(result)
