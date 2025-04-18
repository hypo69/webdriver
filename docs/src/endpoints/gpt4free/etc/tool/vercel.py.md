# Модуль для получения и обработки информации о моделях Vercel AI SDK

## Обзор

Модуль предназначен для извлечения информации о доступных моделях из Vercel AI SDK, преобразования этой информации в удобный формат и генерации кода для использования этих моделей в проекте `hypotez`. Модуль использует библиотеки `quickjs` и `curl_cffi` для работы с JavaScript и выполнения HTTP-запросов.

## Подробней

Данный модуль играет важную роль в интеграции с Vercel AI SDK. Он позволяет автоматически получать актуальную информацию о доступных моделях, их параметрах и идентификаторах, а также генерировать код, необходимый для использования этих моделей в проекте `hypotez`. Это упрощает процесс добавления новых моделей и обновления существующих, так как не требует ручного изменения кода при каждом изменении в Vercel AI SDK.

## Функции

### `get_model_info`

```python
def get_model_info() -> dict[str, Any]:
    """Получает информацию о моделях из Vercel AI SDK.

    Args:
        None

    Returns:
        dict[str, Any]: Словарь, содержащий информацию о моделях.

    Raises:
        Exception: Если происходит ошибка при выполнении HTTP-запросов или обработке данных.

    Как работает функция:
    1.  Выполняет GET-запрос к URL "https://sdk.vercel.ai".
    2.  Извлекает из HTML-ответа пути к JavaScript-файлам, содержащим информацию о моделях.
    3.  Для каждого пути выполняет GET-запрос и извлекает содержимое JavaScript-файла.
    4.  Ищет в содержимом JavaScript-файла строку, содержащую информацию о моделях в формате JavaScript-объекта.
    5.  Преобразует найденную строку в JSON-объект с использованием библиотеки `quickjs`.
    6.  Возвращает полученный JSON-объект.

    Схема работы функции:
        A: Выполнение GET-запроса к "https://sdk.vercel.ai"
        ↓
        B: Извлечение путей к JavaScript-файлам
        ↓
        C: Выполнение GET-запросов к JavaScript-файлам
        ↓
        D: Поиск строки с информацией о моделях
        ↓
        E: Преобразование строки в JSON-объект
        ↓
        F: Возврат JSON-объекта

    Примеры:
        >>> get_model_info()
        {'model1': {'id': 'model1_id', 'parameters': {...}}, 'model2': {...}}
    """
```

### `convert_model_info`

```python
def convert_model_info(models: dict[str, Any]) -> dict[str, Any]:
    """Преобразует информацию о моделях в формат, удобный для использования в проекте `hypotez`.

    Args:
        models (dict[str, Any]): Словарь с информацией о моделях, полученный от `get_model_info`.

    Returns:
        dict[str, Any]: Словарь, содержащий преобразованную информацию о моделях.

    Как работает функция:
    1.  Создает пустой словарь `model_info` для хранения преобразованной информации.
    2.  Для каждой модели в словаре `models`:
        a.  Извлекает параметры модели.
        b.  Преобразует параметры в словарь параметров по умолчанию с помощью функции `params_to_default_params`.
        c.  Добавляет в словарь `model_info` информацию об идентификаторе модели и параметрах по умолчанию.
    3.  Возвращает словарь `model_info`.

    Схема работы функции:

        A: Получение словаря с информацией о моделях
        ↓
        B: Итерация по моделям
        ↓
        C: Преобразование параметров в параметры по умолчанию
        ↓
        D: Добавление информации в словарь `model_info`
        ↓
        E: Возврат словаря `model_info`

    Примеры:
        >>> models = {'model1': {'id': 'model1_id', 'parameters': {'param1': {'value': 'value1'}}}, 'model2': {...}}
        >>> convert_model_info(models)
        {'model1': {'id': 'model1_id', 'default_params': {'param1': 'value1'}}, 'model2': {...}}
    """
```

### `params_to_default_params`

```python
def params_to_default_params(parameters: dict[str, Any]):
    """Преобразует словарь параметров модели в словарь параметров по умолчанию.

    Args:
        parameters (dict[str, Any]): Словарь параметров модели.

    Returns:
        dict[str, Any]: Словарь параметров по умолчанию.

    Как работает функция:
    1.  Создает пустой словарь `defaults` для хранения параметров по умолчанию.
    2.  Для каждого параметра в словаре `parameters`:
        a.  Если ключ параметра равен "maximumLength", заменяет его на "maxTokens".
        b.  Добавляет в словарь `defaults` значение параметра.
    3.  Возвращает словарь `defaults`.

    Схема работы функции:

        A: Получение словаря параметров модели
        ↓
        B: Итерация по параметрам
        ↓
        C: Замена ключа "maximumLength" на "maxTokens" (если необходимо)
        ↓
        D: Добавление значения параметра в словарь `defaults`
        ↓
        E: Возврат словаря `defaults`

    Примеры:
        >>> parameters = {'param1': {'value': 'value1'}, 'maximumLength': {'value': 100}}
        >>> params_to_default_params(parameters)
        {'param1': 'value1', 'maxTokens': 100}
    """
```

### `get_model_names`

```python
def get_model_names(model_info: dict[str, Any]):
    """Извлекает список имен моделей из словаря информации о моделях.

    Args:
        model_info (dict[str, Any]): Словарь с информацией о моделях.

    Returns:
        list[str]: Список имен моделей.

    Как работает функция:
    1.  Извлекает ключи (имена моделей) из словаря `model_info`.
    2.  Фильтрует список, исключая модели "openai:gpt-4" и "openai:gpt-3.5-turbo".
    3.  Сортирует список имен моделей в алфавитном порядке.
    4.  Возвращает отсортированный список имен моделей.

    Схема работы функции:

        A: Получение словаря информации о моделях
        ↓
        B: Извлечение имен моделей
        ↓
        C: Фильтрация списка моделей
        ↓
        D: Сортировка списка моделей
        ↓
        E: Возврат списка моделей

    Примеры:
        >>> model_info = {'model1': {...}, 'openai:gpt-4': {...}, 'model2': {...}}
        >>> get_model_names(model_info)
        ['model1', 'model2']
    """
```

### `print_providers`

```python
def print_providers(model_names: list[str]):
    """Генерирует и выводит код для определения моделей в проекте `hypotez`.

    Args:
        model_names (list[str]): Список имен моделей.

    Returns:
        None

    Как работает функция:
    1.  Для каждого имени модели в списке `model_names`:
        a.  Разделяет имя модели на компоненты, используя символы ":" и "/".
        b.  Извлекает базового провайдера из первого компонента.
        c.  Преобразует имя модели в имя переменной, заменяя символы "-" и "." на "_".
        d.  Формирует строку кода для определения модели, используя имя переменной, имя модели и базового провайдера.
        e.  Выводит сформированную строку кода.

    Схема работы функции:

        A: Получение списка имен моделей
        ↓
        B: Итерация по именам моделей
        ↓
        C: Разделение имени модели на компоненты
        ↓
        D: Извлечение базового провайдера
        ↓
        E: Преобразование имени модели в имя переменной
        ↓
        F: Формирование строки кода
        ↓
        G: Вывод строки кода

    Примеры:
        >>> model_names = ['provider1:model-name', 'provider2/another.model']
        >>> print_providers(model_names)
        model_name = Model(name="provider1:model-name", base_provider="provider1", best_provider=Vercel,)
        another_model = Model(name="provider2/another.model", base_provider="provider2", best_provider=Vercel,)
    """
```

### `print_convert`

```python
def print_convert(model_names: list[str]):
    """Генерирует и выводит код для создания словаря соответствия между именами моделей и переменными.

    Args:
        model_names (list[str]): Список имен моделей.

    Returns:
        None

    Как работает функция:
    1.  Для каждого имени модели в списке `model_names`:
        a.  Разделяет имя модели на компоненты, используя символы ":" и "/".
        b.  Извлекает ключ из последнего компонента.
        c.  Преобразует имя модели в имя переменной, заменяя символы "-" и "." на "_".
        d.  Формирует строку кода для добавления элемента в словарь соответствия, используя ключ и имя переменной.
        e.  Выводит сформированную строку кода.

    Схема работы функции:

        A: Получение списка имен моделей
        ↓
        B: Итерация по именам моделей
        ↓
        C: Разделение имени модели на компоненты
        ↓
        D: Извлечение ключа
        ↓
        E: Преобразование имени модели в имя переменной
        ↓
        F: Формирование строки кода
        ↓
        G: Вывод строки кода

    Примеры:
        >>> model_names = ['provider1:model-name', 'provider2/another.model']
        >>> print_convert(model_names)
                "model-name": model_name,
                "another.model": another_model,
    """
```

### `main`

```python
def main():
    """Основная функция модуля, которая выполняет получение, преобразование и вывод информации о моделях.

    Args:
        None

    Returns:
        None

    Как работает функция:
    1.  Получает информацию о моделях с помощью функции `get_model_info`.
    2.  Преобразует полученную информацию с помощью функции `convert_model_info`.
    3.  Выводит преобразованную информацию в формате JSON.
    4.  Получает список имен моделей с помощью функции `get_model_names`.
    5.  Генерирует и выводит код для определения моделей с помощью функции `print_providers`.
    6.  Генерирует и выводит код для создания словаря соответствия с помощью функции `print_convert`.

    Схема работы функции:

        A: Получение информации о моделях
        ↓
        B: Преобразование информации о моделях
        ↓
        C: Вывод информации в формате JSON
        ↓
        D: Получение списка имен моделей
        ↓
        E: Генерация и вывод кода для определения моделей
        ↓
        F: Генерация и вывод кода для создания словаря соответствия

    Примеры:
        >>> main()
        {
          "model1": {
            "id": "model1_id",
            "default_params": {
              "param1": "value1"
            }
          },
          "model2": {
            "id": "model2_id",
            "default_params": {
              "param2": "value2"
            }
          }
        }
        ------------------------------------------------------------------------------------------------------------------------
        model1 = Model(name="model1", base_provider="provider1", best_provider=Vercel,)
        model2 = Model(name="model2", base_provider="provider2", best_provider=Vercel,)
        ------------------------------------------------------------------------------------------------------------------------
                "model1": model1,
                "model2": model2,
    """
```