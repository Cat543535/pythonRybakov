# Написать функцию, которая принимает объект datetime 
# и возвращает третью среду месяца.

import datetime

def get_third_wednesday(date_obj):
    """Принимает объект datetime и возвращает третью среду месяца."""
    first_day_of_month = date_obj.replace(day=1)
    weekday = first_day_of_month.weekday()
    # 2 - индекс среды
    days_to_add = (2 - weekday + 7) % 7
    first_wednesday = first_day_of_month + datetime.timedelta(days=days_to_add)
    third_wednesday = first_wednesday + datetime.timedelta(weeks=2)
    return third_wednesday

# Пример
today = datetime.date.today()
third_wednesday_of_month = get_third_wednesday(today)

print(f"Для даты {today} третья среда месяца: {third_wednesday_of_month}")

# Пример для другого месяца
some_date = datetime.date(2025, 5, 5)
third_wednesday_of_may = get_third_wednesday(some_date)
print(f"Для даты {some_date} третья среда месяца: {third_wednesday_of_may}")
