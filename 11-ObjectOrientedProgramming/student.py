# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.country = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.country = "Spain"
    student2.name = "Olivia"
    student2.age = 21
    student2.country = "Canada"
    student3.name = "Suzuya"
    student3.age = 14
    student3.country = "Japan"


    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, {student1.country}')
    print(f'{student2.name}, {student2.age} years old, {student2.country}')
    print(f'{student3.name}, {student3.age} years old, {student3.country}')

if __name__ == "__main__":
    main()