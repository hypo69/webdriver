# Модуль `tools`

## Обзор

Модуль содержит классы инструментов (`TinyTool`, `TinyCalendar`, `TinyWordProcessor`), которые агенты могут использовать для выполнения специализированных задач. Инструменты позволяют агентам выполнять различные действия, такие как ведение календаря, создание и редактирование документов.

## Подробней

Модуль предоставляет базовый класс `TinyTool`, от которого наследуются конкретные инструменты, такие как `TinyCalendar` и `TinyWordProcessor`. Каждый инструмент имеет имя, описание, владельца (агента), флаг, указывающий на наличие реальных побочных эффектов, а также может использовать экспортер и обогатитель контента.

## Классы

### `TinyTool`

**Описание**: Базовый класс для инструментов, используемых агентами.

**Принцип работы**:
1.  Инициализируется с именем, описанием, владельцем, флагом реальных побочных эффектов, экспортером и обогатителем.
2.  Метод `process_action` выполняет действия, защищая от реальных побочных эффектов и проверяя владельца инструмента.
3.  Абстрактные методы `_process_action`, `actions_definitions_prompt` и `actions_constraints_prompt` должны быть реализованы в подклассах.

**Атрибуты**:

*   `name` (str): Имя инструмента.
*   `description` (str): Описание инструмента.
*   `owner` (str): Владелец инструмента (агент). Если `None`, инструмент может использоваться любым агентом.
*   `real_world_side_effects` (bool): Флаг, указывающий на наличие реальных побочных эффектов.
*   `exporter` (ArtifactExporter): Экспортер для сохранения результатов действий инструмента.
*   `enricher` (TinyEnricher): Обогатитель для улучшения результатов действий инструмента.

**Методы**:

*   `__init__(self, name: str, description: str, owner: str | None = None, real_world_side_effects: bool = False, exporter: ArtifactExporter | None = None, enricher: TinyEnricher | None = None)`

    **Назначение**: Инициализирует новый инструмент.

    **Параметры**:

    *   `name` (str): Имя инструмента.
    *   `description` (str): Описание инструмента.
    *   `owner` (str | None, optional): Владелец инструмента (агент). По умолчанию `None`.
    *   `real_world_side_effects` (bool, optional): Флаг, указывающий на наличие реальных побочных эффектов. По умолчанию `False`.
    *   `exporter` (ArtifactExporter | None, optional): Экспортер для сохранения результатов действий инструмента. По умолчанию `None`.
    *   `enricher` (TinyEnricher | None, optional): Обогатитель для улучшения результатов действий инструмента. По умолчанию `None`.

*   `_process_action(self, agent, action: dict) -> bool`

    **Назначение**: Обрабатывает действие, выполняемое агентом с использованием инструмента.

    **Параметры**:

    *   `agent`: Агент, выполняющий действие.
    *   `action` (dict): Словарь, содержащий информацию о действии.

    **Возвращает**:

    *   `bool`: Возвращает `True`, если действие успешно обработано, `False` в противном случае.

    **Вызывает исключения**:

    *   `NotImplementedError`: Если метод не реализован в подклассе.

*   `_protect_real_world(self)`

    **Назначение**: Предупреждает о реальных побочных эффектах инструмента.
*   `_enforce_ownership(self, agent)`

    **Назначение**: Проверяет, имеет ли агент право на использование инструмента.

    **Параметры**:

    *   `agent`: Агент, пытающийся использовать инструмент.

    **Вызывает исключения**:

    *   `ValueError`: Если агент не является владельцем инструмента.

*   `set_owner(self, owner)`

    **Назначение**: Устанавливает владельца инструмента.

    **Параметры**:

    *   `owner`: Новый владелец инструмента.
*   `actions_definitions_prompt(self) -> str`

    **Назначение**: Возвращает описание действий, которые может выполнять инструмент, в формате строки для подсказок.

    **Возвращает**:

    *   `str`: Описание действий инструмента.

    **Вызывает исключения**:

    *   `NotImplementedError`: Если метод не реализован в подклассе.

*   `actions_constraints_prompt(self) -> str`

    **Назначение**: Возвращает описание ограничений на действия, которые может выполнять инструмент, в формате строки для подсказок.

    **Возвращает**:

    *   `str`: Описание ограничений на действия инструмента.

    **Вызывает исключения**:

    *   `NotImplementedError`: Если метод не реализован в подклассе.

*   `process_action(self, agent, action: dict) -> bool`

    **Назначение**: Обрабатывает действие, выполняемое агентом с использованием инструмента, с проверкой на побочные эффекты и владельца.

    **Параметры**:

    *   `agent`: Агент, выполняющий действие.
    *   `action` (dict): Словарь, содержащий информацию о действии.

    **Возвращает**:

    *   `bool`: Возвращает `True`, если действие успешно обработано, `False` в противном случае.

    **Как работает функция**:

    1.  Защищает от реальных побочных эффектов, вызывая `self._protect_real_world()`.
    2.  Проверяет право собственности агента на инструмент, вызывая `self._enforce_ownership(agent)`.
    3.  Вызывает `self._process_action(agent, action)` для выполнения фактической обработки действия.
    ```
    Начало
    │
    ├── Защита от побочных эффектов: _protect_real_world()
    │
    ├── Проверка владельца: _enforce_ownership(agent)
    │
    └── Обработка действия: _process_action(agent, action)
    │
    Конец
    ```

### `TinyCalendar`

**Описание**: Инструмент календаря, позволяющий агентам отслеживать встречи и события.

**Наследует**:

*   `TinyTool`: Расширяет базовый класс `TinyTool`.

**Принцип работы**:

1.  Инициализируется как инструмент с именем "calendar" и описанием "A basic calendar tool that allows agents to keep track meetings and appointments.".
2.  Хранит события в словаре `calendar`, где ключом является дата, а значением - список событий.
3.  Метод `add_event` добавляет новое событие в календарь.
4.  Метод `_process_action` обрабатывает действие `CREATE_EVENT`, добавляя новое событие в календарь на основе содержимого действия.
5.  Метод `actions_definitions_prompt` предоставляет описание действия `CREATE_EVENT` и его параметров в формате JSON.
6.  Метод `actions_constraints_prompt` предоставляет описание ограничений на действия календаря.

**Атрибуты**:

*   `calendar` (dict): Словарь, хранящий события календаря. Ключ - дата, значение - список событий (словарей).

**Методы**:

*   `__init__(self, owner: str | None = None)`

    **Назначение**: Инициализирует новый инструмент календаря.

    **Параметры**:

    *   `owner` (str | None, optional): Владелец инструмента (агент). По умолчанию `None`.

*   `add_event(self, date, title, description: str | None = None, owner: str | None = None, mandatory_attendees: str | None = None, optional_attendees: str | None = None, start_time: str | None = None, end_time: str | None = None)`

    **Назначение**: Добавляет новое событие в календарь.

    **Параметры**:

    *   `date`: Дата события.
    *   `title`: Название события.
    *   `description` (str | None, optional): Описание события. По умолчанию `None`.
    *   `owner` (str | None, optional): Владелец события. По умолчанию `None`.
    *   `mandatory_attendees` (str | None, optional): Список обязательных участников. По умолчанию `None`.
    *   `optional_attendees` (str | None, optional): Список необязательных участников. По умолчанию `None`.
    *   `start_time` (str | None, optional): Время начала события. По умолчанию `None`.
    *   `end_time` (str | None, optional): Время окончания события. По умолчанию `None`.

*   `find_events(self, year, month, day, hour: str | None = None, minute: str | None = None)`

    **Назначение**: Находит события в календаре по дате и времени.

    **Параметры**:

    *   `year`: Год события.
    *   `month`: Месяц события.
    *   `day`: День события.
    *   `hour` (str | None, optional): Час события. По умолчанию `None`.
    *   `minute` (str | None, optional): Минута события. По умолчанию `None`.

*   `_process_action(self, agent, action: dict) -> bool`

    **Назначение**: Обрабатывает действие, выполняемое агентом с использованием инструмента календаря.

    **Параметры**:

    *   `agent`: Агент, выполняющий действие.
    *   `action` (dict): Словарь, содержащий информацию о действии.

    **Возвращает**:

    *   `bool`: Возвращает `True`, если действие успешно обработано, `False` в противном случае.

    **Как работает функция**:

    1.  Проверяет, является ли тип действия `CREATE_EVENT`.
    2.  Если тип действия `CREATE_EVENT`, извлекает содержимое события из действия.
    3.  Проверяет наличие недопустимых полей в содержимом события.
    4.  Использует `self.add_event` для добавления нового события в календарь.

    ```
    Начало
    │
    ├── Проверка типа действия: action['type'] == "CREATE_EVENT"
    │
    ├── Извлечение содержимого события: event_content = json.loads(action['content'])
    │
    ├── Проверка полей содержимого: utils.check_valid_fields(event_content, valid_keys)
    │
    └── Добавление события в календарь: self.add_event(event_content)
    │
    Конец
    ```
*   `actions_definitions_prompt(self) -> str`

    **Назначение**: Возвращает описание действий, которые можно выполнять с инструментом календаря, в формате строки для подсказок.

    **Возвращает**:

    *   `str`: Описание действий инструмента календаря.

*   `actions_constraints_prompt(self) -> str`

    **Назначение**: Возвращает описание ограничений на действия, которые можно выполнять с инструментом календаря, в формате строки для подсказок.

    **Возвращает**:

    *   `str`: Описание ограничений на действия инструмента календаря.

### `TinyWordProcessor`

**Описание**: Инструмент текстового процессора, позволяющий агентам писать документы.

**Наследует**:

*   `TinyTool`: Расширяет базовый класс `TinyTool`.

**Принцип работы**:

1.  Инициализируется как инструмент с именем "wordprocessor" и описанием "A basic word processor tool that allows agents to write documents.".
2.  Использует `ArtifactExporter` для сохранения документов в различных форматах (md, docx, json).
3.  Использует `TinyEnricher` для обогащения контента документов.
4.  Метод `write_document` создает новый документ, обогащает его контент и экспортирует в различных форматах.
5.  Метод `_process_action` обрабатывает действие `WRITE_DOCUMENT`, создавая новый документ на основе содержимого действия.
6.  Метод `actions_definitions_prompt` предоставляет описание действия `WRITE_DOCUMENT` и его параметров в формате JSON.
7.  Метод `actions_constraints_prompt` предоставляет описание ограничений на действия текстового процессора.

**Методы**:

*   `__init__(self, owner: str | None = None, exporter: ArtifactExporter | None = None, enricher: TinyEnricher | None = None)`

    **Назначение**: Инициализирует новый инструмент текстового процессора.

    **Параметры**:

    *   `owner` (str | None, optional): Владелец инструмента (агент). По умолчанию `None`.
    *   `exporter` (ArtifactExporter | None, optional): Экспортер для сохранения документов. По умолчанию `None`.
    *   `enricher` (TinyEnricher | None, optional): Обогатитель для улучшения контента документов. По умолчанию `None`.

*   `write_document(self, title, content, author: str | None = None)`

    **Назначение**: Создает новый документ, обогащает его контент и экспортирует в различных форматах.

    **Параметры**:

    *   `title`: Название документа.
    *   `content`: Содержание документа.
    *   `author` (str | None, optional): Автор документа. По умолчанию `None`.

    **Как работает функция**:

    1.  Логирует запись документа с указанием заголовка и содержания.
    2.  Если `self.enricher` не `None`, обогащает контент документа с использованием `self.enricher.enrich_content`.
    3.  Если `self.exporter` не `None`, экспортирует документ в различных форматах (md, docx, json) с использованием `self.exporter.export`.

    ```
    Начало
    │
    ├── Логирование записи документа: logger.debug(f"Writing document with title {title} and content: {content}")
    │
    ├── Обогащение контента: self.enricher.enrich_content(...) (если self.enricher не None)
    │
    └── Экспорт документа: self.exporter.export(...) (если self.exporter не None)
    │
    Конец
    ```
*   `_process_action(self, agent, action: dict) -> bool`

    **Назначение**: Обрабатывает действие, выполняемое агентом с использованием инструмента текстового процессора.

    **Параметры**:

    *   `agent`: Агент, выполняющий действие.
    *   `action` (dict): Словарь, содержащий информацию о действии.

    **Возвращает**:

    *   `bool`: Возвращает `True`, если действие успешно обработано, `False` в противном случае.

    **Как работает функция**:

    1.  Проверяет, является ли тип действия `WRITE_DOCUMENT`.
    2.  Если тип действия `WRITE_DOCUMENT`, извлекает спецификацию документа из действия.
    3.  Проверяет наличие недопустимых полей в спецификации документа.
    4.  Использует `self.write_document` для создания нового документа.
    5.  Обрабатывает исключение `json.JSONDecodeError`, если возникает ошибка при разборе JSON.

    ```
    Начало
    │
    ├── Проверка типа действия: action['type'] == "WRITE_DOCUMENT"
    │
    ├── Извлечение спецификации документа: doc_spec = json.loads(action['content'])
    │
    ├── Проверка полей спецификации: utils.check_valid_fields(doc_spec, valid_keys)
    │
    └── Создание документа: self.write_document(**doc_spec)
    │
    Конец
    ```
*   `actions_definitions_prompt(self) -> str`

    **Назначение**: Возвращает описание действий, которые можно выполнять с инструментом текстового процессора, в формате строки для подсказок.

    **Возвращает**:

    *   `str`: Описание действий инструмента текстового процессора.

*   `actions_constraints_prompt(self) -> str`

    **Назначение**: Возвращает описание ограничений на действия, которые можно выполнять с инструментом текстового процессора, в формате строки для подсказок.

    **Возвращает**:

    *   `str`: Описание ограничений на действия инструмента текстового процессора.

## Функции

В данном модуле нет отдельных функций, не относящихся к классам.