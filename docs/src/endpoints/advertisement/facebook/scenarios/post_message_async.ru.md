# Документация модуля `src.endpoints.advertisement.facebook.post_message_async`

## Обзор

Этот модуль, расположенный в директории `hypotez/src/endpoints/advertisement/facebook/scenarios`, предназначен для автоматизации процесса публикации сообщений на Facebook. Он позволяет программно взаимодействовать со страницей Facebook для выполнения задач, таких как отправка текста, загрузка медиафайлов и обновление подписей к ним.

## Подробнее

Модуль автоматизирует процесс создания рекламных постов в Facebook, начиная с отправки заголовка и описания, заканчивая загрузкой медиафайлов и продвижением поста. Он использует веб-драйвер для эмуляции действий пользователя в браузере, что позволяет автоматизировать рутинные операции и повысить эффективность рекламных кампаний.

## Содержание

1.  [Функции](#Функции)
    *   [post_title](#post_title)
    *   [upload_media](#upload_media)
    *   [update_images_captions](#update_images_captions)
    *   [promote_post](#promote_post)

## Функции

### `post_title`

```python
def post_title(d: Driver, category: SimpleNamespace) -> bool:
    """
    Отправляет заголовок и описание кампании в поле сообщения на Facebook.

    Args:
        d (Driver): Экземпляр `Driver` для взаимодействия с веб-страницей.
        category (SimpleNamespace): Категория, содержащая заголовок и описание для отправки.

    Returns:
        bool: `True`, если заголовок и описание были успешно отправлены, иначе `None`.
    """
    ...
```

**Назначение**: Отправляет заголовок и описание рекламной кампании в поле сообщения на странице Facebook.

**Параметры**:
*   `d` (Driver): Экземпляр класса `Driver`, используемый для управления веб-браузером и взаимодействия с элементами страницы Facebook.
*   `category` (SimpleNamespace): Объект, содержащий атрибуты `title` (заголовок) и `description` (описание) для публикации.

**Возвращает**:
*   `bool`: Возвращает `True`, если заголовок и описание успешно отправлены. В случае неудачи возвращает `None`.

**Как работает функция**:

1.  Функция получает экземпляр драйвера и объект категории с данными для публикации.
2.  Используя методы драйвера, функция находит поле для ввода сообщения на странице Facebook.
3.  Функция вводит заголовок и описание в поле сообщения.
4.  Функция проверяет успешность отправки сообщения и возвращает соответствующее логическое значение.

**ASCII Flowchart**:

```
Начало
|
Получение экземпляра драйвера и объекта категории
|
Находит поле для ввода сообщения на странице Facebook
|
Вводит заголовок в поле сообщения
|
Вводит описание в поле сообщения
|
Проверяет успешность отправки сообщения
|
Конец (возвращает True или None)
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Инициализация Driver (пример)
driver = Driver(browser_name="chrome")

# Создание объекта category
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")

# Вызов функции
result = post_title(driver, category)
print(result)  # Вывод: True или None
```

### `upload_media`

```python
def upload_media(d: Driver, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Загружает медиафайлы на пост Facebook и обновляет их подписи.

    Args:
        d (Driver): Экземпляр `Driver` для взаимодействия с веб-страницей.
        products (List[SimpleNamespace]): Список продуктов, содержащих пути к медиафайлам.
        no_video (bool, optional): Флаг, указывающий, следует ли пропустить загрузку видео. По умолчанию `False`.

    Returns:
        bool: `True`, если медиафайлы были успешно загружены, иначе `None`.
    """
    ...
```

**Назначение**: Загружает медиафайлы (изображения и видео) на пост в Facebook.

**Параметры**:

*   `d` (Driver): Экземпляр класса `Driver`, используемый для управления веб-браузером и взаимодействия с элементами страницы Facebook.
*   `products` (List[SimpleNamespace]): Список объектов, каждый из которых содержит информацию о продукте, включая пути к медиафайлам.
*   `no_video` (bool, optional): Флаг, указывающий, нужно ли пропускать загрузку видео. По умолчанию `False`.

**Возвращает**:

*   `bool`: Возвращает `True`, если медиафайлы успешно загружены. В случае неудачи возвращает `None`.

**Как работает функция**:

1.  Функция получает экземпляр драйвера, список продуктов и флаг пропуска видео.
2.  Используя методы драйвера, функция находит элементы для загрузки медиафайлов на странице Facebook.
3.  Для каждого продукта функция загружает соответствующие медиафайлы (изображения и видео).
4.  Функция проверяет успешность загрузки каждого файла и возвращает соответствующее логическое значение.

**ASCII Flowchart**:

```
Начало
|
Получение экземпляра драйвера, списка продуктов и флага пропуска видео
|
Находит элементы для загрузки медиафайлов на странице Facebook
|
Для каждого продукта:
    |
    Загружает медиафайлы (изображения и видео)
    |
    Проверяет успешность загрузки каждого файла
|
Конец (возвращает True или None)
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Инициализация Driver (пример)
driver = Driver(browser_name="chrome")

# Создание списка products
products = [
    SimpleNamespace(local_image_path="путь/к/изображению1.jpg"),
    SimpleNamespace(local_image_path="путь/к/изображению2.jpg"),
    SimpleNamespace(local_video_path="путь/к/видео.mp4")
]

# Вызов функции
result = upload_media(driver, products)
print(result)  # Вывод: True или None

# Вызов функции с флагом пропуска видео
result = upload_media(driver, products, no_video=True)
print(result)  # Вывод: True или None
```

### `update_images_captions`

```python
def update_images_captions(d: Driver, products: List[SimpleNamespace], textarea_list: List[WebElement]) -> None:
    """
    Асинхронно добавляет описания к загруженным медиафайлам.

    Args:
        d (Driver): Экземпляр `Driver` для взаимодействия с веб-страницей.
        products (List[SimpleNamespace]): Список продуктов с деталями для обновления.
        textarea_list (List[WebElement]): Список текстовых полей, куда добавляются подписи.
    """
    ...
```

**Назначение**: Добавляет подписи к загруженным медиафайлам на посте в Facebook.

**Параметры**:

*   `d` (Driver): Экземпляр класса `Driver`, используемый для управления веб-браузером и взаимодействия с элементами страницы Facebook.
*   `products` (List[SimpleNamespace]): Список объектов, каждый из которых содержит информацию о продукте, включая текст подписи.
*   `textarea_list` (List[WebElement]): Список элементов `textarea`, в которые нужно добавить подписи.

**Возвращает**:

*   `None`: Функция ничего не возвращает.

**Как работает функция**:

1.  Функция получает экземпляр драйвера, список продуктов и список текстовых полей.
2.  Для каждого продукта функция находит соответствующее текстовое поле в списке.
3.  Функция добавляет текст подписи продукта в текстовое поле.
4.  Функция выполняет асинхронную операцию для обновления подписи на странице Facebook.

**ASCII Flowchart**:

```
Начало
|
Получение экземпляра драйвера, списка продуктов и списка текстовых полей
|
Для каждого продукта:
    |
    Находит соответствующее текстовое поле
    |
    Добавляет текст подписи продукта в текстовое поле
    |
    Выполняет асинхронную операцию для обновления подписи
|
Конец
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace
from selenium.webdriver.remote.webelement import WebElement

# Инициализация Driver (пример)
driver = Driver(browser_name="chrome")

# Создание списка products
products = [
    SimpleNamespace(caption="Подпись к изображению 1"),
    SimpleNamespace(caption="Подпись к изображению 2")
]

# Создание списка textarea_list (пример - необходимо получить реальные элементы со страницы)
textarea_list = [
    WebElement(None, None, None),
    WebElement(None, None, None)
]

# Вызов функции
update_images_captions(driver, products, textarea_list)
```

### `promote_post`

```python
def promote_post(d: Driver, category: SimpleNamespace, products: List[SimpleNamespace], no_video: bool = False) -> bool:
    """
    Управляет процессом продвижения поста с заголовком, описанием и медиафайлами.

    Args:
        d (Driver): Экземпляр `Driver` для взаимодействия с веб-страницей.
        category (SimpleNamespace): Детали категории, используемые для заголовка и описания поста.
        products (List[SimpleNamespace]): Список продуктов, содержащих медиа и детали для публикации.
        no_video (bool, optional): Флаг, указывающий, следует ли пропустить загрузку видео. По умолчанию `False`.

    Returns:
        bool: `True`, если пост был успешно продвинут, иначе `None`.
    """
    ...
```

**Назначение**: Управляет всем процессом продвижения поста, включая отправку заголовка, загрузку медиафайлов и обновление подписей.

**Параметры**:

*   `d` (Driver): Экземпляр класса `Driver`, используемый для управления веб-браузером и взаимодействия с элементами страницы Facebook.
*   `category` (SimpleNamespace): Объект, содержащий информацию о категории поста, включая заголовок и описание.
*   `products` (List[SimpleNamespace]): Список объектов, каждый из которых содержит информацию о продукте, включая медиафайлы и подписи.
*   `no_video` (bool, optional): Флаг, указывающий, нужно ли пропускать загрузку видео. По умолчанию `False`.

**Возвращает**:

*   `bool`: Возвращает `True`, если пост был успешно продвинут. В случае неудачи возвращает `None`.

**Как работает функция**:

1.  Функция получает экземпляр драйвера, объект категории, список продуктов и флаг пропуска видео.
2.  Функция вызывает функцию `post_title` для отправки заголовка и описания поста.
3.  Функция вызывает функцию `upload_media` для загрузки медиафайлов.
4.  Функция вызывает функцию `update_images_captions` для добавления подписей к медиафайлам.
5.  Функция выполняет действия для завершения процесса продвижения поста на странице Facebook.
6.  Функция проверяет успешность продвижения поста и возвращает соответствующее логическое значение.

**ASCII Flowchart**:

```
Начало
|
Получение экземпляра драйвера, объекта категории, списка продуктов и флага пропуска видео
|
Вызывает функцию post_title для отправки заголовка и описания
|
Вызывает функцию upload_media для загрузки медиафайлов
|
Вызывает функцию update_images_captions для добавления подписей
|
Выполняет действия для завершения процесса продвижения поста
|
Проверяет успешность продвижения поста
|
Конец (возвращает True или None)
```

**Примеры**:

```python
from src.webdriver.driver import Driver
from types import SimpleNamespace

# Инициализация Driver (пример)
driver = Driver(browser_name="chrome")

# Создание объекта category
category = SimpleNamespace(title="Заголовок кампании", description="Описание кампании")

# Создание списка products
products = [
    SimpleNamespace(local_image_path="путь/к/изображению1.jpg", caption="Подпись к изображению 1"),
    SimpleNamespace(local_image_path="путь/к/изображению2.jpg", caption="Подпись к изображению 2")
]

# Вызов функции
result = promote_post(driver, category, products)
print(result)  # Вывод: True или None

# Вызов функции с флагом пропуска видео
result = promote_post(driver, category, products, no_video=True)
print(result)  # Вывод: True или None
```