# Написать функцию, которая принимает путь к HTML и 
# путь к CSS файлам и возвращает словарь, в котором ключами 
# выступают теги, идентификаторы или классы в файле CSS, а 
# значениями список списков, где первым элементом внутренне
# го списка будет наименование тега, которые попадают под сти
# ли, указанные в файле CSS, а вторым – номер строк, в которых 
# они находятся. Например, {'#inline-text': [[‘h1’, 29], [‘p’, 50]]}.

import re
from collections import defaultdict

def parse_html_css(html_path, css_path):
    """
    Анализирует файлы HTML и CSS и находит, какие теги HTML подпадают под CSS-селекторы.
    """
    try:
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
    except FileNotFoundError:
        return f"Ошибка: CSS файл не найден по пути {css_path}"

    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_lines = f.readlines()
    except FileNotFoundError:
        return f"Ошибка: HTML файл не найден по пути {html_path}"

    # Извлечение селекторов из CSS
    css_content = re.sub(r'/\*.*?\*/', '', css_content, flags=re.DOTALL)
    raw_selectors = re.findall(r'([^{}]+?)\s*{', css_content)
    
    # Поиск тегов в HTML
    tags_by_line = {}
    for i, line in enumerate(html_lines):
        found_tags = re.findall(r'<([a-zA-Z0-9]+)', line)
        if found_tags:
            tags_by_line[i + 1] = {'tags': found_tags, 'line_content': line}

    # Сопоставление селекторов и тегов
    result = defaultdict(list)
    for raw_selector in raw_selectors:
        selectors = [s.strip() for s in raw_selector.strip().split(',')]
        
        for selector in selectors:
            if not selector:
                continue
            
            for line_num, line_data in tags_by_line.items():
                line_content = line_data['line_content']
                
                for tag_name in line_data['tags']:
                    match = False
                    if selector.startswith('.'):
                        class_name = selector[1:]
                        if re.search(f'class=[\'"].*\\b{class_name}\\b.*[\'"]', line_content):
                            match = True
                    elif selector.startswith('#'):
                        id_name = selector[1:]
                        if f'id="{id_name}"' in line_content or f"id='{id_name}'" in line_content:
                            match = True
                    elif selector.lower() == tag_name.lower():
                        match = True
                    
                    if match:
                        entry = [tag_name, line_num]
                        if entry not in result[raw_selector.strip()]:
                            result[raw_selector.strip()].append(entry)

    for key in result:
        result[key].sort(key=lambda x: x[1])

    return dict(result)

# Пример
if __name__ == '__main__':
    html_file_path = 'index1.html'
    css_file_path = 'style1.css'
    
    analysis_result = parse_html_css(html_file_path, css_file_path)
    
    import json
    print("Результат анализа:")
    print(json.dumps(analysis_result, indent=4, ensure_ascii=False))
