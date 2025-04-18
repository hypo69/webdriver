# Документация модуля `VoiGpt.py`

## Обзор

Модуль `VoiGpt.py` предоставляет класс `VoiGpt`, который является провайдером для взаимодействия с сайтом VoiGpt.com. Этот модуль позволяет генерировать ответы на основе предоставленных сообщений, используя API VoiGpt. Для работы с этим провайдером требуется получить CSRF токен/cookie с сайта voigpt.com.

## Подробней

Модуль предназначен для интеграции с VoiGpt.com, предоставляя удобный интерфейс для отправки сообщений и получения ответов. Он использует библиотеку `requests` для отправки HTTP-запросов и `json` для обработки данных в формате JSON.

## Классы

### `VoiGpt`

**Описание**: Класс `VoiGpt` является провайдером для VoiGpt.com. Он наследуется от `AbstractProvider` и предоставляет метод `create_completion` для генерации ответов на основе предоставленных сообщений.

**Наследует**:
- `AbstractProvider`: Абстрактный класс, определяющий интерфейс для всех провайдеров.

**Аттрибуты**:
- `url` (str): URL сайта VoiGpt.com.
- `working` (bool): Флаг, указывающий, работает ли провайдер.
- `supports_gpt_35_turbo` (bool): Флаг, указывающий, поддерживает ли провайдер модель `gpt-3.5-turbo`.
- `supports_message_history` (bool): Флаг, указывающий, поддерживает ли провайдер историю сообщений.
- `supports_stream` (bool): Флаг, указывающий, поддерживает ли провайдер потоковую передачу данных.
- `_access_token` (str): Приватный атрибут для хранения CSRF токена.

**Методы**:
- `create_completion`: Метод для создания завершения (генерации ответа) на основе предоставленных сообщений.

## Функции

### `create_completion`

```python
@classmethod
def create_completion(
    cls,
    model: str,
    messages: Messages,
    stream: bool,
    proxy: str = None,
    access_token: str = None,
    **kwargs
) -> CreateResult:
    """
    Создает завершение (генерацию ответа) на основе предоставленных сообщений.

    Args:
        model (str): Модель для использования.
        messages (Messages): Сообщения для отправки.
        stream (bool): Флаг, указывающий, использовать ли потоковую передачу данных.
        proxy (str, optional): Прокси для использования. По умолчанию `None`.
        access_token (str, optional): CSRF токен для использования. По умолчанию `None`.
        **kwargs: Дополнительные именованные аргументы.

    Returns:
        CreateResult: Объект `CreateResult`, содержащий сгенерированный ответ.

    Raises:
        RuntimeError: Если возникает ошибка при получении ответа от сервера.
    """
```

**Назначение**:
Метод `create_completion` класса `VoiGpt` предназначен для генерации ответа на основе предоставленных сообщений, используя API VoiGpt. Он отправляет HTTP-запрос к VoiGpt.com с использованием CSRF токена для аутентификации и получает ответ в формате JSON.

**Параметры**:
- `cls`: Ссылка на класс `VoiGpt`.
- `model` (str): Модель для использования при генерации ответа. Если не указана, используется "gpt-3.5-turbo".
- `messages` (Messages): Список сообщений, которые будут отправлены в запросе.
- `stream` (bool): Флаг, указывающий, следует ли использовать потоковый режим. В текущей реализации всегда `False`.
- `proxy` (str, optional): Адрес прокси-сервера для использования при отправке запроса. По умолчанию `None`.
- `access_token` (str, optional): CSRF токен для аутентификации. Если не указан, пытается получить его автоматически.
- `**kwargs`: Дополнительные именованные аргументы, которые могут быть переданы в функцию.

**Возвращает**:
- `CreateResult`: Объект, представляющий результат создания, содержащий сгенерированный ответ. В данном случае, это генератор, выдающий текст ответа.

**Вызывает исключения**:
- `RuntimeError`: Вызывается, если получен некорректный ответ от сервера VoiGpt.com.

**Как работает функция**:

1. **Инициализация**:
   - Проверяется, передана ли модель. Если нет, устанавливается значение по умолчанию `"gpt-3.5-turbo"`.
   - Проверяется, передан ли токен доступа `access_token`. Если нет, используется значение из атрибута класса `cls._access_token`.
   - Если токен доступа отсутствует, он получается с сайта `VoiGpt.com` путем выполнения HTTP-запроса `GET`.

2. **Подготовка заголовков**:
   - Формируются заголовки HTTP-запроса, включая `Cookie` с CSRF токеном и `X-Csrftoken` с токеном доступа.

3. **Формирование полезной нагрузки (payload)**:
   - Создается словарь `payload`, содержащий сообщения для отправки.

4. **Отправка запроса**:
   - Отправляется HTTP-запрос `POST` на URL `f"{cls.url}/generate_response/"` с заголовками и полезной нагрузкой.

5. **Обработка ответа**:
   - Извлекается текст ответа из HTTP-ответа.
   - Пытается преобразовать текст ответа в JSON.
   - Извлекается сгенерированный ответ из JSON-ответа (`response["response"]`).
   - Функция использует `yield` для возврата результата как генератора.

6. **Обработка ошибок**:
   - Если происходит ошибка при обработке ответа, вызывается исключение `RuntimeError` с текстом ответа от сервера.

**ASCII flowchart**:

```
A (Проверка и получение access_token)
│
├───> B (Формирование заголовков HTTP-запроса)
│
├───> C (Формирование payload с сообщениями)
│
├───> D (Отправка POST запроса на VoiGpt.com)
│
├───> E (Обработка JSON ответа)
│
└───> F (Возврат сгенерированного ответа)
```

**Примеры**:

```python
# Пример использования create_completion с минимальными параметрами
messages = [{"role": "user", "content": "Hello, how are you?"}]
result = VoiGpt.create_completion(model="gpt-3.5-turbo", messages=messages, stream=False)
for item in result:
    print(item)

# Пример использования create_completion с указанием прокси и токена доступа
messages = [{"role": "user", "content": "What is the capital of France?"}]
result = VoiGpt.create_completion(model="gpt-3.5-turbo", messages=messages, stream=False, proxy="http://proxy.example.com", access_token="your_access_token")
for item in result:
    print(item)