def movingTiles(l, s1, s2, queries):
    if s1 > s2:
        return (l**4) / (s1 - s2)
    return (l **4) / (s2 - s1)
    
if __name__ == '__main__':
    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    print(result)
