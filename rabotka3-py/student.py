import re

class Student:
    def __init__(self, student_id, name, age, group, grades=None, email=None):
        if age < 16:
            raise ValueError("Возраст студента должен быть не менее 16 лет")
        self.student_id = student_id
        self.name = name
        self.age = age
        self.group = group
        self.grades = grades if grades is not None else []
        self.email = email
        if email:
            self.set_email(email)

    def set_email(self, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            self.email = email
        else:
            raise ValueError("Некорректный адрес электронной почты")

    def add_grade(self, grade):
        if 2 <= grade <= 5:
            self.grades.append(grade)
        else:
            raise ValueError("Оценка должна быть от 2 до 5")

    def remove_last_grade(self):
        if self.grades:
            return self.grades.pop()
        return None

    def get_max_grade(self):
        return max(self.grades) if self.grades else 0

    def get_min_grade(self):
        return min(self.grades) if self.grades else 0

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_unique_grades(self):
        return set(self.grades)

    def is_successful(self):
        return self.get_average_grade() >= 3

    def get_status(self):
        avg = self.get_average_grade()
        if avg >= 4.5:
            return "Отличник"
        elif avg >= 3:
            return "Успевающий"
        else:
            return "Неуспевающий"

    def show_info(self):
        print(f"Студент: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Группа: {self.group}")
        print(f"Оценки: {self.grades}")
        print(f"Средний балл: {self.get_average_grade():.2f}")
        print(f"Статус: {self.get_status()}")
        if self.email:
            print(f"Email: {self.email}")

    def __str__(self):
        return f"[{self.student_id}] {self.name}, {self.age} лет, группа {self.group}, средний балл: {self.get_average_grade():.2f}"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "group": self.group,
            "grades": self.grades,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            group=data["group"],
            grades=data.get("grades", []),
            email=data.get("email")
        )


class ExcellentStudent(Student):
    def __init__(self, student_id, name, age, group, scholarship, grades=None, email=None):
        super().__init__(student_id, name, age, group, grades, email)
        self.scholarship = scholarship

    def show_info(self):
        super().show_info()
        print(f"Стипендия: {self.scholarship} руб.")

    def get_scholarship(self):
        return self.scholarship

    def to_dict(self):
        data = super().to_dict()
        data["scholarship"] = self.scholarship
        data["type"] = "excellent"
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            group=data["group"],
            scholarship=data.get("scholarship", 0),
            grades=data.get("grades", []),
            email=data.get("email")
        )