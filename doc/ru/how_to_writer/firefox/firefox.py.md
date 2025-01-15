Как использовать модуль кастомного Firefox WebDriver для Selenium
=========================================================================================

Описание
-------------------------
Модуль предоставляет кастомную реализацию Firefox WebDriver на основе Selenium. Он расширяет стандартный `webdriver.Firefox`, позволяя настраивать профиль пользователя, режим киоска, пользовательский агент и прокси, опираясь на файл конфигурации `firefox.json`.

Шаги выполнения
-------------------------
1.  **Импорт модуля:**
    -  Импортируйте класс `Firefox` из модуля `src.webdriver.firefox.firefox`.
    - Пример: `from src.webdriver.firefox.firefox import Firefox`.
2.  **Инициализация WebDriver:**
     - Создайте экземпляр класса `Firefox`, передав необходимые параметры.
     -  Пример:
          ```python
          from src.webdriver.firefox.firefox import Firefox
          
          browser = Firefox(
              profile_name='custom_profile',
              geckodriver_version='v0.29.0',
              firefox_version='78.0',
              proxy_file_path='path/to/proxies.txt',
               options=["--headless"]
          )
          ```
     - Параметры:
        -   `profile_name` (str, optional): Имя пользовательского профиля Firefox.
        -  `geckodriver_version` (str, optional): Версия geckodriver.
        -  `firefox_version` (str, optional): Версия Firefox.
        -   `user_agent` (str, optional): Пользовательский агент. Если не указан, будет сгенерирован случайный.
        - `proxy_file_path` (str, optional): Путь к файлу с прокси.
        -   `options` (list, optional): Список опций для Firefox (например, `"--headless"`).
        -  `window_mode` (str, optional): Режим окна браузера ('windowless', 'kiosk').
     - Если параметры не переданы, будут использоваться значения по умолчанию из файла `firefox.json`.
3. **Настройка профиля Firefox:**
    - Укажите путь к пользовательскому профилю с помощью `profile_name`.
    - Если указано имя профиля, создается новый профиль с указанным именем.
     -  Если в пути профиля встречается переменная окружения `%LOCALAPPDATA%`, то она заменяется на фактический путь.
4.  **Настройка прокси:**
    -   Если в конфигурационном файле `firefox.json` установлен флаг `proxy_enabled` как `true`, будет использован рабочий прокси из списка.
    -  Прокси выбирается случайным образом из списка и проверяется на работоспособность.
5.  **Управление режимом окна:**
   - Установите режим окна браузера, используя параметр `window_mode` при инициализации.
    - Возможные значения:
        - `kiosk`: полноэкранный режим без элементов интерфейса.
        -   `windowless`: безголовый режим.
6.  **Использование WebDriver:**
    -   После создания экземпляра используйте методы Selenium WebDriver для навигации и взаимодействия со страницей.
    -  Примеры:
         -  `browser.get(url)`: Загружает URL.
        -  `browser.find_element(By.ID, 'element_id')`: Находит элемент по ID.
        -  `browser.execute_script('...')`: Выполняет JavaScript.
         -  `driver.get_url(url)`: загружает URL, сохраняя куки и предыдущую ссылку (из `src.webdriver.driver.Driver`).
          -  `driver.scroll(scrolls=2, direction='down')`: прокрутка страницы (из `src.webdriver.driver.Driver`).
7.  **Использование `ExecuteLocator` и `JavaScript`:**
    - Класс `Firefox` автоматически инициализирует `ExecuteLocator` и `JavaScript` и предоставляет их методы через методы экземпляра.
     - Примеры:
        - `driver.execute_locator(locator)`: выполняет действия с элементом, описанные в локаторе.
         -   `driver.get_webelement_by_locator(locator)`: получает элемент, используя локатор.
        -  `driver.get_attribute_by_locator(locator)`: получает атрибут элемента по локатору.
        -  `driver.send_message(locator, message)`: отправляет текст в элемент.
         - `driver.get_page_lang()`: возвращает язык страницы.
         - `driver.ready_state`: возвращает состояние загрузки страницы.
         - `driver.unhide_DOM_element(element)`: делает элемент видимым.
         -  `driver.window_focus()`: фокусирует окно браузера.
8. **Обработка ошибок:**
   -   Модуль использует `logger` для вывода ошибок и предупреждений.
   - Проверяйте логи для отладки.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.firefox.firefox import Firefox
    from selenium.webdriver.common.by import By
    import asyncio
    from src.webdriver.executor import ExecuteLocator
    from src.utils.jjson import j_loads_ns
    from pathlib import Path
    from src import gs

    async def main():
      # Загрузка настроек из файла
        settings = j_loads_ns(Path(gs.path.src / 'webdriver' / 'firefox' / 'firefox.json'))

        # Инициализация Firefox WebDriver
        driver = Firefox(
            # profile_name='custom_profile',
            #geckodriver_version='v0.31.0',
            #firefox_version='108.0',
            #user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            #proxy_file_path='path/to/proxies.txt',
            options=["--headless"],
            window_mode='full_window'
        )

        if driver.get_url("https://www.example.com"):
            print("Успешно перешли по URL")
        
         # Поиск элемента
        element = driver.find_element(By.CSS_SELECTOR, 'h1')
        if element:
           print(f'Заголовок страницы: {element.text}')
           
         # Использование ExecuteLocator для клика
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