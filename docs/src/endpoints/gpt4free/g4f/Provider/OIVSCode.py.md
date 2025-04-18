# Документация модуля OIVSCode

## Обзор

Модуль `OIVSCode.py` предоставляет класс `OIVSCode`, который является подклассом `OpenaiTemplate`. Он предназначен для взаимодействия с сервером OI VSCode. Класс содержит конфигурации, специфичные для этого сервера, такие как URL, базовый URL API, поддерживаемые модели и флаги, указывающие на его функциональность.

## Подробней

Этот модуль играет важную роль в проекте `hypotez`, обеспечивая возможность взаимодействия с сервером OI VSCode для выполнения различных задач, связанных с обработкой кода. Он определяет, какие модели поддерживаются, нужно ли аутентифицироваться и поддерживает ли сервер потоковую передачу данных.

## Классы

### `OIVSCode`

**Описание**: Класс `OIVSCode` предоставляет конфигурации для взаимодействия с сервером OI VSCode.

**Наследует**:
- `OpenaiTemplate`: Класс `OIVSCode` наследует функциональность от `OpenaiTemplate`, что позволяет использовать общие методы и атрибуты для взаимодействия с API OpenAI.

**Атрибуты**:
- `label` (str): Метка, идентифицирующая провайдера (в данном случае, "OI VSCode Server").
- `url` (str): URL сервера OI VSCode ("https://oi-vscode-server.onrender.com").
- `api_base` (str): Базовый URL API сервера OI VSCode ("https://oi-vscode-server-2.onrender.com/v1").
- `working` (bool): Указывает, что провайдер в настоящее время работает (True).
- `needs_auth` (bool): Указывает, требуется ли аутентификация для использования провайдера (False).
- `supports_stream` (bool): Указывает, поддерживает ли провайдер потоковую передачу данных (True).
- `supports_system_message` (bool): Указывает, поддерживает ли провайдер системные сообщения (True).
- `supports_message_history` (bool): Указывает, поддерживает ли провайдер историю сообщений (True).
- `default_model` (str): Модель, используемая по умолчанию ("gpt-4o-mini-2024-07-18").
- `default_vision_model` (str): Модель для работы с изображениями, используемая по умолчанию (совпадает с `default_model`).
- `vision_models` (List[str]): Список моделей, поддерживающих обработку изображений ([default_model, "gpt-4o-mini"]).
- `models` (List[str]): Список всех поддерживаемых моделей (vision_models + ["deepseek-ai/DeepSeek-V3"]).
- `model_aliases` (Dict[str, str]): Словарь псевдонимов моделей, позволяющий использовать короткие имена для обращения к моделям.

## Принцип работы класса `OIVSCode`

Класс `OIVSCode` предназначен для конфигурации и настройки взаимодействия с сервером OI VSCode, предоставляя необходимые параметры и флаги для успешной работы.

1. **Инициализация**:
   - Класс наследует атрибуты и методы от `OpenaiTemplate`.
   - Устанавливает значения атрибутов, специфичные для сервера OI VSCode, такие как URL, базовый URL API и поддерживаемые модели.

2. **Конфигурация моделей**:
   - Определяет список моделей, поддерживающих обработку изображений (`vision_models`).
   - Формирует общий список поддерживаемых моделей (`models`), объединяя модели для изображений и другие модели, такие как "deepseek-ai/DeepSeek-V3".
   - Создает словарь псевдонимов моделей (`model_aliases`), упрощающий обращение к моделям по коротким именам.

3. **Использование**:
   - Класс используется для создания экземпляра, который затем применяется для взаимодействия с сервером OI VSCode через API `OpenaiTemplate`.
   - Флаги `working`, `needs_auth`, `supports_stream`, `supports_system_message` и `supports_message_history` позволяют настроить поведение клиента при взаимодействии с сервером.

## Примеры

```python
from src.endpoints.gpt4free.g4f.Provider.OIVSCode import OIVSCode

# Создание экземпляра класса OIVSCode
oivscode = OIVSCode()

# Вывод атрибутов класса
print(f"Label: {oivscode.label}")
print(f"URL: {oivscode.url}")
print(f"API Base: {oivscode.api_base}")
print(f"Supports Stream: {oivscode.supports_stream}")
print(f"Default Model: {oivscode.default_model}")
print(f"Vision Models: {oivscode.vision_models}")
```

## Функции

В данном модуле функции отсутствуют.