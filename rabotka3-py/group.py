from student import Student

class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            return True
        return False

    def remove_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                return True
        return False

    def show_students(self):
        print(f"Группа: {self.name}")
        for s in self.students:
            print(f"  {s.name} (средний балл: {s.get_average_grade():.2f})")

    def get_average(self):
        if not self.students:
            return 0
        return sum(s.get_average_grade() for s in self.students) / len(self.students)