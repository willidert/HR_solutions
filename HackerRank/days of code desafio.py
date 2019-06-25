'''Lets review'''
n = int(input())
for i in range(n):
    string = input()
    print(string[0:len(string):2], string[1:len(string):2])

''' Recursion'''
# Complete the factorial function below.
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*(factorial(n-1))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    result = factorial(n)
    fptr.write(str(result) + '\n')
    fptr.close()

'''Binary Numbers '''
"print(len(max(re.findall(r'(1+)', bin(int(input()))))))" # aprender re :(
'''while(n > 0):
    remainder = n%2;
    n = n/2;
    Insert remainder to front of a list or push onto a stack'''
if __name__ == '__main__':
    n = int(input())
    bina = []
    seq = 0
    maiorseq = 0
    while n > 0:
        resto = n%2
        n = int(n/2)
        bina.insert(0, resto)
    #O erro ta aqui pelo laço!!!
    for i in range(len(bina)):
        if bina[i] == 1:
            seq += 1
            if seq == len(bina):
                maiorseq = seq
                break
        elif seq > maiorseq:
            maiorseq = seq

    print(maiorseq)
