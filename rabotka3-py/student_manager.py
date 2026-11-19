from student import Student, ExcellentStudent

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if self.find_student(student.student_id):
            print("Студент с таким ID уже существует!")
            return False
        self.students.append(student)
        return True

    def show_students(self):
        if not self.students:
            print("Список студентов пуст.")
            return
        for s in self.students:
            print(s)

    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def find_by_name(self, name):
        found = [s for s in self.students if name.lower() in s.name.lower()]
        return found

    def delete_student(self, student_id):
        student = self.find_student(student_id)
        if student:
            self.students.remove(student)
            return True
        return False

    def update_student(self, student_id, name=None, age=None, group=None):
        student = self.find_student(student_id)
        if not student:
            return False
        if name:
            student.name = name
        if age:
            if age < 16:
                raise ValueError("Возраст должен быть не менее 16")
            student.age = age
        if group:
            student.group = group
        return True

    def find_by_group(self, group):
        return [s for s in self.students if s.group == group]

    def count_students(self):
        return len(self.students)

    def get_students_above_average(self, threshold=4.0):
        return [s for s in self.students if s.get_average_grade() > threshold]

    def get_students_older_than(self, age=18):
        return [s for s in self.students if s.age > age]

    def get_best_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.get_average_grade())

    def get_worst_student(self):
        if not self.students:
            return None
        return min(self.students, key=lambda s: s.get_average_grade())

    def get_random_student(self):
        import random
        if not self.students:
            return None
        return random.choice(self.students)