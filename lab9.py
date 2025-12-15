# Лабораторная работа №9. Разработка GUI приложения с помощью графических библиотек.
# Вариант 10: Приложение для проверки регулярных выражений с подсветкой совпадений.

import tkinter as tk
from tkinter import messagebox
import re


def check_regex():
    """
    Основная функция, которая вызывается при нажатии кнопки.
    Она берет регулярное выражение, компилирует его и ищет совпадения в тексте.
    """
    # 1. Получаем данные из полей ввода
    pattern = entry_regex.get()
    text_content = text_field.get("1.0", tk.END)  # Читаем весь текст с 1-й строки до конца

    # 2. Очищаем предыдущую подсветку (удаляем тег 'highlight' со всего текста)
    text_field.tag_remove('highlight', '1.0', tk.END)

    # Если паттерн пустой, ничего не делаем
    if not pattern:
        return

    try:
        # 3. Пытаемся скомпилировать регулярное выражение
        # Если выражение некорректно (например, незакрытая скобка), re вызовет ошибку
        regex = re.compile(pattern)

        # 4. Ищем все совпадения в тексте
        # finditer возвращает итератор с объектами match, содержащими позиции (start, end)
        matches = regex.finditer(text_content)

        count = 0
        for match in matches:
            count += 1
            # Получаем индексы начала и конца совпадения
            start_idx = match.start()
            end_idx = match.end()

            # Tkinter требует индексы в формате "строка.символ".
            # Так как мы получили просто числовую позицию в строке, нужно конвертировать.
            # Но проще воспользоваться встроенным поиском Tkinter или конвертировать индексы.
            # В данном случае, так как get("1.0", END) возвращает всё одной строкой с \n,
            # позиции от re совпадают с позициями в Tkinter, если использовать "1.0 + N chars"

            # Формируем индексы для Tkinter
            tk_start = f"1.0 + {start_idx} chars"
            tk_end = f"1.0 + {end_idx} chars"

            # Применяем тег подсветки к найденному диапазону
            text_field.tag_add('highlight', tk_start, tk_end)

        # Обновляем статусную строку
        lbl_status.config(text=f"Найдено совпадений: {count}", fg="green")

    except re.error as e:
        # 5. Обработка ошибки в регулярном выражении
        error_message = f"Ошибка в регулярном выражении:\n{e}"
        messagebox.showerror("Ошибка Regex", error_message)
        lbl_status.config(text="Ошибка в выражении", fg="red")


# --- Настройка графического интерфейса (GUI) ---

root = tk.Tk()
root.title("Regex Checker (Лабораторная №9)")
root.geometry("500x450")

# Блок ввода регулярного выражения
frame_top = tk.Frame(root, pady=10)
frame_top.pack(fill=tk.X, padx=10)

lbl_regex = tk.Label(frame_top, text="Регулярное выражение:", font=("Arial", 10, "bold"))
lbl_regex.pack(anchor=tk.W)

entry_regex = tk.Entry(frame_top, font=("Consolas", 12))
entry_regex.pack(fill=tk.X, pady=5)
# Привязываем нажатие Enter в поле regex к запуску поиска
entry_regex.bind('<Return>', lambda event: check_regex())

# Блок ввода текста для поиска
frame_mid = tk.Frame(root)
frame_mid.pack(fill=tk.BOTH, expand=True, padx=10)

lbl_text = tk.Label(frame_mid, text="Текст для проверки:", font=("Arial", 10, "bold"))
lbl_text.pack(anchor=tk.W)

text_field = tk.Text(frame_mid, font=("Arial", 11), height=10)
text_field.pack(fill=tk.BOTH, expand=True, pady=5)

# Настройка стиля подсветки (тег 'highlight')
# background - цвет фона, foreground - цвет текста
text_field.tag_config('highlight', background="yellow", foreground="black")

# Блок с кнопкой и статусом
frame_bot = tk.Frame(root, pady=10)
frame_bot.pack(fill=tk.X, padx=10)

btn_check = tk.Button(frame_bot, text="Проверить / Найти", command=check_regex, bg="#dddddd", font=("Arial", 10))
btn_check.pack(side=tk.LEFT)

lbl_status = tk.Label(frame_bot, text="", font=("Arial", 9))
lbl_status.pack(side=tk.RIGHT)

# Заполним тестовыми данными для удобства
entry_regex.insert(0, r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")  # Regex для Email
text_field.insert("1.0", "Здесь есть текст и email: test@example.com.\nА также invalid-email@com и admin@site.org")

# Запуск основного цикла приложения
root.mainloop()