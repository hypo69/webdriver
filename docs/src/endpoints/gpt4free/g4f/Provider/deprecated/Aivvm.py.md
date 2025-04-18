# Модуль `Aivvm.py`

## Обзор

Модуль `Aivvm.py` предоставляет класс `Aivvm`, который является провайдером для взаимодействия с сервисом Aivvm (chat.aivvm.com) для получения ответов от языковых моделей, таких как GPT-3.5 и GPT-4. Этот модуль является частью проекта `hypotez` и предназначен для интеграции с различными AI-моделями.

## Подробнее

Модуль определяет доступные модели и их идентификаторы, а также предоставляет метод `create_completion` для отправки запросов к Aivvm и получения ответов в режиме реального времени (stream).

## Классы

### `Aivvm`

**Описание**: Класс `Aivvm` предоставляет интерфейс для взаимодействия с сервисом Aivvm.

**Наследует**:
- `AbstractProvider`: класс наследует `AbstractProvider` из `..base_provider`, что подразумевает реализацию абстрактного класса для работы с провайдером.

**Атрибуты**:
- `url` (str): URL сервиса Aivvm (`https://chat.aivvm.com`).
- `supports_stream` (bool): Указывает, поддерживается ли потоковая передача данных (значение `True`).
- `working` (bool): Указывает, работает ли провайдер в данный момент (значение `False`).
- `supports_gpt_35_turbo` (bool): Указывает, поддерживается ли модель `gpt-3.5-turbo` (значение `True`).
- `supports_gpt_4` (bool): Указывает, поддерживается ли модель `gpt-4` (значение `True`).

**Методы**:
- `create_completion`: Создает запрос к сервису Aivvm и возвращает ответ в режиме реального времени (stream).

## Функции

### `create_completion`

```python
    @classmethod
    def create_completion(cls,
        model: str,
        messages: Messages,
        stream: bool,
        **kwargs
    ) -> CreateResult:
        """Создает запрос к сервису Aivvm и возвращает ответ в режиме реального времени (stream).

        Args:
            model (str): Идентификатор модели, которую необходимо использовать (например, "gpt-3.5-turbo").
            messages (Messages): Список сообщений для отправки в запросе.
            stream (bool): Указывает, следует ли возвращать ответ в режиме реального времени (stream).
            **kwargs: Дополнительные аргументы, такие как `system_message` (системное сообщение для модели) и `temperature` (температура модели).

        Returns:
            CreateResult: Результат выполнения запроса.

        Raises:
            ValueError: Если указанная модель не поддерживается.
        """
```

**Назначение**: Функция `create_completion` отправляет запрос к сервису Aivvm с указанными параметрами и возвращает ответ в режиме реального времени (stream).

**Параметры**:
- `model` (str): Идентификатор модели, которую необходимо использовать (например, "gpt-3.5-turbo").
- `messages` (Messages): Список сообщений для отправки в запросе.
- `stream` (bool): Указывает, следует ли возвращать ответ в режиме реального времени (stream).
- `**kwargs`: Дополнительные аргументы, такие как `system_message` (системное сообщение для модели) и `temperature` (температура модели).

**Возвращает**:
- `CreateResult`: Результат выполнения запроса.

**Вызывает исключения**:
- `ValueError`: Если указанная модель не поддерживается.

**Как работает функция**:

1.  **Выбор модели**: Если модель не указана, используется "gpt-3.5-turbo" по умолчанию. Если указанная модель не поддерживается, вызывается исключение `ValueError`.
2.  **Формирование данных запроса**: Создается словарь `json_data` с параметрами запроса, такими как модель, сообщения, системное сообщение и температура.
3.  **Преобразование данных в JSON**: Словарь `json_data` преобразуется в строку JSON.
4.  **Формирование заголовков запроса**: Создается словарь `headers` с заголовками запроса, такими как `Content-Type`, `Content-Length` и `User-Agent`.
5.  **Отправка POST-запроса**: Отправляется POST-запрос к сервису Aivvm с указанными заголовками и данными.
6.  **Обработка ответа**: Функция итерируется по содержимому ответа, декодируя каждый чанк в кодировке UTF-8. В случае ошибки декодирования используется кодировка `unicode-escape`.

**ASCII flowchart**:

```
    Выбор модели
    │
    Формирование данных запроса
    │
    Преобразование данных в JSON
    │
    Формирование заголовков запроса
    │
    Отправка POST-запроса
    │
    Обработка ответа
    │
    Декодирование чанка
    │
    Вывод чанка
```

**Примеры**:

```python
# Пример использования create_completion с минимальными параметрами
messages = [{"role": "user", "content": "Hello, how are you?"}]
result = Aivvm.create_completion(model="gpt-3.5-turbo", messages=messages, stream=True)
for chunk in result:
    print(chunk, end="")

# Пример использования create_completion с указанием системного сообщения и температуры
messages = [{"role": "user", "content": "Translate 'hello' to Russian."}]
result = Aivvm.create_completion(
    model="gpt-4",
    messages=messages,
    stream=True,
    system_message="You are a translator.",
    temperature=0.5,
)
for chunk in result:
    print(chunk, end="")