def utopianTree(n):
    altura = 1
    for i in range(1, n+1):
        if i % 2 == 0:
            altura += 1
        else:
            altura *= 2
    return altura

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(result)
