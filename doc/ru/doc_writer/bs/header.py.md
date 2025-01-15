# Документация модуля `src.webdriver.bs.header`

## Обзор

Модуль `header.py` предназначен для определения корневого каталога проекта и добавления его в `sys.path`.

## Оглавление

- [Обзор](#обзор)
- [Функции](#функции)
    - [`set_project_root`](#set_project_root)
- [Переменные](#переменные)
    - [`__root__`](#__root__)

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