from src.primitive_db.utils import load_metadata, save_metadata, load_table_data, save_table_data
    
def create_table(metadata, table_name, columns):
    '''
    Она должна принимать текущие метаданные, имя таблицы и список столбцов.
    Автоматически добавлять столбец ID:int в начало списка столбцов.
    Проверять, не существует ли уже таблица с таким именем. Если да, выводить ошибку.
    Проверять корректность типов данных (только int, str, bool).
    В случае успеха, обновлять словарь metadata и возвращать его.
    '''
    if table_name in metadata.keys():
        print(f'Таблица {table_name} уже существует!')
    else:
        if 'ID' not in columns.keys():
            columns.update({'ID' : int})
        metadata.update({table_name : columns})
        print(f'Таблица {table_name} успешно создана!')
    return metadata


def drop_table(metadata, table_name):
    '''
    Проверяет существование таблицы. Если таблицы нет, выводит ошибку.
    Удаляет информацию о таблице из metadata и возвращает обновленный словарь.
    '''
    if table_name not in metadata.keys():
        print(f'Таблица {table_name} не существует!')
    else:
        metadata.pop(table_name)
        print(f'Таблица {table_name} успешно удалена!')
    return metadata

def list_tables(metadata):
    return metadata.keys()

def insert(metadata, table_name, values):
    '''
    Проверяет, существует ли таблица.
    Проверяет, что количество переданных значений соответствует количеству столбцов (минус ID).
    Валидирует типы данных для каждого значения в соответствии со схемой в metadata.
    Генерирует новый ID (например, max(IDs) + 1 или len(data) + 1).
    Добавляет новую запись (в виде словаря) в данные таблицы и возвращает их.
    '''
    if table_name not in metadata.keys():
        print(f'Таблица {table_name} не существует!')
    current_table = metadata.get(table_name)
    if len(values) != len(current_table.keys()) - 1:
        print('Не соответствует числу столбцов!')
    real_table = load_table_data(f'data/{table_name}')
    real_table['ID'].append(len(real_table.get('ID')))
    for i, key in enumerate(real_table.keys()):
        if not isinstance(values[i], current_table.get(key)):
            print(f'Не соответствует тип {key}!')
            break
        real_table[key].append(values[i])
    else:
        return real_table
    return load_table_data(f'data/{table_name}')
    

def select(table_data, where_clause=None):
    '''
    Если where_clause не задан, возвращает все данные.
    Если задан (например, {'age': 28}), фильтрует и возвращает только подходящие записи.
    '''
    if where_clause != None:
        result = {}
        mask = [val == where_clause[1] for val in table_data.get(where_clause[0])]
        for key in table_data.keys():
            arr = table_data.get(key)
            result_arr = [arr[i] for i in range(len(arr)) if mask[i]]
            result.update({key : result_arr})
        table_data = result
    return table_data

def update(table_data, set_clause, where_clause):
    '''
    Находит записи по where_clause.
    Обновляет в найденных записях поля согласно set_clause.
    Возвращает измененные данные.
    '''
    mask = [val == where_clause[1] for val in table_data.get(where_clause[0])]
    key, value = set_clause
    arr = table_data.get(key)
    result_arr = [value if mask[i] else arr[i] for i in range(len(arr))]
    table_data.update({key : result_arr})
    return table_data

def delete(table_data, where_clause):
    '''
    Находит записи по where_clause и удаляет их.
    Возвращает измененные данные.
    '''
    result = {}
    mask = [val != where_clause[1] for val in table_data.get(where_clause[0])]
    for key in table_data.keys():
        arr = table_data.get(key)
        result_arr = [arr[i] for i in range(len(arr)) if mask[i]]
        result.update({key : result_arr})
    table_data = result
    return table_data
    

def info(metadata, table_name):
    current_table = metadata.get(table_name)
    arr = []
    for key in current_table.keys():
        arr.append(f'{key}: {current_table.get(key).__name__}')
    return ', '.join(arr)