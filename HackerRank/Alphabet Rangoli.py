# biblioteca muito útil
import string

def print_rangoli(size):
    # your code goes here
    alpha = string.ascii_lowercase
    rangoli = []
    for i in range(size):
        s = "-".join(alpha[i:n])
        rangoli.append(s[::-1]+s[1:])
    ##inverto a string e concateno c ela mesma

    width = len(rangoli[0])
    ## rangoli[0] está fora do range!
    for i in range(size-1, 0, -1):
        print(rangoli[i].center(width, "-"))

    ## conserto aqui :)
    for i in range(size):
        print(rangoli[i].center(width, "-"))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
