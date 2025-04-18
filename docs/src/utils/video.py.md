# Модуль для работы с видеофайлами
=========================================

Модуль предоставляет асинхронные функции для скачивания и сохранения видеофайлов, а также для получения видеоданных.
Он включает обработку ошибок и логирование для обеспечения надежной работы.

Пример использования
----------------------

```python
import asyncio
asyncio.run(save_video_from_url("https://example.com/video.mp4", "local_video.mp4"))
PosixPath('local_video.mp4')  # или None, если не удалось

data = get_video_data("local_video.mp4")
if data:
    print(data[:10])  # Print first 10 bytes to check
b'\x00\x00\x00...'
```

## Обзор

Модуль `src.utils.video` предназначен для асинхронной загрузки и сохранения видеофайлов, а также для извлечения данных из видеофайлов. Он обеспечивает обработку ошибок и журналирование для обеспечения надежной работы.

## Подробнее

Этот модуль предоставляет асинхронные функции для загрузки и сохранения видеофайлов, а также для извлечения видеоданных. Он включает обработку ошибок и ведение журнала для обеспечения надежной работы.

Расположение модуля в проекте: `hypotez/src/utils/video.py`.

## Функции

### `save_video_from_url`

```python
async def save_video_from_url(url: str, save_path: str) -> Optional[Path]:
    """Скачивает видео по URL и сохраняет его локально асинхронно.

    Args:
        url (str): URL, из которого нужно скачать видео.
        save_path (str): Путь для сохранения скачанного видео.

    Returns:
        Optional[Path]: Путь к сохраненному файлу или `None`, если операция не удалась. Возвращает `None` в случае ошибок и если размер файла равен 0 байт.

    Raises:
        aiohttp.ClientError: при сетевых проблемах во время скачивания.
    """
```

**Как работает функция**:
1. Функция принимает URL-адрес видео и путь для сохранения.
2. Инициализирует асинхронную сессию клиента с помощью `aiohttp`.
3. Отправляет GET-запрос по указанному URL-адресу и проверяет наличие HTTP-ошибок.
4. Создает родительские каталоги, если они не существуют.
5. Асинхронно открывает файл по указанному пути для записи в двоичном режиме.
6. Читает содержимое ответа чанками по 8192 байт и записывает их в файл, пока не будет достигнут конец содержимого.
7. После завершения записи проверяет, был ли файл успешно сохранен и не является ли он пустым.
8. В случае успеха возвращает путь к сохраненному файлу. Если во время процесса возникают какие-либо ошибки (например, сетевые ошибки или ошибки сохранения), они регистрируются, и функция возвращает `None`.

```ascii
    Начало
     ↓
    Получение URL и пути сохранения
     ↓
    Создание асинхронной сессии
     ↓
    Отправка GET-запроса по URL
     ↓
    Проверка HTTP-статуса ответа
     ↓
    Создание родительских директорий (при необходимости)
     ↓
    Открытие файла для записи
     ↓
    Чтение и запись чанков данных
     ↓
    Проверка успешности сохранения файла
     ↓
    Проверка размера файла
     ↓
    Успех: Возврат пути к файлу / Ошибка: Логирование и возврат None
     ↓
    Конец
```

**Примеры**:

```python
import asyncio
from pathlib import Path

# Пример успешной загрузки
url = "https://example.com/video.mp4"  # Замените на реальный URL
save_path = "local_video.mp4"
result = asyncio.run(save_video_from_url(url, save_path))
if result:
    print(f"Видео успешно сохранено в {result}")

# Пример с несуществующим URL
url = "https://example.com/nonexistent_video.mp4"
save_path = "local_video.mp4"
result = asyncio.run(save_video_from_url(url, save_path))
if not result:
    print("Не удалось скачать видео")

# Пример с указанием пути сохранения в несуществующую директорию
url = "https://example.com/video.mp4"
save_path = "new_directory/local_video.mp4"
result = asyncio.run(save_video_from_url(url, save_path))
if result:
    print(f"Видео успешно сохранено в {result}")

```

### `get_video_data`

```python
def get_video_data(file_name: str) -> Optional[bytes]:
    """Извлекает бинарные данные видеофайла, если он существует.

    Args:
        file_name (str): Путь к видеофайлу для чтения.

    Returns:
        Optional[bytes]: Бинарные данные файла, если он существует, или `None`, если файл не найден или произошла ошибка.
    """
```

**Как работает функция**:
1. Функция принимает имя файла видео в качестве входных данных.
2. Преобразует имя файла в объект `Path`.
3. Проверяет, существует ли файл по указанному пути. Если файл не существует, функция регистрирует ошибку и возвращает `None`.
4. Если файл существует, функция открывает файл в двоичном режиме чтения (`"rb"`) и считывает все его содержимое.
5. В случае успеха функция возвращает содержимое файла в виде байтов. Если во время процесса возникают какие-либо ошибки (например, ошибки чтения файла), они регистрируются, и функция возвращает `None`.

```ascii
    Начало
     ↓
    Получение имени файла
     ↓
    Проверка существования файла
     ↓
    Файл существует?
     ├── Да: Открытие файла для чтения в двоичном режиме
     │    ↓
     │    Чтение содержимого файла
     │    ↓
     │    Успех: Возврат данных файла / Ошибка: Логирование и возврат None
     └── Нет: Логирование ошибки "Файл не найден" и возврат None
     ↓
    Конец
```

**Примеры**:

```python
from pathlib import Path

# Пример успешного чтения данных из файла
file_name = "local_video.mp4"  # Убедитесь, что файл существует
data = get_video_data(file_name)
if data:
    print(f"Первые 10 байт: {data[:10]}")

# Пример с несуществующим файлом
file_name = "nonexistent_video.mp4"
data = get_video_data(file_name)
if not data:
    print("Файл не найден")

# Пример с созданием файла и чтением данных
file_name = "test_video.mp4"
Path(file_name).write_bytes(b"Test video data")  # Создание файла с тестовыми данными
data = get_video_data(file_name)
if data:
    print(f"Данные из файла: {data}")

```

### `main`

```python
def main():
    url = "https://example.com/video.mp4"  # Replace with a valid URL!
    save_path = "local_video.mp4"
    result = asyncio.run(save_video_from_url(url, save_path))
    if result:
        print(f"Video saved to {result}")
```

**Как работает функция**:

1. Определяет URL-адрес видео для загрузки и путь для сохранения.
2. Запускает асинхронную функцию `save_video_from_url` для загрузки и сохранения видео.
3. Если загрузка прошла успешно, выводит сообщение об успешном сохранении видео.

**Примеры**:

```python
# Пример использования функции main
main()