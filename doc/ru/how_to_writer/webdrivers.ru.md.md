Как использовать веб-драйверы и их настройки в проекте
=========================================================================================

Описание
-------------------------
Этот документ предоставляет обзор всех веб-драйверов, доступных в проекте, их настроек и опций. Каждый веб-драйвер имеет свои параметры, которые можно настроить в соответствующих файлах JSON. Документ охватывает Firefox, Chrome, Edge, Playwright и парсеры на базе BeautifulSoup и XPath.

Шаги выполнения
-------------------------
1. **Выбор веб-драйвера:**
   - Определитесь, какой веб-драйвер вам нужен в зависимости от задач автоматизации или сбора данных.
2. **Настройка веб-драйвера:**
   - Откройте соответствующий JSON-файл конфигурации (например, `firefox.json`, `chrome.json`, `edge.json`, `playwrid.json`, `bs.json`).
   - Настройте необходимые параметры, такие как:
     -  `profile_name` (имя профиля пользователя).
     -  `geckodriver_version`/`chromedriver_version`/`edgedriver_version` (версия драйвера).
     -  `firefox_version`/`chrome_version`/`edge_version` (версия браузера).
     -  `user_agent` (пользовательский агент).
     -  `proxy_file_path` (путь к файлу с прокси).
     -  `options` (список опций браузера, например, `--headless`).
     -  `executable_path` (пути к исполняемым файлам браузера и драйвера).
     -  `headers` (заголовки запроса).
     -  `proxy_enabled` (флаг для включения/выключения прокси).
     -  Для Playwright: `max_requests`, `headless`, `browser_type`, `proxy`, `viewport`, `timeout`, `ignore_https_errors`.
     -  Для парсера: `default_url`, `default_file_path`, `default_locator`, `logging`, `proxy`, `timeout`, `encoding`.
3.  **Использование веб-драйвера в коде:**
    - Загрузите необходимую конфигурацию из соответствующего JSON файла.
    - Создайте экземпляр веб-драйвера, передав в него загруженные настройки.
    -  Используйте методы веб-драйвера для навигации, взаимодействия с элементами и сбора данных.

4.  **Примеры конфигураций:**
    -   **Firefox (`firefox.json`):**
        -  Настройка пользовательского профиля, прокси, user-agent.
        -  Опции: `--kiosk`, `--headless`.
    -   **Chrome (`chrome.json`):**
        -  Настройка профилей, user-agent, прокси.
        -  Опции: `--headless`, `--disable-gpu`.
    -   **Edge (`edge.json`):**
        -  Аналогичные настройки, как у Chrome.
        -  Опции: `--headless`, `--disable-gpu`.
    -   **Playwright (`playwrid.json`):**
        -  Настройка прокси, user-agent, размера окна, таймаутов.
        -  Поддержка режимов headless.
        -  Поддержка разных типов браузеров (`chromium`, `firefox`, `webkit`).
    -   **BeautifulSoup и XPath (`bs.json`):**
        -   Настройка URL/файла по умолчанию, локатора для извлечения элементов.
        -  Настройка таймаутов и кодировки.

5.  **Взаимодействие с элементами**:
    - Используйте методы `ExecuteLocator` для выполнения различных действий с веб-элементами (клик, ввод текста, извлечение атрибутов и т.д.).
    - Создайте локатор для нужного элемента, настроив `by`, `selector`, `event`, `attribute` и т.д.
    -  Выполните действие с помощью `execute_locator` или напрямую используя методы браузера (например, `find_element`).

Пример использования
-------------------------
.. code-block:: python

    import json
    from pathlib import Path
    from src.webdriver.driver import Driver, Chrome
    from src.webdriver.executor import ExecuteLocator
    from selenium.webdriver.common.by import By
    import asyncio

    async def main():
        # Путь к файлу конфигурации Chrome
        config_path = Path('src/webdriver/chrome.json')

        # Загрузка конфигурации из JSON файла
        with open(config_path, 'r', encoding='utf-8') as config_file:
            config = json.load(config_file)

        # Создание экземпляра Chrome Driver с настройками
        chrome_driver = Driver(Chrome, **config)
        
        # Переход на example.com
        if chrome_driver.get_url("https://www.example.com"):
            print("Successfully navigated to the URL")
        
        # Извлечение заголовка страницы
        element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
           print(f'Заголовок страницы: {element.text}')

        # Настройка локатора
        locator = {
            "by": "CSS_SELECTOR",
            "selector": "h1",
            "attribute": 'innerText'
        }
        
        # Использование ExecuteLocator для извлечения текста из заголовка
        executor = ExecuteLocator(driver=chrome_driver)
        result = await executor.get_attribute_by_locator(locator)
        print(f"Текст заголовка: {result}")
        
        # Закрытие браузера
        chrome_driver.quit()
        
    if __name__ == "__main__":
        asyncio.run(main())