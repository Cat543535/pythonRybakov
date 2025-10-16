# Написать функцию, которая принимает список и выводит в консоль значения списка через точку с запятой. 
# Требуется решить задачу одной строкой с использованием списка с оператором «*».

def print_list_with_semicolon(items):
    print(*items, sep=';')

# Пример
my_items = [1, 'test', 3.14, 'hello']
print_list_with_semicolon(my_items)
