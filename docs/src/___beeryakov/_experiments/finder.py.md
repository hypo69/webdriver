# Модуль `finder.py`

## Обзор

Модуль `finder.py` предназначен для поиска категорий в заданной директории. Он сканирует указанную директорию и ее поддиректории, чтобы найти папки, содержащие слово `category` или файлы с именем `category.py`.

## Подробней

Этот модуль используется для поиска и определения категорий в структуре проекта. Он обходит дерево директорий, начиная с указанной корневой директории, и добавляет в список все пути, где встречается папка `translator` в директории `category`, или файл `category.py`. Это может быть полезно для автоматического обнаружения и обработки категорий в проекте.

## Функции

### `find_categories`

```python
def find_categories(directory: str) -> list[str]:
    """
    Поиск категорий в заданной директории.

    Args:
        directory (str): Путь к директории для поиска категорий.

    Returns:
        list[str]: Список путей к найденным категориям.
    """
```

**Как работает функция**:
Функция `find_categories` принимает путь к директории в качестве аргумента. Она использует функцию `os.walk` для обхода дерева директорий, начиная с указанной директории. Для каждой директории и списка файлов в ней проверяется наличие папки `category` в списке директорий (`dirs`) или файла `category.py` в списке файлов (`files`). Если папка `category` найдена, путь к папке `translator` внутри этой категории добавляется в список категорий. Если файл `category.py` найден, путь к этому файлу добавляется в список категорий. В конце функция возвращает список всех найденных путей к категориям.

**Параметры**:
- `directory` (str): Путь к директории, в которой производится поиск категорий.

**Возвращает**:
- `list[str]`: Список путей к найденным категориям.

**Примеры**:

```python
from pathlib import Path
from src import gs
src = str(Path(gs.path.src))
found_categories = find_categories(src)
for item in found_categories:
    print(item)
```