# Модуль Replicate
## Обзор

Модуль `Replicate` предоставляет асинхронный генератор для взаимодействия с платформой Replicate, которая позволяет запускать и масштабировать модели машинного обучения. Он включает в себя функциональность для аутентификации, форматирования запросов и обработки потоковых ответов от API Replicate.

## Подробней

Модуль предназначен для интеграции с API Replicate для генерации текста на основе предоставленных сообщений, используя различные модели, размещенные на платформе Replicate. Он поддерживает аутентификацию через API-ключ, настройку параметров модели, таких как температура, максимальное количество токенов и другие, а также обработку потоковых ответов для получения сгенерированного текста в режиме реального времени.

## Классы

### `Replicate`

**Описание**: Класс `Replicate` является провайдером для работы с API Replicate и предоставляет асинхронный генератор для получения ответов от модели.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает базовую функциональность для асинхронных генераторов.
- `ProviderModelMixin`: Предоставляет вспомогательные методы для работы с моделями.

**Атрибуты**:
- `url` (str): URL главной страницы Replicate.
- `login_url` (str): URL страницы для получения API-токенов.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `needs_auth` (bool): Флаг, указывающий, требуется ли аутентификация.
- `default_model` (str): Модель, используемая по умолчанию (meta/meta-llama-3-70b-instruct).
- `models` (list[str]): Список поддерживаемых моделей.

### `create_async_generator`

```python
@classmethod
async def create_async_generator(
    cls,
    model: str,
    messages: Messages,
    api_key: str = None,
    proxy: str = None,
    timeout: int = 180,
    system_prompt: str = None,
    max_tokens: int = None,
    temperature: float = None,
    top_p: float = None,
    top_k: float = None,
    stop: list = None,
    extra_data: dict = {},
    headers: dict = {
        "accept": "application/json",
    },
    **kwargs
) -> AsyncResult:
    """Создает асинхронный генератор для получения ответов от API Replicate.

    Args:
        cls (Replicate): Класс Replicate.
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для отправки в модель.
        api_key (str, optional): API-ключ для аутентификации. По умолчанию `None`.
        proxy (str, optional): Прокси-сервер для использования. По умолчанию `None`.
        timeout (int, optional): Время ожидания ответа от сервера. По умолчанию `180`.
        system_prompt (str, optional): Системный запрос для модели. По умолчанию `None`.
        max_tokens (int, optional): Максимальное количество токенов в ответе. По умолчанию `None`.
        temperature (float, optional): Параметр температуры для модели. По умолчанию `None`.
        top_p (float, optional): Параметр top_p для модели. По умолчанию `None`.
        top_k (float, optional): Параметр top_k для модели. По умолчанию `None`.
        stop (list, optional): Список стоп-слов для остановки генерации. По умолчанию `None`.
        extra_data (dict, optional): Дополнительные данные для отправки в запросе. По умолчанию `{}`.
        headers (dict, optional): Дополнительные заголовки для отправки в запросе. По умолчанию `{"accept": "application/json"}`.
        **kwargs: Дополнительные аргументы.

    Returns:
        AsyncResult: Асинхронный генератор, выдающий текст ответа от API Replicate.

    Raises:
        MissingAuthError: Если `api_key` не предоставлен, когда требуется аутентификация.
        ResponseError: Если получен невалидный ответ от API Replicate.
    """

    # Внутренняя функция не используется
```

**Как работает функция**:

1. **Получение модели**:
   - Функция извлекает название модели, используя `cls.get_model(model)`.

2. **Проверка аутентификации**:
   - Проверяется, требуется ли аутентификация и предоставлен ли API-ключ. Если ключ отсутствует и требуется аутентификация, вызывается исключение `MissingAuthError`.

3. **Формирование заголовков**:
   - Если предоставлен API-ключ, он добавляется в заголовок `Authorization`.

4. **Определение базового URL**:
   - В зависимости от наличия API-ключа определяется базовый URL для запросов.

5. **Создание сессии**:
   - Создается асинхронная сессия с использованием `StreamSession` для выполнения запросов.

6. **Подготовка данных для запроса**:
   - Формируются данные для отправки в запросе, включая входные параметры, такие как `prompt`, `system_prompt`, `max_new_tokens`, `temperature`, `top_p`, `top_k` и `stop_sequences`.

7. **Формирование URL**:
   - Формируется URL для отправки запроса на основе базового URL и названия модели.

8. **Отправка POST-запроса**:
   - Отправляется POST-запрос к API Replicate с данными в формате JSON.

9. **Обработка ответа**:
   - Проверяется статус ответа и вызывается исключение `ResponseError` в случае ошибки.
   - Извлекается `id` из JSON-ответа. Если `id` отсутствует, вызывается исключение `ResponseError`.

10. **Получение потока**:
    - Отправляется GET-запрос к URL потока, указанному в ответе, для получения потоковых данных.

11. **Обработка потоковых данных**:
    - Итерируется по строкам ответа.
    - Если строка начинается с `event: `, извлекается тип события.
    - Если событие равно `done`, генерация прекращается.
    - Если событие равно `output`, извлекаются данные и декодируются.
    - Новые текстовые данные передаются через `yield`.

```
Начало
    ↓
Проверка API-ключа и аутентификации
    ↓
Создание заголовков запроса
    ↓
Создание асинхронной сессии
    ↓
Форматирование данных запроса (prompt, параметры модели)
    ↓
Отправка POST-запроса к API Replicate
    ↓
Получение ID предсказания из ответа
    ↓
Отправка GET-запроса для получения потока
    ↓
Обработка потока данных (события и текст)
    ↓
Выдача текста через yield
    ↓
Конец (при событии "done")
```

**Примеры**:

```python
# Пример использования create_async_generator
messages = [{"role": "user", "content": "Напиши короткий рассказ о космосе."}]
api_key = "YOUR_API_KEY"  # Замените на свой API-ключ

async def main():
    generator = await Replicate.create_async_generator(
        model="meta/meta-llama-3-70b-instruct",
        messages=messages,
        api_key=api_key
    )
    async for text in generator:
        print(text, end="")

# Запуск примера
# import asyncio
# asyncio.run(main())