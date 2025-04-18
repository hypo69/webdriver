# Модуль запуска Telegram-бота для работы с фильмами
## Обзор

Модуль `run.py` является точкой входа для запуска Telegram-бота, предназначенного для работы с информацией о фильмах. Он инициализирует и запускает бота, используя библиотеку `aiogram` для обработки входящих сообщений и взаимодействия с пользователями. Модуль загружает переменные окружения из файла `.dotenv`, настраивает логирование и включает обработчики сообщений.

## Подробнее

Данный модуль играет важную роль в проекте, так как обеспечивает запуск и непрерывную работу Telegram-бота. Он использует `aiogram` для создания и управления ботом, а также подключает промежуточное ПО (middleware) для ограничения частоты запросов (throttling). Логирование необходимо для отслеживания работы бота и выявления возможных проблем.

## Функции

### `main`

```python
async def main() -> None:
    """ Асинхронная функция для запуска Telegram-бота.

    Args:
        None

    Returns:
        None

    Raises:
        Нет. Функция выполняет запуск бота и не предполагает выброса исключений.
    """
```

**Назначение**:
Функция `main` является точкой входа для асинхронного запуска Telegram-бота. Она создает экземпляр бота, подключает промежуточное ПО для ограничения частоты запросов, включает обработчики сообщений и запускает процесс получения обновлений от Telegram.

**Как работает функция**:

1.  **Инициализация бота**: Создает экземпляр бота `aiogram.Bot` с использованием токена, полученного из переменных окружения.

2.  **Подключение middleware**: Добавляет промежуточное ПО `ThrottlingMiddleware` для ограничения частоты запросов, чтобы предотвратить злоупотребление ботом.

3.  **Подключение обработчиков**: Включает маршрутизатор (`router`) с обработчиками сообщений, который определяет, как бот будет реагировать на различные типы входящих сообщений.

4.  **Запуск polling**: Запускает процесс `start_polling`, который непрерывно опрашивает Telegram на предмет новых сообщений и передает их в обработчики.

**ASCII flowchart**:

```
Инициализация бота
     ↓
Подключение middleware
     ↓
Подключение обработчиков
     ↓
Запуск polling
```

**Примеры**:

Запуск функции `main` не требует параметров:

```python
import asyncio
asyncio.run(main())
```

## Запуск модуля

```python
if __name__ == "__main__":
    logging.basic_colorized_config(
        level=logging.INFO,
        format='%(asctime)s - [%(levelname)s] - %(name)s - '
               '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s',
        datefmt='%H:%M:%S'
    )
    asyncio.run(main())
```

**Назначение**:
Этот блок кода запускает основную функцию `main` при непосредственном запуске скрипта. Он также настраивает логирование для отображения информационных сообщений в консоли.

**Как работает**:

1.  **Проверка `__name__`**: Условие `if __name__ == "__main__":` проверяет, запущен ли скрипт как основной модуль.
2.  **Настройка логирования**: Функция `logging.basic_colorized_config` настраивает базовый формат логирования, включая уровень логирования, формат сообщений и формат даты.
3.  **Запуск `main`**: Функция `asyncio.run(main())` запускает асинхронную функцию `main`, которая инициализирует и запускает Telegram-бота.