x, k = [int(x) for x in input().split()]
if eval(input()) == k:
## eval() recebe uma string e calcula a string, ex: 'x**2 + 2'
    print('True')
else:
    print('False')
