# Документация модуля `src.webdriver.firefox.header`

## Обзор

Модуль `header.py` предназначен для определения корневого каталога проекта, загрузки настроек и метаданных проекта.

## Оглавление

-   [Обзор](#обзор)
-   [Функции](#функции)
    -   [`set_project_root`](#set_project_root)
-   [Переменные](#переменные)
    -   [`__root__`](#__root__)
    -   [`settings`](#settings)
    -   [`doc_str`](#doc_str)
    -   [`__project_name__`](#__project_name__)
    -   [`__version__`](#__version__)
    -   [`__doc__`](#__doc__)
    -   [`__details__`](#__details__)
    -   [`__author__`](#__author__)
    -   [`__copyright__`](#__copyright__)
    -   [`__cofee__`](#__cofee__)

## Функции

### `set_project_root`

```python
def set_project_root(marker_files=('__root__','.git')) -> Path:
    """
    Finds the root directory of the project starting from the current file's directory,
    searching upwards and stopping at the first directory containing any of the marker files.

    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__
```

**Описание**: Функция `set_project_root` определяет корневой каталог проекта, начиная с каталога текущего файла, ища вверх по иерархии каталогов до тех пор, пока не будет найден каталог, содержащий один из файлов-маркеров.

**Параметры**:

-   `marker_files` (tuple): Кортеж с именами файлов или каталогов, которые идентифицируют корень проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:

-   `Path`: Путь к корневому каталогу проекта, если он найден. В противном случае возвращает каталог, в котором находится скрипт.

## Переменные

### `__root__`

```python
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""
```

**Описание**: Переменная `__root__` хранит путь к корневому каталогу проекта, полученный с помощью функции `set_project_root`.

**Тип**: `Path`

### `settings`

```python
settings:dict = None
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

**Описание**: Переменная `settings` хранит настройки проекта, загруженные из файла `settings.json`, расположенного в каталоге `src`. Если файл не найден или содержит ошибки JSON, значение переменной останется `None`.

**Тип**: `dict | None`

### `doc_str`

```python
doc_str:str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError):
    ...
```

**Описание**: Переменная `doc_str` содержит содержимое файла `README.MD`, расположенного в каталоге `src`. Если файл не найден, значение переменной останется `None`.

**Тип**: `str | None`

### `__project_name__`

```python
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
```

**Описание**: Переменная `__project_name__` хранит имя проекта, полученное из файла `settings.json` с ключом `project_name`. Если ключ отсутствует или файл не может быть загружен, по умолчанию используется значение `'hypotez'`.

**Тип**: `str`

### `__version__`

```python
__version__: str = settings.get("version", '')  if settings  else ''
```

**Описание**: Переменная `__version__` хранит версию проекта, полученную из файла `settings.json` с ключом `version`. Если ключ отсутствует или файл не может быть загружен, значением будет пустая строка `''`.

**Тип**: `str`

### `__doc__`

```python
__doc__: str = doc_str if doc_str else ''
```

**Описание**: Переменная `__doc__` хранит содержимое файла `README.MD`, если он был успешно загружен в переменную `doc_str`. В противном случае значением будет пустая строка `''`.

**Тип**: `str`

### `__details__`

```python
__details__: str = ''
```

**Описание**: Переменная `__details__` является заглушкой и всегда содержит пустую строку `''`.

**Тип**: `str`

### `__author__`

```python
__author__: str = settings.get("author", '')  if settings  else ''
```

**Описание**: Переменная `__author__` хранит имя автора проекта, полученное из файла `settings.json` с ключом `author`. Если ключ отсутствует или файл не может быть загружен, значением будет пустая строка `''`.

**Тип**: `str`

### `__copyright__`

```python
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
```

**Описание**: Переменная `__copyright__` хранит информацию об авторских правах проекта, полученную из файла `settings.json` с ключом `copyrihgnt`. Если ключ отсутствует или файл не может быть загружен, значением будет пустая строка `''`.

**Тип**: `str`

### `__cofee__`

```python
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```

**Описание**: Переменная `__cofee__` хранит сообщение с предложением поддержать разработчика чашкой кофе, полученное из файла `settings.json` с ключом `cofee`. Если ключ отсутствует или файл не может быть загружен, используется сообщение по умолчанию.

**Тип**: `str`