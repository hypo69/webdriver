# Модуль `AmigoChat.py`

## Обзор

Модуль `AmigoChat.py` предоставляет реализацию асинхронного генератора для взаимодействия с сервисом AmigoChat. Он включает поддержку как текстовых запросов (chat), так и запросов на генерацию изображений (image). Модуль определяет модели, используемые для взаимодействия с API AmigoChat, и предоставляет методы для создания асинхронных генераторов, отправки запросов и обработки ответов.

## Подробнее

Модуль предназначен для интеграции с другими частями проекта `hypotez`, где требуется взаимодействие с AmigoChat для генерации текста или изображений. Он использует асинхронные запросы для эффективной обработки данных и предоставляет удобные методы для работы с API AmigoChat. В модуле реализована поддержка стриминга ответов для текстовых запросов и обработки ответов, содержащих URL-адреса изображений для запросов на генерацию изображений. Также модуль содержит обработку ошибок и повторные попытки при возникновении проблем с запросами.

## Классы

### `AmigoChat`

**Описание**: Класс `AmigoChat` предоставляет методы для взаимодействия с API AmigoChat, включая генерацию текста и изображений.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает поддержку асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `url` (str): Базовый URL сервиса AmigoChat (`https://amigochat.io/chat/`).
- `chat_api_endpoint` (str): URL для отправки запросов на генерацию текста (`https://api.amigochat.io/v1/chat/completions`).
- `image_api_endpoint` (str): URL для отправки запросов на генерацию изображений (`https://api.amigochat.io/v1/images/generations`).
- `working` (bool): Указывает, работает ли провайдер (в данном случае `False`).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер стриминг ответов (в данном случае `True`).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (в данном случае `True`).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (в данном случае `True`).
- `default_model` (str): Модель, используемая по умолчанию (`gpt-4o-mini`).
- `chat_models` (list[str]): Список моделей, поддерживаемых для генерации текста.
- `image_models` (list[str]): Список моделей, поддерживаемых для генерации изображений.
- `models` (list[str]): Объединенный список моделей для генерации текста и изображений.
- `model_aliases` (dict[str, str]): Словарь псевдонимов моделей.

**Методы**:
- `get_personaId(model: str) -> str`: Возвращает идентификатор личности (personaId) для заданной модели.
- `generate_chat_id() -> str`: Генерирует уникальный идентификатор чата в формате UUID.
- `create_async_generator(...) -> AsyncResult`: Создает асинхронный генератор для выполнения запросов к API AmigoChat.

## Функции

### `get_personaId`

```python
    @classmethod
    def get_personaId(cls, model: str) -> str:
        """Возвращает идентификатор личности (personaId) для заданной модели.

        Args:
            model (str): Название модели.

        Returns:
            str: Идентификатор личности (personaId) для заданной модели.

        Raises:
            ValueError: Если модель не найдена в списках `chat_models` или `image_models`.
        """
        ...
```

**Назначение**: Получает идентификатор личности (personaId) для указанной модели из словаря `MODELS`.

**Параметры**:
- `model` (str): Название модели, для которой требуется получить personaId.

**Возвращает**:
- `str`: Значение `persona_id` из словаря `MODELS` для указанной модели.

**Вызывает исключения**:
- `ValueError`: Если модель не найдена ни в `chat_models`, ни в `image_models`.

**Как работает функция**:

1.  Проверяет, находится ли модель в списке `chat_models`. Если да, возвращает соответствующий `persona_id` из словаря `MODELS['chat']`.
2.  Если модель не найдена в `chat_models`, проверяет, находится ли модель в списке `image_models`. Если да, возвращает соответствующий `persona_id` из словаря `MODELS['image']`.
3.  Если модель не найдена ни в одном из списков, вызывает исключение `ValueError` с сообщением о том, что модель не найдена.

```
    Модель_в_chat_models? -- Нет --> Модель_в_image_models? -- Нет --> ValueError: Модель не найдена
    | Да
    | Возвращает persona_id из MODELS['chat']
    |
    Возвращает persona_id из MODELS['image']
```

**Примеры**:

```python
# Пример вызова функции get_personaId
persona_id = AmigoChat.get_personaId('gpt-4o-mini')
print(persona_id)  # Вывод: amigo

persona_id = AmigoChat.get_personaId('flux-pro/v1.1')
print(persona_id)  # Вывод: flux-1-1-pro
```

### `generate_chat_id`

```python
    @staticmethod
    def generate_chat_id() -> str:
        """Generate a chat ID in format: 8-4-4-4-12 hexadecimal digits"""
        return str(uuid.uuid4())
```

**Назначение**: Генерирует уникальный идентификатор чата в формате UUID (Universally Unique Identifier).

**Возвращает**:
- `str`: Строковое представление UUID, сгенерированного с помощью `uuid.uuid4()`.

**Как работает функция**:

1.  Вызывает функцию `uuid.uuid4()` для генерации нового UUID.
2.  Преобразует UUID в строковое представление с помощью `str()`.
3.  Возвращает строковое представление UUID.

```
    Генерация UUID --> Преобразование в строку --> Возврат строки
```

**Примеры**:

```python
# Пример вызова функции generate_chat_id
chat_id = AmigoChat.generate_chat_id()
print(chat_id)  # Вывод: например, 'a1b2c3d4-e5f6-7890-1234-567890abcdef'
```

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        stream: bool = False,
        timeout: int = 300,
        frequency_penalty: float = 0,
        max_tokens: int = 4000,
        presence_penalty: float = 0,
        temperature: float = 0.5,
        top_p: float = 0.95,
        **kwargs
    ) -> AsyncResult:
        """Создает асинхронный генератор для выполнения запросов к API AmigoChat.

        Args:
            model (str): Название модели для использования.
            messages (Messages): Список сообщений для отправки.
            proxy (str, optional): URL прокси-сервера. По умолчанию `None`.
            stream (bool, optional): Включает ли стриминг ответов. По умолчанию `False`.
            timeout (int, optional): Максимальное время ожидания запроса в секундах. По умолчанию 300.
            frequency_penalty (float, optional): Штраф за частоту. По умолчанию 0.
            max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию 4000.
            presence_penalty (float, optional): Штраф за присутствие. По умолчанию 0.
            temperature (float, optional): Температура. По умолчанию 0.5.
            top_p (float, optional): Top P. По умолчанию 0.95.
            **kwargs: Дополнительные аргументы.

        Returns:
            AsyncResult: Асинхронный генератор, выдающий ответы от API AmigoChat.

        Raises:
            Exception: Если происходит ошибка при выполнении запроса.
        """
        ...
```

**Назначение**: Создает асинхронный генератор для взаимодействия с API AmigoChat, позволяющий отправлять запросы на генерацию текста или изображений и получать ответы в асинхронном режиме.

**Параметры**:
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений для отправки.
- `proxy` (str, optional): URL прокси-сервера. По умолчанию `None`.
- `stream` (bool, optional): Включает ли стриминг ответов. По умолчанию `False`.
- `timeout` (int, optional): Максимальное время ожидания запроса в секундах. По умолчанию 300.
- `frequency_penalty` (float, optional): Штраф за частоту. По умолчанию 0.
- `max_tokens` (int, optional): Максимальное количество токенов в ответе. По умолчанию 4000.
- `presence_penalty` (float, optional): Штраф за присутствие. По умолчанию 0.
- `temperature` (float, optional): Температура. По умолчанию 0.5.
- `top_p` (float, optional): Top P. По умолчанию 0.95.
- `**kwargs`: Дополнительные аргументы.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, выдающий ответы от API AmigoChat.

**Вызывает исключения**:
- `Exception`: Если происходит ошибка при выполнении запроса.

**Как работает функция**:

1.  Получает название модели, используя `cls.get_model(model)`.
2.  Генерирует UUID устройства (`device_uuid`) для идентификации клиента.
3.  Устанавливает максимальное количество повторных попыток (`max_retries`) равным 3.
4.  Инициализирует счетчик повторных попыток (`retry_count`) равным 0.
5.  Запускает цикл `while`, который выполняется до тех пор, пока `retry_count` меньше `max_retries`.
6.  Внутри цикла:
    -   Формирует заголовки (`headers`) для HTTP-запроса, включая `user-agent`, `content-type` и другие необходимые параметры.
    -   Создает асинхронную сессию (`StreamSession`) с использованием указанных заголовков и прокси-сервера (если указан).
    -   Проверяет, находится ли модель в списке `image_models`.
        -   Если модель не находится в `image_models` (т.е., это запрос на генерацию текста):
            -   Формирует данные (`data`) для запроса, включая `chatId`, `messages`, `model`, `personaId` и другие параметры.
            -   Отправляет POST-запрос к `cls.chat_api_endpoint` с использованием сформированных данных и заголовков.
            -   Обрабатывает ответ от API AmigoChat в асинхронном режиме, итерируясь по строкам ответа.
            -   Декодирует каждую строку, удаляет префикс `data: `, и пытается загрузить строку как JSON.
            -   Извлекает содержимое (`content`) из JSON-объекта и выдает его с помощью `yield`.
        -   Если модель находится в `image_models` (т.е., это запрос на генерацию изображения):
            -   Извлекает запрос (`prompt`) из последнего сообщения в списке `messages`.
            -   Формирует данные (`data`) для запроса на генерацию изображения, включая `prompt`, `model` и `personaId`.
            -   Отправляет POST-запрос к `cls.image_api_endpoint` с использованием сформированных данных.
            -   Обрабатывает ответ от API AmigoChat, извлекая URL-адреса сгенерированных изображений из JSON-ответа.
            -   Создает объект `ImageResponse` с URL-адресами изображений и запросом (`prompt`), и выдает его с помощью `yield`.
    -   Если запрос выполнен успешно, выходит из цикла `while` с помощью `break`.
7.  Если во время выполнения запроса происходит исключение `ResponseStatusError` или `Exception`:
    -   Увеличивает счетчик `retry_count` на 1.
    -   Проверяет, достигло ли количество повторных попыток максимума (`retry_count >= max_retries`).
        -   Если достигло, вызывает исключение повторно.
        -   Если не достигло, генерирует новый `device_uuid` и повторяет попытку.

```
    Получение модели --> Генерация UUID устройства --> Цикл повторных попыток:
    |-- Формирование заголовков
    |-- Создание асинхронной сессии
    |-- Модель в image_models?
    |   |-- Да: Запрос на генерацию изображения
    |   |   |-- Формирование данных для запроса изображения
    |   |   |-- Отправка POST-запроса к image_api_endpoint
    |   |   |-- Обработка ответа, извлечение URL-адресов изображений
    |   |   |-- Выдача ImageResponse с URL-адресами изображений
    |   |-- Нет: Запрос на генерацию текста
    |   |   |-- Формирование данных для запроса текста
    |   |   |-- Отправка POST-запроса к chat_api_endpoint
    |   |   |-- Обработка потока ответа, извлечение содержимого
    |   |   |-- Выдача содержимого
    |-- Обработка исключений (ResponseStatusError, Exception)
    |   |-- Увеличение retry_count
    |   |-- retry_count >= max_retries?
    |   |   |-- Да: Вызов исключения повторно
    |   |   |-- Нет: Генерация нового device_uuid, повтор цикла
    |-- Успешное выполнение: Выход из цикла
```

**Примеры**:

```python
# Пример использования create_async_generator для генерации текста
model = 'gpt-4o-mini'
messages = [{'role': 'user', 'content': 'Hello, how are you?'}]
async for chunk in AmigoChat.create_async_generator(model=model, messages=messages):
    print(chunk, end='')

# Пример использования create_async_generator для генерации изображения
model = 'flux-pro/v1.1'
messages = [{'role': 'user', 'content': 'A futuristic cityscape'}]
async for image_response in AmigoChat.create_async_generator(model=model, messages=messages):
    if image_response:
        print(image_response.image_urls)