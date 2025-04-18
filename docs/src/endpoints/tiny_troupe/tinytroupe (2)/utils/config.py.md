# Модуль конфигурации и утилит запуска TinyTroupe
## Обзор

Модуль `config.py` предназначен для чтения, обработки и предоставления конфигурационных параметров для проекта TinyTroupe. Он включает функции для чтения конфигурационных файлов (`config.ini`), отображения текущей конфигурации и запуска системы логирования.

## Подробнее

Этот модуль играет важную роль в инициализации и настройке приложения TinyTroupe. Он обеспечивает гибкость в настройке приложения, позволяя использовать как значения по умолчанию, так и пользовательские конфигурации.

## Функции

### `read_config_file`

```python
def read_config_file(use_cache: bool = True, verbose: bool = True) -> configparser.ConfigParser:
    """
    Читает файл конфигурации и возвращает объект `configparser.ConfigParser`.

    Args:
        use_cache (bool, optional): Использовать ли кэшированную конфигурацию, если она существует. По умолчанию `True`.
        verbose (bool, optional): Выводить ли отладочную информацию в консоль. По умолчанию `True`.

    Returns:
        configparser.ConfigParser: Объект конфигурации.

    Raises:
        ValueError: Если не удается найти файл конфигурации по умолчанию.
    """
```

**Назначение**: Чтение файла конфигурации.

**Параметры**:
- `use_cache` (bool): Определяет, следует ли использовать кэшированную версию конфигурации, если она доступна. Если `True`, функция попытается использовать уже загруженную конфигурацию.
- `verbose` (bool): Определяет, следует ли выводить отладочные сообщения в процессе чтения конфигурации. Если `True`, в консоль будут выводиться сообщения о поиске и загрузке файлов конфигурации.

**Возвращает**:
- `configparser.ConfigParser`: Объект `ConfigParser`, содержащий параметры конфигурации.

**Вызывает исключения**:
- `ValueError`: Вызывается, если не удается найти файл конфигурации по умолчанию (`config.ini`) в директории модуля.

**Как работает функция**:

1. **Проверяет кэш**: Если `use_cache` установлен в `True` и конфигурация уже была загружена (т.е. `_config` не `None`), функция возвращает кэшированную конфигурацию.
2. **Инициализирует ConfigParser**: Если кэш не используется или недоступен, создается новый экземпляр `configparser.ConfigParser`.
3. **Читает конфигурацию по умолчанию**: Функция пытается прочитать файл `config.ini`, расположенный в директории модуля. Если файл существует, его содержимое загружается в объект `config`.
4. **Переопределяет значения пользовательской конфигурацией**: Функция ищет файл `config.ini` в текущей рабочей директории. Если такой файл существует, его содержимое используется для переопределения значений конфигурации, загруженных из файла по умолчанию.
5. **Возвращает конфигурацию**: Функция возвращает объект `config`, содержащий объединенную конфигурацию (значения по умолчанию с переопределениями из пользовательского файла, если таковой имеется).

**ASCII схема работы функции**:

```
A [Проверка кэша: использовать кэш и _config не None?]
|
├── No  --> B [Создание ConfigParser]
|   |
|   └── Yes --> Возврат _config
|
B [Поиск файла config.ini в директории модуля]
|
├── Не найден --> C [Выброс ValueError]
|   |
|   └── Найден --> D [Чтение значений по умолчанию из config.ini]
|
D [Поиск файла config.ini в текущей рабочей директории]
|
├── Не найден --> F [Вывод сообщения об использовании значений по умолчанию]
|   |
|   └── Найден --> E [Чтение значений из пользовательского config.ini (переопределение)]
|
E [Применение пользовательских значений]
|
F [Сохранение конфигурации в кэш (_config)]
|
G [Возврат объекта config]
```

**Примеры**:

```python
# Чтение конфигурации с использованием кэша (если доступен) и выводом отладочной информации
config = read_config_file(use_cache=True, verbose=True)

# Чтение конфигурации без использования кэша и без вывода отладочной информации
config = read_config_file(use_cache=False, verbose=False)
```

### `pretty_print_config`

```python
def pretty_print_config(config: configparser.ConfigParser) -> None:
    """
    Выводит текущую конфигурацию в удобочитаемом формате.

    Args:
        config (configparser.ConfigParser): Объект конфигурации для отображения.
    """
```

**Назначение**: Вывод текущей конфигурации в удобочитаемом формате.

**Параметры**:
- `config` (configparser.ConfigParser): Объект конфигурации, который необходимо вывести.

**Возвращает**:
- `None`

**Как работает функция**:

1. **Выводит заголовок**: Функция выводит заголовок, указывающий на начало блока конфигурации.
2. **Перебирает секции**: Функция перебирает все секции в объекте `config`.
3. **Выводит значения**: Для каждой секции функция выводит имя секции и все пары ключ-значение, содержащиеся в этой секции.

**ASCII схема работы функции**:

```
A [Вывод заголовка]
|
B [Перебор секций в config]
|
C [Для каждой секции: вывод имени секции]
|
D [Перебор элементов (ключ-значение) в секции]
|
E [Вывод пары "ключ = значение"]
|
F [Конец]
```

**Примеры**:

```python
# Чтение конфигурации
config = read_config_file()

# Вывод конфигурации в консоль
pretty_print_config(config)
```

### `start_logger`

```python
def start_logger(config: configparser.ConfigParser) -> None:
    """
    Инициализирует и запускает логгер с заданным уровнем логирования.

    Args:
        config (configparser.ConfigParser): Объект конфигурации, содержащий параметры логирования.
    """
```

**Назначение**: Инициализация и запуск логгера с заданным уровнем логирования.

**Параметры**:
- `config` (configparser.ConfigParser): Объект конфигурации, содержащий параметры логирования.

**Возвращает**:
- `None`

**Как работает функция**:

1. **Получает логгер**: Функция получает экземпляр логгера с именем "tinytroupe".
2. **Определяет уровень логирования**: Функция извлекает уровень логирования из конфигурации (секция `Logging`, ключ `LOGLEVEL`). Если уровень не указан, используется уровень `INFO` по умолчанию.
3. **Устанавливает уровень логирования**: Функция устанавливает уровень логирования для логгера.
4. **Создает обработчик консоли**: Функция создает обработчик консоли (`logging.StreamHandler`) и устанавливает для него уровень логирования.
5. **Создает форматтер**: Функция создает форматтер (`logging.Formatter`), определяющий формат сообщений журнала.
6. **Добавляет форматтер к обработчику**: Функция добавляет форматтер к обработчику консоли.
7. **Добавляет обработчик к логгеру**: Функция добавляет обработчик консоли к логгеру.

**ASCII схема работы функции**:

```
A [Получение логгера "tinytroupe"]
|
B [Извлечение уровня логирования из конфигурации]
|
C [Установка уровня логирования для логгера]
|
D [Создание обработчика консоли]
|
E [Установка уровня логирования для обработчика]
|
F [Создание форматтера]
|
G [Добавление форматтера к обработчику]
|
H [Добавление обработчика к логгеру]
|
I [Конец]
```

**Примеры**:

```python
# Чтение конфигурации
config = read_config_file()

# Запуск логгера с параметрами из конфигурации
start_logger(config)