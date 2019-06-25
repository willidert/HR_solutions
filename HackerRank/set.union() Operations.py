nI = int(input())

english = set(map(int, input().split()))

nF = int(input())

french = set(map(int, input().split()))

students = english.union(french)

print(len(both))
