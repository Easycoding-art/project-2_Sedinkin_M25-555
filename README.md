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