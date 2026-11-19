import re
import random
import string

def check_login(login):
    """
    Проверяет логин.
    Логин должен быть от 4 до 16 символов, состоять только из букв, цифр и _.
    """
    # Проверка на некорректные данные (если передали не строку)
    if not isinstance(login, str):
        return False, "Ошибка: логин должен быть строкой"
    
    # Если длина не подходит
    if len(login) < 4 or len(login) > 16:
        return False, "Ошибка: длина логина должна быть от 4 до 16 символов"
    
    # Проверяем через регулярные выражения (буквы, цифры и нижнее подчеркивание)
    if not re.match(r'^[a-zA-Z0-9_]+$', login):
        return False, "Ошибка: логин может содержать только буквы, цифры и _"
    
    return True, "Логин корректный"

def check_password_strength(password):
    """
    Проверяет надежность пароля.
    Пароль должен быть минимум 8 символов, содержать цифру и заглавную букву.
    """
    if not isinstance(password, str):
        return False, "Ошибка: пароль должен быть строкой"
        
    if len(password) < 8:
        return False, "Слабый пароль: нужно минимум 8 символов"
        
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    
    if not has_digit:
        return False, "Слабый пароль: добавьте хотя бы одну цифру"
    if not has_upper:
        return False, "Слабый пароль: добавьте хотя бы одну заглавную букву"
        
    return True, "Пароль надежный"

def generate_random_password(length=12):
    """
    Генерирует случайный пароль заданной длины.
    Использует модули random и string.
    """
    if length < 8:
        length = 8 # Минимальная длина для безопасности
        
    # Берем буквы (верхний и нижний регистр) + цифры + спецсимволы
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(chars) for _ in range(length))
    return password