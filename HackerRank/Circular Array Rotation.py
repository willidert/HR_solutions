def right_rotation(a, k):
   # if the size of k > len(a), rotate only necessary with
   # module of the division
   rotations = k % len(a)
   return a[-rotations:] + a[:-rotations]

def circularArrayRotation(a, k, queries):
    ## k é o númeor de rotações
    if k < len(a):
        a = a[-k:] + a[:-k]
    elif k > len(a):
        rot = k % len(a)
        a = a[-rot:] + a[:-rot]
##    else:
##        rot = len(a)  % k
##        a = a[rot:]+a[:rot]

    buscas = []
    for i in queries:
        buscas.append(a[i])
    return buscas

          
if __name__ == '__main__':
    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    print(result)
