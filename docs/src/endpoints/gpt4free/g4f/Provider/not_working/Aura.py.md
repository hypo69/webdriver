# Модуль Aura

## Обзор

Модуль предоставляет асинхронный генератор для взаимодействия с моделью Aura, доступной через API `openchat.team`. Он позволяет отправлять сообщения и получать ответы в виде чанков, используя асинхронные запросы.

## Подробней

Этот модуль предназначен для интеграции с сервисом Aura, предоставляющим доступ к модели OpenChat 3.6. Он использует `aiohttp` для асинхронных запросов и предоставляет удобный интерфейс для отправки сообщений и получения ответов в виде генератора.

## Классы

### `Aura`

**Описание**: Класс `Aura` является провайдером асинхронного генератора для работы с API `openchat.team`.

**Наследует**:
- `AsyncGeneratorProvider`: Наследует функциональность асинхронного генератора.

**Атрибуты**:
- `url` (str): URL для API `openchat.team`.
- `working` (bool): Указывает, работает ли провайдер (в данном случае `False`).

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    temperature: float = 0.5,
    max_tokens: int = 8192,
    webdriver = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с API Aura.

    Args:
        model (str): Не используется, указан для совместимости с интерфейсом.
        messages (Messages): Список сообщений для отправки в API.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        temperature (float, optional): Температура для генерации текста. По умолчанию `0.5`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию `8192`.
        webdriver: Веб-драйвер для выполнения запросов (не используется в коде).
        **kwargs: Дополнительные аргументы (не используются в коде).

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий чанки текста из API.

    Raises:
        Exception: Если возникает ошибка при выполнении запроса к API.

    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API Aura.

**Параметры**:
- `cls`: Ссылка на класс.
- `model` (str): Не используется, указан для совместимости с интерфейсом.
- `messages` (Messages): Список сообщений для отправки в API.
- `proxy` (str, optional): Прокси-сервер для использования. По умолчанию `None`.
- `temperature` (float, optional): Температура для генерации текста. По умолчанию `0.5`.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию `8192`.
- `webdriver`: Веб-драйвер для выполнения запросов (не используется в коде).
- `**kwargs`: Дополнительные аргументы (не используются в коде).

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий чанки текста из API.

**Вызывает исключения**:
- `aiohttp.ClientError`: Если возникает ошибка при выполнении запроса к API.

**Как работает функция**:
1. Извлекает аргументы для сессии `aiohttp` с использованием `get_args_from_browser` (предположительно, функция не определена в данном коде).
2. Создает асинхронную сессию `aiohttp.ClientSession` с переданными аргументами.
3. Разделяет входные сообщения на системные и обычные сообщения.
4. Формирует данные для отправки в API, включая модель, сообщения, ключ, системное сообщение и температуру.
5. Отправляет POST-запрос к API `openchat.team` с сформированными данными.
6. Итерируется по чанкам в ответе и декодирует каждый чанк, используя кодировку `error="ignore"`.
7. Возвращает асинхронный генератор, который выдает декодированные чанки.

**Внутренние функции**: Нет.

```
A -- get_args_from_browser --> B
|
C
|
D
|
E
|
F
```

Где:
- `A`: Получение аргументов для сессии aiohttp.
- `B`: Создание асинхронной сессии aiohttp.
- `C`: Разделение сообщений на системные и обычные.
- `D`: Формирование данных для отправки в API.
- `E`: Отправка POST-запроса к API.
- `F`: Итерация по чанкам в ответе и декодирование.

**Примеры**:

```python
# Пример использования (требует реализации get_args_from_browser и AsyncResult)
# async def example():
#     messages = [{"role": "user", "content": "Hello, world!"}]
#     async for chunk in Aura.create_async_generator(model="openchat_3.6", messages=messages):
#         print(chunk, end="")

# asyncio.run(example())