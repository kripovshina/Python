import json
import os
from student import Student, ExcellentStudent

def save_students(students, filename="data/students.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data = [s.to_dict() for s in students]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Данные сохранены в {filename}")

def load_students(filename="data/students.json"):
    if not os.path.exists(filename):
        print("Файл не найден. Создана пустая коллекция.")
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        students = []
        for item in data:
            if item.get("type") == "excellent":
                students.append(ExcellentStudent.from_dict(item))
            else:
                students.append(Student.from_dict(item))
        print(f"Загружено {len(students)} студентов.")
        return students
    except json.JSONDecodeError:
        print("Ошибка: файл содержит некорректные данные.")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке: {e}")
        return []