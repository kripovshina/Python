import uuid

def generate_user_id():
    """
    Генерирует уникальный идентификатор пользователя (UUID).
    Возвращает строку.
    """
    # uuid4 создает случайный уникальный ID
    return str(uuid.uuid4())

def calculate_age(birth_year):
    """
    Простая функция для вычисления возраста (для примера).
    """
    from datetime import datetime
    current_year = datetime.now().year
    
    if birth_year > current_year:
        return "Ошибка: год рождения не может быть в будущем"
        
    return current_year - birth_year