# Модуль для определения моделей OpenAI
## Обзор

Модуль `models.py` содержит списки доступных моделей для работы с API OpenAI в проекте `hypotez`. Он определяет модели для генерации текста и изображений, а также включает общие списки моделей. Этот модуль предназначен для централизованного хранения информации о доступных моделях, что упрощает их использование и обновление в других частях проекта.

## Подробней

Модуль предоставляет списки различных моделей, используемых для генерации текста и изображений через API OpenAI. Здесь определены модели по умолчанию, такие как `default_model` и `default_image_model`, а также списки моделей для различных задач: `image_models`, `text_models` и `vision_models`. Это позволяет легко ориентироваться в доступных моделях и использовать их в соответствующих контекстах.

## Переменные

### `default_model`

**Описание**: Строка, содержащая название модели по умолчанию для генерации текста.

### `default_image_model`

**Описание**: Строка, содержащая название модели по умолчанию для генерации изображений.

### `image_models`

**Описание**: Список строк, содержащий названия моделей, предназначенных для генерации изображений.

### `text_models`

**Описание**: Список строк, содержащий названия моделей, предназначенных для генерации текста.

### `vision_models`

**Описание**: Список строк, содержащий названия моделей, поддерживающих функциональность зрения (vision).

### `models`

**Описание**: Список строк, содержащий объединенный список моделей для текста и изображений.

**Как работает**:

1.  Определяются переменные `default_model` и `default_image_model`, содержащие названия моделей по умолчанию для текста и изображений соответственно.
2.  Создаются списки `image_models`, `text_models` и `vision_models` с перечислением доступных моделей для каждой категории.
3.  Список `models` формируется путем объединения списков `text_models` и `image_models`.

```
default_model & default_image_model --> Определяются модели по умолчанию
|
|
--> text_models & image_models & vision_models -->  Формирование списков моделей для каждой категории
|
|
--> models --> Объединение списков текстовых и графических моделей
```

**Примеры**:

```python
default_model = "auto"
default_image_model = "dall-e-3"
image_models = [default_image_model]
text_models = [default_model, "gpt-4", "gpt-4.5", "gpt-4o", "gpt-4o-mini", "o1", "o1-preview", "o1-mini", "o3-mini", "o3-mini-high"]
vision_models = text_models
models = text_models + image_models