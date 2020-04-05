nI = int(input())

english = set(map(int, input().split()))

nF = int(input())

french = set(map(int, input().split()))

students_english_or_french = english.symmetric_difference(french)

print(len(students_english_or_french))
