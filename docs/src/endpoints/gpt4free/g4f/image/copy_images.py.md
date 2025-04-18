# Модуль для копирования изображений
## Обзор

Модуль `copy_images.py` предназначен для скачивания и сохранения изображений локально, обеспечивая безопасные имена файлов с поддержкой Unicode. Он включает в себя функции для обработки различных типов медиа, проверки форматов файлов и создания URL-адресов для доступа к сохраненным медиафайлам.

## Подробней

Этот модуль играет важную роль в проекте `hypotez`, поскольку обеспечивает возможность сохранения медиаконтента (изображений, аудио, видео) локально. Это может быть полезно для различных целей, таких как кэширование контента, обработка медиафайлов и предоставление доступа к ним через локальные URL-адреса. Модуль обрабатывает различные типы медиа, проверяет их форматы и генерирует безопасные имена файлов.

## Функции

### `get_media_extension`

```python
def get_media_extension(media: str) -> str:
    """Extract media file extension from URL or filename"""
```

**Назначение**: Извлекает расширение медиафайла из URL или имени файла.

**Параметры**:

- `media` (str): URL или имя файла медиа.

**Возвращает**:

- `str`: Расширение файла (например, ".jpg", ".mp3"). Возвращает пустую строку, если расширение не найдено.

**Вызывает исключения**:

- `ValueError`: Если расширение файла не поддерживается.

**Как работает функция**:

1.  Парсит URL, чтобы извлечь путь.
2.  Извлекает расширение файла из пути или имени файла.
3.  Проверяет, поддерживается ли расширение.
4.  Возвращает расширение файла.

```
URL_парсинг --> Извлечение_расширения --> Проверка_поддержки --> Возврат_расширения
```

**Примеры**:

```python
>>> get_media_extension("https://example.com/image.jpg")
'.jpg'
>>> get_media_extension("audio.mp3")
'.mp3'
```

### `ensure_images_dir`

```python
def ensure_images_dir():
    """Create images directory if it doesn't exist"""
```

**Назначение**: Создает директорию для изображений, если она не существует.

**Как работает функция**:

1.  Проверяет, существует ли директория `images_dir`.
2.  Если директория не существует, создает ее.
3.  Если директория существует - ничего не делает

```
Проверка_существования_директории --> Создание_директории_(если_не_существует)
```

### `get_source_url`

```python
def get_source_url(image: str, default: str = None) -> str:
    """Extract original URL from image parameter if present"""
```

**Назначение**: Извлекает исходный URL из параметра image, если он присутствует.

**Параметры**:

-   `image` (str): Строка, содержащая URL изображения.
-   `default` (Optional[str], optional): Значение по умолчанию, которое возвращается, если URL не найден. По умолчанию `None`.

**Возвращает**:

-   `str`: Исходный URL изображения или значение по умолчанию, если URL не найден.

**Как работает функция**:

1.  Проверяет, содержит ли параметр `image` строку "url=".
2.  Если содержит, извлекает URL из параметра `image`.
3.  Проверяет, начинается ли извлеченный URL с "http://" или "https://".
4.  Если начинается, возвращает извлеченный URL.
5.  Если URL не найден, возвращает значение по умолчанию.

```
Проверка_наличия_URL --> Извлечение_URL --> Проверка_формата_URL --> Возврат_URL
```

**Примеры**:

```python
>>> get_source_url("image.jpg?url=https://example.com/image.jpg")
'https://example.com/image.jpg'
>>> get_source_url("image.jpg", "https://example.com/default.jpg")
'https://example.com/default.jpg'
```

### `is_valid_media_type`

```python
def is_valid_media_type(content_type: str) -> bool:
    return content_type in MEDIA_TYPE_MAP or content_type.startswith("audio/") or content_type.startswith("video/")
```

**Назначение**: Проверяет, является ли тип контента допустимым медиа типом.

**Параметры**:

-   `content_type` (str): Тип контента для проверки.

**Возвращает**:

-   `bool`: `True`, если тип контента является допустимым медиа типом, `False` в противном случае.

**Как работает функция**:

1.  Проверяет, содержится ли тип контента в `MEDIA_TYPE_MAP`.
2.  Проверяет, начинается ли тип контента с "audio/" или "video/".
3.  Если хотя бы одно из условий выполняется, возвращает `True`.
4.  В противном случае возвращает `False`.

```
Проверка_в_MEDIA_TYPE_MAP --> Проверка_префикса_audio_video --> Возврат_результата
```

**Примеры**:

```python
>>> is_valid_media_type("image/jpeg")
True
>>> is_valid_media_type("audio/mpeg")
True
>>> is_valid_media_type("text/html")
False
```

### `save_response_media`

```python
async def save_response_media(response: StreamResponse, prompt: str, tags: list[str]) -> AsyncIterator:
    """Save media from response to local file and return URL"""
```

**Назначение**: Сохраняет медиафайл из ответа на локальный файл и возвращает URL.

**Параметры**:

-   `response` (StreamResponse): Ответ от сервера.
-   `prompt` (str): Описание изображения.
-   `tags` (list[str]): Список тегов.

**Возвращает**:

-   `AsyncIterator`: Асинхронный итератор, возвращающий объект `ImageResponse`, `AudioResponse` или `VideoResponse`.

**Вызывает исключения**:

-   `ValueError`: Если тип медиа не поддерживается.

**Как работает функция**:

1.  Определяет тип контента из заголовков ответа.
2.  Извлекает расширение файла на основе типа контента.
3.  Генерирует имя файла с использованием тегов, описания и расширения.
4.  Сохраняет содержимое ответа в локальный файл.
5.  Создает URL для доступа к сохраненному файлу.
6.  Возвращает объект `ImageResponse`, `AudioResponse` или `VideoResponse` с URL.

```
Определение_типа_контента --> Извлечение_расширения --> Генерация_имени_файла --> Сохранение_файла --> Создание_URL --> Возврат_объекта_ответа
```

### `get_filename`

```python
def get_filename(tags: list[str], alt: str, extension: str, image: str) -> str:
    return "".join((
        f"{int(time.time())}_",
        f"{secure_filename('+'.join([tag for tag in tags if tag]))}+" if tags else "",
        f"{secure_filename(alt)}_",
        hashlib.sha256(image.encode()).hexdigest()[:16],
        extension
    ))
```

**Назначение**: Генерирует имя файла на основе тегов, альтернативного текста, расширения и хеша изображения.

**Параметры**:

-   `tags` (list[str]): Список тегов.
-   `alt` (str): Альтернативный текст.
-   `extension` (str): Расширение файла.
-   `image` (str): Изображение.

**Возвращает**:

-   `str`: Сгенерированное имя файла.

**Как работает функция**:

1.  Генерирует временную метку.
2.  Генерирует безопасную строку из тегов.
3.  Генерирует безопасную строку из альтернативного текста.
4.  Вычисляет SHA256 хеш изображения и берет первые 16 символов.
5.  Объединяет все компоненты в имя файла.

```
Генерация_временной_метки --> Генерация_безопасной_строки_из_тегов --> Генерация_безопасной_строки_из_альтернативного_текста --> Вычисление_хеша_изображения --> Объединение_компонентов
```

**Примеры**:

```python
>>> get_filename(["tag1", "tag2"], "alt_text", ".jpg", "image_data")
'1678886400_tag1+tag2+alt_text_a1b2c3d4e5f67890.jpg'
```

### `copy_media`

```python
async def copy_media(
    images: list[str],\
    cookies: Optional[Cookies] = None,\
    headers: Optional[dict] = None,\
    proxy: Optional[str] = None,\
    alt: str = None,\
    tags: list[str] = None,\
    add_url: bool = True,\
    target: str = None,\
    ssl: bool = None\
) -> list[str]:
    """
    Download and store images locally with Unicode-safe filenames
    Returns list of relative image URLs
    """
```

**Назначение**: Загружает и сохраняет изображения локально с безопасными именами файлов, поддерживающими Unicode. Возвращает список относительных URL-адресов изображений.

**Параметры**:

-   `images` (list[str]): Список URL-адресов изображений для загрузки.
-   `cookies` (Optional[Cookies], optional): Файлы cookie для использования при загрузке изображений. По умолчанию `None`.
-   `headers` (Optional[dict], optional): Заголовки для использования при загрузке изображений. По умолчанию `None`.
-   `proxy` (Optional[str], optional): Прокси-сервер для использования при загрузке изображений. По умолчанию `None`.
-   `alt` (str, optional): Альтернативный текст для использования при создании имени файла. По умолчанию `None`.
-   `tags` (list[str], optional): Список тегов для использования при создании имени файла. По умолчанию `None`.
-   `add_url` (bool, optional): Добавлять ли исходный URL в URL-адрес локального файла. По умолчанию `True`.
-   `target` (str, optional): Целевой путь для сохранения изображений. По умолчанию `None`.
-   `ssl` (bool, optional): Использовать ли SSL при загрузке изображений. По умолчанию `None`.

**Возвращает**:

-   `list[str]`: Список относительных URL-адресов загруженных изображений.

**Внутренние функции**:

#### `copy_image`

```python
async def copy_image(image: str, target: str = None) -> str:
    """Process individual image and return its local URL"""
```

**Назначение**: Обрабатывает отдельное изображение и возвращает его локальный URL.

**Параметры**:

-   `image` (str): URL-адрес изображения для обработки.
-   `target` (str, optional): Целевой путь для сохранения изображения. По умолчанию `None`.

**Возвращает**:

-   `str`: Локальный URL-адрес обработанного изображения.

**Как работает функция**:

1.  Проверяет, является ли изображение локальным. Если да, возвращает его.
2.  Определяет целевой путь для сохранения изображения.
3.  Обрабатывает различные типы изображений (data URI, URL).
4.  Загружает изображение и сохраняет его в локальный файл.
5.  Проверяет формат файла и переименовывает его, если необходимо.
6.  Создает URL-адрес для доступа к сохраненному файлу.
7.  Возвращает URL-адрес.

```
Проверка_локальности_изображения --> Определение_целевого_пути --> Обработка_типа_изображения --> Загрузка_и_сохранение --> Проверка_формата --> Создание_URL --> Возврат_URL
```

**Как работает функция `copy_media`**:

1.  Инициализирует асинхронную сессию `ClientSession` с заданными параметрами (proxy, cookies, headers).
2.  Определяет, нужно ли добавлять исходный URL в URL-адрес локального файла.
3.  Создает директорию для изображений, если она не существует.
4.  Определяет асинхронную функцию `copy_image` для обработки каждого изображения.
5.  Параллельно обрабатывает все изображения с использованием `asyncio.gather`.
6.  Возвращает список локальных URL-адресов обработанных изображений.

```
Инициализация_асинхронной_сессии --> Определение_параметра_add_url --> Создание_директории --> Определение_copy_image --> Параллельная_обработка_изображений --> Возврат_списка_URL
```

**Примеры**:

```python
>>> asyncio.run(copy_media(["https://example.com/image.jpg"], tags=["tag1", "tag2"], alt="alt_text"))
['/media/1678886400_tag1+tag2+alt_text_a1b2c3d4e5f67890.jpg?url=https%3A//example.com/image.jpg']