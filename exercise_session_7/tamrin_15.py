class Course:
    def __init__(self, name, professor, max_capacity):
        self.name = name
        self.professor = professor
        self.max_capacity = max_capacity
        self.students = []

    def enroll(self, student):
        if len(self.students) < self.max_capacity:
            self.students.append(student)
            return True
        return False

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def enroll(self, course):
        if course.enroll(self):
            print(f"{self.name} dar dars {course.name} sabtnam shode ast")
        else:
            print(f"Sabtnam baraye {self.name} dar dars {course.name} namofagh bood")

    def add_grade(self, course, grade):
        self.grades[course.name] = grade

    def show_grades(self):
        for course, grade in self.grades.items():
            print(f"Dars: {course}, Nomre: {grade}")

class School:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)

    def add_student(self, student):
        self.students.append(student)

    def enroll_student_in_course(self, student, course):
        student.enroll(course)

    def record_grade(self, student, course, grade):
        student.add_grade(course, grade)

    def show_students_in_course(self, course):
        for student in course.students:
            print(student.name)

if __name__ == "__main__":
    madrese = School()
    dars_riazi = Course("Riazi", "Ostad Ahmadi", 3)
    dars_fizik = Course("Fizik", "Ostad Mohammadi", 2)
    madrese.add_course(dars_riazi)
    madrese.add_course(dars_fizik)
    danesh_amoze1 = Student("Ali")
    danesh_amoze2 = Student("Zahra")
    danesh_amoze3 = Student("Reza")
    madrese.add_student(danesh_amoze1)
    madrese.add_student(danesh_amoze2)
    madrese.add_student(danesh_amoze3)
    madrese.enroll_student_in_course(danesh_amoze1, dars_riazi)
    madrese.enroll_student_in_course(danesh_amoze2, dars_riazi)
    madrese.enroll_student_in_course(danesh_amoze3, dars_riazi)
    madrese.enroll_student_in_course(danesh_amoze1, dars_fizik)
    madrese.record_grade(danesh_amoze1, dars_riazi, 18)
    madrese.record_grade(danesh_amoze2, dars_riazi, 16)
    madrese.record_grade(danesh_amoze1, dars_fizik, 19)
    print("\nNomarat Ali:")
    danesh_amoze1.show_grades()
    print("\nDanesh-amoozan dar dars Riazi:")
    madrese.show_students_in_course(dars_riazi)
