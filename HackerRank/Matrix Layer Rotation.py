import math
import os
import random
import re
import sys

'''Ele usa duas matrizes!!!
entender direito as regras que parecem simples
while True é um tal de 'brute force'
'''

# Só submeter quando entender esse código!!!
def matrixRotation(matrix, r):
    linha=len(matrix)
    coluna=len(matrix[0])
    k=min(linha//2,coluna//2)                 #boundaries for mid rows & cols

    while r>0:
        O= [[1 for i in range(coluna)] for j in range(linha)]      #Output canvas   
        print(O)
        for i in range(0,k):
            for j in range(i,coluna-1-i):    #note j range to change mid r&c
                O[i][coluna-j-2]=matrix[i][coluna-j-1]                 #Top row 
                O[linha-i-1][coluna-j-1]=matrix[linha-i-1][coluna-j-2]          #Bottom row

            for j in range(i,linha-1-i):
                O[linha-j-1][i]=matrix[linha-j-2][i]  #Left col
                O[linha-j-2][coluna-i-1]=matrix[linha-j-1][coluna-i-1]           #Right col
        matrix=O              #store matrix after 1 rotation
        r-=1

    for i in O:               #Print final output
        for j in i:
             print(j, end=" ")
        print(end='\n')

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
