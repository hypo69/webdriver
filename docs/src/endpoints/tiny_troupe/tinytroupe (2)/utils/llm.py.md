# Модуль `llm.py`

## Обзор

Модуль содержит утилиты для работы с большими языковыми моделями (LLM). Он включает в себя функции для составления входных сообщений для LLM, декоратор для преобразования функций в функции на основе LLM, утилиты для извлечения данных из ответов LLM, функции для управления вызовами моделей и функции для prompt engineering.

## Подробней

Модуль предоставляет инструменты для упрощения взаимодействия с LLM, такие как OpenAI. Он позволяет определять системные и пользовательские промпты с использованием шаблонов, автоматически преобразовывать функции в LLM-вызовы и извлекать структурированные данные из ответов модели. Также модуль включает механизмы повторных попыток при ошибках и добавления переменных для управления поведением модели.

## Функции

### `compose_initial_LLM_messages_with_templates`

```python
def compose_initial_LLM_messages_with_templates(system_template_name: str, user_template_name: str = None,
                                                base_module_folder: str = None,
                                                rendering_configs: dict = {}) -> list:
    """
    Составляет начальные сообщения для вызова LLM-модели, предполагая, что всегда есть
    системное сообщение (общее описание задачи) и необязательное пользовательское сообщение (конкретное описание задачи).
    Эти сообщения составляются с использованием указанных шаблонов и конфигураций рендеринга.

    Args:
        system_template_name (str): Имя файла шаблона для системного сообщения.
        user_template_name (str, optional): Имя файла шаблона для пользовательского сообщения. По умолчанию `None`.
        base_module_folder (str, optional): Базовая папка модуля для поиска шаблонов. По умолчанию `None`.
        rendering_configs (dict, optional): Словарь с конфигурациями для рендеринга шаблонов. По умолчанию `{}`.

    Returns:
        list: Список сообщений для LLM, где каждое сообщение представляет собой словарь с ключами "role" и "content".

    Как работает функция:
        1. Определяет путь к папке с шаблонами, используя `base_module_folder` или значение по умолчанию `"../prompts/"`.
        2. Формирует полные пути к шаблонам системного и пользовательского сообщений.
        3. Создает список сообщений, начиная с системного сообщения, содержимое которого рендерится с использованием `chevron.render`.
        4. Если указан `user_template_name`, добавляет пользовательское сообщение, содержимое которого также рендерится.
        5. Возвращает список сообщений.

    ASCII flowchart:

    Начало
    |
    Определение пути к папке с шаблонами
    |
    Формирование путей к шаблонам
    |
    Создание списка сообщений с системным сообщением
    |
    Проверка наличия пользовательского шаблона
    |
    Добавление пользовательского сообщения (если есть)
    |
    Конец

    Примеры:
        >>> messages = compose_initial_LLM_messages_with_templates('system_prompt.md', 'user_prompt.md', rendering_configs={'task': 'summarization'})
        >>> print(messages)
        [{'role': 'system', 'content': 'System prompt content'}, {'role': 'user', 'content': 'User prompt content'}]

        >>> messages = compose_initial_LLM_messages_with_templates('system_prompt.md')
        >>> print(messages)
        [{'role': 'system', 'content': 'System prompt content'}]
    """
```

### `llm`

```python
def llm(**model_overrides):
    """
    Декоратор, который преобразует декорируемую функцию в функцию на основе LLM.
    Декорируемая функция должна либо возвращать строку (инструкцию для LLM),
    либо параметры функции будут использоваться в качестве инструкции для LLM.
    Ответ LLM приводится к аннотированному типу возвращаемого значения функции, если он присутствует.

    Args:
        **model_overrides: Переопределения параметров модели LLM (например, model, temperature, max_tokens).

    Returns:
        function: Декоратор, который принимает функцию и возвращает обертку вокруг нее.

    Примеры:
        @llm(model="gpt-4-0613", temperature=0.5, max_tokens=100)
        def joke():
            return "Tell me a joke."

        @llm(model="gpt-3.5-turbo", temperature=0.7)
        def summarize(text: str) -> str:
            """Summarize the given text."""
            return f"Summarize this: {text}"
    """
```

### `extract_json`

```python
def extract_json(text: str) -> dict:
    """
    Извлекает JSON-объект из строки, игнорируя: любой текст перед первой
    открывающей фигурной скобкой; и любые открывающие (```json) или закрывающие (```) теги Markdown.

    Args:
        text (str): Строка, из которой нужно извлечь JSON.

    Returns:
        dict: Извлеченный JSON-объект в виде словаря. Возвращает пустой словарь, если не удалось извлечь JSON.

    Как работает функция:
        1. Использует регулярные выражения для удаления всего текста до первой открывающей фигурной или квадратной скобки.
        2. Использует регулярные выражения для удаления всего текста после последней закрывающей фигурной или квадратной скобки.
        3. Заменяет недопустимые escape-последовательности.
        4. Использует `json.loads` для преобразования строки в JSON-объект.
        5. В случае ошибки логирует ошибку и возвращает пустой словарь.

    ASCII flowchart:

    Начало
    |
    Удаление текста до первой скобки
    |
    Удаление текста после последней скобки
    |
    Замена недопустимых escape-последовательностей
    |
    Преобразование в JSON
    |
    Конец (возврат JSON или пустого словаря)

    Примеры:
        >>> extract_json('```json\\n{"name": "John", "age": 30}\\n```')
        {'name': 'John', 'age': 30}

        >>> extract_json('Some text {"name": "John", "age": 30}')
        {'name': 'John', 'age': 30}

        >>> extract_json('Invalid JSON')
        {}
    """
```

### `extract_code_block`

```python
def extract_code_block(text: str) -> str:
    """
    Извлекает блок кода из строки, игнорируя любой текст перед первыми
    открывающими тройными обратными кавычками и любой текст после закрывающих тройных обратных кавычек.

    Args:
        text (str): Строка, из которой нужно извлечь блок кода.

    Returns:
        str: Извлеченный блок кода. Возвращает пустую строку, если не удалось извлечь блок кода.

    Как работает функция:
        1. Использует регулярные выражения для удаления всего текста до первых открывающих тройных обратных кавычек.
        2. Использует регулярные выражения для удаления всего текста после последних закрывающих тройных обратных кавычек.
        3. Возвращает извлеченный блок кода.
        4. В случае ошибки возвращает пустую строку.

    ASCII flowchart:

    Начало
    |
    Удаление текста до первого "```"
    |
    Удаление текста после последнего "```"
    |
    Конец (возврат блока кода или пустой строки)

    Примеры:
        >>> extract_code_block('```python\\nprint("Hello")\\n```')
        '```python\\nprint("Hello")\\n```'

        >>> extract_code_block('Some text ```python\\nprint("Hello")\\n```')
        '```python\\nprint("Hello")\\n```'

        >>> extract_code_block('No code block')
        ''
    """
```

### `repeat_on_error`

```python
def repeat_on_error(retries: int, exceptions: list):
    """
    Декоратор, который повторяет вызов указанной функции, если возникает исключение из числа указанных,
    до указанного количества повторных попыток. Если это количество повторных попыток превышено,
    исключение выбрасывается. Если исключение не возникает, функция возвращается нормально.

    Args:
        retries (int): Количество повторных попыток.
        exceptions (list): Список классов исключений, которые нужно перехватывать.

    Returns:
        function: Декоратор, который принимает функцию и возвращает обертку вокруг нее.

    Примеры:
        @repeat_on_error(retries=3, exceptions=[ValueError, TypeError])
        def process_data(data):
            # Process data that might raise ValueError or TypeError
            return result
    """
```

### `add_rai_template_variables_if_enabled`

```python
def add_rai_template_variables_if_enabled(template_variables: dict) -> dict:
    """
    Добавляет переменные шаблона RAI в указанный словарь, если включены дисклеймеры RAI.
    Они могут быть настроены в файле config.ini. Если они включены, переменные загрузят дисклеймеры RAI из
    соответствующих файлов в каталоге prompts. В противном случае переменные будут установлены в None.

    Args:
        template_variables (dict): Словарь переменных шаблона, в который нужно добавить переменные RAI.

    Returns:
        dict: Обновленный словарь переменных шаблона.

    Как работает функция:
        1. Импортирует конфигурацию из `tinytroupe.config`.
        2. Получает значения `RAI_HARMFUL_CONTENT_PREVENTION` и `RAI_COPYRIGHT_INFRINGEMENT_PREVENTION` из конфигурации.
        3. Читает содержимое файлов `rai_harmful_content_prevention.md` и `rai_copyright_infringement_prevention.md`.
        4. Добавляет переменные `rai_harmful_content_prevention` и `rai_copyright_infringement_prevention` в словарь `template_variables`, устанавливая их значения в содержимое файлов или `None` в зависимости от конфигурации.
        5. Возвращает обновленный словарь `template_variables`.
    """
```

### `truncate_actions_or_stimuli`

```python
def truncate_actions_or_stimuli(list_of_actions_or_stimuli: Collection[dict], max_content_length: int) -> Collection[str]:
    """
    Усекает содержимое действий или стимулов до указанной максимальной длины. Не изменяет исходный список.

    Args:
        list_of_actions_or_stimuli (Collection[dict]): Список действий или стимулов для усечения.
        max_content_length (int): Максимальная длина содержимого.

    Returns:
        Collection[str]: Усеченный список действий или стимулов. Это новый список, а не ссылка на исходный список,
        чтобы избежать неожиданных побочных эффектов.
    """