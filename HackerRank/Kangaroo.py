## Repensar

def kangaroo(x1, v1, x2, v2):
    if x1 < x2 and v1 <= v2:
        return 'NO'
    elif x1 < x2 and v1 - v2 > x2:
        return 'NO'
    elif x2 < x1 and v2 <= v1:
        return 'NO'
    elif x2 < x1 and v2 - v1 > x1:
        return 'NO'
    else:
        return 'YES'


## x1 + y * v1 == x2 + y * v2
## y = (x2  - x1) // (v2 - v1)
## refazer

'''Fizeram usando força bruta :('''
def kangaroo(x1, v1, x2, v2):
    k1 = x1
    k2 = x2
    if x2 > x1 and v2 > v1:
        return "NO"    
    if v1 == v2 and not x1 == x2:
        return "NO"    
    while True:  
        k1 += v1
        k2 += v2
        if k1 == k2:
            return "YES"
        if k1 > k2:
            return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    fptr.write(result + '\n')
    fptr.close()
