# Написать функцию, которая принимает целочисленный 
# список, состоящий из n элементов, и возвращает True, если он 
# содержит числа 2 или 3.

def contains_two_or_three(int_list):
    for num in int_list:
        if num == 2 or num == 3:
            return True
    return False

# Список для проверки
my_list = [1, 5, 8, 9]

result = contains_two_or_three(my_list)
print(f"Список {my_list} содержит 2 или 3: {result}")
