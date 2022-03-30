class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
        

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        # self.name = name
        # self.phoneNumber = phoneNumber
        
        # 명시적으로 부모 생성자 호출
        Person.__init__(self, name, phoneNumber)

        self.subject = subject
        self.studentID = studentID

    # override
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1}, subject: {2}, year:{3})".format(self.name, self.phoneNumber, self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
print(p.__dict__)
print(s.__dict__)
# s1 = Student('ws', '000-000-000')
# print(s1.__dict__)
p.printInfo()
s.printInfo()


