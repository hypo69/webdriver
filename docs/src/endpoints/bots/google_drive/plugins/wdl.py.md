# Модуль для скачивания файлов с использованием wget

## Обзор

Модуль содержит функцию `wget_dl`, которая позволяет скачивать файлы по URL-адресу с использованием утилиты `wget`. Функция обрабатывает исключения и возвращает имя скачанного файла или сообщение об ошибке.

## Подробней

Этот модуль предоставляет простой способ скачивания файлов из интернета, используя команду `wget`. Он полезен в тех случаях, когда необходимо автоматизировать загрузку файлов в скриптах или приложениях.  `wget_dl` используется для скачивания файлов, необходимых для работы других модулей. Функция пытается скачать файл по указанному URL и возвращает имя файла или сообщение об ошибке в случае неудачи.

## Функции

### `wget_dl`

```python
def wget_dl(url: str) -> str | tuple[str, str]:
    """
    Скачивает файл по URL-адресу с использованием утилиты wget.

    Args:
        url (str): URL-адрес файла для скачивания.

    Returns:
        str | tuple[str, str]: Имя скачанного файла в случае успеха или кортеж ("error", filename) в случае ошибки.
    """
```

**Назначение**: Скачивание файла по URL-адресу с использованием утилиты `wget`.

**Параметры**:

- `url` (str): URL-адрес файла для скачивания.

**Возвращает**:

- `str | tuple[str, str]`: Имя скачанного файла в случае успеха или кортеж `("error", filename)` в случае ошибки.

**Как работает функция**:

1.  Выводит сообщение "Downloading Started" в консоль.
2.  Извлекает имя файла из URL-адреса.
3.  Использует `subprocess.check_output` для выполнения команды `wget` с указанным URL-адресом и именем файла.
4.  Выводит сообщение "Downloading Complete" и имя файла в консоль в случае успеха.
5.  Возвращает имя скачанного файла.
6.  В случае возникновения исключения выводит сообщение об ошибке в консоль и возвращает кортеж `("error", filename)`.

```
    A: Начало
    |
    B: Вывод "Downloading Started"
    |
    C: Извлечение имени файла из URL
    |
    D: Выполнение команды wget
    |
    E: Обработка результата wget
    |
    F: Вывод "Downloading Complete" и имени файла
    |
    G: Возврат имени файла
    |
    H: Обработка исключения
    |
    I: Вывод сообщения об ошибке
    |
    J: Возврат ("error", filename)
    |
    K: Конец
```

**Примеры**:

```python
# Пример успешного скачивания файла
filename = wget_dl("https://example.com/file.txt")
print(filename)  # Вывод: file.txt

# Пример неудачного скачивания файла
result = wget_dl("https://example.com/nonexistent_file.txt")
print(result)  # Вывод: ('error', 'nonexistent_file.txt')