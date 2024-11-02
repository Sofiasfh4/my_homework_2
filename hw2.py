import datetime

class Student:


    def __init__(self,name, surname, birthdate, height=160):
        self.name = name
        self.surname = surname
        self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
        self.height = height

    def printStudent(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Birthdate: {self.birthdate.strftime('%d.%m.%Y')}")
        print(f"Height: {self.height}")





# створення об'єкта
first_student = Student('kira', 'kasheva', '10.5.2008',165)
second_student = Student('vlad', 'gantelin', '4.12.2007',178)

first_student.printStudent()
print('------------------------------')
second_student.printStudent()