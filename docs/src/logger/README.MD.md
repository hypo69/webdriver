# Документация для модуля `src.logger`

## Обзор

Модуль `src.logger` предоставляет гибкую систему логирования, поддерживающую логирование в консоль, файлы и JSON. Он использует паттерн проектирования Singleton, чтобы гарантировать использование только одного экземпляра логгера во всем приложении. Логгер поддерживает различные уровни логирования (например, `INFO`, `ERROR`, `DEBUG`) и включает цветной вывод для консольных логов. Вы также можете настраивать форматы вывода логов и управлять логированием в разные файлы.

## Подробнее

Этот модуль предоставляет комплексную и гибкую систему логирования для Python-приложений. Вы можете настроить логирование в консоль и файлы с различными форматами и цветами, управлять уровнями логирования и корректно обрабатывать исключения. Конфигурация для файлового логирования хранится в словаре `config`, что позволяет легко настраивать параметры.

## Содержание

- [Классы](#классы)
  - [SingletonMeta](#singletonmeta)
  - [JsonFormatter](#jsonformatter)
  - [Logger](#logger)
- [Функции](#функции)
  - [`__init__`](#__init__)
  - [`_configure_logger`](#_configure_logger)
  - [`initialize_loggers`](#initialize_loggers)
  - [`log`](#log)
  - [`info`](#info)
  - [`success`](#success)
  - [`warning`](#warning)
  - [`debug`](#debug)
  - [`error`](#error)
  - [`critical`](#critical)
- [Параметры для логгера](#параметры-для-логгера)
- [Конфигурация файлового логирования (`config`)](#конфигурация-файлового-логирования-config)
- [Пример использования](#пример-использования)

## Классы

### `SingletonMeta`

**Описание**:
Метакласс, реализующий паттерн Singleton для логгера. Это гарантирует, что только один экземпляр логгера будет существовать во всем приложении.

### `JsonFormatter`

**Описание**:
Пользовательский форматтер, который выводит логи в формате JSON.

### `Logger`

**Описание**:
Основной класс логгера, который поддерживает логирование в консоль, файлы и JSON.

**Методы**:
- [`__init__`](#__init__): Инициализирует экземпляр логгера с заполнителями для различных типов логгеров (консоль, файл и JSON).
- [`_configure_logger`](#_configure_logger): Настраивает и возвращает экземпляр логгера.
- [`initialize_loggers`](#initialize_loggers): Инициализирует логгеры для консоли и файлового логирования (info, debug, error и JSON).
- [`log`](#log): Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможностью добавления исключения и цветового форматирования.
- [`info`](#info): Записывает информационное сообщение.
- [`success`](#success): Записывает сообщение об успехе.
- [`warning`](#warning): Записывает предупреждающее сообщение.
- [`debug`](#debug): Записывает отладочное сообщение.
- [`error`](#error): Записывает сообщение об ошибке.
- [`critical`](#critical): Записывает критическое сообщение.

## Функции

### `__init__`

```python
def __init__() -> None:
    """
    Инициализирует экземпляр Logger с заполнителями для различных типов логгеров (консоль, файл и JSON).
    """
    ...
```

**Назначение**:
Инициализирует экземпляр класса `Logger`.

**Как работает функция**:
1. Инициализирует атрибуты экземпляра, такие как `console_logger`, `file_loggers` и `json_logger`, устанавливая их в `None`. Это создает основу для дальнейшей настройки логгеров разных типов.

**Примеры**:
```python
logger = Logger()
```

### `_configure_logger`

```python
def _configure_logger(name: str, log_path: str, level: Optional[int] = logging.DEBUG, formatter: Optional[logging.Formatter] = None, mode: Optional[str] = 'a') -> logging.Logger:
    """
    Настраивает и возвращает экземпляр логгера.

    Args:
        name (str): Имя логгера.
        log_path (str): Путь к файлу логов.
        level (Optional[int]): Уровень логирования, например, `logging.DEBUG`. По умолчанию `logging.DEBUG`.
        formatter (Optional[logging.Formatter]): Пользовательский форматтер (необязательно).
        mode (Optional[str]): Режим файла, например, `'a'` для добавления (по умолчанию).

    Returns:
        logging.Logger: Настроенный экземпляр `logging.Logger`.
    """
    ...
```

**Назначение**:
Создает и настраивает экземпляр логгера с заданными параметрами.

**Параметры**:
- `name` (str): Имя логгера. Используется для идентификации логгера.
- `log_path` (str): Путь к файлу, в который будут записываться логи.
- `level` (Optional[int]): Уровень логирования (например, `logging.DEBUG`, `logging.INFO`, `logging.ERROR`). Определяет, какие сообщения будут записываться в лог. По умолчанию `logging.DEBUG`.
- `formatter` (Optional[logging.Formatter]): Форматтер для сообщений лога. Если не указан, используется формат по умолчанию.
- `mode` (Optional[str]): Режим открытия файла лога (например, `'a'` для добавления, `'w'` для перезаписи). По умолчанию `'a'`.

**Возвращает**:
- `logging.Logger`: Настроенный экземпляр логгера.

**Как работает функция**:

```
A[Получение базового логгера]
|
B[Настройка уровня логирования]
|
C[Создание файлового обработчика]
|
D[Установка форматтера для обработчика]
|
E[Добавление обработчика к логгеру]
|
F[Возврат настроенного логгера]
```

1.  **Получение базового логгера (`A`)**:
    -   Использует `logging.getLogger(name)` для получения экземпляра логгера с указанным именем. Если логгер с таким именем уже существует, возвращает его; иначе создает новый.

2.  **Настройка уровня логирования (`B`)**:
    -   Устанавливает уровень логирования для логгера с помощью `logger.setLevel(level)`. Это определяет, какие сообщения будут обрабатываться (например, если уровень установлен на `logging.INFO`, то сообщения с уровнем `DEBUG` будут игнорироваться).

3.  **Создание файлового обработчика (`C`)**:
    -   Создает экземпляр `logging.FileHandler(log_path, mode=mode)` для записи логов в файл. Указывается путь к файлу и режим открытия файла (например, `'a'` для добавления в конец файла или `'w'` для перезаписи файла).

4.  **Установка форматтера для обработчика (`D`)**:
    -   Если указан пользовательский форматтер (`formatter`), он устанавливается для файлового обработчика с помощью `file_handler.setFormatter(formatter)`. Если форматтер не указан, используется форматтер по умолчанию.

5.  **Добавление обработчика к логгеру (`E`)**:
    -   Файловый обработчик добавляется к логгеру с помощью `logger.addHandler(file_handler)`. Это позволяет логгеру направлять сообщения в указанный файл.

6.  **Возврат настроенного логгера (`F`)**:
    -   Возвращает настроенный экземпляр логгера.

**Примеры**:
```python
logger = _configure_logger('my_logger', 'logs/my_log.log', level=logging.INFO)
```

### `initialize_loggers`

```python
def initialize_loggers(info_log_path: Optional[str] = '', debug_log_path: Optional[str] = '', errors_log_path: Optional[str] = '', json_log_path: Optional[str] = '') -> None:
    """
    Инициализирует логгеры для консоли и файлового логирования (info, debug, error и JSON).

    Args:
        info_log_path (Optional[str]): Путь к файлу для информационных логов (необязательно).
        debug_log_path (Optional[str]): Путь к файлу для отладочных логов (необязательно).
        errors_log_path (Optional[str]): Путь к файлу для логов ошибок (необязательно).
        json_log_path (Optional[str]): Путь к файлу для JSON-логов (необязательно).
    """
    ...
```

**Назначение**:
Инициализирует и настраивает различные логгеры для записи логов в файлы разных уровней (info, debug, error) и в формате JSON.

**Параметры**:
- `info_log_path` (Optional[str]): Путь к файлу для записи информационных логов. Если не указан, логи уровня INFO не будут записываться в файл.
- `debug_log_path` (Optional[str]): Путь к файлу для записи отладочных логов. Если не указан, логи уровня DEBUG не будут записываться в файл.
- `errors_log_path` (Optional[str]): Путь к файлу для записи логов ошибок. Если не указан, логи уровня ERROR не будут записываться в файл.
- `json_log_path` (Optional[str]): Путь к файлу для записи логов в формате JSON. Если не указан, JSON-логи не будут записываться в файл.

**Как работает функция**:
```
A[Настройка консольного логгера]
|
B[Настройка файловых логгеров (info, debug, error, json)]
```

1.  **Настройка консольного логгера (`A`)**:

    *   Создает и настраивает консольный логгер (`console_logger`), который будет выводить логи в консоль.
    *   Устанавливает уровень логирования для консольного логгера на `logging.DEBUG`, чтобы все сообщения (DEBUG, INFO, WARNING, ERROR, CRITICAL) выводились в консоль.
    *   Настраивает форматтер для консольного логгера, добавляя информацию о времени, уровне логирования и сообщении.

2.  **Настройка файловых логгеров (info, debug, error, json) (`B`)**:

    *   Для каждого из уровней логирования (info, debug, error) и для JSON-логирования проверяет, указан ли путь к файлу.
    *   Если путь указан, создает и настраивает файловый логгер с использованием функции `_configure_logger`.
    *   Для JSON-логгера использует форматтер `JsonFormatter`, чтобы логи записывались в формате JSON.

**Примеры**:
```python
initialize_loggers(
    info_log_path='logs/info.log',
    debug_log_path='logs/debug.log',
    errors_log_path='logs/errors.log',
    json_log_path='logs/log.json'
)
```

### `log`

```python
def log(level: int, message: str, ex: Optional[Exception] = None, exc_info: bool = False, color: Optional[tuple] = None) -> None:
    """
    Записывает сообщение на указанном уровне (например, `INFO`, `DEBUG`, `ERROR`) с возможностью добавления исключения и цветового форматирования.

    Args:
        level (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`).
        message (str): Сообщение лога.
        ex (Optional[Exception]): Исключение для логирования (необязательно).
        exc_info (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
        color (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
    ...
```

**Назначение**:
Записывает логи с указанным уровнем, сообщением, информацией об исключении и цветом.

**Параметры**:
- `level` (int): Уровень логирования (например, `logging.INFO`, `logging.DEBUG`, `logging.ERROR`).
- `message` (str): Сообщение, которое нужно записать в лог.
- `ex` (Optional[Exception]): Исключение, которое нужно записать в лог (если есть).
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении (стек вызовов и т.д.).
- `color` (Optional[tuple]): Кортеж, содержащий цвет текста и цвет фона для консольного вывода.

**Как работает функция**:
```
A[Форматирование сообщения]
|
B[Логирование в консоль]
|
C[Логирование в файл (если настроено)]
|
D[Логирование в JSON (если настроено)]
```

1.  **Форматирование сообщения (`A`)**:
    -   Формирует сообщение для логирования, добавляя информацию об исключении, если оно передано и установлен флаг `exc_info`.

2.  **Логирование в консоль (`B`)**:
    -   Если консольный логгер (`console_logger`) существует, записывает сообщение в консоль с использованием указанного уровня логирования и цвета (если указан).

3.  **Логирование в файл (если настроено) (`C`)**:
    -   Если файловые логгеры (`file_loggers`) настроены, проверяет, существует ли логгер для указанного уровня.
    -   Если логгер существует, записывает сообщение в файл с использованием указанного уровня логирования.

4.  **Логирование в JSON (если настроено) (`D`)**:
    -   Если JSON-логгер (`json_logger`) существует, формирует словарь с уровнем логирования, сообщением и информацией об исключении (если есть).
    -   Записывает словарь в JSON-файл.

**Примеры**:
```python
log(logging.INFO, 'This is an info message')
log(logging.ERROR, 'This is an error message', ex=ValueError('Invalid value'), exc_info=True)
log(logging.DEBUG, 'This is a debug message', color=(colorama.Fore.GREEN, colorama.Back.BLACK))
```

### `info`

```python
def info(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Записывает информационное сообщение.

    Args:
        message (str): Информационное сообщение для логирования.
        ex (Optional[Exception]): Исключение для логирования (необязательно).
        exc_info (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
    ...
```

**Назначение**:
Записывает сообщение с уровнем логирования `INFO`.

**Параметры**:
- `message` (str): Информационное сообщение для логирования.
- `ex` (Optional[Exception]): Исключение для логирования (необязательно).
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.INFO` и переданными параметрами.

**Примеры**:
```python
info('This is an info message')
info('This is an info message with exception', ex=ValueError('Invalid value'))
info('This is an info message with color', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
```

### `success`

```python
def success(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Записывает сообщение об успехе.

    Args:
        message (str): Сообщение об успехе для логирования.
        ex (Optional[Exception]): Исключение для логирования (необязательно).
        exc_info (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
    ...
```

**Назначение**:
Записывает сообщение с уровнем логирования, который можно интерпретировать как "успех".  Функция, по сути, вызывает `log` с уровнем `logging.INFO`.

**Параметры**:
- `message` (str): Сообщение об успехе для логирования.
- `ex` (Optional[Exception]): Исключение для логирования (необязательно).
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.INFO` и переданными параметрами.

**Примеры**:
```python
success('Operation completed successfully')
success('File created', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
```

### `warning`

```python
def warning(message: str, ex: Optional[Exception] = None, exc_info: bool = False, colors: Optional[tuple] = None) -> None:
    """
    Записывает предупреждающее сообщение.

    Args:
        message (str): Предупреждающее сообщение для логирования.
        ex (Optional[Exception]): Исключение для логирования (необязательно).
        exc_info (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
        colors (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
    ...
```

**Назначение**:
Записывает сообщение с уровнем логирования `WARNING`.

**Параметры**:
- `message` (str): Предупреждающее сообщение для логирования.
- `ex` (Optional[Exception]): Исключение для логирования (необязательно).
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `False`).
- `colors` (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.WARNING` и переданными параметрами.

**Примеры**:
```python
warning('This is a warning message')
warning('This is a warning message with exception', ex=UserWarning('Something went wrong'))
```

### `debug`

```python
def debug(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Записывает отладочное сообщение.

    Args:
        message (str): Отладочное сообщение для логирования.
        ex (Optional[Exception]): Исключение для логирования (необязательно).
        exc_info (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
    ...
```

**Назначение**:
Записывает сообщение с уровнем логирования `DEBUG`.

**Параметры**:
- `message` (str): Отладочное сообщение для логирования.
- `ex` (Optional[Exception]): Исключение для логирования (необязательно).
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.DEBUG` и переданными параметрами.

**Примеры**:
```python
debug('This is a debug message')
debug('This is a debug message with exception', ex=Exception('Some debug exception'))
```

### `error`

```python
def error(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Записывает сообщение об ошибке.

    Args:
        message (str): Сообщение об ошибке для логирования.
        ex (Optional[Exception]): Исключение для логирования (необязательно).
        exc_info (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
    ...
```

**Назначение**:
Записывает сообщение с уровнем логирования `ERROR`.

**Параметры**:
- `message` (str): Сообщение об ошибке для логирования.
- `ex` (Optional[Exception]): Исключение для логирования (необязательно).
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.ERROR` и переданными параметрами.

**Примеры**:
```python
error('This is an error message')
error('This is an error message with exception', ex=IOError('File not found'))
```

### `critical`

```python
def critical(message: str, ex: Optional[Exception] = None, exc_info: bool = True, colors: Optional[tuple] = None) -> None:
    """
    Записывает критическое сообщение.

    Args:
        message (str): Критическое сообщение для логирования.
        ex (Optional[Exception]): Исключение для логирования (необязательно).
        exc_info (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `True`).
        colors (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).
    """
    ...
```

**Назначение**:
Записывает сообщение с уровнем логирования `CRITICAL`.

**Параметры**:
- `message` (str): Критическое сообщение для логирования.
- `ex` (Optional[Exception]): Исключение для логирования (необязательно).
- `exc_info` (bool): Флаг, указывающий, нужно ли включать информацию об исключении (по умолчанию `True`).
- `colors` (Optional[tuple]): Кортеж с цветами текста и фона для вывода в консоль (необязательно).

**Как работает функция**:
Вызывает функцию `log` с уровнем логирования `logging.CRITICAL` и переданными параметрами.

**Примеры**:
```python
critical('This is a critical message')
critical('This is a critical message with exception', ex=RuntimeError('Critical error'))
```

## Параметры для логгера

Класс `Logger` принимает несколько необязательных параметров для настройки поведения логирования.

- **Level**: Управляет серьезностью регистрируемых логов. Общие уровни включают:
  - `logging.DEBUG`: Подробная информация, полезная для диагностики проблем.
  - `logging.INFO`: Общая информация, такая как успешные операции.
  - `logging.WARNING`: Предупреждения, которые не обязательно требуют немедленных действий.
  - `logging.ERROR`: Сообщения об ошибках.
  - `logging.CRITICAL`: Критические ошибки, требующие немедленного внимания.

- **Formatter**: Определяет формат сообщений лога. По умолчанию сообщения форматируются как `'%(asctime)s - %(levelname)s - %(message)s'`. Вы можете предоставить пользовательский форматтер для различных форматов, таких как JSON.

- **Color**: Цвета для сообщений лога в консоли. Цвета указываются в виде кортежа с двумя элементами:
  - **Text color**: Указывает цвет текста (например, `colorama.Fore.RED`).
  - **Background color**: Указывает цвет фона (например, `colorama.Back.WHITE`).

Цвет можно настроить для разных уровней лога (например, зеленый для информации, красный для ошибок и т.д.).

## Конфигурация файлового логирования (`config`)

Чтобы записывать сообщения в файл, вы можете указать пути к файлам в конфигурации.

```python
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
```

Пути к файлам, указанные в `config`, используются для записи логов в соответствующие файлы для каждого уровня логирования.

## Пример использования

#### 1. Инициализация логгера:

```python
logger: Logger = Logger()
config = {
    'info_log_path': 'logs/info.log',
    'debug_log_path': 'logs/debug.log',
    'errors_log_path': 'logs/errors.log',
    'json_log_path': 'logs/log.json'
}
logger.initialize_loggers(**config)
```

#### 2. Запись сообщений на разных уровнях:

```python
logger.info('This is an info message')
logger.success('This is a success message')
logger.warning('This is a warning message')
logger.debug('This is a debug message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```

#### 3. Настройка цветов:

```python
logger.info('This message will be green', colors=(colorama.Fore.GREEN, colorama.Back.BLACK))
logger.error('This message will have a red background', colors=(colorama.Fore.WHITE, colorama.Back.RED))
```