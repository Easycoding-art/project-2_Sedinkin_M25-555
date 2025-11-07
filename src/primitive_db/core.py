from src.decorators import confirm_action, log_time
from src.primitive_db.utils import load_table_data


def create_table(metadata, table_name, columns):
    '''
    Автоматически добавлять столбец ID:int в начало списка столбцов.
    В случае успеха, обновлять словарь metadata и возвращать его.
    '''
    if table_name in metadata.keys():
        print(f'Таблица {table_name} уже существует!')
    else:
        if 'ID' not in columns.keys():
            columns.update({'ID' : "int"})
        metadata.update({table_name : columns})
        print(f'Таблица {table_name} успешно создана!')
    return metadata

@confirm_action("удаление таблицы")
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

@log_time
def insert(metadata, table_name, values):
    '''
    Добавляет новую запись (в виде словаря) в данные таблицы и возвращает их.
    '''
    if table_name not in metadata.keys():
        print(f'Таблица {table_name} не существует!')
        return {}
    current_table = metadata.get(table_name)
    real_table = load_table_data(f'data/{table_name}')
    if len(values) != len(current_table.keys()) - 1:
        print('Не соответствует числу столбцов!')
        return real_table
    if real_table == {}:
        data = {key : [] for key in current_table.keys()}
        real_table.update(data)
    for i, key in enumerate(real_table.keys()):
        if key != 'ID':
            current_type = eval(current_table.get(key))
            transformed_value = current_type(values[i])
            real_table[key].append(transformed_value)
        else:
            real_table['ID'].append(len(real_table.get('ID')))
    return real_table
    
@log_time
def select(table_data, where_clause=None):
    '''
    Если where_clause не задан, возвращает все данные.
    Фильтрует и возвращает только подходящие записи.
    '''
    if where_clause is not None:
        result = {}
        filter_arr = table_data.get(where_clause[0])
        this_type = type(filter_arr[0])
        x = this_type(where_clause[1])
        mask = [val == x for val in filter_arr]
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
    filter_arr = table_data.get(where_clause[0])
    this_type = type(filter_arr[0])
    x = this_type(where_clause[1])
    mask = [val == x for val in filter_arr]
    key, str_value = set_clause
    arr = table_data.get(key)
    value_type = type(arr[0])
    value = value_type(str_value)
    result_arr = [value if mask[i] else arr[i] for i in range(len(arr))]
    table_data.update({key : result_arr})
    return table_data

@confirm_action("удаление данных")
def delete(table_data, where_clause):
    '''
    Находит записи по where_clause и удаляет их.
    Возвращает измененные данные.
    '''
    result = {}
    filter_arr = table_data.get(where_clause[0])
    this_type = type(filter_arr[0])
    x = this_type(where_clause[1])
    mask = [val != x for val in filter_arr]
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
        arr.append(f'{key}: {current_table.get(key)}')
    return ', '.join(arr)