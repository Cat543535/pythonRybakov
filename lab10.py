# Лабораторная работа №10. Визуализация результатов работы математических алгоритмов.
# Вариант 9: Генерация матрицы 5x5, поиск min/max и визуализация.

import numpy as np
import matplotlib.pyplot as plt


def generate_and_analyze_matrix():
    """
    Генерирует матрицу 5x5 случайных целых чисел,
    находит минимальное и максимальное значения.
    """
    # 1. Генерируем матрицу 5x5 случайными числами от 0 до 99
    # np.random.randint(low, high, size)
    matrix = np.random.randint(0, 100, size=(5, 5))

    # 2. Находим минимум и максимум с помощью методов NumPy
    min_val = matrix.min()
    max_val = matrix.max()

    return matrix, min_val, max_val


if __name__ == '__main__':
    # Получаем данные
    mat, minimum, maximum = generate_and_analyze_matrix()

    # Вывод в консоль (текстовый вид)
    print("Сгенерированная матрица 5x5:")
    print(mat)
    print("-" * 20)
    print(f"Минимальное значение: {minimum}")
    print(f"Максимальное значение: {maximum}")

    # --- Визуализация (Matplotlib) ---

    # Создаем фигуру
    plt.figure(figsize=(6, 6))

    # Отображаем матрицу как картинку (тепловая карта)
    # cmap='viridis' - цветовая схема, interpolation='nearest' - четкие квадраты без размытия
    plt.imshow(mat, cmap='viridis', interpolation='nearest')

    # Добавляем шкалу цвета справа
    plt.colorbar(label='Значение элемента')

    # Добавляем заголовок
    plt.title(f"Матрица 5x5\nMin: {minimum}, Max: {maximum}")

    # Добавляем текстовые подписи значений внутрь квадратов
    for i in range(5):
        for j in range(5):
            # i - строка (y), j - столбец (x)
            val = mat[i, j]
            # Если цвет слишком темный или светлый, можно менять цвет текста,
            # но для простоты оставим белый или красный.
            plt.text(j, i, str(val), ha='center', va='center', color='white', fontweight='bold')

    # Скрываем оси координат (галочки 0, 1, 2...), если они не нужны,
    # или оставляем для наглядности индексов.
    # plt.axis('off')

    # Показываем график
    plt.show()