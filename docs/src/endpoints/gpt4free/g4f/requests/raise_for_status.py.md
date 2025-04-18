# Модуль обработки статусов ответов HTTP

## Обзор

Модуль предназначен для обработки HTTP ответов и генерации исключений в зависимости от статуса ответа и его содержимого. Он включает функции для проверки наличия ошибок Cloudflare и OpenAI, а также для генерации соответствующих исключений.

## Подробней

Этот модуль используется для стандартизации обработки ошибок при работе с API, особенно при взаимодействии с сервисами, использующими Cloudflare или OpenAI. Он проверяет статус ответа и его содержимое, чтобы определить, нужно ли генерировать исключение. Если статус указывает на ошибку, модуль генерирует исключение с соответствующим сообщением.

## Функции

### `is_cloudflare`

```python
def is_cloudflare(text: str) -> bool:
    """
    Проверяет, является ли переданный текст ответом Cloudflare.

    Args:
        text (str): Текст ответа, который необходимо проверить.

    Returns:
        bool: `True`, если текст содержит признаки Cloudflare, иначе `False`.

    Как работает функция:
    1. Проверяет наличие подстрок, указывающих на Cloudflare, в переданном тексте.
    2. Если одна из подстрок обнаружена, функция возвращает `True`.
    3. Если ни одна из подстрок не обнаружена, функция возвращает `False`.

    ASCII flowchart:
    Проверка наличия "Generated by cloudfront" или '<p id="cf-spinner-please-wait">' в тексте --> 
    Если да, возврат True -->
    Если нет, проверка наличия "<title>Attention Required! | Cloudflare</title>" или 'id="cf-cloudflare-status"' в тексте -->
    Если да, возврат True -->
    Если нет, проверка наличия '<div id="cf-please-wait">' или "<title>Just a moment...</title>" в тексте -->
    Если да, возврат True -->
    Если нет, возврат False

    Примеры:
    >>> is_cloudflare("Generated by cloudfront")
    True
    >>> is_cloudflare("<title>Attention Required! | Cloudflare</title>")
    True
    >>> is_cloudflare("Some other text")
    False
    """
    ...
```

### `is_openai`

```python
def is_openai(text: str) -> bool:
    """
    Проверяет, является ли переданный текст ответом OpenAI.

    Args:
        text (str): Текст ответа, который необходимо проверить.

    Returns:
        bool: `True`, если текст содержит признаки OpenAI, иначе `False`.

    Как работает функция:
    1. Проверяет наличие подстрок, указывающих на OpenAI, в переданном тексте.
    2. Если одна из подстрок обнаружена, функция возвращает `True`.
    3. Если ни одна из подстрок не обнаружена, функция возвращает `False`.

    ASCII flowchart:
    Проверка наличия "<p>Unable to load site</p>" или 'id="challenge-error-text"' в тексте -->
    Если да, возврат True -->
    Если нет, возврат False

    Примеры:
    >>> is_openai("<p>Unable to load site</p>")
    True
    >>> is_openai("Some other text")
    False
    """
    ...
```

### `raise_for_status_async`

```python
async def raise_for_status_async(response: Union[StreamResponse, ClientResponse], message: str = None):
    """
    Асинхронно проверяет статус ответа и генерирует исключение, если ответ не OK.

    Args:
        response (Union[StreamResponse, ClientResponse]): Объект ответа, который необходимо проверить.
        message (str, optional): Дополнительное сообщение для исключения. По умолчанию `None`.

    Raises:
        MissingAuthError: Если статус ответа 401.
        CloudflareError: Если статус ответа 403 и обнаружен Cloudflare.
        ResponseStatusError: Если статус ответа 403 и обнаружен OpenAI Bot, 502 или любой другой статус, отличный от OK.
        RateLimitError: Если статус ответа 504 или 429/402 (ограничение скорости).

    Как работает функция:
    1. Проверяет, является ли статус ответа OK. Если да, функция завершается.
    2. Если `message` не передано, пытается извлечь сообщение об ошибке из содержимого ответа (JSON или текст).
    3. Если статус ответа 401, генерирует исключение `MissingAuthError`.
    4. Если статус ответа 403 и обнаружен Cloudflare, генерирует исключение `CloudflareError`.
    5. Если статус ответа 403 и обнаружен OpenAI, генерирует исключение `ResponseStatusError`.
    6. Если статус ответа 502, генерирует исключение `ResponseStatusError`.
    7. Если статус ответа 504, генерирует исключение `RateLimitError`.
    8. В остальных случаях генерирует исключение `ResponseStatusError` с сообщением об ошибке.

    ASCII flowchart:
    Начало --> Проверка response.ok --> Если True: Выход --> Если False:
    |
    V
    message is None? --> Да: Получение content_type из headers --> content_type json? --> Да: Извлечение error из json --> Извлечение message из error -->
    |                                                                                                                                         Нет: Получение текста из response --> is_html?
    V
    message is None или is_html? --> Да: response.status == 520? --> Да: message = "Unknown error (Cloudflare)" --> Нет: response.status in (429, 402)? --> Да: message = "Rate limit"
    |
    V
    response.status == 401? --> Да: raise MissingAuthError
    |
    V
    response.status == 403 и is_cloudflare? --> Да: raise CloudflareError
    |
    V
    response.status == 403 и is_openai? --> Да: raise ResponseStatusError
    |
    V
    response.status == 502? --> Да: raise ResponseStatusError
    |
    V
    response.status == 504? --> Да: raise RateLimitError
    |
    V
    raise ResponseStatusError

    Примеры:
    ```python
    # Пример использования требует асинхронного контекста и мокирования response
    # В реальном коде это будет выглядеть примерно так:
    # async with session.get(url) as response:
    #     await raise_for_status_async(response)
    ```
    """
    ...
```

### `raise_for_status`

```python
def raise_for_status(response: Union[Response, StreamResponse, ClientResponse, RequestsResponse], message: str = None):
    """
    Проверяет статус ответа и генерирует исключение, если ответ не OK.

    Args:
        response (Union[Response, StreamResponse, ClientResponse, RequestsResponse]): Объект ответа, который необходимо проверить.
        message (str, optional): Дополнительное сообщение для исключения. По умолчанию `None`.

    Raises:
        MissingAuthError: Если статус ответа 401.
        CloudflareError: Если статус ответа 403 и обнаружен Cloudflare.
        ResponseStatusError: Если статус ответа 403 и обнаружен OpenAI Bot, 502 или любой другой статус, отличный от OK.
        RateLimitError: Если статус ответа 504 или 429/402 (ограничение скорости).

    Как работает функция:
    1. Проверяет наличие атрибута `status` у объекта `response`. Если он есть, вызывает асинхронную функцию `raise_for_status_async` и завершается.
    2. Если статус ответа OK, функция завершается.
    3. Если `message` не передано, пытается извлечь сообщение об ошибке из содержимого ответа (JSON или текст).
    4. Если статус ответа 401, генерирует исключение `MissingAuthError`.
    5. Если статус ответа 403 и обнаружен Cloudflare, генерирует исключение `CloudflareError`.
    6. Если статус ответа 403 и обнаружен OpenAI, генерирует исключение `ResponseStatusError`.
    7. Если статус ответа 502, генерирует исключение `ResponseStatusError`.
    8. Если статус ответа 504 или 429/402 (ограничение скорости), генерирует исключение `RateLimitError`.
    9. В остальных случаях генерирует исключение `ResponseStatusError` с сообщением об ошибке.

    ASCII flowchart:
    Начало --> hasattr(response, "status")? --> Да: raise_for_status_async(response, message) --> Выход
    |                                      Нет: response.ok? --> Да: Выход
    V                                                               Нет: message is None? --> Да: is_html? --> Получение message из response
    is_html или message is None? --> Да: response.status_code == 520? --> Да: message = "Unknown error (Cloudflare)"
    |                                                                      Нет: response.status_code in (429, 402)? --> Да: raise RateLimitError
    V
    response.status_code == 401? --> Да: raise MissingAuthError
    |
    V
    response.status_code == 403 и is_cloudflare? --> Да: raise CloudflareError
    |
    V
    response.status_code == 403 и is_openai? --> Да: raise ResponseStatusError
    |
    V
    response.status_code == 502? --> Да: raise ResponseStatusError
    |
    V
    response.status_code == 504? --> Да: raise RateLimitError
    |
    V
    raise ResponseStatusError

    Примеры:
    ```python
    # Пример использования требует мокирования response
    # В реальном коде это будет выглядеть примерно так:
    # response = requests.get(url)
    # raise_for_status(response)
    ```
    """
    ...
```

## Классы

### `CloudflareError`

```python
class CloudflareError(ResponseStatusError):
    """
    Исключение, которое выбрасывается, когда обнаружена защита Cloudflare.

    Inherits:
        ResponseStatusError: Наследует от класса `ResponseStatusError`.
    """
    ...