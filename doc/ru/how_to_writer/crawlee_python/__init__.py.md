Как использовать модуль `src.webdriver.crawlee_python`
=========================================================================================

Описание
-------------------------
Модуль `__init__.py` в директории `src.webdriver.crawlee_python` предназначен для импорта и экспорта класса `CrawleePython` из модуля `crawlee_python.py`. Это позволяет упростить импорт класса `CrawleePython` в другие части проекта, делая его доступным напрямую из пакета `src.webdriver.crawlee_python`.

Шаги выполнения
-------------------------
1. **Импорт модуля:**
   - Импортируйте класс `CrawleePython` из пакета `src.webdriver.crawlee_python`.
   - Пример: `from src.webdriver.crawlee_python import CrawleePython`.
   - Благодаря файлу `__init__.py` импорт класса `CrawleePython` становится проще, так как нет необходимости указывать путь к файлу `crawlee_python.py`.
2. **Использование класса `CrawleePython`:**
   - После импорта класса `CrawleePython` вы можете создать экземпляр кастомного краулера Playwright.
   -  Пример:
        ```python
        from src.webdriver.crawlee_python import CrawleePython
        import asyncio

        async def main():
            crawler = CrawleePython(
               max_requests=5,
               headless=True,
               browser_type='chromium',
               options=['--disable-gpu']
           )
           # ...
        ```
   - Далее вы можете использовать методы объекта `crawler` для настройки и запуска краулинга, как описано в инструкции к модулю `crawlee_python.py`.
3. **Преимущества:**
   -  Упрощает импорт: позволяет импортировать класс, не указывая путь к файлу `crawlee_python.py`.
   -   Улучшает структуру: обеспечивает более чистый и организованный код.
   -  Облегчает рефакторинг: изменения в структуре пакета могут быть сделаны без изменения кода, импортирующего класс `CrawleePython`.

Пример использования
-------------------------
.. code-block:: python

    import asyncio
    from src.webdriver.crawlee_python import CrawleePython

    async def main():
         # Создание экземпляра CrawleePython
        crawler = CrawleePython(
            max_requests=3,
            headless=True,
            browser_type='firefox',
            options=['--disable-gpu']
        )
        # Запуск краулинга
        await crawler.run(['https://www.example.com'])
        
        # Получение извлеченных данных
        data = await crawler.get_data()
        print("Извлеченные данные:")
        for item in data:
             print(item)
   
    if __name__ == "__main__":
        asyncio.run(main())