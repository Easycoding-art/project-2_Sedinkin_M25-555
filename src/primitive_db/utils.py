import json
 
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

def save_table_data(table_name, data):
    '''
    Сохраняет таблицу в JSON-файл.
    '''
    with open(f'{table_name}.json', 'w') as file:
        json.dump(data, file)

def load_table_data(table_name):
    '''
    Загружает таблицу из JSON-файла.
    Если файл не найден, возвращает пустой словарь {}.
    Используйте try...except FileNotFoundError.
    '''
    try:
        with open(f'{table_name}.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}