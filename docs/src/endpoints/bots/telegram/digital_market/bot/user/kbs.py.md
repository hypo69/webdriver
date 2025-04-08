# Модуль для формирования клавиатур Telegram-бота цифрового рынка
==================================================================

Модуль содержит функции для создания различных типов клавиатур, используемых в Telegram-боте цифрового рынка.
Клавиатуры формируются с использованием библиотеки `aiogram` и предназначены для навигации по каталогу,
отображения информации о магазине, совершения покупок и управления профилем пользователя.

## Обзор

Модуль предоставляет набор функций для создания инлайн-клавиатур, которые позволяют пользователям взаимодействовать с ботом,
выбирать категории товаров, совершать покупки и переходить в другие разделы бота.

## Подробнее

Этот модуль играет важную роль в обеспечении удобной навигации и пользовательского опыта в Telegram-боте цифрового рынка.
Он содержит функции для создания клавиатур главного меню, каталога товаров, профиля пользователя и других разделов бота.
Клавиатуры создаются с использованием библиотеки `aiogram` и содержат кнопки с различными действиями, такими как переход
в каталог, отображение информации о магазине, совершение покупок и т.д.

## Функции

### `main_user_kb`

```python
def main_user_kb(user_id: int) -> InlineKeyboardMarkup:
    """
    Создает главную клавиатуру пользователя с кнопками: "Мои покупки", "Каталог", "О магазине", "Поддержать автора" и "Админ панель" (если пользователь является администратором).

    Args:
        user_id (int): ID пользователя.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    Как работает функция:
    1. Инициализирует построитель инлайн-клавиатуры `kb`.
    2. Добавляет кнопки "👤 Мои покупки", "🛍 Каталог", "ℹ️ О магазине", "🌟 Поддержать автора 🌟" с соответствующими callback_data и URL.
    3. Проверяет, является ли `user_id` администратором (присутствует ли он в `settings.ADMIN_IDS`). Если да, добавляет кнопку "⚙️ Админ панель".
    4. Настраивает расположение кнопок в один столбец.
    5. Преобразует построитель клавиатуры в объект `InlineKeyboardMarkup` и возвращает его.

    Блоки функции:

    A - Создание кнопок основного меню
    |
    B - Проверка, является ли пользователь администратором
    |
    C - Добавление кнопки "Админ панель" (если пользователь - администратор)
    |
    D - Формирование клавиатуры
    |
    E - Возврат сформированной клавиатуры

    ```
    A
    |
    B --> C?
    |       |
    |       D
    |
    E
    ```

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> user_id = 12345
        >>> keyboard = main_user_kb(user_id)
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    ...
```

### `catalog_kb`

```python
def catalog_kb(catalog_data: List[Category]) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру каталога с кнопками для каждой категории и кнопкой "На главную".

    Args:
        catalog_data (List[Category]): Список объектов категорий.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    Как работает функция:
    1. Инициализирует построитель инлайн-клавиатуры `kb`.
    2. Перебирает список категорий `catalog_data` и для каждой категории добавляет кнопку с названием категории и callback_data в формате "category_{category.id}".
    3. Добавляет кнопку "🏠 На главную" с callback_data "home".
    4. Настраивает расположение кнопок в два столбца.
    5. Преобразует построитель клавиатуры в объект `InlineKeyboardMarkup` и возвращает его.

    Блоки функции:

    A - Инициализация клавиатуры
    |
    B - Добавление кнопок категорий
    |
    C - Добавление кнопки "На главную"
    |
    D - Формирование клавиатуры
    |
    E - Возврат сформированной клавиатуры

    ```
    A
    |
    B
    |
    C
    |
    D
    |
    E
    ```
    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> catalog_data = [Category(id=1, category_name='Category 1'), Category(id=2, category_name='Category 2')]
        >>> keyboard = catalog_kb(catalog_data)
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    ...
```

### `purchases_kb`

```python
def purchases_kb() -> InlineKeyboardMarkup:
    """
    Создает клавиатуру раздела покупок с кнопками: "Смотреть покупки" и "На главную".

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    Как работает функция:
    1. Инициализирует построитель инлайн-клавиатуры `kb`.
    2. Добавляет кнопки "🗑 Смотреть покупки" и "🏠 На главную" с соответствующими callback_data.
    3. Настраивает расположение кнопок в один столбец.
    4. Преобразует построитель клавиатуры в объект `InlineKeyboardMarkup` и возвращает его.

    Блоки функции:

    A - Создание клавиатуры
    |
    B - Добавление кнопки просмотра покупок
    |
    C - Добавление кнопки "На главную"
    |
    D - Формирование клавиатуры
    |
    E - Возврат сформированной клавиатуры

    ```
    A
    |
    B
    |
    C
    |
    D
    |
    E
    ```

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> keyboard = purchases_kb()
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    ...
```

### `product_kb`

```python
def product_kb(product_id, price, stars_price) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру товара с кнопками для оплаты через ЮКасса, Robocassa и звездами, а также кнопками "Назад" и "На главную".

    Args:
        product_id: ID товара.
        price: Цена товара.
        stars_price: Цена товара в звездах.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    Как работает функция:
    1. Инициализирует построитель инлайн-клавиатуры `kb`.
    2. Добавляет кнопки для оплаты через ЮКасса, Robocassa и звездами с соответствующими callback_data.
    3. Добавляет кнопки "🛍 Назад" и "🏠 На главную" с соответствующими callback_data.
    4. Настраивает расположение кнопок в два столбца.
    5. Преобразует построитель клавиатуры в объект `InlineKeyboardMarkup` и возвращает его.

    Блоки функции:

    A - Создание клавиатуры
    |
    B - Добавление кнопок оплаты
    |
    C - Добавление кнопок навигации
    |
    D - Формирование клавиатуры
    |
    E - Возврат сформированной клавиатуры

    ```
    A
    |
    B
    |
    C
    |
    D
    |
    E
    ```
   Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> product_id = 123
        >>> price = 100
        >>> stars_price = 50
        >>> keyboard = product_kb(product_id, price, stars_price)
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    ...
```

### `get_product_buy_youkassa`

```python
def get_product_buy_youkassa(price) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для оплаты товара через ЮКасса.

    Args:
        price: Цена товара.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    Как работает функция:
    1. Создает `InlineKeyboardMarkup` с двумя кнопками:
        - Кнопка "Оплатить {price}₽" с установленным параметром `pay=True`, что указывает на необходимость оплаты.
        - Кнопка "Отменить" с `callback_data='home'`, возвращающая пользователя на главную страницу.
    2. Возвращает созданную клавиатуру.

    Блоки функции:
    A - Создание кнопки оплаты
    |
    B - Создание кнопки отмены
    |
    C - Формирование клавиатуры
    |
    D - Возврат клавиатуры

    ```
    A
    |
    B
    |
    C
    |
    D
    ```

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> price = 100
        >>> keyboard = get_product_buy_youkassa(price)
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    ...
```

### `get_product_buy_robocassa`

```python
def get_product_buy_robocassa(price: int, payment_link: str) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для оплаты товара через Robocassa.

    Args:
        price (int): Цена товара.
        payment_link (str): Ссылка для оплаты.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    Как работает функция:
    1. Создает `InlineKeyboardMarkup` с двумя кнопками:
        - Кнопка "Оплатить {price}₽" с использованием `WebAppInfo` для перенаправления пользователя по ссылке `payment_link` в веб-приложение Robocassa.
        - Кнопка "Отменить" с `callback_data='home'`, возвращающая пользователя на главную страницу.
    2. Возвращает созданную клавиатуру.

    Блоки функции:

    A - Создание кнопки оплаты с ссылкой на Robocassa
    |
    B - Создание кнопки отмены
    |
    C - Формирование клавиатуры
    |
    D - Возврат клавиатуры

    ```
    A
    |
    B
    |
    C
    |
    D
    ```

    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> price = 100
        >>> payment_link = 'https://example.com/robocassa'
        >>> keyboard = get_product_buy_robocassa(price, payment_link)
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    ...
```

### `get_product_buy_stars`

```python
def get_product_buy_stars(price) -> InlineKeyboardMarkup:
    """
    Создает клавиатуру для оплаты товара звездами.

    Args:
        price: Цена товара в звездах.

    Returns:
        InlineKeyboardMarkup: Объект инлайн-клавиатуры.

    Как работает функция:
    1. Создает `InlineKeyboardMarkup` с двумя кнопками:
        - Кнопка "Оплатить {price} ⭐" с установленным параметром `pay=True`, что указывает на необходимость оплаты.
        - Кнопка "Отменить" с `callback_data='home'`, возвращающая пользователя на главную страницу.
    2. Возвращает созданную клавиатуру.

    Блоки функции:

    A - Создание кнопки оплаты звездами
    |
    B - Создание кнопки отмены
    |
    C - Формирование клавиатуры
    |
    D - Возврат клавиатуры

    ```
    A
    |
    B
    |
    C
    |
    D
    ```
    Примеры:
        >>> from aiogram.types import InlineKeyboardMarkup
        >>> price = 50
        >>> keyboard = get_product_buy_stars(price)
        >>> assert isinstance(keyboard, InlineKeyboardMarkup)
    """
    ...