# My database

Консольная СУБД, осень 2025 года

---

## Содержание

- [Описание](#-описание)
- [Установка и запуск](#-установка-и-запуск)
- [Управление таблицами](#-управление-таблицами)

---

## Описание

Этот проект демонстрирует владение ООП в Python.

---

## Установка и запуск

Проект использует [Poetry](https://python-poetry.org/) для управления зависимостями и виртуальным окружением.

### Требования
- Python ≥ 3.12
- Poetry ≥ 2.2

### Шаги

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/Easycoding-art/project-2_Sedinkin_M25-555.git
   ```

2. **Установите зависимости**
   ```bash
   poetry install
   ```

3. **Активируйте виртуальное окружение и запустите игру**
   ```bash
   make install
   make package-install
   make build
   make project
   ```

---

## Управление таблицами
Список команд
   ```
   <command> create_table <имя_таблицы> <столбец1:тип> <столбец2:тип> .. - создать таблицу
   <command> list_tables - показать список всех таблиц
   <command> drop_table <имя_таблицы> - удалить таблицу
   <command> exit - выход из программы
   <command> help - справочная информация
   ```

Пример работы
   ```
   >>> database

   ***Процесс работы с таблицей***
   Функции:
   <command> create_table <имя_таблицы> <столбец1:тип> <столбец2:тип> .. - создать таблицу
   <command> list_tables - показать список всех таблиц
   <command> drop_table <имя_таблицы> - удалить таблицу
   <command> exit - выход из программы
   <command> help - справочная информация 

   >>>Введите команду: create_table users name:str age:int is_active:bool
   Таблица "users" успешно создана со столбцами: ID:int, name:str, age:int, is_active:bool

   >>>Введите команду: create_table users name:str
   Ошибка: Таблица "users" уже существует.

   >>>Введите команду: list_tables
   - users

   >>>Введите команду: drop_table users
   Таблица "users" успешно удалена.

   >>>Введите команду: drop_table products
   Ошибка: Таблица "products" не существует.

   >>>Введите команду: help
   ***Процесс работы с таблицей***
   Функции:
   <command> create_table <имя_таблицы> <столбец1:тип> <столбец2:тип> .. - создать таблицу
   <command> list_tables - показать список всех таблиц
   <command> drop_table <имя_таблицы> - удалить таблицу
   <command> exit - выход из программы
   <command> help - справочная информация 
   ```

CRUD-операции
   ```
   database

   ***Операции с данными***

   Функции:
   <command> insert into <имя_таблицы> values (<значение1>, <значение2>, ...) - создать запись.
   <command> select from <имя_таблицы> where <столбец> = <значение> - прочитать записи по условию.
   <command> select from <имя_таблицы> - прочитать все записи.
   <command> update <имя_таблицы> set <столбец1> = <новое_значение1> where <столбец_условия> = <значение_условия> - обновить запись.
   <command> delete from <имя_таблицы> where <столбец> = <значение> - удалить запись.
   <command> info <имя_таблицы> - вывести информацию о таблице.
   <command> exit - выход из программы
   <command> help- справочная информация

   >>> Введите команду: insert into users values ("Sergei", 28, true)
   Запись с ID=1 успешно добавлена в таблицу "users".

   >>> Введите команду: select from users where age = 28
   +----+--------+-----+-----------+
   | ID |  name  | age | is_active |
   +----+--------+-----+-----------+
   | 1  | Sergei | 28  |    True   |
   +----+--------+-----+-----------+

   >>> Введите команду: update users set age = 29 where name = "Sergei"
   Запись с ID=1 в таблице "users" успешно обновлена.

   >>> Введите команду: delete from users where ID = 1
   Запись с ID=1 успешно удалена из таблицы "users".

   >>> Введите команду: info users
   Таблица: users
   Столбцы: ID:int, name:str, age:int, is_active:bool
   Количество записей: 0
   ```