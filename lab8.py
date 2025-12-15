# Лабораторная работа №8. Обработка изображений с применением библиотеки PIL.
# Вариант 9: Написать функцию, которая принимает путь к изображению и список пикселей
# и заменяет полученные пиксели прозрачным цветом, сохраняя изображение в той же директории.

from PIL import Image
import os


def make_pixels_transparent(image_path, pixel_coordinates):
    """
    Открывает изображение, делает указанные пиксели прозрачными
    и сохраняет результат в той же папке в формате PNG.

    :param image_path: Путь к исходному изображению.
    :param pixel_coordinates: Список кортежей с координатами (x, y).
    """
    if not os.path.exists(image_path):
        print(f"Ошибка: Файл {image_path} не найден.")
        return

    try:
        # Открываем изображение
        with Image.open(image_path) as img:
            # Конвертируем в RGBA, чтобы появился альфа-канал (прозрачность)
            img = img.convert("RGBA")

            # Получаем доступ к пиксельным данным для чтения и записи
            # Это быстрее, чем использовать putpixel в цикле
            pixels = img.load()

            width, height = img.size

            # Проходим по переданному списку координат
            count = 0
            for x, y in pixel_coordinates:
                # Проверяем, что координаты находятся в пределах изображения
                if 0 <= x < width and 0 <= y < height:
                    # Устанавливаем цвет пикселя в (0, 0, 0, 0) - полностью прозрачный
                    # Формат кортежа: (Red, Green, Blue, Alpha)
                    pixels[x, y] = (0, 0, 0, 0)
                    count += 1

            print(f"Обработано пикселей: {count}")

            # Формируем имя нового файла в той же директории
            # Обязательно сохраняем как PNG, так как JPG не поддерживает прозрачность
            file_dir, file_name = os.path.split(image_path)
            name_without_ext = os.path.splitext(file_name)[0]
            new_file_name = f"{name_without_ext}_transparent.png"
            new_file_path = os.path.join(file_dir, new_file_name)

            img.save(new_file_path, "PNG")
            print(f"Изображение сохранено: {new_file_path}")

    except Exception as e:
        print(f"Произошла ошибка при обработке: {e}")


if __name__ == '__main__':
    # --- Блок тестирования ---

    # 1. Создадим тестовое изображение (красный квадрат), чтобы было с чем работать
    test_image_name = "test_image_lab8.jpg"

    # Создаем RGB изображение 100x100 красного цвета
    img = Image.new('RGB', (100, 100), color='red')
    img.save(test_image_name)
    print(f"Создано тестовое изображение: {test_image_name}")

    # 2. Подготовим список пикселей, которые хотим стереть
    # Например, сделаем "дырку" посередине квадрата (от 40 до 60 пикселя по x и y)
    pixels_to_remove = []
    for x in range(40, 60):
        for y in range(40, 60):
            pixels_to_remove.append((x, y))

    # Добавим еще диагональную линию для наглядности
    for i in range(100):
        pixels_to_remove.append((i, i))

    # 3. Вызываем функцию
    make_pixels_transparent(test_image_name, pixels_to_remove)

    # 4. (Опционально) Удаляем исходный тестовый файл
    # os.remove(test_image_name)
    # Результат (test_image_lab8_transparent.png) останется в папке проекта.