# Модуль `Theb`

## Обзор

Модуль `Theb` предоставляет реализацию для взаимодействия с сервисом `TheB.AI` для создания текстовых завершений с использованием различных моделей, таких как `GPT-3.5 Turbo`, `GPT-4`, `Claude 2` и других. Он использует Selenium WebDriver для автоматизации взаимодействия с веб-интерфейсом `TheB.AI`.

## Подробней

Модуль предназначен для интеграции с другими частями проекта `hypotez`, обеспечивая возможность использования различных AI-моделей через единый интерфейс. Он поддерживает потоковую передачу данных, позволяя получать ответы от моделей в режиме реального времени.

## Классы

### `Theb`

**Описание**: Класс `Theb` является провайдером для работы с сервисом `TheB.AI`. Он наследует `AbstractProvider` и реализует метод `create_completion` для создания завершений текста.

**Наследует**: `AbstractProvider`

**Атрибуты**:
- `label` (str): Метка провайдера, `"TheB.AI"`.
- `url` (str): URL сервиса `TheB.AI`, `"https://beta.theb.ai"`.
- `working` (bool): Указывает, работает ли провайдер в данный момент, `False`.
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных, `True`.
- `models` (dict): Словарь доступных моделей.

**Методы**:
- `create_completion`: Создает завершение текста на основе переданных параметров.

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
    webdriver: WebDriver = None,
    virtual_display: bool = True,
    **kwargs
) -> CreateResult:
    """
    Создает завершение текста, используя сервис TheB.AI.

    Args:
        model (str): Название модели для использования.
        messages (Messages): Список сообщений для формирования запроса.
        stream (bool): Флаг, указывающий на необходимость потоковой передачи данных.
        proxy (str, optional): Адрес прокси-сервера. По умолчанию `None`.
        webdriver (WebDriver, optional): Инстанс WebDriver для управления браузером. По умолчанию `None`.
        virtual_display (bool, optional): Флаг, указывающий на необходимость использования виртуального дисплея. По умолчанию `True`.
        **kwargs: Дополнительные параметры.

    Returns:
        CreateResult: Результат создания завершения текста.

    Raises:
        Exception: Если возникает ошибка при взаимодействии с сервисом.

    """
    ...
```

**Назначение**: Создает запрос к сервису `TheB.AI` для получения завершения текста на основе предоставленных сообщений и параметров модели.

**Параметры**:
- `cls`: Ссылка на класс `Theb`.
- `model` (str): Имя модели, которую нужно использовать для генерации ответа.
- `messages (Messages)`: Список сообщений, представляющих контекст для генерации ответа.
- `stream (bool)`: Указывает, нужно ли возвращать ответ в виде потока.
- `proxy (str, optional)`: Прокси-сервер для использования при подключении к сервису. По умолчанию `None`.
- `webdriver (WebDriver, optional)`: Экземпляр веб-драйвера для управления браузером. По умолчанию `None`.
- `virtual_display (bool, optional)`: Указывает, следует ли использовать виртуальный дисплей. По умолчанию `True`.
- `**kwargs`: Дополнительные аргументы, которые могут быть переданы.

**Возвращает**:
- `CreateResult`: Результат создания завершения текста.

**Вызывает исключения**:
- `Exception`: В случае возникновения ошибки при взаимодействии с веб-сервисом.

**Как работает функция**:

1. **Преобразование имени модели**:
   - Если `model` находится в словаре `models`, происходит замена имени модели на соответствующее значение из словаря.
2. **Форматирование промпта**:
   - Используется функция `format_prompt` для преобразования списка сообщений `messages` в строку промпта.
3. **Инициализация веб-сессии**:
   - Создается экземпляр класса `WebDriverSession` для управления сессией браузера с использованием `webdriver`, `virtual_display` и `proxy`.
4. **Настройка перехвата fetch запросов**:
   - Внедряется JavaScript-код в браузер для перехвата fetch-запросов, чтобы получить ответ от сервиса.
5. **Взаимодействие с веб-интерфейсом**:
   - Открывается страница `TheB.AI` в браузере.
   - Дожидается появления элемента ввода текста.
   - Выбирается модель, если она указана.
   - Вводится промпт в поле ввода текста.
6. **Чтение ответа с использованием потока**:
   - Используется JavaScript-код для чтения ответа из потока данных, полученного от сервиса.
   - Ответ возвращается частями с использованием `yield`, что позволяет обрабатывать его в режиме реального времени.

**Внутренние функции**:
Внутри данной функции нет внутренних функций

**Примеры**:

```python
# Пример использования create_completion
model_name = "gpt-3.5-turbo"
messages_list = [{"role": "user", "content": "Hello, how are you?"}]
stream_mode = True
# Assuming webdriver is already initialized
result = Theb.create_completion(
    model=model_name, messages=messages_list, stream=stream_mode, webdriver=webdriver_instance
)
for chunk in result:
    print(chunk, end="")

```

ASCII flowchart:

```
A [Проверка и преобразование имени модели]
|
B [Форматирование промпта]
|
C [Инициализация веб-сессии]
|
D [Настройка перехвата fetch запросов]
|
E [Открытие страницы TheB.AI]
|
F [Взаимодействие с веб-интерфейсом (выбор модели, ввод промпта)]
|
G [Чтение ответа с использованием потока]