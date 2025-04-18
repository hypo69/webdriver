# Модуль notebook_header

## Обзор

Модуль `notebook_header.py` предназначен для настройки окружения и импорта необходимых модулей для экспериментов и разработки в рамках проекта `hypotez`. Он добавляет корневую директорию проекта в `sys.path`, что позволяет импортировать модули из других частей проекта.

## Подробней

Этот модуль необходим для того, чтобы запускать код из блокнотов (например, Jupyter Notebook), обеспечивая доступ ко всем необходимым модулям проекта `hypotez`. Он также включает импорты различных классов и функций, используемых в проекте, таких как `Driver`, `Supplier`, `Product`, `Category` и другие утилиты.

## Функции

### `start_supplier`

```python
def start_supplier(supplier_prefix, locale):
    """ Старт поставщика """
    ...
```

**Назначение**: Функция `start_supplier` предназначена для инициализации и запуска поставщика (Supplier) с заданным префиксом и локалью.

**Параметры**:

-   `supplier_prefix` (str): Префикс поставщика.
-   `locale` (str): Локаль поставщика.

**Возвращает**:

-   `Supplier` или `str`: Возвращает экземпляр класса `Supplier` или сообщение об ошибке, если не заданы префикс поставщика и локаль.

**Как работает функция**:

1.  **Проверка входных параметров**:
    -   Функция проверяет, заданы ли параметры `supplier_prefix` и `locale`. Если хотя бы один из них не задан, возвращается сообщение об ошибке.
2.  **Создание словаря параметров**:
    -   Создается словарь `params`, содержащий `supplier_prefix` и `locale`.
3.  **Инициализация поставщика**:
    -   Создается экземпляр класса `Supplier` с использованием переданных параметров.

**Пример:**

```python
supplier = start_supplier(supplier_prefix='hb', locale='ru_RU')
```

### Блок-схема функции `start_supplier`

```
Проверка параметров
│
└─> Если supplier_prefix и locale не заданы:
│   │
│   └─> Возврат сообщения об ошибке
│   │
└─> Создание словаря параметров params
│
└─> Инициализация поставщика Supplier с параметрами params
│
└─> Возврат экземпляра Supplier
```

### Пример вызова функции `start_supplier`

```python
start_supplier(supplier_prefix="SomePrefix", locale="en_US")