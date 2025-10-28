import json
'''
Вся информация о таблицах (их имена и структура столбцов) будет храниться в одном файле, например, db_meta.json.
'''
 
def load_metadata(filepath):
    '''
    Загружает данные из JSON-файла.
    Если файл не найден, возвращает пустой словарь {}.
    Используйте try...except FileNotFoundError.
    '''
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def save_metadata(filepath, data):
    '''
    Сохраняет переданные данные в JSON-файл.
    '''
    with open(filepath, 'w') as file:
        json.dump(data, file)