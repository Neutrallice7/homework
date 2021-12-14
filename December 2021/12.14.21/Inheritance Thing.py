class Person:
    def __init__(self, name, address):
        __name = name
        __address = address
    def getName(self):
        self.__name = ''
    def getAdress(self):
        self.__address = ''
    def setAdress(self):
        self.__setaddress = __address
    
class Student(Person):
    def __init__(self, numCourse, courses, grades):
        __numCourse = ['']
        __courses = ['English', 'Math', 'Science']
        __grades = {'English':'', 'Math':'', 'Science':''}
        Person.__init__(name, address)
    def addGrades(self):
        self.__grades = ""
    def printGrades(self):
        return self.__grades
    def getAverageGrade(self):
       AverageGrade = (self.__grades['English'] + self.__grades['Math'] + self.__grades['Science']) / 3

class Teacher(Person):
    def __init__(self, numCourse, courses):
        __numCourse = ['']
        __courses = ['English', 'Math', 'Science']
        Person.__init__(name, address)
    def addCourses(self):
        self.__course.append
    def removeCourse(self):
        self.__courses.remove