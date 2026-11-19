import user_tools
import math_tools

def main():
    print("=== Демонстрация работы библиотеки ===\n")

    # --- 1. Проверка логина ---
    print("1. Проверка логина:")
    test_login = "student_123"
    is_valid, message = user_tools.check_login(test_login)
    print(f"Логин: {test_login} -> {message}")
    
    bad_login = "ab"
    is_valid, message = user_tools.check_login(bad_login)
    print(f"Логин: {bad_login} -> {message}\n")

    # --- 2. Проверка пароля ---
    print("2. Проверка пароля:")
    test_pass = "MySuperPass123"
    is_valid, message = user_tools.check_password_strength(test_pass)
    print(f"Пароль: {test_pass} -> {message}")
    
    weak_pass = "12345"
    is_valid, message = user_tools.check_password_strength(weak_pass)
    print(f"Пароль: {weak_pass} -> {message}\n")

    # --- 3. Генерация пароля ---
    print("3. Генерация случайного пароля:")
    new_pass = user_tools.generate_random_password(10)
    print(f"Сгенерированный пароль: {new_pass}\n")

    # --- 4. Генерация ID пользователя ---
    print("4. Генерация ID пользователя:")
    user_id = math_tools.generate_user_id()
    print(f"Новый ID: {user_id}\n")

    # --- 5. Вычисление возраста ---
    print("5. Вычисление возраста:")
    age = math_tools.calculate_age(2005)
    print(f"Если год рождения 2005, то возраст: {age}")

if __name__ == "__main__":
    main()