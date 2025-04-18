# Модуль для работы с H2o Provider

## Обзор

Модуль предоставляет функциональность для взаимодействия с H2o AI моделями через API `gpt-gm.h2o.ai`. Он включает в себя функцию `_create_completion`, которая отправляет запросы к API для генерации текста на основе предоставленных сообщений и параметров.

## Подробней

Модуль предназначен для использования в проекте `hypotez` как один из провайдеров для генерации текста с использованием различных AI-моделей. Он поддерживает потоковую передачу данных и предоставляет возможность настройки параметров генерации, таких как температура, максимальное количество токенов и другие.

## Функции

### `_create_completion`

```python
def _create_completion(model: str, messages: list, stream: bool, **kwargs):
    """ Функция отправляет запрос к H2o AI API для генерации текста на основе предоставленных сообщений и параметров.

    Args:
        model (str): Идентификатор модели для использования.
        messages (list): Список сообщений для передачи в модель.
        stream (bool): Флаг, указывающий на необходимость потоковой передачи данных.
        **kwargs: Дополнительные параметры для настройки генерации текста.

    Returns:
        Generator[str, None, None]: Генератор токенов, полученных от API.

    Raises:
        Exception: Если возникает ошибка при взаимодействии с API.

    Example:
        >>> model = 'falcon-40b'
        >>> messages = [{'role': 'user', 'content': 'Hello, how are you?'}]
        >>> stream = True
        >>> for token in _create_completion(model, messages, stream):
        ...     print(token, end='')
        I am doing well, thank you for asking.
    """
```

**Параметры**:

- `model` (str): Идентификатор модели для использования. Допустимые значения: `'falcon-40b'`, `'falcon-7b'`, `'llama-13b'`.
- `messages` (list): Список сообщений для передачи в модель. Каждое сообщение должно быть словарем с ключами `'role'` и `'content'`.
- `stream` (bool): Флаг, указывающий на необходимость потоковой передачи данных. Если `True`, функция возвращает генератор токенов.
- `**kwargs`: Дополнительные параметры для настройки генерации текста:
    - `temperature` (float): Температура генерации (по умолчанию 0.4).
    - `truncate` (int): Максимальная длина входного текста (по умолчанию 2048).
    - `max_new_tokens` (int): Максимальное количество новых токенов для генерации (по умолчанию 1024).
    - `do_sample` (bool): Флаг, указывающий на необходимость использования дискретизации (по умолчанию `True`).
    - `repetition_penalty` (float): Штраф за повторение токенов (по умолчанию 1.2).
    - `return_full_text` (bool): Флаг, указывающий на необходимость возврата полного текста (по умолчанию `False`).
    - `id` (str): Идентификатор запроса (по умолчанию сгенерированный UUID).
    - `response_id` (str): Идентификатор ответа (по умолчанию сгенерированный UUID).

**Возвращает**:

- `Generator[str, None, None]`: Генератор токенов, полученных от API, если `stream` равен `True`. В противном случае возвращает строку с полным текстом ответа.

**Как работает функция**:

1. **Подготовка запроса**: Функция формирует текст запроса, объединяя сообщения из параметра `messages` в формате, ожидаемом API H2o.

2. **Создание сессии**:  Используется `requests.Session()` для управления HTTP-соединением.

3. **Настройка заголовков**:  Устанавливаются необходимые заголовки для HTTP-запроса, включая `authority`, `origin`, `referer` и `user-agent`.

4. **Выполнение запроса**:  Отправляется POST-запрос к API `gpt-gm.h2o.ai` с текстом запроса и параметрами.

5. **Обработка ответа**:  Если `stream` равен `True`, функция итерируется по строкам ответа и извлекает токены, возвращая их через генератор.

6. **Параметры генерации**:  Параметры генерации, такие как температура и максимальное количество токенов, передаются в API через параметр `json`.

7. **Завершение**:  Генерация завершается, когда встречается токен `<|endoftext|>`.

```
A: Формирование текста запроса и инициализация сессии
|
B: Установка заголовков запроса
|
C: Отправка POST-запроса к API
|
D: Обработка потокового ответа
|
E: Извлечение и генерация токенов
|
F: Завершение при получении <|endoftext|>
```

**Примеры**:

```python
model = 'falcon-7b'
messages = [
    {'role': 'user', 'content': 'Напиши короткое стихотворение о весне.'},
    {'role': 'assistant', 'content': 'Весна пришла, природа оживает,\nСолнце светит, птички поют.'}
]
stream = True

for token in _create_completion(model, messages, stream, temperature=0.5, max_new_tokens=50):
    print(token, end='')
```

```python
model = 'llama-13b'
messages = [
    {'role': 'user', 'content': 'Расскажи о себе.'}
]
stream = True
generator = _create_completion(model, messages, stream, max_new_tokens=200)
for token in generator:
    print(token, end='')
```

```python
model = 'falcon-40b'
messages = [
    {'role': 'user', 'content': 'Translate to French: Hello, how are you?'}
]
stream = True
for token in _create_completion(model, messages, stream):
    print(token, end='')
```

```python
params = f'g4f.Providers.{os.path.basename(__file__)[:-3]} supports: ' + \
    '(%s)' % ', '.join([f"{name}: {get_type_hints(_create_completion)[name].__name__}" for name in _create_completion.__code__.co_varnames[:_create_completion.__code__.co_argcount]])
```

## Переменные модуля

- `url` (str): URL API `gpt-gm.h2o.ai`.
- `model` (list): Список поддерживаемых моделей: `'falcon-40b'`, `'falcon-7b'`, `'llama-13b'`.
- `supports_stream` (bool): Флаг, указывающий на поддержку потоковой передачи данных (`True`).
- `needs_auth` (bool): Флаг, указывающий на необходимость аутентификации (`False`).
- `models` (dict): Словарь, связывающий короткие имена моделей с полными именами моделей для API.