# Модуль для сбора данных с Amazon
## Обзор

Модуль `graber.py` предназначен для сбора информации о товарах с сайта `amazon.com`. Он содержит класс `Graber`, который наследует функциональность класса `Graber` из модуля `src.suppliers.graber`. Основная задача класса `Graber` - извлечение значений различных полей со страницы товара Amazon.

## Подробнее

Этот модуль является частью системы для сбора данных о товарах с различных онлайн-магазинов. Он специализируется на обработке данных с сайта `amazon.com`. Для каждой характеристики товара, такой как название, цена, описание и т.д., предусмотрена функция для извлечения соответствующего значения. Если стандартных методов обработки недостаточно, эти функции переопределяются в классе `Graber` для кастомной обработки.

Модуль использует декораторы для выполнения предварительных действий перед отправкой запроса к веб-драйверу, например, для закрытия всплывающих окон.

## Классы

### `Graber`

**Описание**: Класс `Graber` предназначен для сбора данных о товарах с сайта `amazon.com`. Он наследует класс `Graber` из модуля `src.suppliers.graber` и переопределяет некоторые его методы для адаптации к специфике `amazon.com`.

**Наследует**:

- `Graber` (as `Grbr`) из `src.suppliers.graber`

**Атрибуты**:

- `supplier_prefix` (str): Префикс поставщика, в данном случае 'amazon'.

**Методы**:

- `__init__(self, driver: Driver, lang_index: int)`: Инициализирует класс `Graber`, устанавливает префикс поставщика и вызывает конструктор родительского класса.

### `__init__`

```python
def __init__(self, driver: Driver, lang_index: int):
    """Инициализация класса сбора полей товара."""
    self.supplier_prefix = 'amazon'
    super().__init__(supplier_prefix=self.supplier_prefix, driver=driver, lang_index=lang_index)
    # Устанавливаем глобальные настройки через Context

    Context.locator_for_decorator = None # <- если будет уастановлено значение - то оно выполнится в декораторе `@close_pop_up`
```

**Назначение**: Инициализирует экземпляр класса `Graber`.

**Параметры**:

- `driver` (Driver): Экземпляр веб-драйвера для взаимодействия с сайтом.
- `lang_index` (int): Индекс языка.

**Как работает функция**:

1. Устанавливает атрибут `supplier_prefix` равным `'amazon'`.
2. Вызывает конструктор родительского класса `Graber` с указанием префикса поставщика, драйвера и индекса языка.
3. Устанавливает значение `Context.locator_for_decorator` в `None`. Если будет установлено другое значение, оно будет выполнено в декораторе `@close_pop_up`.

```
A: Установка supplier_prefix = 'amazon'
|
B: Вызов super().__init__(...)
|
C: Установка Context.locator_for_decorator = None
```

**Примеры**:

```python
from src.webdriver.driver import Driver, Chrome
from src.suppliers.amazon.graber import Graber

driver = Driver(Chrome)
graber = Graber(driver=driver, lang_index=0)
print(graber.supplier_prefix)  # Вывод: amazon