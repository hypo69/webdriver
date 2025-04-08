# Модуль `file_counter.py`

## Обзор

Модуль `file_counter.py` предназначен для рекурсивного подсчета количества строк в текстовых файлах, а также количества классов и функций в указанной директории и её поддиректориях. Этот инструмент полезен для анализа размера и сложности кодовой базы проекта `hypotez`.

## Подробней

Данный модуль предоставляет следующие возможности:

- Рекурсивный обход директории для поиска текстовых файлов.
- Исключение бинарных файлов, файлов из директорий `__pycache__` и `firefox_profiles`, файлов Jupyter Notebook (`.ipynb`) и файла `__init__.py` из подсчета.
- Подсчет общего количества строк, классов и функций в найденных файлах.

Модуль состоит из нескольких функций: `count_lines_in_files`, `is_binary`, и `count_classes_and_functions`. Каждая функция выполняет определенную задачу в процессе анализа файлов и подсчета строк, классов и функций.

## Функции

### `count_lines_in_files`

```python
def count_lines_in_files(directory):
    """
     Recursively counts the number of lines in text files in the specified directory and its subdirectories, as well as the number of classes and functions.
    
    @param directory: Path to the directory
    @return: Total number of lines in text files, number of classes, and number of functions
    """
    ...
```

**Описание**: Рекурсивно подсчитывает количество строк в текстовых файлах в указанной директории и её поддиректориях, а также количество классов и функций.

**Как работает функция**:
1. Инициализирует счетчики `total_lines`, `total_classes` и `total_functions` нулями.
2. Получает список файлов и поддиректорий в указанной директории с помощью `os.listdir(directory)`.
3. Перебирает каждый элемент в списке:
   - Если элемент является файлом (`os.path.isfile(filepath)`):
     - Проверяет, является ли файл текстовым, не принадлежит ли он директориям `__pycache__` или `firefox_profiles`, и не является ли он файлом Jupyter Notebook (`.ipynb`) или файлом `__init__.py`.
     - Если файл удовлетворяет условиям, открывает его в режиме чтения с указанием кодировки `utf-8` и обработкой ошибок (`errors='ignore'`).
     - Подсчитывает количество строк в файле с помощью генератора `sum(1 for line in file)` и добавляет его к `total_lines`.
     - Вызывает функцию `count_classes_and_functions` для подсчета классов и функций в файле и добавляет результаты к `total_classes` и `total_functions` соответственно.
   - Если элемент является директорией (`os.path.isdir(filepath)`):
     - Рекурсивно вызывает функцию `count_lines_in_files` для подсчета строк, классов и функций в поддиректории.
     - Добавляет полученные значения к `total_lines`, `total_classes` и `total_functions` соответственно.
4. Возвращает общее количество строк, классов и функций.

**Параметры**:
- `directory` (str): Путь к директории, в которой необходимо выполнить подсчет.

**Возвращает**:
- `tuple[int, int, int]`: Кортеж, содержащий общее количество строк, классов и функций.

**Примеры**:

```python
src_directory = 'src'
total_lines, total_classes, total_functions = count_lines_in_files(src_directory)
print(f"Total lines in text files in '{src_directory}': {total_lines}")
print(f"Total classes: {total_classes}")
print(f"Total functions: {total_functions}")
```

### `is_binary`

```python
def is_binary(filepath):
    """
     Checks if the file is binary.
    
    @param filepath: Path to the file
    @return: True if the file is binary, otherwise False
    """
    ...
```

**Описание**: Проверяет, является ли файл бинарным.

**Как работает функция**:
1. Пытается открыть файл в режиме чтения байтов (`'rb'`).
2. Читает первые 512 байтов файла.
3. Проверяет, содержит ли прочитанный блок нулевые байты (`b'\\0'`). Если содержит, то файл считается бинарным и возвращается `True`.
4. Если при чтении файла возникает исключение, то файл также считается бинарным и возвращается `True`.

**Параметры**:
- `filepath` (str): Путь к файлу, который необходимо проверить.

**Возвращает**:
- `bool`: `True`, если файл является бинарным, `False` в противном случае.

**Примеры**:

```python
file_path = 'example.txt'
if is_binary(file_path):
    print(f"File '{file_path}' is binary.")
else:
    print(f"File '{file_path}' is not binary.")
```

### `count_classes_and_functions`

```python
def count_classes_and_functions(filepath):
    """
     Counts the number of classes and functions in the file.
    
    @param filepath: Path to the file
    @return: Number of classes and number of functions
    """
    ...
```

**Описание**: Подсчитывает количество классов и функций в файле.

**Как работает функция**:
1. Инициализирует счетчики `total_classes` и `total_functions` нулями.
2. Открывает файл в режиме чтения с указанием кодировки `utf-8` и обработкой ошибок (`errors='ignore'`).
3. Перебирает каждую строку в файле.
4. Проверяет, начинается ли строка с ключевого слова `class` (после удаления пробельных символов в начале и конце строки). Если да, увеличивает счетчик `total_classes`.
5. Проверяет, начинается ли строка с ключевого слова `def` (после удаления пробельных символов в начале и конце строки). Если да, увеличивает счетчик `total_functions`.
6. Возвращает общее количество классов и функций.

**Параметры**:
- `filepath` (str): Путь к файлу, в котором необходимо выполнить подсчет.

**Возвращает**:
- `tuple[int, int]`: Кортеж, содержащий количество классов и функций.

**Примеры**:

```python
file_path = 'example.py'
classes, functions = count_classes_and_functions(file_path)
print(f"Number of classes in '{file_path}': {classes}")
print(f"Number of functions in '{file_path}': {functions}")
```