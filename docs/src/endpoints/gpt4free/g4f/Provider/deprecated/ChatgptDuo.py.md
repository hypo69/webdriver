# Модуль ChatgptDuo

## Обзор

Модуль `ChatgptDuo` предоставляет асинхронный интерфейс для взаимодействия с моделью ChatGPT Duo через веб-сайт `chatgptduo.com`. Он позволяет отправлять запросы к модели и получать ответы, а также извлекать источники, использованные для формирования ответа. Этот модуль является частью пакета `g4f.Provider.deprecated` и предоставляет функциональность, аналогичную другим провайдерам в данном пакете. Модуль поддерживает модель `gpt-3.5-turbo`.

## Подробней

Модуль `ChatgptDuo` предоставляет класс `ChatgptDuo`, который наследуется от `AsyncProvider`. Он использует библиотеку `httpx` для выполнения асинхронных HTTP-запросов. Модуль предназначен для использования в асинхронных приложениях, где требуется взаимодействие с ChatGPT Duo.
Пример использования:
```python
messages = [{"role": "user", "content": "Hello, ChatGPT Duo!"}]
response = await ChatgptDuo.create_async(model="gpt-3.5-turbo", messages=messages)
print(response)
```

## Классы

### `ChatgptDuo`

**Описание**: Класс `ChatgptDuo` предоставляет асинхронный интерфейс для взаимодействия с моделью ChatGPT Duo.

**Наследует**:
- `AsyncProvider`: Наследует от `AsyncProvider`, что позволяет использовать общую логику для работы с различными провайдерами.

**Атрибуты**:
- `url` (str): URL веб-сайта ChatGPT Duo (`https://chatgptduo.com`).
- `supports_gpt_35_turbo` (bool): Указывает, поддерживает ли провайдер модель `gpt-3.5-turbo` (`True`).
- `working` (bool): Указывает, работает ли провайдер в данный момент (`False`).
- `_sources` (list): Список источников, используемых для формирования ответа (инициализируется как пустой список).

**Методы**:
- `create_async`: Асинхронный метод для отправки запроса к модели ChatGPT Duo и получения ответа.
- `get_sources`: Метод для получения списка источников, использованных для формирования ответа.

## Функции

### `create_async`

```python
@classmethod
async def create_async(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    timeout: int = 120,
    **kwargs
) -> str:
    """
    Асинхронно отправляет запрос к модели ChatGPT Duo и возвращает ответ.

    Args:
        model (str): Имя модели для использования.
        messages (Messages): Список сообщений для отправки в запросе.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания запроса в секундах. По умолчанию `120`.
        **kwargs: Дополнительные аргументы.

    Returns:
        str: Ответ от модели ChatGPT Duo.

    Raises:
        httpx.HTTPStatusError: Если возникает HTTP-ошибка при выполнении запроса.

    """
```

**Назначение**: Асинхронная функция `create_async` отправляет запрос к модели ChatGPT Duo и возвращает ответ.

**Параметры**:
- `cls`: Ссылка на класс `ChatgptDuo`.
- `model` (str): Имя модели для использования.
- `messages` (Messages): Список сообщений для отправки в запросе.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `timeout` (int, optional): Время ожидания запроса в секундах. По умолчанию `120`.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `str`: Ответ от модели ChatGPT Duo.

**Вызывает исключения**:
- `httpx.HTTPStatusError`: Если возникает HTTP-ошибка при выполнении запроса.

**Как работает функция**:

1. **Инициализация сессии**: Функция создает асинхронную сессию `StreamSession` с указанием `impersonate="chrome107"`, настройками прокси и времени ожидания.
2. **Форматирование запроса**: Функция форматирует список сообщений `messages` с использованием функции `format_prompt`.
3. **Подготовка данных**: Подготавливает данные для отправки в запросе, включая `prompt`, `search` и `purpose`.
4. **Отправка запроса**: Отправляет POST-запрос к URL `cls.url` с подготовленными данными.
5. **Обработка ответа**: Обрабатывает ответ от сервера, извлекая JSON-данные и список источников `results`.
6. **Извлечение источников**: Извлекает список источников из данных ответа и сохраняет их в атрибуте `_sources` класса.
7. **Возврат ответа**: Возвращает текст ответа из поля `answer` в JSON-данных.

**ASCII Flowchart**:

```
A: Инициализация асинхронной сессии StreamSession
|
B: Форматирование списка сообщений messages -> prompt
|
C: Подготовка данных для запроса (prompt, search, purpose)
|
D: Отправка POST-запроса к cls.url с данными
|
E: Обработка ответа от сервера (извлечение JSON)
|
F: Извлечение списка источников results -> _sources
|
G: Возврат текста ответа answer
```

**Примеры**:

```python
messages = [{"role": "user", "content": "Hello, ChatGPT Duo!"}]
response = await ChatgptDuo.create_async(model="gpt-3.5-turbo", messages=messages)
print(response)

messages = [{"role": "user", "content": "Tell me a joke."}]
response = await ChatgptDuo.create_async(model="gpt-3.5-turbo", messages=messages, proxy="http://proxy.example.com")
print(response)
```

### `get_sources`

```python
@classmethod
def get_sources(cls):
    """
    Возвращает список источников, использованных для формирования ответа.

    Returns:
        list: Список источников.
    """
```

**Назначение**: Возвращает список источников, использованных для формирования ответа.

**Параметры**:
- `cls`: Ссылка на класс `ChatgptDuo`.

**Возвращает**:
- `list`: Список источников.

**Как работает функция**:

Функция возвращает значение атрибута `_sources`, который содержит список источников, извлеченных из ответа ChatGPT Duo.

**Примеры**:

```python
sources = ChatgptDuo.get_sources()
print(sources)