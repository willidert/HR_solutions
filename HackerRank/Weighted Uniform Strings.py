import string
from datetime import datetime

def weightedUniformStrings(s, queries):
    
    dic = {}
    alpha = string.ascii_lowercase
    numbers = list(range(1, 27))

    for i in range(26):
        dic[alpha[i]] = numbers[i]

    cont = 0
    
    res = []
    
    for char, peso in dic.items():
        for q in range(len(queries)):
            add = False
            if queries[q] % peso == 0 and char * (queries[q] // peso) in s:
                print(char * (queries[q] // peso))
                add = True
                res.append('Yes')
            
            print(char)
            res.append('No')
##    res = [any(i) for i in subsIn]
##    for i in range(len(res)):
##        if res[i] == True:
##            res[i] = 'YES'
##        else:
##            res[i] = 'NO'
    return res

    
if __name__ == '__main__':
    inicio = datetime.now()

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)
    print(result)
    print(datetime.now() - inicio)
