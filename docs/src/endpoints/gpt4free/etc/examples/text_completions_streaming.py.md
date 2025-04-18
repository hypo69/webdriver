# Модуль для демонстрации потоковой передачи текста с использованием g4f

## Обзор

Этот модуль демонстрирует, как использовать библиотеки `g4f` для выполнения потоковой передачи текста как в синхронном, так и в асинхронном режимах. Он включает в себя функции для настройки клиентов, отправки запросов к модели gpt-4 и обработки полученных результатов.

## Подробнее

Модуль предназначен для демонстрации возможностей потоковой передачи текста с использованием `gpt-4` через библиотеку `g4f`. Он показывает, как можно отправлять запросы к модели и получать ответы в виде потока данных, что позволяет отображать текст в реальном времени. Это полезно для создания интерактивных приложений, требующих немедленного отображения генерируемого текста.

## Функции

### `sync_stream`

```python
def sync_stream():
    """
    Функция выполняет синхронный запрос к gpt-4 для потоковой передачи текста.

    Функция создает клиент `g4f.client.Client`, отправляет запрос к модели gpt-4 и выводит полученные чанки текста в консоль.

    Raises:
        Exception: Если возникает ошибка при создании потока или обработке чанков.

    Как работает функция:
    1. Создается экземпляр класса `Client`.
    2. Вызывается метод `chat.completions.create` с параметрами:
       - `model`: "gpt-4" - указывает на использование модели gpt-4.
       - `messages`: список сообщений, содержащих роль и контент запроса.
       - `stream`: `True` - включает режим потоковой передачи.
    3. В цикле перебираются чанки потока, и каждый чанк обрабатывается:
       - Проверяется наличие содержимого в `chunk.choices[0].delta.content`.
       - Если содержимое есть, оно выводится в консоль без добавления новой строки в конце.

    ASCII flowchart:

    Создание клиента
    ↓
    Отправка запроса к gpt-4 в режиме потоковой передачи
    ↓
    Получение чанка
    ↓
    Проверка наличия содержимого в чанке
    ↓
    Вывод содержимого в консоль

    Примеры:
        >>> sync_stream()
        Привет! Вот как можно рекурсивно перечислить все файлы в каталоге в Python:
        <ответ gpt-4>
    """
    ...
```

### `async_stream`

```python
async def async_stream():
    """
    Функция выполняет асинхронный запрос к gpt-4 для потоковой передачи текста.

    Функция создает асинхронный клиент `g4f.client.AsyncClient`, отправляет запрос к модели gpt-4 и выводит полученные чанки текста в консоль.

    Raises:
        Exception: Если возникает ошибка при создании потока или обработке чанков.

    Как работает функция:
    1. Создается экземпляр класса `AsyncClient`.
    2. Вызывается метод `chat.completions.create` с параметрами:
       - `model`: "gpt-4" - указывает на использование модели gpt-4.
       - `messages`: список сообщений, содержащих роль и контент запроса.
       - `stream`: `True` - включает режим потоковой передачи.
    3. В асинхронном цикле перебираются чанки потока, и каждый чанк обрабатывается:
       - Проверяется наличие содержимого в `chunk.choices[0].delta.content`.
       - Если содержимое есть, оно выводится в консоль без добавления новой строки в конце.

    ASCII flowchart:

    Создание асинхронного клиента
    ↓
    Отправка асинхронного запроса к gpt-4 в режиме потоковой передачи
    ↓
    Получение чанка
    ↓
    Проверка наличия содержимого в чанке
    ↓
    Вывод содержимого в консоль

    Примеры:
        >>> asyncio.run(async_stream())
        Привет! Вот как можно рекурсивно перечислить все файлы в каталоге в Python:
        <ответ gpt-4>
    """
    ...
```

### `main`

```python
def main():
    """
    Главная функция для запуска синхронного и асинхронного потоков.

    Функция вызывает `sync_stream` для выполнения синхронной потоковой передачи и `async_stream` для выполнения асинхронной потоковой передачи.
    Она выводит заголовки для каждого потока, чтобы разделить их вывод в консоли.

    Как работает функция:
    1. Выводит в консоль заголовок "Synchronous Stream:".
    2. Вызывает функцию `sync_stream()` для выполнения синхронной потоковой передачи.
    3. Выводит в консоль разделитель строк "\\n\\nAsynchronous Stream:".
    4. Вызывает функцию `asyncio.run(async_stream())` для выполнения асинхронной потоковой передачи.

    ASCII flowchart:

    Вывод заголовка "Synchronous Stream:"
    ↓
    Вызов sync_stream()
    ↓
    Вывод разделителя
    ↓
    Вывод заголовка "Asynchronous Stream:"
    ↓
    Вызов asyncio.run(async_stream())

    Примеры:
        >>> main()
        Synchronous Stream:
        <ответ gpt-4 в синхронном режиме>

        Asynchronous Stream:
        <ответ gpt-4 в асинхронном режиме>
    """
    ...