# Модуль `Qwen_Qwen_2_5M.py`

## Обзор

Модуль предоставляет асинхронный генератор для взаимодействия с моделью Qwen-2.5M через API Hugging Face Space. Он поддерживает потоковую передачу ответов и системные сообщения. Модуль предназначен для генерации текста на основе предоставленных сообщений.

## Подробней

Модуль `Qwen_Qwen_2_5M` использует асинхронные запросы к API Hugging Face Space для взаимодействия с моделью Qwen-2.5M. Он реализует функциональность потоковой передачи ответов, что позволяет получать результаты генерации текста частями, а не целиком. Модуль также поддерживает отправку системных сообщений, что позволяет задавать контекст для генерации текста.

## Классы

### `Qwen_Qwen_2_5M`

**Описание**: Класс `Qwen_Qwen_2_5M` является асинхронным генератором, который взаимодействует с моделью Qwen-2.5M через API Hugging Face Space.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет методы для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера, "Qwen Qwen-2.5M".
- `url` (str): URL Hugging Face Space, "https://qwen-qwen2-5-1m-demo.hf.space".
- `api_endpoint` (str): URL API, сформированный из `url`.
- `working` (bool): Флаг, указывающий, что провайдер работает, `True`.
- `supports_stream` (bool): Флаг, указывающий, что провайдер поддерживает потоковую передачу, `True`.
- `supports_system_message` (bool): Флаг, указывающий, что провайдер поддерживает системные сообщения, `True`.
- `supports_message_history` (bool): Флаг, указывающий, что провайдер поддерживает историю сообщений, `False`.
- `default_model` (str): Модель по умолчанию, "qwen-2.5-1m-demo".
- `model_aliases` (dict): Алиасы моделей, `{"qwen-2.5-1m": default_model}`.
- `models` (list): Список моделей, полученный из ключей `model_aliases`.

**Методы**:
- `create_async_generator`: Создает асинхронный генератор для взаимодействия с моделью.

## Функции

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    proxy: str = None,
    return_conversation: bool = False,
    conversation: JsonConversation = None,
    **kwargs
) -> AsyncResult:
    """
    Создает асинхронный генератор для взаимодействия с моделью Qwen-2.5M.

    Args:
        model (str): Название модели.
        messages (Messages): Список сообщений для отправки модели.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        return_conversation (bool, optional): Флаг, указывающий, нужно ли возвращать объект разговора. По умолчанию `False`.
        conversation (JsonConversation, optional): Объект разговора. По умолчанию `None`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, возвращающий результаты взаимодействия с моделью.
    """
```

**Назначение**: Создает асинхронный генератор для взаимодействия с моделью Qwen-2.5M через API Hugging Face Space.

**Параметры**:
- `cls`: Ссылка на класс `Qwen_Qwen_2_5M`.
- `model` (str): Название модели для использования.
- `messages` (Messages): Список сообщений, которые будут отправлены модели для получения ответа.
- `proxy` (str, optional): Адрес прокси-сервера, если необходимо использовать прокси для подключения к API. По умолчанию `None`.
- `return_conversation` (bool, optional): Флаг, указывающий, нужно ли возвращать объект разговора (`JsonConversation`). Если `True`, то в начале генерации возвращается объект `JsonConversation` с информацией о сессии. По умолчанию `False`.
- `conversation` (JsonConversation, optional): Объект разговора, содержащий информацию о текущей сессии. Если передан, используется для продолжения разговора. По умолчанию `None`.
- `**kwargs`: Дополнительные параметры, которые могут быть переданы в API.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, который выдает результаты взаимодействия с моделью. Может возвращать частичные ответы в режиме потоковой передачи.

**Как работает функция**:
1. **Генерация хеша сессии**: Если объект разговора (`conversation`) не передан, генерируется уникальный хеш сессии (`session_hash`). Если `conversation` передан, используется его `session_hash`.
2. **Возврат объекта разговора**: Если `return_conversation` установлен в `True`, генератор возвращает объект `JsonConversation` с хешем сессии.
3. **Форматирование промпта**: Если объект разговора не передан, формируется промпт из списка сообщений (`messages`). Если `conversation` передан, извлекается последнее сообщение пользователя.
4. **Формирование заголовков**: Создаются заголовки HTTP-запроса, включающие `accept`, `accept-language`, `content-type`, `origin`, `referer` и `user-agent`.
5. **Формирование полезной нагрузки (payload)**: Создается полезная нагрузка для отправки запроса к API, включающая текст промпта, идентификатор функции (`fn_index`), идентификатор триггера (`trigger_id`) и хеш сессии.
6. **Отправка запроса к API**: Отправляется POST-запрос к API (`cls.api_endpoint`) с заголовками и полезной нагрузкой. Полученный ответ преобразуется в JSON.
7. **Формирование данных для присоединения к очереди**: Создаются данные для присоединения к очереди обработки запросов, включающие промпт, идентификатор функции (`fn_index`), идентификатор триггера (`trigger_id`) и хеш сессии.
8. **Присоединение к очереди**: Отправляется POST-запрос к URL присоединения к очереди (`join_url`) с заголовками и данными. Получается идентификатор события (`event_id`).
9. **Подготовка запроса потока данных**: Формируется URL для получения потока данных (`url_data`) с хешем сессии.
10. **Формирование заголовков для потока данных**: Создаются заголовки HTTP-запроса для получения потока данных, включающие `accept`, `referer` и `user-agent`.
11. **Отправка запроса потока данных**: Отправляется GET-запрос к URL потока данных (`url_data`) с заголовками.
12. **Обработка потока данных**:
    - Читаются строки из потока ответа.
    - Если строка начинается с `data: `, извлекается JSON-данные из строки.
    - Если `msg` в JSON-данных равно `process_generating`, извлекается текст из `output_data` и возвращается как часть ответа.
    - Если `msg` в JSON-данных равно `process_completed`, извлекается полный текст ответа из `output_data` и возвращается.
13. **Обработка ошибок JSON**: Если происходит ошибка при декодировании JSON, регистрируется сообщение об ошибке.

```
Генерация хеша сессии --> Формирование промпта --> Формирование заголовков --> Формирование полезной нагрузки
                                                                                                    |
                                                                                                    V
                                                       Отправка запроса к API --> Присоединение к очереди --> Подготовка запроса потока данных
                                                                                                    |
                                                                                                    V
                                                                            Обработка потока данных --> Извлечение текста из JSON --> Возврат текста
```

### `generate_session_hash`

```python
def generate_session_hash():
    """Generate a unique session hash."""
    return str(uuid.uuid4()).replace('-', '')[:12]
```

**Назначение**: Генерирует уникальный хеш сессии.

**Возвращает**:
- `str`: Уникальный хеш сессии длиной 12 символов.

**Как работает функция**:
1. Генерируется UUID (Universally Unique Identifier) с использованием `uuid.uuid4()`.
2. UUID преобразуется в строку с помощью `str()`.
3. Из строки удаляются все символы дефиса (`-`) с помощью `replace('-', '')`.
4. Из полученной строки извлекаются первые 12 символов `[:12]`.
5. Результат возвращается как уникальный хеш сессии.

**Примеры**:
```python
session_hash = generate_session_hash()
print(session_hash)  # Пример: 'a1b2c3d4e5f6'