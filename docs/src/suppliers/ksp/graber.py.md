# Модуль для сбора данных о товарах с сайта ksp.co.il

## Обзор

Модуль `graber.py` предназначен для сбора информации о товарах с сайта ksp.co.il. Он содержит класс `Graber`, который наследует функциональность от родительского класса `Graber` (Grbr). Модуль предоставляет механизмы для обработки различных полей на странице товара, включая возможность переопределения стандартных методов обработки для нестандартных ситуаций. Также поддерживается предварительная обработка запросов к веб-драйверу через декораторы.

## Подробней

Этот модуль является частью системы для сбора и обработки данных о товарах с различных онлайн-магазинов. Он специализируется на сборе информации с сайта ksp.co.il.  Модуль использует веб-драйвер для взаимодействия со страницей и извлечения необходимых данных. В случае необходимости выполнения предварительных действий перед запросом к веб-драйверу, предусмотрены декораторы.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора данных о товарах с сайта ksp.co.il. Он наследует функциональность от базового класса `Graber` (Grbr) и предоставляет возможность переопределять методы обработки полей для нестандартных случаев.

**Принцип работы**:
Класс инициализируется с драйвером веб-браузера и индексом языка. Он определяет префикс поставщика как 'ksp' и использует его при инициализации родительского класса. Если текущий URL содержит '/mob/', класс загружает локаторы для мобильной версии сайта. Также класс позволяет устанавливать локаторы для декоратора `@close_pop_up`, который выполняет предварительные действия перед запросом к веб-драйверу.

**Наследует**:
- `Graber` (из `src.suppliers.graber`): Обеспечивает базовую функциональность для сбора данных о товарах с веб-страниц.

**Аттрибуты**:
- `supplier_prefix` (str): Префикс поставщика, устанавливается в значение 'ksp'.

**Методы**:
- `__init__(self, driver: 'Driver', lang_index: int)`: Инициализирует класс `Graber`, устанавливает префикс поставщика, вызывает конструктор родительского класса, проверяет мобильную версию сайта и устанавливает локаторы.

### `__init__`

```python
    def __init__(self, driver: 'Driver', lang_index:int):
        """Инициализация класса сбора полей товара."""
        self.supplier_prefix = 'ksp'
        super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)
        time.sleep(3)
        if '/mob/' in self.driver.current_url: # <- бывет, что подключается к мобильной версии сайта
            self.locator = j_loads_ns(gs.path.src / 'suppliers' / 'ksp' / 'locators' / 'product_mobile_site.json')
            logger.info("Установлены локаторы для мобильной версии сайта KSP")
            ...

        Context.locator_for_decorator = None # <- если будет уастановлено значение - то оно выполнится в декораторе `@close_pop_up`
```

**Назначение**: Инициализация экземпляра класса `Graber`.

**Параметры**:
- `driver` (Driver): Экземпляр веб-драйвера для управления браузером.
- `lang_index` (int): Индекс языка.

**Как работает функция**:

1. Устанавливает атрибут `supplier_prefix` в значение `'ksp'`.
2. Вызывает конструктор родительского класса `Graber` (Grbr) с указанием префикса поставщика, драйвера и индекса языка.
3. Приостанавливает выполнение на 3 секунды с помощью `time.sleep(3)`.
4. Проверяет, содержит ли текущий URL драйвера подстроку `'/mob/'`. Если да, то загружает локаторы для мобильной версии сайта из файла `product_mobile_site.json`, используя функцию `j_loads_ns`, и логирует информацию об этом.
5. Устанавливает атрибут `Context.locator_for_decorator` в значение `None`, чтобы убедиться, что декоратор `@close_pop_up` не будет выполняться без необходимости.

**Примеры**:

```python
# Пример инициализации класса Graber
from src.webdriver import Driver
from src.webdriver import Firefox

driver = Driver(Firefox)
lang_index = 0
graber = Graber(driver, lang_index)
```
## Функции

### `close_pop_up`

```python
# def close_pop_up(value: Any = None) -> Callable:
#     """Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

#     Args:
#         value (Any): Дополнительное значение для декоратора.

#     Returns:
#         Callable: Декоратор, оборачивающий функцию.
#     """
#     def decorator(func: Callable) -> Callable:
#         @wraps(func)
#         async def wrapper(*args, **kwargs):
#             try:
#                 # await Context.driver.execute_locator(Context.locator.close_pop_up)  # Await async pop-up close  
#                 ... 
#             except ExecuteLocatorException as e:
#                 logger.debug(f'Ошибка выполнения локатора: {e}')
#             return await func(*args, **kwargs)  # Await the main function
#         return wrapper
#     return decorator
# return decorator
```

**Назначение**: Создает декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

**Параметры**:
- `value` (Any, optional): Дополнительное значение для декоратора. По умолчанию `None`.

**Возвращает**:
- `Callable`: Декоратор, оборачивающий функцию.

**Как работает функция**:
1. Определяет внутреннюю функцию `decorator`, которая принимает функцию `func` в качестве аргумента.
2. Внутри `decorator` определяет асинхронную функцию `wrapper`, которая будет выполняться вместо исходной функции `func`.
3. Внутри `wrapper` оборачивает вызов исходной функции в блок `try...except` для обработки возможных исключений.
4. В блоке `try` пытается выполнить локатор для закрытия всплывающего окна, используя `Context.driver.execute_locator(Context.locator.close_pop_up)`.
5. В блоке `except` перехватывает исключение `ExecuteLocatorException` и логирует сообщение об ошибке.
6. После обработки исключения вызывает исходную функцию `func` с помощью `await func(*args, **kwargs)` и возвращает результат.
7. Возвращает функцию `wrapper`.
8. Возвращает декоратор.

**Примеры**:

```python
# Пример использования декоратора close_pop_up
# @close_pop_up()
# async def my_function():
#     # Some code here
#     ...
```