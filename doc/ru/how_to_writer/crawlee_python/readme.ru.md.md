Как использовать модуль Crawlee Python для автоматизации и сбора данных
=========================================================================================

Описание
-------------------------
Модуль `src.webdriver.crawlee_python` предоставляет кастомную реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Модуль позволяет настраивать параметры запуска браузера, обрабатывать веб-страницы и извлекать из них данные, опираясь на конфигурацию в файле `crawlee_python.json`.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
   - Убедитесь, что установлены библиотеки `playwright` и `crawlee`.
   -  Если нет, выполните команду: `pip install playwright crawlee`.
   -   Установите браузеры с помощью команды: `playwright install`.
2.  **Настройка конфигурации:**
    - Отредактируйте файл `crawlee_python.json`, чтобы настроить параметры краулера.
    - Основные параметры:
      - `max_requests`: Максимальное количество запросов для обхода (по умолчанию 10).
      -   `headless`: Запускать ли браузер в безголовом режиме (`true` или `false`, по умолчанию `true`).
      -   `browser_type`: Тип браузера (`chromium`, `firefox`, `webkit`, по умолчанию `chromium`).
      - `options`: Список дополнительных параметров командной строки для браузера.
      - `user_agent`: строка User-Agent для запросов.
      - `proxy`: настройки прокси (включен/выключен, адрес, логин, пароль).
      -   `viewport`: размеры окна браузера (`width`, `height`).
      -   `timeout`: максимальное время ожидания (в миллисекундах, по умолчанию 30000).
      -   `ignore_https_errors`: игнорировать ли ошибки HTTPS (по умолчанию `false`).
3. **Инициализация `CrawleePython`:**
    - Создайте экземпляр класса `CrawleePython`.
    - Пример:
        ```python
        import asyncio
        from src.webdriver.crawlee_python import CrawleePython
        
        async def main():
             crawler = CrawleePython(
                  max_requests=10,
                  headless=True,
                  browser_type='chromium',
                  options=['--disable-gpu']
            )
         ```
    -  Передайте параметры конфигурации, чтобы переопределить значения по умолчанию.
4.  **Настройка и запуск краулера:**
    - Метод `setup_crawler` настраивает `PlaywrightCrawler` и задает обработчик по умолчанию `request_handler`, который выполняет следующие действия:
        -  Логирует обрабатываемый URL.
        - Ставит в очередь найденные ссылки.
        -   Извлекает данные (URL, заголовок, контент).
        -  Отправляет данные в датасет.
    -   Метод `run(urls)` выполняет следующие шаги:
        - Настраивает краулер (`setup_crawler()`).
        - Запускает краулер (`run_crawler()`).
        - Экспортирует данные в файл `results.json` в директорию `gs.path.tmp` (`export_data()`).
        - Получает и логирует извлечённые данные (`get_data()`).
    - Пример:
        ```python
        await crawler.run(['https://www.example.com'])
        ```
5. **Экспорт данных:**
   -   Метод `export_data(file_path)` экспортирует данные в JSON-файл.
   -   Пример: `await crawler.export_data('results.json')`.
   -   По умолчанию экспортируется в файл `results.json` в директории, указанной в `gs.path.tmp`.
6.  **Получение данных:**
    -   Используйте метод `get_data()` для получения данных в формате словаря.
    -  Пример: `data = await crawler.get_data()`.
7.  **Логирование:**
    - Модуль использует `logger` для записи ошибок, предупреждений и общей информации.
    - Логирование настраивается в файле `crawlee_python.json` через параметр `logging`.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver.crawlee_python import CrawleePython
    from src.utils.jjson import j_loads_ns
    from pathlib import Path
    from src import gs
    
    async def main():
      # Загрузка настроек из файла
        settings = j_loads_ns(Path(gs.path.src / 'webdriver' / 'crawlee_python' / 'crawlee_python.json'))
     
       # Инициализация CrawleePython с настройками из файла
        crawler = CrawleePython(
           max_requests=settings.max_requests,
            headless=settings.headless,
            browser_type=settings.browser_type,
            options=settings.options
        )
        
        # Список URL для обработки
        urls = ["https://www.example.com", "https://example.org"]
        
        # Запуск краулера
        await crawler.run(urls)
        
        # Получение извлеченных данных
        data = await crawler.get_data()
        print("Извлеченные данные:")
        for item in data:
            print(item)
    
    if __name__ == "__main__":
        asyncio.run(main())
```