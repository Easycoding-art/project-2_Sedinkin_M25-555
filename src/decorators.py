import time
import prompt

def handle_db_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print("Ошибка: Файл данных не найден. Возможно, база данных не инициализирована.")
        except KeyError as e:
            print(f"Ошибка: Таблица или столбец {e} не найден.")
        except ValueError as e:
            print(f"Ошибка валидации: {e}")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")
    return wrapper

def confirm_action(action_name):
    '''
        Это должен быть декоратор с аргументом (фабрика декораторов). Он будет запрашивать у пользователя подтверждение для опасных операций.
    Пример использования:

    @confirm_action("удаление таблицы")
    def drop_table(metadata, table_name):
        # ... логика удаления
        pass
    
    Перед выполнением drop_table в консоли должно появиться: . Если пользователь вводит не "y", операция отменяется.
    Примените этот декоратор к функциям drop_table и delete в core.
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            match func.__name__:
                case 'drop':
                    print('Вы уверены, что хотите выполнить удаление таблицы?')
                case 'delete':
                    print('Вы уверены, что хотите выполнить удаление записей таблицы?')
                case _:
                    print('Вы уверены, что хотите выполнить это действие?')
            result = prompt.string('[y/n]: ')
            if result == 'y':
                return func(*args, **kwargs)
            else:
                print('Операция отменена!')
        return wrapper
    return decorator

def log_time(func):
    '''
    Этот декоратор должен замерять время выполнения функции и выводить его в консоль.
    Используйте модуль time (time.monotonic()).
    Вывод должен быть в формате: Функция <имя_функции> выполнилась за X.XXX секунд.
    Примените этот декоратор к "медленным" операциям, которые работают с файлами, например, select и insert.
    '''
    def wrapper(*args, **kwargs):
        start_time = time.monotonic()
        func(*args, **kwargs)
        end_time = time.monotonic()
        elapsed_time = end_time - start_time
        print(f'Функция {func.__name__} выполнилась за {elapsed_time} секунд.')
    return wrapper

def create_cacher():
    cache = {}
    def cache_result(key, value_func):
        if key in cache:
            return cache[key]
        else:
            result = value_func()
            cache[key] = result
            return result
    return cache_result