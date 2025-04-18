# Модуль BlackForestLabs_Flux1Schnell

## Обзор

Модуль `BlackForestLabs_Flux1Schnell` предназначен для асинхронной генерации изображений с использованием API Black Forest Labs Flux-1-Schnell. Он предоставляет класс `BlackForestLabs_Flux1Schnell`, который наследуется от `AsyncGeneratorProvider` и `ProviderModelMixin`, что позволяет интегрировать его в систему асинхронных провайдеров.

## Подробней

Этот модуль позволяет пользователям генерировать изображения на основе текстовых запросов, используя API Black Forest Labs Flux-1-Schnell. Он поддерживает настройку ширины и высоты изображения, количества шагов инференса, зерна для воспроизводимости результатов и другие параметры. Модуль также обрабатывает ошибки, возвращаемые API, и предоставляет сгенерированные изображения в формате URL.

## Классы

### `BlackForestLabs_Flux1Schnell`

**Описание**: Класс для взаимодействия с API Black Forest Labs Flux-1-Schnell для генерации изображений.

**Наследует**:
- `AsyncGeneratorProvider`: Обеспечивает асинхронную генерацию данных.
- `ProviderModelMixin`: Предоставляет функциональность для работы с моделями.

**Атрибуты**:
- `label` (str): Метка провайдера ("BlackForestLabs Flux-1-Schnell").
- `url` (str): URL главной страницы Black Forest Labs Flux-1-Schnell.
- `api_endpoint` (str): URL API для вызова инференса.
- `working` (bool): Флаг, указывающий на работоспособность провайдера (True).
- `default_model` (str): Модель, используемая по умолчанию ("black-forest-labs-flux-1-schnell").
- `default_image_model` (str): Псевдоним для `default_model`.
- `model_aliases` (dict): Псевдонимы моделей изображений.
- `image_models` (list): Список моделей изображений.
- `models` (list): Список моделей (совпадает с `image_models`).

**Методы**:
- `create_async_generator`: Асинхронный генератор изображений на основе текстового запроса.

## Функции

### `create_async_generator`

```python
    @classmethod
    async def create_async_generator(
        cls,
        model: str,
        messages: Messages,
        proxy: str = None,
        prompt: str = None,
        width: int = 768,
        height: int = 768,
        num_inference_steps: int = 2,
        seed: int = 0,
        randomize_seed: bool = True,
        **kwargs
    ) -> AsyncResult:
        """Асинхронно генерирует изображения на основе текстового запроса, используя API Black Forest Labs Flux-1-Schnell.

        Args:
            model (str): Название модели для генерации изображения.
            messages (Messages): Список сообщений, используемых для формирования запроса (обычно содержит текстовый запрос).
            proxy (str, optional): URL прокси-сервера для использования. По умолчанию `None`.
            prompt (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
            width (int, optional): Ширина изображения в пикселях. По умолчанию 768.
            height (int, optional): Высота изображения в пикселях. По умолчанию 768.
            num_inference_steps (int, optional): Количество шагов инференса. По умолчанию 2.
            seed (int, optional): Зерно для воспроизводимости результатов. По умолчанию 0.
            randomize_seed (bool, optional): Флаг для рандомизации зерна. По умолчанию `True`.
            **kwargs: Дополнительные параметры.

        Returns:
            AsyncResult: Асинхронный генератор, возвращающий URL сгенерированного изображения.

        Raises:
            ResponseError: Если API возвращает ошибку.

        """
        ...
```

**Назначение**: Создание асинхронного генератора для получения изображений от API Black Forest Labs Flux-1-Schnell.

**Параметры**:
- `model` (str): Модель, используемая для генерации изображения.
- `messages` (Messages): Список сообщений, используемых для формирования запроса (текстовый запрос).
- `proxy` (str, optional): URL прокси-сервера (если требуется). По умолчанию `None`.
- `prompt` (str, optional): Текстовый запрос для генерации изображения. По умолчанию `None`.
- `width` (int, optional): Ширина изображения в пикселях. По умолчанию 768.
- `height` (int, optional): Высота изображения в пикселях. По умолчанию 768.
- `num_inference_steps` (int, optional): Количество шагов инференса. По умолчанию 2.
- `seed` (int, optional): Зерно для воспроизводимости результатов. По умолчанию 0.
- `randomize_seed` (bool, optional): Флаг для рандомизации зерна. По умолчанию `True`.
- `**kwargs`: Дополнительные параметры.

**Возвращает**:
- `AsyncResult`: Асинхронный генератор, возвращающий URL сгенерированного изображения.

**Вызывает исключения**:
- `ResponseError`: Если API возвращает ошибку.

**Как работает функция**:

1. **Подготовка параметров**:
   - Функция принимает различные параметры, такие как модель, сообщения, прокси, текстовый запрос, ширину, высоту, количество шагов инференса, зерно и флаг рандомизации зерна.
   -  Ширина и высота корректируются, чтобы быть кратными 8 и не меньше 32.
   - Форматируется текстовый запрос на основе предоставленных сообщений.

2. **Формирование payload**:
   - Создается словарь `payload` с данными для отправки в API, включая текстовый запрос, зерно, флаг рандомизации зерна, ширину, высоту и количество шагов инференса.

3. **Взаимодействие с API**:
   - Используется асинхронная сессия для выполнения POST-запроса к API `cls.api_endpoint` с сформированным `payload`.
   - Вызывается `raise_for_status` для проверки статуса ответа и выбрасывания исключения в случае ошибки.

4. **Получение и обработка данных**:
   - Полученные данные преобразуются в JSON-формат и извлекается `event_id`.
   - Запускается бесконечный цикл для получения обновлений статуса запроса.

5. **Цикл обработки событий**:
   - Внутри цикла выполняется GET-запрос к API статуса `f"{cls.api_endpoint}/{event_id}"`.
   - Читаются данные из ответа до тех пор, пока не будет достигнут конец содержимого (`status_response.content.at_eof()`).
   - Каждая строка, заканчивающаяся на `b'\n\n'`, интерпретируется как событие.
   - Если событие начинается с `b'event:'`, происходит разделение строки на части для извлечения типа события и данных.

6. **Обработка различных типов событий**:
   - Если тип события `b'error'`, выбрасывается исключение `ResponseError` с сообщением об ошибке.
   - Если тип события `b'complete'`, данные преобразуются из JSON-формата, извлекается URL изображения и генерируется `ImageResponse`, который возвращается через `yield`. После этого функция завершается.

```
Подготовка параметров
↓
Формирование payload
↓
Взаимодействие с API
│
└──> Проверка статуса ответа
│   │
│   └──> Ошибка: ResponseError
│   │
│   └──> Успех: Получение event_id
│
Цикл обработки событий
│
└──> GET-запрос к API статуса
│   │
│   └──> Чтение данных из ответа
│   │
│   └──> Разделение строки на части
│   │
│   └──> Определение типа события
│       │
│       ├──> error: ResponseError
│       │
│       └──> complete: ImageResponse
│
Завершение
```

**Примеры**:

```python
# Пример 1: Генерация изображения с использованием минимальных параметров
result = BlackForestLabs_Flux1Schnell.create_async_generator(
    model="black-forest-labs-flux-1-schnell",
    messages=[{"role": "user", "content": "A cat in a hat"}]
)

# Пример 2: Генерация изображения с указанием размеров и зерна
result = BlackForestLabs_Flux1Schnell.create_async_generator(
    model="black-forest-labs-flux-1-schnell",
    messages=[{"role": "user", "content": "A dog playing guitar"}],
    width=512,
    height=512,
    seed=42
)

# Пример 3: Генерация изображения с использованием прокси
result = BlackForestLabs_Flux1Schnell.create_async_generator(
    model="black-forest-labs-flux-1-schnell",
    messages=[{"role": "user", "content": "A bird singing a song"}],
    proxy="http://your-proxy-url:8080"
)