import math
## dAB = sqrt((x2 - x1)**2 + (y2- y1)**2)

def solve(coordinates):
    distante = 0.000000
    for ponto in range(len(coordinates)):
        x1, y1 = coordinates[ponto]
        j = ponto + 1
        while j < len(coordinates):
            x2, y2 = coordinates[j]
            d = math.sqrt((x2 - x1)**2 + (y2  - y1)**2)
            if d > distante:
                distante = d
            j += 1
    return round(distante, 6)
    

if __name__ == '__main__':
    n = int(input())

    coordinates = []

    for _ in range(n):
        coordinates.append(list(map(int, input().rstrip().split())))

    result = solve(coordinates)

    print(result)
