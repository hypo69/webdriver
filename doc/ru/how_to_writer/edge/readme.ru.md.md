Как использовать модуль кастомной реализации Edge WebDriver для Selenium
=========================================================================================

Описание
-------------------------
Модуль предоставляет кастомную реализацию Edge WebDriver на основе Selenium. Он интегрирует настройки из файла `edge.json`, такие как user-agent и профиль браузера, для обеспечения гибкости и автоматизированного взаимодействия с браузером Edge.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
    - Убедитесь, что установлены библиотеки `selenium` и `fake_useragent`.
    - Если нет, установите их с помощью команды: `pip install selenium fake_useragent`.
    -  Убедитесь, что бинарник `msedgedriver` доступен в системе или путь к нему указан в конфигурационном файле `edge.json`.
2. **Настройка конфигурации (edge.json):**
   - Отредактируйте файл `edge.json` для настройки параметров Edge WebDriver.
   -  Основные параметры:
        -   `options`: список опций для Edge (например, `--disable-dev-shm-usage`, `--headless`).
        -   `profiles`: пути к профилям пользователя (для разных сред): `os` - для систем Windows, `internal` - внутренний путь для WebDriver.
        -   `executable_path`: путь к бинарнику `msedgedriver.exe` (`default` путь).
        -   `headers`: пользовательские заголовки HTTP-запросов.
        -   `proxy_enabled`: булево значение для включения прокси (не используется в текущей реализации).
3. **Инициализация Edge WebDriver:**
   - Создайте экземпляр класса `Edge`, передав необходимые параметры.
   - Пример:
       ```python
       from src.webdriver.edge import Edge
   
       browser = Edge(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
             options=["--headless", "--disable-gpu"]
        )
       ```
   - Параметры:
      -   `profile_name` (str, optional): Имя пользовательского профиля Edge.
      -   `user_agent` (str, optional): Пользовательский агент. Если не указан, то будет сгенерирован случайный.
      - `options` (list, optional): Список опций для Edge (например, `"--headless"`, `"--disable-gpu"`).
       - `window_mode` (str, optional): Режим окна браузера ('windowless', 'kiosk', 'full_window').
    -  Настройки загружаются из `edge.json`, если не переданы параметры.
4.  **Управление режимом окна:**
    -   Укажите режим окна браузера, используя параметр `window_mode`:
        - `kiosk`: полноэкранный режим без элементов интерфейса.
        - `windowless`: безголовый режим.
       -  `full_window`: обычное окно в полноэкранном режиме.
5. **Использование WebDriver:**
   - После создания экземпляра класса `Edge` используйте методы Selenium WebDriver для управления браузером.
    -  Примеры:
         -  `browser.get(url)`: Загружает URL.
         -  `browser.find_element(By.ID, 'element_id')`: Находит элемент.
         -  `browser.execute_script('...')`: Выполняет JavaScript.
          - `browser.get_url(url)`: загружает URL, сохраняя куки и предыдущую ссылку (из `src.webdriver.driver.Driver`).
          -   `browser.scroll(scrolls=2, direction='down')`: прокрутка страницы (из `src.webdriver.driver.Driver`).
6.  **Использование `ExecuteLocator` и `JavaScript`:**
    -  Класс `Edge` автоматически инициализирует `ExecuteLocator` и `JavaScript`.
    -   Используйте их методы напрямую через объект `driver`.
    -  Примеры:
         -   `driver.execute_locator(locator)`: выполняет действия с элементом по локатору.
         - `driver.get_webelement_by_locator(locator)`: получает элемент по локатору.
        -   `driver.get_attribute_by_locator(locator)`: получает атрибут элемента.
        -  `driver.send_message(locator, message)`: отправляет сообщение в элемент.
        -   `driver.get_page_lang()`: возвращает язык страницы.
        -   `driver.ready_state`: возвращает статус загрузки страницы.
        -  `driver.unhide_DOM_element(element)`: делает элемент видимым.
        -  `driver.window_focus()`: устанавливает фокус на окно браузера.
7. **Логирование:**
   -  Модуль использует `logger` для логирования ошибок и предупреждений.
   -  Просматривайте логи для отладки.
8. **Паттерн Singleton:**
    -  Класс использует паттерн Singleton, гарантируя, что будет создан только один экземпляр Edge WebDriver.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.edge import Edge
    from selenium.webdriver.common.by import By
    import asyncio
    from src.webdriver.executor import ExecuteLocator
    from src.utils.jjson import j_loads_ns
    from pathlib import Path
    from src import gs

    async def main():
       # Загрузка настроек из файла
        settings = j_loads_ns(Path(gs.path.src / 'webdriver' / 'edge' / 'edge.json'))
     
       # Инициализация Edge WebDriver
        driver = Edge(
             user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62',
            window_mode='full_window'
        )
    
        if driver.get_url("https://www.example.com"):
             print("Успешно перешли по URL")
    
        # Поиск заголовка страницы
        element = driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
            print(f'Заголовок страницы: {element.text}')
    
        # Пример с execute_locator для клика
        executor = ExecuteLocator(driver=driver)
        locator = {"by": "ID", "selector": "some_id", "event": "click()"}
        result = await executor.execute_locator(locator)
        print(f"Результат execute_locator (click): {result}")
       
         # Пример с execute_locator для получения текста
        locator = {"by": "CSS_SELECTOR", "selector": "h1", "attribute": "innerText"}
        text = await driver.get_attribute_by_locator(locator)
        if text:
            print(f"Извлеченный текст: {text}")
       
        # Закрытие браузера
        driver.quit()
    
    if __name__ == "__main__":
       asyncio.run(main())