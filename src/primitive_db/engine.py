import prompt
import shlex
from src.primitive_db.utils import load_metadata, save_metadata, load_table_data, save_table_data
from src.primitive_db.core import *
from prettytable import PrettyTable

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
    metadata = load_metadata(file_path)
    if db_name not in metadata.keys():
        metadata.update({db_name : {}})
        save_metadata(file_path, metadata)
    db_metadata = metadata.get(db_name)
    while True:
        query = prompt.string('Введите команду: ')
        args = shlex.split(query)
        print(args)
        #args = query.split()
        match args[0]:
            case 'create':
                create_table()
            case 'drop':
                drop_table()
            case 'list_tables':
                table_str = ', '.join(list_tables())
                print(f'Список таблиц:\n{table_str}')
            case 'info':
                info()
            case 'select':
                dct = select()#add
                table = PrettyTable()
                for c in dct.keys():
                    table.add_column(c, [])
                to_str = lambda arr: [str(val) for val in arr]
                table.add_row(['\n'.join(to_str(dct[c])) for c in dct.keys()])
                print(table)
            case 'update':
                update()#add
            case 'delete':
                delete()#add
            case 'insert':
                insert()#add
            case 'exit':
                break
            case 'help':
                print_help()
            case _:
                print(f'Функции {args[0]} нет. Попробуйте снова.')