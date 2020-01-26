# Inheritance - User input student name, surname and ID on 1 line - The input amount fo scores for student and then input different 
# scores for student on one line. The progrfam will work out the average and print out the students details + symbol achieved

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        
    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)
        
class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        self.scores = scores
        
    def calculate(self):
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90:
            return "A+"
        if avg >= 80:
            return 'A'
        if avg >= 75:
            return 'B+'
        if avg >= 70:
            return 'B'
        if avg >= 65:
            return 'C+'
        if avg >= 60:
            return 'C'
        if avg >= 55:
            return 'D+'
        if avg >= 50:
            return 'D'
        if avg >= 40:
            return 'E'
        return 'T'
    
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list(map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
