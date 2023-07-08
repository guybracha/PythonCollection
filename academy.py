class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        Value = 0
        for student in self.students:
            Value += student.get_grade()

        return Value / len(self.students)

s1 = Student("tim", 19, 95)
s2 = Student("bill", 19, 75)
s3 = Student("jill",19,65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.add_student(s3))
print(course.get_average_grade())
courseOne = Course("Computer Science", 4)
print(courseOne.add_student(s1))
print(courseOne.name)
print(course.name)