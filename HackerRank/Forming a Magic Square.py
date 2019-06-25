def formingMagicSquare(s):
    pares = list(range(2, 10, 2))
    impares = list(range(1, 10, 2))
    
            
    return s
    
if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    for i in result:
        print(i)
