Как использовать модуль `src.webdriver.chrome.chrome`
=========================================================================================

Описание
-------------------------
Модуль `chrome.py` предоставляет класс `Chrome`, который расширяет возможности стандартного `webdriver.Chrome` из Selenium. Он добавляет поддержку пользовательских профилей, прокси, user-agent, а также позволяет настраивать режим окна и другие параметры, опираясь на конфигурацию из файла `chrome.json`.

Шаги выполнения
-------------------------
1. **Импорт модуля:**
   - Импортируйте класс `Chrome` из модуля `src.webdriver.chrome.chrome`.
   - Пример: `from src.webdriver.chrome.chrome import Chrome`.
2. **Инициализация драйвера:**
   - Создайте экземпляр класса `Chrome`, передав необходимые параметры.
   - Пример:
     ```python
     from src.webdriver.chrome.chrome import Chrome
    
     driver = Chrome(
         profile_name='my_profile',
         user_agent='Mozilla/5.0...',
         proxy_file_path='path/to/proxy.txt',
         options=['--headless', '--disable-gpu'],
         window_mode='kiosk'
     )
     ```
   - Параметры:
     -   `profile_name` (str, optional): Имя пользовательского профиля Chrome.
     -  `chromedriver_version` (str, optional): Версия chromedriver.
     -   `user_agent` (str, optional): Пользовательский агент. Если не указан, будет сгенерирован случайный.
     -  `proxy_file_path` (str, optional): Путь к файлу с прокси.
     - `options` (list, optional): Список опций для Chrome (например, `--headless`).
     -   `window_mode` (str, optional): Режим окна браузера ('windowless', 'kiosk', 'full_window').
   - Если параметры не переданы, то используются значения из файла `chrome.json`.
3. **Настройка прокси:**
    - Если в конфигурации (`chrome.json`) установлен флаг `proxy_enabled` в значение `true`, то будет использован рабочий прокси из файла, указанного в `proxy_file_path` (или из файла прокси, указанного в настройках `gs`).
    - Функция `set_proxy` автоматически выбирает один рабочий прокси из списка.
4. **Управление окном браузера:**
   - Выберите режим окна браузера, используя параметр `window_mode` (kiosk, windowless, full_window) или оставьте по умолчанию (обычное окно).
   - `kiosk` - полноэкранный режим без элементов интерфейса.
   - `windowless` - безголовый режим.
   - `full_window` - обычное окно в полноэкранном режиме.
5. **Использование драйвера:**
    - После создания экземпляра класса `Chrome`, используйте методы Selenium WebDriver для навигации, взаимодействия с элементами и т.д.
    -   Примеры методов:
        - `driver.get(url)`: Загружает URL.
        -   `driver.find_element(By.ID, 'element_id')`: Находит элемент.
        -  `driver.execute_script('...')`: Выполняет JavaScript.
        - `driver.get_url(url)`: загружает URL, сохраняет куки и предыдущую ссылку (из `src.webdriver.driver.Driver`).
        - `driver.scroll(scrolls=2, direction='down')`: прокрутка страницы (из `src.webdriver.driver.Driver`).
6.  **Использование `ExecuteLocator` и `JavaScript`:**
   - Класс `Chrome` автоматически инициализирует `ExecuteLocator` и `JavaScript` и предоставляет их методы через методы экземпляра.
   -  Примеры:
        -  `driver.execute_locator(locator)`: Выполняет действия с элементом, описанные в локаторе.
        -  `driver.get_webelement_by_locator(locator)`: Получает элемент, используя локатор.
        -   `driver.get_attribute_by_locator(locator)`: Получает значение атрибута элемента, используя локатор.
        -  `driver.send_message(locator, message)`: Отправляет сообщение в элемент.
        -   `driver.get_page_lang()`: Возвращает язык страницы.
        -   `driver.ready_state`: Возвращает состояние загрузки страницы.
        -  `driver.unhide_DOM_element(element)`: делает элемент видимым.
        -  `driver.window_focus()`: фокусирует окно браузера.
7. **Обработка ошибок:**
    - Логирование ошибок происходит с помощью модуля `logger`.
    -  Основные возможные ошибки:
        - Ошибка запуска WebDriver (обновление Chrome, отсутствие Chrome).
        - Ошибка работы Chrome WebDriver (неожиданные ошибки во время работы).

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.chrome.chrome import Chrome
    from selenium.webdriver.common.by import By
    import asyncio
    from src.webdriver.executor import ExecuteLocator
    from src.utils.jjson import j_loads_ns
    from pathlib import Path
    from src import gs
    
    async def main():
        # Загрузка настроек из файла
        settings = j_loads_ns(Path(gs.path.src / 'webdriver' / 'chrome' / 'chrome.json'))
    
        # Пример создания экземпляра Chrome драйвера
        driver = Chrome(
           #chromedriver_version='111',
            #profile_name='my_profile',
           # user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
           #proxy_file_path='path/to/proxy.txt',
            #options=['--headless', '--disable-gpu'],
            window_mode='full_window'
        )
        if driver.get_url("https://www.example.com"):
           print("Успешно перешли по URL")
           
        # Получение заголовка страницы
        element = driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
           print(f'Заголовок страницы: {element.text}')

         # Example 11: Using ExecuteLocator for click action
        executor = ExecuteLocator(driver=driver)
        locator = {"by": "ID", "selector": "some_id", "event": "click()"}
        result = await executor.execute_locator(locator)
        print(f"Result of execute_locator click: {result}")
    
        # Пример использования execute_locator для извлечения текста
        locator = {"by": "CSS_SELECTOR", "selector": "h1", "attribute": "innerText"}
        
        text = await driver.get_attribute_by_locator(locator)
        if text:
            print(f"Извлеченный текст: {text}")
    
        # Закрытие браузера
        driver.quit()
    
    if __name__ == "__main__":
       asyncio.run(main())