Как использовать модуль CrawleePython для веб-краулинга
=========================================================================================

Описание
-------------------------
Модуль `crawlee_python.py` предоставляет класс `CrawleePython`, который является кастомной реализацией `PlaywrightCrawler` из библиотеки Crawlee. Он позволяет настраивать параметры браузера, обрабатывать запросы и извлекать данные с веб-страниц, предоставляя гибкость и расширенные возможности для веб-краулинга.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
   - Убедитесь, что у вас установлены библиотеки `crawlee` и `playwright`.
   - Если они не установлены, выполните команду: `pip install crawlee playwright`.
2.  **Импорт модуля:**
    -  Импортируйте класс `CrawleePython` из модуля.
    - Пример: `from src.webdriver.crawlee_python import CrawleePython`.
3.  **Инициализация класса:**
    -  Создайте экземпляр класса `CrawleePython`, передав необходимые параметры.
    -  Пример:
         ```python
         import asyncio
         from src.webdriver.crawlee_python import CrawleePython
         
         async def main():
              crawler = CrawleePython(
                 max_requests=5,
                 headless=False,
                 browser_type='firefox',
                 options=["--headless"]
              )
             # ...
         ```
    - Параметры:
        -  `max_requests` (int): максимальное количество запросов для краулера (по умолчанию 5).
        -  `headless` (bool): запускать ли браузер в безголовом режиме (по умолчанию `False`).
        - `browser_type` (str): тип браузера ('chromium', 'firefox', 'webkit', по умолчанию 'firefox').
        - `options` (list, optional): список дополнительных опций для браузера.
4. **Настройка краулера:**
   -  Используйте метод `setup_crawler()` для настройки `PlaywrightCrawler` экземпляра.
   -  Метод также задаёт обработчик запросов по умолчанию (`request_handler`), который выполняет следующие действия:
        - Логирует URL обрабатываемой страницы.
        - Ставит в очередь все найденные ссылки.
        -  Извлекает данные (URL, title, первые 100 символов контента).
        -  Отправляет извлечённые данные в датасет.
5. **Запуск краулера:**
   - Используйте метод `run_crawler(urls)` для запуска краулера с указанным списком URL.
   - Пример: `await crawler.run_crawler(['https://www.example.com'])`.
6. **Экспорт данных:**
   -  Используйте метод `export_data(file_path)` для экспорта всего датасета в JSON-файл.
   -   Пример: `await crawler.export_data('results.json')`.
   -  По умолчанию используется путь `gs.path.tmp / 'results.json'`.
7.  **Получение данных:**
    - Используйте метод `get_data()` для получения данных в виде словаря.
    -  Пример: `data = await crawler.get_data()`.
8.  **Запуск всего процесса:**
    - Используйте метод `run(urls)` для настройки, запуска краулера, экспорта данных и получения результата.
    - Пример:
         ```python
            await crawler.run(['https://www.example.com'])
         ```
        - Метод обрабатывает исключения, возникшие во время работы.
9. **Логирование:**
   - Используйте модуль `logger` из `src.logger.logger` для логирования информации, ошибок и предупреждений.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver.crawlee_python import CrawleePython

    async def main():
        # Инициализация краулера
        crawler = CrawleePython(
            max_requests=5,
            headless=True,
            browser_type='chromium',
            options=["--disable-gpu"]
        )

        # Список URL для обработки
        urls = ['https://www.example.com', 'https://www.example.org']
    
        # Запуск краулера
        await crawler.run(urls)
        
        # Получение извлеченных данных
        data = await crawler.get_data()
        print("Извлечённые данные:")
        for item in data:
           print(item)
    
    if __name__ == "__main__":
        asyncio.run(main())