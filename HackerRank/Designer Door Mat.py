n, m = map(int, input().split())

cont_pb = 1
cont_t = (m//2) - 1
for i in range(n):
    if i == n//2:
        print('WELCOME'.center(m, '-'))
    elif i < n//2:
        print('-'*cont_t+('.|.'*cont_pb)+'-'*cont_t)
        cont_pb += 2
        cont_t -= 3
    else:
        cont_pb -= 2
        cont_t += 3
        print('-'*cont_t+('.|.'*cont_pb)+'-'*cont_t)
