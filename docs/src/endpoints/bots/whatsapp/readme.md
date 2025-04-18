# Документация для разработчика: Автоматизированная отправка сообщений WhatsApp

## Обзор

Этот документ описывает процесс создания и использования скрипта Python для автоматической отправки сообщений через WhatsApp. Он предназначен для разработчиков, желающих автоматизировать отправку сообщений, и содержит инструкции по установке необходимых библиотек, настройке скрипта и решению возможных проблем.

## Подробнее

Документ предоставляет пошаговое руководство по созданию скрипта, начиная с установки необходимых библиотек Python и заканчивая запуском скрипта в терминале. Он охватывает настройку пользовательского ввода, создание банка сообщений и основной цикл отправки сообщений. Особое внимание уделяется обработке исключений и решению распространенных проблем, таких как проблемы с `pywhatkit` и подключением к WhatsApp Web.

## Содержание

1.  [Введение](#введение)
    *   [Назначение](#назначение)
    *   [Целевая аудитория](#целевая-аудитория)
    *   [Предпосылки](#предпосылки)
2.  [Необходимые компоненты](#необходимые-компоненты)
    *   [Библиотеки Python](#библиотеки-python)
    *   [Зависимости](#зависимости)
    *   [Требования к системе](#требования-к-системе)
3.  [Процесс разработки](#процесс-разработки)
    *   [Функция отправки сообщений (`send_whatsapp_message`)](#функция-отправки-сообщений-send_whatsapp_message)
    *   [Банк сообщений](#банк-сообщений)
    *   [Пользовательский ввод](#пользовательский-ввод)
    *   [Основной цикл отправки](#основной-цикл-отправки)
4.  [Возможные проблемы и решения](#возможные-проблемы-и-решения)
    *   [Проблемы с `pywhatkit`](#проблемы-с-pywhatkit)
    *   [Подключение к WhatsApp Web](#подключение-к-whatsapp-web)
    *   [Динамическая задержка](#динамическая-задержка)
    *   [Зависимость от браузера и версии WhatsApp](#зависимость-от-браузера-и-версии-whatsapp)
5.  [Код (пример)](#код-пример)
6.  [Выполнение скрипта](#выполнение-скрипта)

## Введение

### Назначение

Документ описывает процесс разработки автоматизированного скрипта на языке Python, предназначенного для отправки случайных сообщений WhatsApp в течение определенного периода времени.

### Целевая аудитория

Данное руководство предназначено для разработчиков, имеющих базовые знания языка Python и понимание работы с командной строкой.

### Предпосылки

Перед использованием данного руководства необходимо наличие установленного Python 3.6+ и менеджера пакетов pip.

## Необходимые компоненты

### Библиотеки Python

*   `pywhatkit`: Для взаимодействия с веб-версией WhatsApp и отправки сообщений.
*   `pyautogui`: Для автоматизации действий мыши и клавиатуры.
*   `pynput`: Для контроля клавиатурного ввода.
*   `emoji`: Для добавления эмодзи в сообщения.
*   `random`: Для генерации случайных сообщений и времени.
*   `time`: Для управления задержками и временем выполнения.

### Зависимости

Установка указанных библиотек выполняется посредством pip:

```bash
pip install pywhatkit pyautogui pynput emoji
```

### Требования к системе

Операционная система с установленным веб-браузером (например, Chrome или Firefox) и возможностью подключения к WhatsApp Web.

## Процесс разработки

### Функция отправки сообщений (`send_whatsapp_message`)

**Назначение**: Отправляет сообщение WhatsApp на указанный номер телефона в заданное время.

**Параметры**:

*   `phone_number` (str): Номер телефона получателя (с кодом страны).
*   `message` (str): Текст сообщения.
*   `hour` (int): Час отправки сообщения (0-23).
*   `minutes` (int): Минуты отправки сообщения (0-59).

**Возвращает**:
Отсутствует

**Вызывает исключения**:
Отсутствует

**Как работает функция**:

1.  Использует `pywhatkit.sendwhatmsg` для инициализации отправки сообщения.
2.  Применяет `time.sleep` для задержки загрузки веб-версии WhatsApp.
3.  Применяет `pyautogui` и `pynput` для имитации нажатия клавиши "Enter" для отправки сообщения.
4.  Обрабатывает исключения с помощью блока `try...except` для вывода ошибок.

```
Инициализация отправки сообщения через pywhatkit
↓
Задержка для загрузки веб-версии WhatsApp
↓
Имитация нажатия клавиши "Enter"
↓
Обработка исключений
```

**Примеры**:

```python
# Пример вызова функции
# send_whatsapp_message('+79991234567', 'Привет!', 10, 30)
```

### Банк сообщений

**Назначение**: Создает и управляет списком сообщений для отправки.

**Параметры**:
Отсутствует

**Возвращает**:
Отсутствует

**Вызывает исключения**:
Отсутствует

**Как работает функция**:

1.  Создает список строк (`messages`) для хранения сообщений.
2.  Использует `emoji.emojize` для добавления эмодзи.
3.  Применяет `random.choice` для случайного выбора сообщения.

```
Создание списка сообщений
↓
Добавление эмодзи в сообщения
↓
Случайный выбор сообщения из списка
```

**Примеры**:

```python
# Пример создания списка сообщений
# messages = ['Привет!', 'Как дела?', 'Что нового?', emoji.emojize('Отличное настроение! :smile:')]
```

### Пользовательский ввод

**Назначение**: Получает от пользователя количество сообщений, начальный и конечный часы отправки.

**Параметры**:
Отсутствует

**Возвращает**:
Отсутствует

**Вызывает исключения**:
Отсутствует

**Как работает функция**:

1.  Получает количество сообщений (`num_messages`) с помощью функции `input`.
2.  Получает начальный час (`start_hour`) и конечный час (`end_hour`) диапазона отправки с помощью `input`.

```
Получение количества сообщений от пользователя
↓
Получение начального часа отправки от пользователя
↓
Получение конечного часа отправки от пользователя
```

**Примеры**:

```python
# Пример получения пользовательского ввода
# num_messages = int(input('Введите количество сообщений: '))
# start_hour = int(input('Введите начальный час отправки: '))
# end_hour = int(input('Введите конечный час отправки: '))
```

### Основной цикл отправки

**Назначение**: Отправляет сообщения в заданном количестве в указанном временном диапазоне.

**Параметры**:
Отсутствует

**Возвращает**:
Отсутствует

**Вызывает исключения**:
Отсутствует

**Как работает функция**:

1.  Цикл `while` выполняется, пока счетчик сообщений (`message_count`) не достигнет заданного количества (`num_messages`).
2.  Генерирует случайный час и минуты с помощью `random.randint`.
3.  Вызывает функцию `send_whatsapp_message` с полученными данными.
4.  Увеличивает счетчик сообщений.

```
Инициализация счетчика сообщений
↓
Цикл: пока счетчик < заданного количества сообщений
    ↓
    Генерация случайного часа и минут
    ↓
    Отправка сообщения через send_whatsapp_message
    ↓
    Увеличение счетчика сообщений
```

**Примеры**:

```python
# Пример основного цикла отправки
# message_count = 0
# while message_count < num_messages:
#     hour = random.randint(start_hour, end_hour)
#     minutes = random.randint(0, 59)
#     send_whatsapp_message('+79991234567', random.choice(messages), hour, minutes)
#     message_count += 1
```

## Возможные проблемы и решения

### Проблемы с `pywhatkit`

В случае неудачной автоматической отправки сообщения использовать `pyautogui` и `pynput` для эмуляции нажатия клавиш и отправки сообщения.

### Подключение к WhatsApp Web

При первом использовании необходимо подключение к веб-версии WhatsApp через веб-браузер.

### Динамическая задержка

Скорость загрузки веб-версии WhatsApp может меняться, поэтому для стабильности увеличьте время задержки.

### Зависимость от браузера и версии WhatsApp

Изменения в браузере или веб-версии WhatsApp могут потребовать корректировки скрипта.

## Код (пример)

```python
# ... (Код ) ...
```

## Выполнение скрипта

*   Сохраните скрипт в файл с расширением `.py`.
*   Выполните скрипт в терминале с помощью команды: `python имя_файла.py`
*   Следуйте инструкциям на экране для ввода необходимых данных.