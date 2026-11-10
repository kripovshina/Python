# Список словарей с товарами
products = [
       {"id": 0, 
    "name": "мышь", 
    "category": "управления", 
    "price": 1500, 
    "quantity": 40},
    {"id": 1, 
    "name": "клавиатура", 
    "category": "управления", 
    "price": 2000, 
    "quantity": 10},
    {"id": 2, 
    "name": "монитор", 
    "category": "не управления", 
    "price": 20000, 
    "quantity": 4},
    {"id": 3, 
    "name": "наушники", 
    "category": "не управления", 
    "price": 1500, 
    "quantity": 30},
    {"id": 4, 
    "name": "веб-камера", 
    "category": "не управления", 
    "price": 4000, 
    "quantity": 35},
    {"id": 5, 
    "name": "микрофон", 
    "category": "не управления", 
    "price": 5000, 
    "quantity": 20},
    {"id": 6, 
    "name": "usb-флешка", 
    "category": "управления", 
    "price": 300, 
    "quantity": 100},
    {"id": 7, 
    "name": "колонки", 
    "category": "не управления", 
    "price": 3500, 
    "quantity": 15}
]


def display_assortment(product_list):
    """Задание 1. Вывод полного списка товаров и общей стоимости склада."""
    print("\n Ассортимент магазина" )
    total_inventory_value = 0.0
    
    for product in product_list:
        # Вывод информации о каждом товаре
        print(f"ID: {product['id']} | Название: {product['name']} | "
              f"Категория: {product['category']} | "
              f"Цена: {product['price']} руб. | Количество: {product['quantity']} шт.")
        
        # Подсчет общей стоимости
        total_inventory_value += product['price'] * product['quantity']
        
    print("-" * 30)
    print(f"Общая стоимость всех товаров на складе: {total_inventory_value} руб.")


def search_by_name(product_list, query):
    """Задание 2. Поиск товаров по названию (без учета регистра)."""
    print(f"\n Результаты поиска по запросу: '{query}' ")
    found_products = []
    
    # Переводим запрос в нижний регистр для поиска без учета регистра
    query_lower = query.lower()
    
    for product in product_list:
        if query_lower in product['name'].lower():
            found_products.append(product)
            
    if found_products:
        for product in found_products:
            print(f"Найдено: {product['name']} (Цена: {product['price']} руб., В наличии: {product['quantity']} шт.)")
    else:
        print("Товары с таким названием не найдены.")


def filter_by_category(product_list, category):
    """Задание 3. Фильтрация товаров по категории."""
    print(f"\n Товары в категории: '{category}' ")
    found_products = False
    
    for product in product_list:
        # Ищем точное совпадение категории (тоже без учета регистра для удобства)
        if product['category'].lower() == category.lower():
            print(f"{product['name']} — {product['price']} руб. (Остаток: {product['quantity']} шт.)")
            found_products = True
            
    if not found_products:
        print("В этой категории пока нет товаров.")


# === Тестирование программы (Вызовы функций) ===

# 1. Вывод всего ассортимента и расчет стоимости
display_assortment(products)

# 2. Поиск по названию (проверяем работу с регистром)
search_by_name(products, "мышь")     # Найдет "Игровая мышь" и "Беспроводная мышь"
search_by_name(products, "МЫШЬ")     # Сработает так же
search_by_name(products, "телефон")  # Выдаст сообщение, что не найдено

# 3. Фильтрация по категории
filter_by_category(products, "Аудио")
filter_by_category(products, "Мониторы")