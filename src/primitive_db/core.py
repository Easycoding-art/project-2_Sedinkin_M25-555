from src.primitive_db.utils import load_metadata, save_metadata

class DBConnector():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, name):
        self.__file_path = 'db_meta.json'
        self.__name = name
        metadata = load_metadata(self.__file_path)
        if self.__name not in metadata.keys():
            metadata.update({self.__name : {}})
            save_metadata(self.__file_path, metadata)
        self.__tables = metadata.get(self.__name)
    
    @property
    def name(self):
        return self.__name
    
    def create_table(self, table_name, columns):
        '''
        Она должна принимать текущие метаданные, имя таблицы и список столбцов.
        Автоматически добавлять столбец ID:int в начало списка столбцов.
        Проверять, не существует ли уже таблица с таким именем. Если да, выводить ошибку.
        Проверять корректность типов данных (только int, str, bool).
        В случае успеха, обновлять словарь metadata и возвращать его.
        '''
        if table_name in self.__tables.keys():
            print(f'Таблица {table_name} уже существует!')
        else:
            if 'ID' not in columns:
                columns.insert(0, 'ID : int')
            self.__tables.upadate({table_name : columns})
            metadata = load_metadata(self.__file_path)
            metadata[self.__name].update(self.__tables)
            save_metadata(self.__file_path, metadata)
            print(f'Таблица {table_name} успешно создана!')

    
    def drop_table(self, metadata, table_name):
        '''
        Проверяет существование таблицы. Если таблицы нет, выводит ошибку.
        Удаляет информацию о таблице из metadata и возвращает обновленный словарь.
        '''
        if table_name not in self.__tables.keys():
            print(f'Таблица {table_name} не существует!')
        else:
            self.__tables.pop(table_name)
            metadata = load_metadata(self.__file_path)
            metadata[self.__name].update(self.__tables)
            save_metadata(self.__file_path, metadata)
            print(f'Таблица {table_name} успешно удалена!')
    
    def list_tables(self):
        return self.__tables.keys()