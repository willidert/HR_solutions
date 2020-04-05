nI = int(input())

english = set(map(int, input().split()))

nF = int(input())

french = set(map(int, input().split()))

students_english = english.difference(french)

print(len(students_english))
