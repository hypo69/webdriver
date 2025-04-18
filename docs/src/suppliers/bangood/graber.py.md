# Модуль `graber` для работы с поставщиком Banggood
## Обзор

Модуль предназначен для сбора информации о товарах с сайта `bangood.com`. Он содержит класс `Graber`, который наследует функциональность от базового класса `Graber` (предположительно, `src.suppliers.graber.Graber`). Класс `Graber` переопределяет некоторые методы родительского класса для специфической обработки полей товаров на сайте Banggood.

## Подробней

Этот модуль является частью системы для сбора данных о товарах от различных поставщиков. Он специализируется на поставщике `bangood.com`. Класс `Graber` содержит логику для извлечения и обработки информации о товарах, используя веб-драйвер для взаимодействия с сайтом.  При необходимости нестандартной обработки полей, функции родительского класса перегружаются в этом классе.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора данных о товарах с сайта `bangood.com`. Он наследуется от класса `Graber` из модуля `src.suppliers.graber` и переопределяет некоторые методы для специфической обработки полей товаров на сайте Banggood.

**Принцип работы**:

1.  Класс инициализируется с драйвером веб-браузера и индексом языка.
2.  Устанавливается префикс поставщика `bangood`.
3.  Происходит инициализация родительского класса `Graber` с указанием префикса поставщика, драйвера и индекса языка.
4.  Устанавливаются глобальные настройки через `Context`, включая `locator_for_decorator`. Если `Context.locator_for_decorator` имеет значение, оно будет выполнено в декораторе `@close_pop_up`.

**Наследует**:
- `src.suppliers.graber.Graber`

**Аттрибуты**:

-   `supplier_prefix` (str): Префикс поставщика, устанавливается в значение `'bangood'`.

**Методы**:
-   `__init__(self, driver: Driver, lang_index: int)`: Инициализирует экземпляр класса `Graber`.

### `close_pop_up`

**Описание**: Функция-декоратор для закрытия всплывающих окон перед выполнением основной логики функции. В данном коде закомментирована.

## Функции

### `__init__`

```python
def __init__(self, driver: Driver, lang_index: int):
    """Инициализация класса сбора полей товара."""
```

**Назначение**: Инициализация экземпляра класса `Graber`.

**Параметры**:

-   `driver` (`Driver`): Экземпляр драйвера веб-браузера для взаимодействия с сайтом.
-   `lang_index` (`int`): Индекс языка, используемый для локализации контента на сайте.

**Возвращает**:

-   None

**Как работает функция**:

1.  Устанавливает атрибут `supplier_prefix` в значение `'bangood'`.
2.  Вызывает конструктор родительского класса `Graber` с передачей префикса поставщика, драйвера и индекса языка.
3.  Устанавливает атрибут `Context.locator_for_decorator` в значение `None`. Это необходимо для работы декоратора `@close_pop_up`, который может выполнять дополнительные действия перед выполнением основной логики функции, если значение `Context.locator_for_decorator` установлено.

**ASCII flowchart**:

```
Начало
    │
    │ Установка supplier_prefix = 'bangood'
    │
    │ Вызов Graber.__init__(supplier_prefix, driver, lang_index)
    │
    │ Установка Context.locator_for_decorator = None
    │
Конец
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from src.webdriver import Firefox

# Создание инстанса драйвера (пример с Firefox)
driver = Driver(Firefox)

# Пример инициализации класса Graber
graber = Graber(driver, 0)
print(graber.supplier_prefix)  # Вывод: bangood
```

### `close_pop_up` (закомментированный декоратор)

```python
def close_pop_up(value: Any = None):
    """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции."""
```

**Назначение**: Создание декоратора для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:

-   `value` (`Any`, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:

-   `Callable`: Декоратор, оборачивающий функцию.

**Как работает функция**:

1.  Определяет внутреннюю функцию `decorator`, которая принимает функцию `func` в качестве аргумента.
2.  Внутри `decorator` определяется функция `wrapper`, которая принимает произвольные аргументы (`*args`, `**kwargs`).
3.  Внутри `wrapper` происходит попытка выполнить локатор для закрытия всплывающего окна с использованием `Context.driver.execute_locator(Context.locator.close_pop_up)`.
4.  В случае ошибки выполнения локатора, информация об ошибке логируется с уровнем `DEBUG`.
5.  После выполнения (или попытки выполнения) локатора вызывается основная функция `func` с передачей аргументов и возвращается результат её выполнения.
6.  Функция `decorator` возвращает функцию `wrapper`.
7.  Функция `close_pop_up` возвращает функцию `decorator`.

**ASCII flowchart**:

```
Начало (close_pop_up)
    │
    │ Определение decorator(func)
    │
    │   Определение wrapper(*args, **kwargs)
    │   │
    │   │ Попытка выполнить Context.driver.execute_locator(Context.locator.close_pop_up)
    │   │
    │   │ Если ошибка -> Логирование ошибки
    │   │
    │   │ Вызов func(*args, **kwargs) и возврат результата
    │
    │ Возврат decorator
    │
Конец (close_pop_up)
```

**Примеры**:

```python
from typing import Callable, Any

# Пример использования декоратора (если бы он не был закомментирован)
# @close_pop_up()
def my_function():
    """Основная логика функции."""
    print("Выполнение основной логики")

# my_function()  # Вывод: "Выполнение основной логики" (после попытки закрытия всплывающего окна)