# Модуль `factory.py`

## Обзор

Модуль `factory.py` предназначен для создания фабрик, которые генерируют экземпляры класса `TinyPerson`. Он содержит базовый класс `TinyFactory`, который служит основой для различных типов фабрик, и класс `TinyPersonFactory`, который специализируется на создании персонажей `TinyPerson` на основе контекста и подсказок. Фабрики можно кэшировать для повышения производительности, особенно в транзакционных средах.

## Подробней

Этот модуль играет ключевую роль в системе, обеспечивая механизм для создания и управления агентами (`TinyPerson`). Он включает в себя функциональность для генерации описаний персонажей на основе широкого контекста, а также для создания самих персонажей с определенными характеристиками. Модуль поддерживает кэширование фабрик и сгенерированных агентов, что позволяет избежать повторной генерации и повысить эффективность системы.

## Классы

### `TinyFactory`

**Описание**:
Базовый класс для различных типов фабрик. Обеспечивает основу для расширения системы и управления кэшированием в транзакционных средах.

**Принцип работы**:
`TinyFactory` предоставляет базовую функциональность для создания и управления фабриками. Он содержит методы для добавления фабрик в глобальный список, очистки списка фабрик, кодирования и декодирования состояния фабрики. Класс также обеспечивает механизм кэширования фабрик в транзакционном режиме, что необходимо для обеспечения согласованности при кэшировании агентов, генерируемых фабриками.

**Атрибуты**:
- `all_factories` (dict): Словарь, содержащий все созданные фабрики. Ключ - имя фабрики, значение - экземпляр фабрики.
- `name` (str): Имя фабрики. Генерируется автоматически при создании экземпляра фабрики.
- `simulation_id` (str, optional): Идентификатор симуляции, к которой принадлежит фабрика. По умолчанию `None`.

**Методы**:
- `__init__(self, simulation_id: str = None) -> None`:
    - Инициализирует экземпляр `TinyFactory`.
    - Параметр `simulation_id` позволяет связать фабрику с определенной симуляцией.
- `__repr__(self)`:
    - Возвращает строковое представление объекта `TinyFactory`.
- `set_simulation_for_free_factories(simulation)`:
    - Устанавливает симуляцию для свободных фабрик (с `simulation_id=None`).
    - Позволяет захватывать свободные окружения конкретными областями симуляции.
- `add_factory(factory)`:
    - Добавляет фабрику в список всех фабрик.
    - Вызывает исключение, если фабрика с таким именем уже существует.
- `clear_factories()`:
    - Очищает глобальный список всех фабрик.
- `encode_complete_state() -> dict`:
    - Кодирует полное состояние фабрики в словарь.
    - Переопределяется подклассами, если они содержат несериализуемые элементы.
- `decode_complete_state(state: dict)`:
    - Декодирует состояние фабрики из словаря.
    - Переопределяется подклассами, если они содержат несериализуемые элементы.

### `TinyPersonFactory`

**Описание**:
Класс, специализирующийся на создании экземпляров `TinyPerson` на основе контекста и подсказок. Наследуется от `TinyFactory`.

**Принцип работы**:
`TinyPersonFactory` использует OpenAI LLM для генерации персонажей `TinyPerson`. Он принимает контекстный текст, который используется для создания подсказок для LLM. Затем LLM генерирует описания персонажей, которые используются для создания экземпляров `TinyPerson`. Фабрика также отслеживает сгенерированных персонажей, чтобы избежать повторной генерации одних и тех же персонажей.

**Наследует**:
- `TinyFactory`: Предоставляет базовую функциональность для создания и управления фабриками.

**Атрибуты**:
- `person_prompt_template_path` (str): Путь к шаблону подсказки для генерации персонажа.
- `context_text` (str): Контекстный текст, используемый для генерации экземпляров `TinyPerson`.
- `generated_minibios` (list): Список сгенерированных мини-биографий персонажей.
- `generated_names` (list): Список сгенерированных имен персонажей.

**Методы**:
- `__init__(self, context_text, simulation_id: str = None)`:
    - Инициализирует экземпляр `TinyPersonFactory`.
    - Принимает контекстный текст и идентификатор симуляции.
- `generate_person_factories(number_of_factories, generic_context_text)`:
    - Генерирует список экземпляров `TinyPersonFactory` с использованием OpenAI LLM.
    - Использует системную подсказку из файла `prompts/generate_person_factory.md`.
    - Извлекает описания персонажей из ответа LLM и создает фабрики.
- `generate_person(self, agent_particularities: str = None, temperature: float = 1.5, attepmpts: int = 5)`:
    - Генерирует экземпляр `TinyPerson` с использованием OpenAI LLM.
    - Использует шаблон подсказки из файла `prompts/generate_person.mustache`.
    - Вызывает вспомогательную функцию `aux_generate` для выполнения вызова модели.
    - Создает экземпляр `TinyPerson` на основе сгенерированных параметров.
- `_aux_model_call(self, messages, temperature)`:
    - Вспомогательный метод для выполнения вызова модели.
    - Используется для кэширования вызова модели в транзакционном режиме.
- `_setup_agent(self, agent, configuration)`:
    - Настраивает агента с использованием предоставленной конфигурации.
    - Определяет атрибуты агента на основе значений в конфигурации.

## Функции

### `TinyFactory.set_simulation_for_free_factories(simulation)`
**Назначение**: Устанавливает симуляцию для всех "свободных" фабрик, у которых `simulation_id` равен `None`. Это позволяет привязать фабрики, не привязанные к конкретной симуляции, к определенной симуляции.

**Параметры**:
- `simulation` (Simulation): Объект симуляции, к которой нужно привязать "свободные" фабрики.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:

1. **Перебор фабрик**: Функция итерируется по всем фабрикам, хранящимся в `TinyFactory.all_factories`.
2. **Проверка `simulation_id`**: Для каждой фабрики проверяется, является ли её атрибут `simulation_id` равным `None`.
3. **Привязка к симуляции**: Если `simulation_id` равен `None`, то вызывается метод `add_factory` объекта `simulation`, чтобы привязать фабрику к данной симуляции.

```
Начало
  |
  V
Перебор фабрик в TinyFactory.all_factories
  |
  V
Проверка: factory.simulation_id is None?
  |
  +-> Да: Привязка фабрики к симуляции (simulation.add_factory(factory))
  |
  +-> Нет: Следующая фабрика
  |
  V
Конец
```

**Примеры**:
```python
# Создание экземпляра симуляции
simulation = Simulation()

# Создание "свободной" фабрики (без указания simulation_id)
factory = TinyFactory()

# Привязка "свободной" фабрики к симуляции
TinyFactory.set_simulation_for_free_factories(simulation)
```

### `TinyFactory.add_factory(factory)`

**Назначение**: Добавляет фабрику в глобальный список всех фабрик (`TinyFactory.all_factories`).

**Параметры**:
- `factory` (TinyFactory): Экземпляр фабрики, который нужно добавить.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `ValueError`: Если фабрика с таким именем уже существует.

**Как работает функция**:

1. **Проверка имени**: Функция проверяет, существует ли фабрика с таким же именем (`factory.name`) в словаре `TinyFactory.all_factories`.
2. **Добавление фабрики**: Если фабрики с таким именем не существует, она добавляется в словарь `TinyFactory.all_factories`, где ключом является имя фабрики, а значением - сам объект фабрики.
3. **Выброс исключения**: Если фабрика с таким именем уже существует, выбрасывается исключение `ValueError` с соответствующим сообщением об ошибке.

```
Начало
  |
  V
Проверка: factory.name in TinyFactory.all_factories?
  |
  +-> Да: Выброс исключения ValueError
  |
  +-> Нет: Добавление фабрики в TinyFactory.all_factories (TinyFactory.all_factories[factory.name] = factory)
  |
  V
Конец
```

**Примеры**:
```python
# Создание экземпляра фабрики
factory = TinyFactory()

# Добавление фабрики в глобальный список
TinyFactory.add_factory(factory)
```

### `TinyFactory.clear_factories()`

**Назначение**: Очищает глобальный список всех фабрик (`TinyFactory.all_factories`).

**Параметры**:
- `Нет параметров`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Как работает функция**:

1. **Очистка списка**: Функция присваивает атрибуту `TinyFactory.all_factories` пустой словарь (`{}`), что приводит к удалению всех фабрик из глобального списка.

```
Начало
  |
  V
Очистка TinyFactory.all_factories (TinyFactory.all_factories = {})
  |
  V
Конец
```

**Примеры**:
```python
# Очистка глобального списка фабрик
TinyFactory.clear_factories()
```

### `TinyFactory.encode_complete_state()`

**Назначение**: Кодирует полное состояние фабрики в словарь для последующего сохранения или передачи.

**Параметры**:
- `Нет параметров`.

**Возвращает**:
- `dict`: Словарь, представляющий полное состояние фабрики.

**Как работает функция**:

1. **Создание копии**: Функция создает глубокую копию словаря `self.__dict__`, который содержит все атрибуты объекта фабрики.
2. **Возврат состояния**: Функция возвращает созданную копию словаря.

```
Начало
  |
  V
Создание глубокой копии self.__dict__
  |
  V
Возврат копии
  |
  V
Конец
```

**Примеры**:
```python
# Создание экземпляра фабрики
factory = TinyFactory()

# Кодирование состояния фабрики
state = factory.encode_complete_state()
```

### `TinyFactory.decode_complete_state(state: dict)`

**Назначение**: Декодирует состояние фабрики из словаря, восстанавливая её атрибуты.

**Параметры**:
- `state` (dict): Словарь, содержащий состояние фабрики.

**Возвращает**:
- `TinyFactory`: Экземпляр фабрики с восстановленным состоянием.

**Как работает функция**:

1. **Создание копии**: Функция создает глубокую копию словаря `state`, чтобы избежать изменения исходного словаря.
2. **Обновление атрибутов**: Функция обновляет атрибуты объекта фабрики (`self.__dict__`) значениями из словаря `state`.
3. **Возврат фабрики**: Функция возвращает экземпляр фабрики с восстановленным состоянием.

```
Начало
  |
  V
Создание глубокой копии state
  |
  V
Обновление self.__dict__ значениями из state
  |
  V
Возврат self
  |
  V
Конец
```

**Примеры**:
```python
# Создание экземпляра фабрики
factory = TinyFactory()

# Кодирование состояния фабрики
state = factory.encode_complete_state()

# Создание нового экземпляра фабрики
new_factory = TinyFactory()

# Декодирование состояния в новый экземпляр
new_factory.decode_complete_state(state)
```

### `TinyPersonFactory.generate_person_factories(number_of_factories, generic_context_text)`

**Назначение**: Генерирует список экземпляров `TinyPersonFactory` на основе предоставленного контекста, используя OpenAI LLM.

**Параметры**:
- `number_of_factories` (int): Количество фабрик персонажей, которые необходимо сгенерировать.
- `generic_context_text` (str): Общий контекстный текст, который будет использоваться для генерации описаний фабрик персонажей.

**Возвращает**:
- `list[TinyPersonFactory] | None`: Список сгенерированных экземпляров `TinyPersonFactory` или `None`, если не удалось сгенерировать фабрики.

**Как работает функция**:

1. **Логирование**: Записывает информацию о начале генерации фабрик персонажей в лог.
2. **Чтение системной подсказки**: Считывает содержимое файла `prompts/generate_person_factory.md`, который содержит системную подсказку для LLM.
3. **Формирование сообщения для LLM**: Создает сообщение для LLM, содержащее системную подсказку и пользовательский запрос на генерацию описаний фабрик персонажей на основе предоставленного контекста.
4. **Отправка запроса в LLM**: Отправляет сообщение в LLM и получает ответ.
5. **Извлечение JSON из ответа**: Извлекает JSON из содержимого ответа LLM, который содержит описания фабрик персонажей.
6. **Создание экземпляров фабрик**: Создает экземпляры `TinyPersonFactory` на основе извлеченных описаний и добавляет их в список.
7. **Возврат списка фабрик**: Возвращает список сгенерированных экземпляров `TinyPersonFactory`.

```
Начало
  |
  V
Логирование: начало генерации фабрик персонажей
  |
  V
Чтение системной подсказки из prompts/generate_person_factory.md
  |
  V
Формирование сообщения для LLM
  |
  V
Отправка запроса в LLM
  |
  V
Извлечение JSON из ответа
  |
  V
Создание экземпляров TinyPersonFactory на основе извлеченных описаний
  |
  V
Возврат списка фабрик
  |
  V
Конец
```

**Примеры**:
```python
# Генерация 3 фабрик персонажей на основе контекста "городская жизнь"
factories = TinyPersonFactory.generate_person_factories(3, "городская жизнь")
```

### `TinyPersonFactory.generate_person(self, agent_particularities: str = None, temperature: float = 1.5, attepmpts: int = 5)`

**Назначение**: Генерирует экземпляр `TinyPerson` (агента) на основе контекста фабрики и дополнительных особенностей, используя OpenAI LLM.

**Параметры**:
- `agent_particularities` (str, optional): Дополнительные особенности агента, которые будут включены в запрос к LLM. По умолчанию `None`.
- `temperature` (float, optional): Температура для управления случайностью при генерации текста LLM. Более высокие значения делают вывод более случайным. По умолчанию `1.5`.
- `attepmpts` (int, optional): Количество попыток генерации агента в случае неудачи. По умолчанию `5`.

**Возвращает**:
- `TinyPerson | None`: Сгенерированный экземпляр `TinyPerson` или `None`, если не удалось сгенерировать агента после нескольких попыток.

**Внутренние функции**:
- `aux_generate()`:
    - **Назначение**: Внутренняя функция для выполнения вызова модели LLM и извлечения параметров агента.
    - **Как работает**:
        1. **Формирование сообщений**: Создает список сообщений для LLM, включающий системную подсказку и запрос пользователя на основе контекста фабрики и особенностей агента.
        2. **Вызов модели**: Вызывает метод `_aux_model_call` для отправки запроса в LLM и получения ответа.
        3. **Извлечение JSON**: Извлекает JSON из содержимого ответа LLM, который содержит параметры агента.
        4. **Проверка имени**: Проверяет, не было ли имя агента уже сгенерировано ранее. Если имя уникально, возвращает параметры агента.
        5. **Возврат None**: Если не удалось сгенерировать подходящего агента, возвращает `None`.

**Как работает функция**:

1. **Логирование**: Записывает информацию о начале генерации персонажа в лог.
2. **Формирование подсказки**: Создает подсказку для LLM на основе контекста фабрики, особенностей агента и списка уже сгенерированных мини-биографий.
3. **Попытки генерации**: Пытается сгенерировать агента несколько раз (определяется параметром `attepmpts`) до тех пор, пока не будет получен успешный результат или не будут исчерпаны все попытки.
4. **Вызов внутренней функции**: Внутри цикла вызывает внутреннюю функцию `aux_generate` для выполнения вызова модели LLM и извлечения параметров агента.
5. **Создание агента**: Если удалось получить параметры агента, создает экземпляр `TinyPerson` на основе этих параметров.
6. **Настройка агента**: Вызывает метод `_setup_agent` для настройки атрибутов агента на основе сгенерированной конфигурации.
7. **Добавление в списки**: Добавляет мини-биографию и имя агента в списки сгенерированных агентов, чтобы избежать повторной генерации.
8. **Логирование ошибки**: Если не удалось сгенерировать агента после всех попыток, записывает сообщение об ошибке в лог.

```
Начало
  |
  V
Логирование: начало генерации персонажа
  |
  V
Формирование подсказки для LLM
  |
  V
Цикл: попытки генерации агента (attepmpts раз)
  |
  V
Вызов aux_generate()
  |
  V
Проверка: удалось сгенерировать агента?
  |
  +-> Да: Создание экземпляра TinyPerson
  |     |
  |     V
  |     Настройка агента (_setup_agent)
  |     |
  |     V
  |     Добавление мини-биографии и имени в списки сгенерированных агентов
  |     |
  |     V
  |     Возврат TinyPerson
  |
  +-> Нет: Следующая попытка
  |
  V
Логирование ошибки: не удалось сгенерировать агента после всех попыток
  |
  V
Возврат None
  |
  V
Конец
```

**Примеры**:
```python
# Создание фабрики персонажей
factory = TinyPersonFactory("Работает в офисе")

# Генерация агента с особенностями "любит кофе"
agent = factory.generate_person(agent_particularities="любит кофе")
```

### `TinyPersonFactory._aux_model_call(self, messages, temperature)`

**Назначение**: Вспомогательный метод для отправки запроса в OpenAI LLM и получения ответа. Используется декоратор `@transactional` для обеспечения кэширования вызова модели в транзакционном режиме.

**Параметры**:
- `messages` (list): Список сообщений, которые будут отправлены в LLM.
- `temperature` (float): Температура для управления случайностью при генерации текста LLM.

**Возвращает**:
- `dict`: Ответ от OpenAI LLM.

**Как работает функция**:

1. **Отправка запроса**: Отправляет запрос в OpenAI LLM, используя метод `openai_utils.client().send_message()`.
2. **Возврат ответа**: Возвращает ответ, полученный от LLM.

```
Начало
  |
  V
Отправка запроса в OpenAI LLM (openai_utils.client().send_message())
  |
  V
Возврат ответа
  |
  V
Конец
```

**Примеры**:
```python
# Создание списка сообщений для LLM
messages = [{"role": "system", "content": "Ты - полезный ассистент"}, {"role": "user", "content": "Напиши короткое стихотворение"}]

# Вызов метода для отправки запроса в LLM
response = factory._aux_model_call(messages, temperature=0.7)
```

### `TinyPersonFactory._setup_agent(self, agent, configuration)`

**Назначение**: Настраивает атрибуты агента (`TinyPerson`) на основе предоставленной конфигурации.

**Параметры**:
- `agent` (TinyPerson): Экземпляр агента, который необходимо настроить.
- `configuration` (dict): Словарь, содержащий конфигурацию агента. Ключи словаря соответствуют именам атрибутов агента, значения - значениям атрибутов.

**Как работает функция**:

1. **Итерация по конфигурации**: Функция итерируется по парам ключ-значение в словаре `configuration`.
2. **Определение атрибутов**: Для каждой пары ключ-значение функция определяет атрибут агента с именем, соответствующим ключу, и значением, соответствующим значению. Если значение является списком, используется метод `agent.define_several()`, иначе используется метод `agent.define()`.

```
Начало
  |
  V
Итерация по configuration
  |
  V
Проверка: value - список?
  |
  +-> Да: Вызов agent.define_several(key, value)
  |
  +-> Нет: Вызов agent.define(key, value)
  |
  V
Конец итерации
  |
  V
Конец
```

**Примеры**:
```python
# Создание экземпляра агента
agent = TinyPerson("Иван")

# Создание конфигурации агента
configuration = {"возраст": 30, "профессия": "врач", "интересы": ["чтение", "путешествия"]}

# Настройка атрибутов агента
factory._setup_agent(agent, configuration)