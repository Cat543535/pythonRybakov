# Написать функцию, которая принимает список и с по
# мощью генераторного выражения создает и возвращает сло
# варь, где в качестве ключей будут номера позиций элементов 
# входящего словаря, а значениями – сами элементы.

def list_to_dict_generator(input_list):
    return {i: input_list[i] for i in range(len(input_list))}

# Пример
my_list = ['apple', 'banana', 'cherry']
result_dict = list_to_dict_generator(my_list)
print(f"Исходный список: {my_list}")
print(f"Созданный словарь: {result_dict}")
