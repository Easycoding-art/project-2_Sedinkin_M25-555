import os
import shlex

import prompt
from prettytable import PrettyTable

from src.decorators import create_cacher
from src.primitive_db.core import create_table, delete, drop_table, info, insert, list_tables, select, update
from src.primitive_db.utils import (
    load_metadata,
    load_table_data,
    save_metadata,
    save_table_data,
)


def print_help():
    """Prints the help message for the current mode."""
   
    print("\n***Процесс работы с таблицей***")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")

    print("\n***Операции с данными***")
    print("Функции:")
    print("<command> insert into <имя_таблицы> values (<значение1>, <значение2>, ...) - создать запись.")
    print("<command> select from <имя_таблицы> where <столбец> = <значение> - прочитать записи по условию.")
    print("<command> select from <имя_таблицы> - прочитать все записи.")
    print("<command> update <имя_таблицы> set <столбец1> = <новое_значение1> where <столбец_условия> = <значение_условия> - обновить запись.")
    print("<command> delete from <имя_таблицы> where <столбец> = <значение> - удалить запись.")
    print("<command> info <имя_таблицы> - вывести информацию о таблице.")
    
    print("\nОбщие команды:")
    print("<command> exit - выход из программы")
    print("<command> help - справочная информация\n")

def welcome():
    print('Добро пожаловать!')
    name = prompt.string('')
    print_help()
    return name


def run():
    db_name = welcome()
    file_path = 'db_meta.json'
    folder_path = "data"
    os.makedirs(folder_path, exist_ok=True)
    metadata = load_metadata(file_path)
    if db_name not in metadata.keys():
        metadata.update({db_name : {}})
        save_metadata(file_path, metadata)
    while True:
        db_metadata = metadata.get(db_name)
        query = prompt.string('Введите команду: ')
        args = shlex.split(query)
        match args[0]:
            case 'create_table':
                table_info = {val.split(':')[0] : val.split(':')[1] for val in args[2:]}
                db_metadata = create_table(db_metadata, args[1], table_info)
                metadata.update({db_name : db_metadata})
                save_metadata(file_path, metadata)
            case 'drop_table':
                db_metadata = drop_table(db_metadata, args[1])
                metadata.update({db_name : db_metadata})
                save_metadata(file_path, metadata)
            case 'list_tables':
                table_str = ', '.join(list_tables(db_metadata))
                print(f'Список таблиц:\n{table_str}')
            case 'info':
                print(info(db_metadata, args[1]))
            case 'select':
                table_data = load_table_data(f'data/{args[2]}')
                select_cached = create_cacher(select)
                condition  = (args[4], args[6]) if len(args) == 7 else None
                key = f'{args[2]} = {condition}'
                dct = select_cached(key, table_data, condition)
                table = PrettyTable()
                for c in dct.keys():
                    table.add_column(c, [])
                to_str = lambda arr: [str(val) for val in arr]
                table.add_row(['\n'.join(to_str(dct[c])) for c in dct.keys()])
                print(table)
            case 'update':
                table_data = load_table_data(f'data/{args[1]}')
                new_table_data = update(table_data, (args[3], args[5]), (args[7], args[9]))
                save_table_data(f'data/{args[1]}', new_table_data)
            case 'delete':
                table_data = load_table_data(f'data/{args[2]}')
                new_table_data = delete(table_data, (args[4], args[6]))
                save_table_data(f'data/{args[2]}', new_table_data)
            case 'insert':
                values = [args[4][1:-1]]
                values.extend([v[1:-1] for v in args[5:-1]])
                values.append(args[-1][:-1])
                new_table_data = insert(db_metadata, args[2], values)
                save_table_data(f'data/{args[2]}', new_table_data)
            case 'exit':
                break
            case 'help':
                print_help()
            case _:
                print(f'Функции {args[0]} нет. Попробуйте снова.')