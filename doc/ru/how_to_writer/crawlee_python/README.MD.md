Как использовать модуль Crawlee Python для автоматизации и сбора данных
=========================================================================================

Описание
-------------------------
Модуль предоставляет кастомную реализацию `PlaywrightCrawler` с использованием библиотеки Crawlee. Он позволяет настраивать параметры запуска браузера, обрабатывать веб-страницы и извлекать из них данные. Управление настройками осуществляется через файл `crawlee_python.json`.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
   -  Убедитесь, что установлены библиотеки `playwright` и `crawlee`.
   - Если они не установлены, выполните: `pip install playwright crawlee`.
   -  Установите браузеры с помощью команды `playwright install`.
2.  **Настройка конфигурации:**
    -  Отредактируйте файл `crawlee_python.json`.
    -  Основные параметры:
       -  `max_requests`: максимальное количество запросов для краулинга (по умолчанию 10).
       -   `headless`: запускать ли браузер в безголовом режиме (по умолчанию `true`).
       -  `browser_type`: тип браузера ('chromium', 'firefox', 'webkit', по умолчанию 'chromium').
       -   `options`: список параметров командной строки для браузера.
       -   `user_agent`: пользовательский агент.
       -   `proxy`: настройки прокси-сервера.
       -  `viewport`: размеры окна браузера.
       - `timeout`: таймаут для операций (в миллисекундах, по умолчанию 30000).
       - `ignore_https_errors`: игнорировать ошибки HTTPS (по умолчанию `false`).
3.  **Инициализация `CrawleePython`:**
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
            # ...
         ```
     - Параметры:
          -   `max_requests`: максимальное количество запросов.
          - `headless`: запускать ли браузер без графического интерфейса.
          -   `browser_type`: тип браузера.
          -   `options`: дополнительные опции для браузера.
4. **Настройка краулера:**
    -   Метод `setup_crawler()` создает экземпляр `PlaywrightCrawler` с заданными параметрами и задаёт обработчик запросов по умолчанию.
    -   Обработчик по умолчанию делает следующее:
        - Логирует URL обрабатываемой страницы.
        - Ставит в очередь найденные на странице ссылки.
        -  Извлекает заголовок (title), URL и первые 100 символов содержимого страницы.
        -   Сохраняет полученные данные.
5.  **Запуск краулера:**
    -   Используйте метод `run_crawler(urls)` для запуска процесса сбора данных.
    -   Пример: `await crawler.run_crawler(['https://www.example.com'])`.
    -   Передайте список URL для начальной обработки.
6.  **Экспорт данных:**
    -   Используйте метод `export_data(file_path)` для сохранения данных в файл JSON.
    -   Пример: `await crawler.export_data('results.json')`.
    -   По умолчанию используется путь `gs.path.tmp / 'results.json'`.
7.  **Получение данных:**
    -   Метод `get_data()` возвращает извлеченные данные как словарь.
    -   Пример: `data = await crawler.get_data()`.
8.  **Запуск всего процесса:**
     - Используйте метод `run(urls)` для запуска краулера, обработки результатов и экспорта данных.
      - Пример: `await crawler.run(['https://www.example.com'])`.
    - Метод автоматически выполняет все шаги: настраивает, запускает, экспортирует данные и логирует результат.
9. **Логирование:**
    - Модуль использует `logger` для вывода логов.
    - Ошибки, предупреждения и информационные сообщения записываются в лог.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver.crawlee_python import CrawleePython
    from src.utils.jjson import j_loads_ns
    from pathlib import Path
    from src import gs

    async def main():
       
        # Load settings from the config file
        settings = j_loads_ns(Path(gs.path.src / "webdriver" / 'crawlee_python' / 'crawlee_python.json'))
        
        # Create a CrawleePython instance
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
         
        # Извлечение данных
        data = await crawler.get_data()
        print("Извлеченные данные:")
        for item in data:
            print(item)
    
    if __name__ == "__main__":
        asyncio.run(main())