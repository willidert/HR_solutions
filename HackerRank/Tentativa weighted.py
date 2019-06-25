#Weighted Uniform Strings
import string
from datetime import datetime


def pesar(s):
    dic = {}
    conj = set(s)
    for i in conj:
        for letter in range(len(list(string.ascii_lowercase))):
            if list(string.ascii_lowercase)[letter] == i:
                dic[list(string.ascii_lowercase)[letter]] = letter + 1
    return dic


def weightedUniformStrings(s, queries):
    dic = pesar(s)
    subsIn = [[] for i in range(len(queries))]
    
    for char, peso in dic.items():
        for q in range(len(queries)):
            if queries[q] % peso == 0:
                aux = char * (queries[q] // peso)
                subsIn[q].append(aux in s) 
    res = [any(i) for i in subsIn]
    for i in range(len(res)):
        if res[i] == True:
            res[i] = 'Yes'
        else:
            res[i] = 'No'
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
