def gradingStudents(grades):
    for nota in range(len(grades)):
        for i in range(40,101,5):
            if grades[nota] < i and i - grades[nota] < 3:
                grades[nota] = i
    return grades

if __name__ == '__main__':
    n = int(input())
    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
