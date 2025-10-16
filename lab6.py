# Написать функцию, которая возвращает наименование 
# всех таблиц связки, которые находятся в базе данных, если они 
# существуют. Стоит отметить, что в данном задании предпола
# гается, что таблицы связки именуются склеиванием имени двух 
# таблиц через знак нижнего подчеркивания «_». 

import sqlite3
import os

def find_junction_tables_from_db(db_path):
    """
    Подключается к базе данных SQLite, находит и возвращает таблицы-связки.
    """
    if not os.path.exists(db_path):
        return f"Ошибка: Файл базы данных не найден по пути {db_path}"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Получаем список всех таблиц в базе данных
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # fetchall() возвращает список кортежей, извлекаем из них имена
    all_tables = [item[0] for item in cursor.fetchall()]
    
    conn.close()

    # Логика поиска таблиц-связок
    junction_tables = []
    table_set = set(all_tables)

    for name in all_tables:
        if '_' in name:
            parts = name.split('_')
            if len(parts) == 2:
                table1, table2 = parts
                # Проверяем, что обе части имени существуют как отдельные таблицы
                if table1 in table_set and table2 in table_set:
                    junction_tables.append(name)
    
    return junction_tables

# Пример
if __name__ == '__main__':
    db_file = 'test_db.sqlite'

    # 1. Создаем временную базу данных и таблицы
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Основные таблицы
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY)")
    cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY)")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY)")
    cursor.execute("CREATE TABLE IF NOT EXISTS roles (id INTEGER PRIMARY KEY)")

    # Таблицы-связки
    cursor.execute("CREATE TABLE IF NOT EXISTS users_products (user_id INT, product_id INT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders_products (order_id INT, product_id INT)")

    cursor.execute("CREATE TABLE IF NOT EXISTS user_permissions (user_id INT, permission_id INT)")

    conn.commit()
    conn.close()

    # 2. Вызываем нашу функцию для поиска таблиц-связок
    print(f"Поиск таблиц-связок в файле '{db_file}'...")
    found_junction_tables = find_junction_tables_from_db(db_file)

    print("\nРезультат:")
    if isinstance(found_junction_tables, list):
        print(f"Найденные таблицы-связки: {found_junction_tables}")
    else:
        print(found_junction_tables) # Вывод ошибки, если файл не найден

    # 3. Удаляем временную базу данных
    try:
        os.remove(db_file)
        print(f"\nВременная база данных '{db_file}' удалена.")
    except OSError as e:
        print(f"Ошибка при удалении файла {db_file}: {e}")
