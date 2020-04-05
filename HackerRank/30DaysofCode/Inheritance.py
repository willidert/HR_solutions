# Learn: FreeCodeCamp

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):

    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    def calculate(self):
        cal = sum(self.scores) / len(self.scores)
        if cal >= 90 and cal <= 100:
            return "O"
        elif cal >= 80 and cal < 90:
            return "E"
        elif cal >= 70 and cal < 80:
            return "A"
        elif cal >= 55 and cal < 70:
            return "P"
        elif cal >= 40 and cal < 55:
            return "D"
        elif cal < 40:
            return "T"

if __name__ == '__main__':
    line = input().split()
    firstName = line[0]
    lastName = line[1]
    idNum = line[2]
    numScores = int(input())  # not needed for Python
    scores = list(map(int, input().split()))
    s = Student(firstName, lastName, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())

