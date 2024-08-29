class Student:
    def __init__(self, name,current_class,roll):
        self.name = name
        self.current_class = current_class
        self.roll = roll 

    def __repr__(self) -> str:
        return f'Student name: {self.name}, class: {self.current_class}, and roll: {self.roll}'


class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher name: {self.name}, subject he teaches: {self.subject}, and his id is: {self.id}'

class School:
    def __init__(self, name) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subject):
       id = len(self.teachers) + 101
       teacher = Teacher(name, subject, id)
       self.teachers.append(teacher)

    def enroll_student(self, name, fee):
      if fee < 6500:
          return "Not enough fee"
      else:
          roll = len(self.students) + 1
          student = Student(name, "C", roll)
          self.students.append(student)
          return f'{name} is enroll with roll: {roll}, extra money {fee - 6500}'
      
    def __repr__(self) -> str:
        print('Welcome to', self.name)
        print('---------Our Teachers-------')
        for teacher in self.teachers:
            print(teacher)
        print('-------Our Student------')
        for student in self.students:
            print(student)
        return 'All done for now'


# rumky = Student("Annika Islam Rumky", 15, 133)
# Murad = Teacher("Md. Murad Ali", "Data structure and Algorithm", 1)
# print(rumky)
# print(Murad)
phitron = School('Phitron Online School')
phitron.enroll_student('Mamun', 4600)
phitron.enroll_student('Hasib', 8700)
phitron.enroll_student('Shikhan', 6500)
phitron.enroll_student('Mim', 90000)

phitron.add_teacher('Lemon', 'DSP')
phitron.add_teacher('Hafeez', 'Antenna')
phitron.add_teacher('Imran', 'Java')

print(phitron)