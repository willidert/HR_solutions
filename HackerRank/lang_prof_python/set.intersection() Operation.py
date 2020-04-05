nI = int(input())

english = set(map(int, input().split()))

nF = int(input())

french = set(map(int, input().split()))

students_both = english.intersection(french)

print(len(students_both))
