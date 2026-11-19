import sys
from datetime import datetime
from student import Student, ExcellentStudent
from student_manager import StudentManager
from student_statistics import (
    calculate_group_average,
    count_excellent_students,
    find_best_student,
    get_group_statistics,
    sort_students_by_average
)
from file_manager import save_students, load_students

def print_menu():
    print("\n" + "=" * 50)
    print("        СИСТЕМА УПРАВЛЕНИЯ СТУДЕНТАМИ")
    print("=" * 50)
    print("1. Добавить студента")
    print("2. Показать всех студентов")
    print("3. Найти студента по ID")
    print("4. Найти студента по имени")
    print("5. Удалить студента")
    print("6. Изменить данные студента")
    print("7. Добавить оценку")
    print("8. Показать статистику")
    print("9. Показать студентов по группе")
    print("10. Случайный студент")
    print("11. Сохранить данные")
    print("12. Загрузить данные")
    print("13. Выход")
    print("=" * 50)

def main():
    manager = StudentManager()
    manager.students = load_students("data/students.json")
    last_modified = datetime.now()

    while True:
        print_menu()
        try:
            choice = input("Введите номер действия: ").strip()
        except KeyboardInterrupt:
            print("\nВыход...")
            break

        if choice == "1":
            try:
                sid = int(input("Введите ID студента: "))
                name = input("Введите ФИО: ")
                age = int(input("Введите возраст: "))
                group = input("Введите группу: ")
                email = input("Введите email (или оставьте пустым): ").strip()
                if email:
                    student = Student(sid, name, age, group, email=email)
                else:
                    student = Student(sid, name, age, group)
                manager.add_student(student)
                last_modified = datetime.now()
            except ValueError as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            try:
                sid = int(input("Введите ID студента: "))
                student = manager.find_student(sid)
                if student:
                    student.show_info()
                else:
                    print("Студент не найден.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == "4":
            name = input("Введите часть имени: ")
            found = manager.find_by_name(name)
            if found:
                for s in found:
                    s.show_info()
            else:
                print("Студенты не найдены.")

        elif choice == "5":
            try:
                sid = int(input("Введите ID студента для удаления: "))
                if manager.delete_student(sid):
                    print("Студент удалён.")
                    last_modified = datetime.now()
                else:
                    print("Студент не найден.")
            except ValueError:
                print("Ошибка: ID должен быть числом.")

        elif choice == "6":
            try:
                sid = int(input("Введите ID студента: "))
                if not manager.find_student(sid):
                    print("Студент не найден.")
                    continue
                name = input("Новое имя (Enter — пропустить): ").strip()
                age_str = input("Новый возраст (Enter — пропустить): ").strip()
                group = input("Новая группа (Enter — пропустить): ").strip()
                age = int(age_str) if age_str else None
                manager.update_student(sid, name or None, age, group or None)
                print("Данные обновлены.")
                last_modified = datetime.now()
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "7":
            try:
                sid = int(input("Введите ID студента: "))
                student = manager.find_student(sid)
                if not student:
                    print("Студент не найден.")
                    continue
                grade = int(input("Введите оценку (2-5): "))
                student.add_grade(grade)
                print("Оценка добавлена.")
                last_modified = datetime.now()
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "8":
            if not manager.students:
                print("Нет студентов для статистики.")
                continue
            print("\n--- Общая статистика ---")
            print(f"Всего студентов: {manager.count_students()}")
            print(f"Средний балл всех студентов: {calculate_group_average(manager.students):.2f}")
            print(f"Отличников: {count_excellent_students(manager.students)}")
            best = find_best_student(manager.students)
            if best:
                print(f"Лучший студент: {best.name} (средний балл: {best.get_average_grade():.2f})")
            print("\n--- Студенты с средним баллом выше 4.0 ---")
            for s in manager.get_students_above_average(4.0):
                print(f"  {s.name} — {s.get_average_grade():.2f}")
            print("\n--- Студенты старше 18 лет ---")
            for s in manager.get_students_older_than(18):
                print(f"  {s.name} — {s.age} лет")
            print("\n--- Сортировка по среднему баллу ---")
            for s in sort_students_by_average(manager.students):
                print(f"  {s.name} — {s.get_average_grade():.2f}")

        elif choice == "9":
            group = input("Введите название группы: ")
            students = manager.find_by_group(group)
            if students:
                for s in students:
                    print(s)
            else:
                print("В этой группе нет студентов.")
            stats = get_group_statistics(manager.students, group)
            print(f"\nСтатистика по группе {group}:")
            print(f"  Количество: {stats['count']}")
            print(f"  Средний балл: {stats['average']:.2f}")
            print(f"  Отличников: {stats['excellent']}")
            print(f"  Неуспевающих: {stats['failing']}")

        elif choice == "10":
            student = manager.get_random_student()
            if student:
                print(f"Случайный студент: {student.name}")
            else:
                print("Нет студентов.")

        elif choice == "11":
            save_students(manager.students, "data/students.json")
            last_modified = datetime.now()

        elif choice == "12":
            manager.students = load_students("data/students.json")
            last_modified = datetime.now()

        elif choice == "13":
            save_students(manager.students, "data/students.json")
            print("Данные сохранены. До свидания!")
            print(f"Последнее изменение: {last_modified.strftime('%Y-%m-%d %H:%M:%S')}")
            break

        else:
            print("Неверный пункт меню. Попробуйте снова.")

if __name__ == "__main__":
    main()