import random

class Student:
    
    def __init__(self, name, grade, points):
        self.name = name
        self.grade = grade
        self.q1points = 0
        self.q2points = 0
        self.q3points = 0
        self.q4points = 0
        self.total_points = self.q1points + self.q2points + self.q3points + self.q4points

    def add_points(self, points):
        self.q1points += points

class Event:

    def __init__(self, name, is_sporting, points):
        self.name = name
        self.is_sporting = is_sporting
        self.points = points

class StudentList:

    def __init__(self, students = []):
        self.students = students
        self.grade_9_students = []
        self.grade_10_students = []
        self.grade_11_students = []
        self.grade_12_students = []
        for student in students:
            eval("self.grade_" + str(student.grade) + "_students").append(student)

    def generate_report(self):
        pass

    def generate_winner(self, grade):
        students = eval("self.grade_" + str(grade) + "_students")
        if students:
            return random.choice(students).name

    def get_top_3(self):
        sorted_students = sorted(self.students, key = lambda x : x.total_points, reverse = True)
        top_3_names = [student.name for student in sorted_students[:3]]
        top_3_points = [student.total_points for student in sorted_students[:3]]
        return top_3_names, top_3_points


student1 = Student("Kevin Li", 11, 0)
student2 = Student("Prateek Singh", 11, 0)
student3 = Student("Shivam Kumar", 10, 10)
student4 = Student("Shreyas Krishnan", 10, 10)
student_list = StudentList([student1, student2, student3, student4])
