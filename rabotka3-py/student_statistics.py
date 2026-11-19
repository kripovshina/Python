def calculate_group_average(students):
    if not students:
        return 0
    return sum(s.get_average_grade() for s in students) / len(students)

def count_excellent_students(students):
    return sum(1 for s in students if s.get_average_grade() >= 4.5)

def find_best_student(students):
    if not students:
        return None
    return max(students, key=lambda s: s.get_average_grade())

def get_group_statistics(students, group):
    group_students = [s for s in students if s.group == group]
    if not group_students:
        return {
            "count": 0,
            "average": 0,
            "excellent": 0,
            "failing": 0
        }
    return {
        "count": len(group_students),
        "average": calculate_group_average(group_students),
        "excellent": count_excellent_students(group_students),
        "failing": sum(1 for s in group_students if s.get_average_grade() < 3)
    }

def sort_students_by_average(students):
    return sorted(students, key=lambda s: s.get_average_grade(), reverse=True)