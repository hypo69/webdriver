Как использовать модуль `src.webdriver.js`
=========================================================================================

Описание
-------------------------
Модуль `js.py` предоставляет набор JavaScript-утилит для взаимодействия с веб-страницами, расширяя возможности Selenium WebDriver. Он включает функции для управления видимостью элементов, получения информации о странице и управления фокусом окна браузера.

Шаги выполнения
-------------------------
1. **Инициализация класса `JavaScript`:**
   - Создайте экземпляр класса `JavaScript`, передав экземпляр Selenium WebDriver.
   - Пример: `js_utils = JavaScript(driver)`.
2. **Сделать невидимый DOM-элемент видимым:**
   - Используйте метод `unhide_DOM_element(element)`, передав WebElement, который нужно сделать видимым.
   - Пример: `js_utils.unhide_DOM_element(element)`.
   - Метод использует JavaScript для изменения стилей элемента, делая его видимым и прокручивая до него.
3. **Получить статус загрузки документа:**
   - Используйте свойство `ready_state`, чтобы получить статус загрузки страницы.
   - Пример: `status = js_utils.ready_state`.
   - Свойство возвращает `'loading'`, если документ еще загружается, и `'complete'`, если загрузка завершена.
4. **Установить фокус на окно браузера:**
   - Используйте метод `window_focus()` для установки фокуса на текущее окно браузера.
   - Пример: `js_utils.window_focus()`.
   - Метод использует JavaScript для перевода окна браузера на передний план.
5.  **Получить URL реферера:**
    - Используйте метод `get_referrer()` для получения URL реферера текущей страницы.
    - Пример: `referrer = js_utils.get_referrer()`.
    - Метод возвращает URL реферера или пустую строку, если реферер отсутствует.
6. **Получить язык страницы:**
    - Используйте метод `get_page_lang()` для получения языка текущей страницы.
    - Пример: `language = js_utils.get_page_lang()`.
    - Метод возвращает код языка страницы или пустую строку, если язык не определен.

Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from src.webdriver.js import JavaScript
    import time

    # Инициализация WebDriver
    driver = webdriver.Chrome()
    driver.get("https://example.com")

    # Инициализация JavaScript utils
    js_utils = JavaScript(driver)

    # Найти скрытый элемент (предположим, что такой есть)
    try:
        element = driver.find_element(By.ID, "some_hidden_element")
    except:
        print("Элемент не найден")
        element = None

    if element:
        # Сделать элемент видимым
        if js_utils.unhide_DOM_element(element):
            print("Элемент сделан видимым")

    # Получить статус загрузки страницы
    print(f"Статус загрузки страницы: {js_utils.ready_state}")

    # Установить фокус на окно
    js_utils.window_focus()

    # Получить реферер
    print(f"Реферер: {js_utils.get_referrer()}")

    # Получить язык страницы
    print(f"Язык страницы: {js_utils.get_page_lang()}")

    # Закрыть браузер
    driver.quit()