# Модуль для создания клавиатур администратора Telegram-бота для цифрового рынка
=========================================================================================

Модуль содержит функции для создания различных встроенных клавиатур (InlineKeyboardMarkup) для административной панели Telegram-бота. Клавиатуры используются для управления каталогом, товарами, статистикой и другими административными функциями.

## Обзор

Этот модуль предоставляет набор функций для создания клавиатур, которые используются в административной панели Telegram-бота. Каждая функция создает определенный тип клавиатуры с кнопками, соответствующими различным действиям администратора.
Все функции используют `InlineKeyboardBuilder` из библиотеки `aiogram` для создания клавиатур и возвращают `InlineKeyboardMarkup`.

## Подробней

Модуль `kbs.py` предназначен для формирования интерактивных клавиатур, используемых в Telegram-боте для администраторов.
Эти клавиатуры позволяют администраторам управлять каталогом товаров, просматривать статистику, добавлять или удалять товары, а также возвращаться в главное меню.
Все функции в модуле используют `InlineKeyboardBuilder` для создания клавиатур и возвращают объект `InlineKeyboardMarkup`, который затем отправляется пользователю через Telegram API.

## Функции

### `catalog_admin_kb`

```python
def catalog_admin_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Создает встроенную клавиатуру для администратора с категориями каталога.

    Args:
        catalog_data (List[Category]): Список объектов Category, содержащих информацию о категориях.

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками для каждой категории и кнопкой "Отмена".
    
    Example:
        Примеры вызовов со всем спектром параметров. которы можно передать в функцию
        catalog_admin_kb(catalog_data=[Category(id=1, category_name='Category 1'), Category(id=2, category_name='Category 2')])
    """
    ...
```

**Назначение**:
Функция создает клавиатуру с кнопками, представляющими категории каталога, для административной панели Telegram-бота.

**Параметры**:
- `catalog_data` (List[Category]): Список объектов `Category`, каждый из которых представляет категорию товара.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект встроенной клавиатуры, готовый для отправки пользователю.

**Как работает функция**:

1.  **Инициализация:** Создается экземпляр `InlineKeyboardBuilder`.
2.  **Перебор категорий:** Для каждой категории в `catalog_data` создается кнопка с текстом, соответствующим имени категории, и callback_data, содержащим ID категории.
3.  **Кнопка отмены:** Добавляется кнопка "Отмена", возвращающая в админ-панель.
4.  **Форматирование:** Кнопки располагаются в два столбца.
5.  **Возврат результата:** Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

**ASCII flowchart**:

```
A: Инициализация InlineKeyboardBuilder
↓
B: Перебор catalog_data
│  ↓
│  C: Создание кнопки для каждой категории
│  ↓
D: Создание кнопки "Отмена"
↓
E: Форматирование клавиатуры (2 столбца)
↓
F: Преобразование в InlineKeyboardMarkup
↓
G: Возврат InlineKeyboardMarkup
```

Где:

-   `A`: Создание экземпляра `InlineKeyboardBuilder`.
-   `B`: Начало итерации по списку категорий.
-   `C`: Создание кнопки для каждой категории с callback_data.
-   `D`: Добавление кнопки "Отмена" с callback_data.
-   `E`: Расположение кнопок в два столбца.
-   `F`: Преобразование структуры клавиатуры в `InlineKeyboardMarkup`.
-   `G`: Возврат готовой клавиатуры.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from typing import List
from bot.dao.models import Category


# Пример использования
catalog_data = [Category(id=1, category_name='Электроника'), Category(id=2, category_name='Одежда')]
keyboard = catalog_admin_kb(catalog_data)
print(type(keyboard))  # Вывод: <class 'aiogram.types.inline_keyboard.InlineKeyboardMarkup'>

catalog_data = [Category(id=1, category_name='Электроника'), Category(id=2, category_name='Одежда'), Category(id=3, category_name='Обувь')]
keyboard = catalog_admin_kb(catalog_data)
print(type(keyboard))  # Вывод: <class 'aiogram.types.inline_keyboard.InlineKeyboardMarkup'>
```

### `admin_send_file_kb`

```python
def admin_send_file_kb() -> InlineKeyboardMarkup:
    """
    Создает встроенную клавиатуру для администратора с кнопками "Без файла" и "Отмена".

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "Без файла" и "Отмена".
    
    Example:
        admin_send_file_kb()
    """
    ...
```

**Назначение**:
Создает клавиатуру с вариантами действий при отправке файла (или отказе от отправки).

**Возвращает**:
- `InlineKeyboardMarkup`: Объект встроенной клавиатуры.

**Как работает функция**:

1.  **Инициализация:** Создается экземпляр `InlineKeyboardBuilder`.
2.  **Кнопка "Без файла":** Добавляется кнопка "Без файла".
3.  **Кнопка "Отмена":** Добавляется кнопка "Отмена".
4.  **Форматирование:** Кнопки располагаются в два столбца.
5.  **Возврат результата:** Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

**ASCII flowchart**:

```
A: Инициализация InlineKeyboardBuilder
↓
B: Создание кнопки "Без файла"
↓
C: Создание кнопки "Отмена"
↓
D: Форматирование клавиатуры (2 столбца)
↓
E: Преобразование в InlineKeyboardMarkup
↓
F: Возврат InlineKeyboardMarkup
```

Где:

-   `A`: Создание экземпляра `InlineKeyboardBuilder`.
-   `B`: Создание кнопки "Без файла" с callback_data.
-   `C`: Создание кнопки "Отмена" с callback_data.
-   `D`: Расположение кнопок в два столбца.
-   `E`: Преобразование структуры клавиатуры в `InlineKeyboardMarkup`.
-   `F`: Возврат готовой клавиатуры.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Пример использования
keyboard = admin_send_file_kb()
print(type(keyboard))  # Вывод: <class 'aiogram.types.inline_keyboard.InlineKeyboardMarkup'>
```

### `admin_kb`

```python
def admin_kb() -> InlineKeyboardMarkup:
    """
    Создает встроенную клавиатуру для администратора с основными функциями управления.

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "📊 Статистика", "🛍️ Управлять товарами" и "🏠 На главную".
    
    Example:
        admin_kb()
    """
    ...
```

**Назначение**:
Создает основную клавиатуру администратора с кнопками для просмотра статистики, управления товарами и возврата на главную.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект встроенной клавиатуры.

**Как работает функция**:

1.  **Инициализация:** Создается экземпляр `InlineKeyboardBuilder`.
2.  **Кнопка "📊 Статистика":** Добавляется кнопка "📊 Статистика".
3.  **Кнопка "🛍️ Управлять товарами":** Добавляется кнопка "🛍️ Управлять товарами".
4.  **Кнопка "🏠 На главную":** Добавляется кнопка "🏠 На главную".
5.  **Форматирование:** Кнопки располагаются в два столбца.
6.  **Возврат результата:** Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

**ASCII flowchart**:

```
A: Инициализация InlineKeyboardBuilder
↓
B: Создание кнопки "📊 Статистика"
↓
C: Создание кнопки "🛍️ Управлять товарами"
↓
D: Создание кнопки "🏠 На главную"
↓
E: Форматирование клавиатуры (2 столбца)
↓
F: Преобразование в InlineKeyboardMarkup
↓
G: Возврат InlineKeyboardMarkup
```

Где:

-   `A`: Создание экземпляра `InlineKeyboardBuilder`.
-   `B`: Создание кнопки "📊 Статистика" с callback_data.
-   `C`: Создание кнопки "🛍️ Управлять товарами" с callback_data.
-   `D`: Создание кнопки "🏠 На главную" с callback_data.
-   `E`: Расположение кнопок в два столбца.
-   `F`: Преобразование структуры клавиатуры в `InlineKeyboardMarkup`.
-   `G`: Возврат готовой клавиатуры.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Пример использования
keyboard = admin_kb()
print(type(keyboard))  # Вывод: <class 'aiogram.types.inline_keyboard.InlineKeyboardMarkup'>
```

### `admin_kb_back`

```python
def admin_kb_back() -> InlineKeyboardMarkup:
    """
    Создает встроенную клавиатуру для администратора с кнопками "⚙️ Админ панель" и "🏠 На главную".

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "⚙️ Админ панель" и "🏠 На главную".
    
    Example:
        admin_kb_back()
    """
    ...
```

**Назначение**:
Создает клавиатуру для возврата в админ-панель или на главную страницу.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект встроенной клавиатуры.

**Как работает функция**:

1.  **Инициализация:** Создается экземпляр `InlineKeyboardBuilder`.
2.  **Кнопка "⚙️ Админ панель":** Добавляется кнопка "⚙️ Админ панель".
3.  **Кнопка "🏠 На главную":** Добавляется кнопка "🏠 На главную".
4.  **Форматирование:** Кнопки располагаются в один столбец.
5.  **Возврат результата:** Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

**ASCII flowchart**:

```
A: Инициализация InlineKeyboardBuilder
↓
B: Создание кнопки "⚙️ Админ панель"
↓
C: Создание кнопки "🏠 На главную"
↓
D: Форматирование клавиатуры (1 столбец)
↓
E: Преобразование в InlineKeyboardMarkup
↓
F: Возврат InlineKeyboardMarkup
```

Где:

-   `A`: Создание экземпляра `InlineKeyboardBuilder`.
-   `B`: Создание кнопки "⚙️ Админ панель" с callback_data.
-   `C`: Создание кнопки "🏠 На главную" с callback_data.
-   `D`: Расположение кнопок в один столбец.
-   `E`: Преобразование структуры клавиатуры в `InlineKeyboardMarkup`.
-   `F`: Возврат готовой клавиатуры.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Пример использования
keyboard = admin_kb_back()
print(type(keyboard))  # Вывод: <class 'aiogram.types.inline_keyboard.InlineKeyboardMarkup'>
```

### `dell_product_kb`

```python
def dell_product_kb(product_id: int) -> InlineKeyboardMarkup:
    """
    Создает встроенную клавиатуру для подтверждения удаления товара.

    Args:
        product_id (int): ID удаляемого товара.

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "🗑️ Удалить", "⚙️ Админ панель" и "🏠 На главную".
    
    Example:
        dell_product_kb(product_id=123)
    """
    ...
```

**Назначение**:
Создает клавиатуру подтверждения удаления товара с кнопками "Удалить", "Админ панель" и "На главную".

**Параметры**:
- `product_id` (int): ID товара, который будет удален.

**Возвращает**:
- `InlineKeyboardMarkup`: Объект встроенной клавиатуры.

**Как работает функция**:

1.  **Инициализация:** Создается экземпляр `InlineKeyboardBuilder`.
2.  **Кнопка "🗑️ Удалить":** Добавляется кнопка "🗑️ Удалить" с callback_data, содержащим ID товара.
3.  **Кнопка "⚙️ Админ панель":** Добавляется кнопка "⚙️ Админ панель".
4.  **Кнопка "🏠 На главную":** Добавляется кнопка "🏠 На главную".
5.  **Форматирование:** Кнопки располагаются в три ряда: 2, 2 и 1 кнопка.
6.  **Возврат результата:** Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

**ASCII flowchart**:

```
A: Инициализация InlineKeyboardBuilder
↓
B: Создание кнопки "🗑️ Удалить"
↓
C: Создание кнопки "⚙️ Админ панель"
↓
D: Создание кнопки "🏠 На главную"
↓
E: Форматирование клавиатуры (2, 2, 1)
↓
F: Преобразование в InlineKeyboardMarkup
↓
G: Возврат InlineKeyboardMarkup
```

Где:

-   `A`: Создание экземпляра `InlineKeyboardBuilder`.
-   `B`: Создание кнопки "🗑️ Удалить" с callback_data, включающим ID товара.
-   `C`: Создание кнопки "⚙️ Админ панель" с callback_data.
-   `D`: Создание кнопки "🏠 На главную" с callback_data.
-   `E`: Расположение кнопок в три ряда: две кнопки, две кнопки, одна кнопка.
-   `F`: Преобразование структуры клавиатуры в `InlineKeyboardMarkup`.
-   `G`: Возврат готовой клавиатуры.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Пример использования
product_id = 123
keyboard = dell_product_kb(product_id)
print(type(keyboard))  # Вывод: <class 'aiogram.types.inline_keyboard.InlineKeyboardMarkup'>
```

### `product_management_kb`

```python
def product_management_kb() -> InlineKeyboardMarkup:
    """
    Создает встроенную клавиатуру для управления товарами.

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "➕ Добавить товар", "🗑️ Удалить товар", "⚙️ Админ панель" и "🏠 На главную".
    
    Example:
        product_management_kb()
    """
    ...
```

**Назначение**:
Создает клавиатуру для управления товарами с кнопками "Добавить товар", "Удалить товар", "Админ панель" и "На главную".

**Возвращает**:
- `InlineKeyboardMarkup`: Объект встроенной клавиатуры.

**Как работает функция**:

1.  **Инициализация:** Создается экземпляр `InlineKeyboardBuilder`.
2.  **Кнопка "➕ Добавить товар":** Добавляется кнопка "➕ Добавить товар".
3.  **Кнопка "🗑️ Удалить товар":** Добавляется кнопка "🗑️ Удалить товар".
4.  **Кнопка "⚙️ Админ панель":** Добавляется кнопка "⚙️ Админ панель".
5.  **Кнопка "🏠 На главную":** Добавляется кнопка "🏠 На главную".
6.  **Форматирование:** Кнопки располагаются в три ряда: 2, 2 и 1 кнопка.
7.  **Возврат результата:** Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

**ASCII flowchart**:

```
A: Инициализация InlineKeyboardBuilder
↓
B: Создание кнопки "➕ Добавить товар"
↓
C: Создание кнопки "🗑️ Удалить товар"
↓
D: Создание кнопки "⚙️ Админ панель"
↓
E: Создание кнопки "🏠 На главную"
↓
F: Форматирование клавиатуры (2, 2, 1)
↓
G: Преобразование в InlineKeyboardMarkup
↓
H: Возврат InlineKeyboardMarkup
```

Где:

-   `A`: Создание экземпляра `InlineKeyboardBuilder`.
-   `B`: Создание кнопки "➕ Добавить товар" с callback_data.
-   `C`: Создание кнопки "🗑️ Удалить товар" с callback_data.
-   `D`: Создание кнопки "⚙️ Админ панель" с callback_data.
-   `E`: Создание кнопки "🏠 На главную" с callback_data.
-   `F`: Расположение кнопок в три ряда: две кнопки, две кнопки, одна кнопка.
-   `G`: Преобразование структуры клавиатуры в `InlineKeyboardMarkup`.
-   `H`: Возврат готовой клавиатуры.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Пример использования
keyboard = product_management_kb()
print(type(keyboard))  # Вывод: <class 'aiogram.types.inline_keyboard.InlineKeyboardMarkup'>
```

### `cancel_kb_inline`

```python
def cancel_kb_inline() -> InlineKeyboardMarkup:
    """
    Создает встроенную клавиатуру с кнопкой "Отмена".

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопкой "Отмена".
    
    Example:
        cancel_kb_inline()
    """
    ...
```

**Назначение**:
Создает клавиатуру с единственной кнопкой "Отмена".

**Возвращает**:
- `InlineKeyboardMarkup`: Объект встроенной клавиатуры.

**Как работает функция**:

1.  **Инициализация:** Создается экземпляр `InlineKeyboardBuilder`.
2.  **Кнопка "Отмена":** Добавляется кнопка "Отмена".
3.  **Возврат результата:** Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

**ASCII flowchart**:

```
A: Инициализация InlineKeyboardBuilder
↓
B: Создание кнопки "Отмена"
↓
C: Преобразование в InlineKeyboardMarkup
↓
D: Возврат InlineKeyboardMarkup
```

Где:

-   `A`: Создание экземпляра `InlineKeyboardBuilder`.
-   `B`: Создание кнопки "Отмена" с callback_data.
-   `C`: Преобразование структуры клавиатуры в `InlineKeyboardMarkup`.
-   `D`: Возврат готовой клавиатуры.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Пример использования
keyboard = cancel_kb_inline()
print(type(keyboard))  # Вывод: <class 'aiogram.types.inline_keyboard.InlineKeyboardMarkup'>
```

### `admin_confirm_kb`

```python
def admin_confirm_kb() -> InlineKeyboardMarkup:
    """
    Создает встроенную клавиатуру для подтверждения действия администратором.

    Returns:
        InlineKeyboardMarkup: Объект встроенной клавиатуры с кнопками "Все верно" и "Отмена".
    
    Example:
        admin_confirm_kb()
    """
    ...
```

**Назначение**:
Создает клавиатуру подтверждения действия с кнопками "Все верно" и "Отмена".

**Возвращает**:
- `InlineKeyboardMarkup`: Объект встроенной клавиатуры.

**Как работает функция**:

1.  **Инициализация:** Создается экземпляр `InlineKeyboardBuilder`.
2.  **Кнопка "Все верно":** Добавляется кнопка "Все верно".
3.  **Кнопка "Отмена":** Добавляется кнопка "Отмена".
4.  **Форматирование:** Кнопки располагаются в один ряд.
5.  **Возврат результата:** Клавиатура преобразуется в `InlineKeyboardMarkup` и возвращается.

**ASCII flowchart**:

```
A: Инициализация InlineKeyboardBuilder
↓
B: Создание кнопки "Все верно"
↓
C: Создание кнопки "Отмена"
↓
D: Форматирование клавиатуры (1 ряд)
↓
E: Преобразование в InlineKeyboardMarkup
↓
F: Возврат InlineKeyboardMarkup
```

Где:

-   `A`: Создание экземпляра `InlineKeyboardBuilder`.
-   `B`: Создание кнопки "Все верно" с callback_data.
-   `C`: Создание кнопки "Отмена" с callback_data.
-   `D`: Расположение кнопок в один ряд.
-   `E`: Преобразование структуры клавиатуры в `InlineKeyboardMarkup`.
-   `F`: Возврат готовой клавиатуры.

**Примеры**:

```python
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Пример использования
keyboard = admin_confirm_kb()
print(type(keyboard))  # Вывод: <class 'aiogram.types.inline_keyboard.InlineKeyboardMarkup'>