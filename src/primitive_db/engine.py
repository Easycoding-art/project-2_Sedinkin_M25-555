import prompt
from src.primitive_db.core import DBConnector

def print_help():
    """Prints the help message for the current mode."""
   
    print("\n***Процесс работы с таблицей***")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")
    
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
    db = DBConnector(db_name)
    while True:
        query = prompt.string('Введите команду: ')
        #args = shlex.split(query)
        args = query.split()
        match args[0]:
            case 'create':
                db.create_table()
            case 'drop':
                db.drop_table()
            case 'list_tables':
                table_str = ', '.join(db.list_tables())
                print(f'Список таблиц:\n{table_str}')
            case 'exit':
                break
            case 'help':
                print_help()
            case _:
                print_help()