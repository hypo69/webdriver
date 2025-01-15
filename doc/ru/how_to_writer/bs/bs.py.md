Как использовать модуль `src.webdriver.bs.bs`
=========================================================================================

Описание
-------------------------
Модуль `bs.py` предоставляет класс `BS` для парсинга HTML-контента с использованием библиотек BeautifulSoup и lxml (для XPath). Он позволяет загружать HTML из URL или локального файла, а также извлекать элементы с помощью XPath.

Шаги выполнения
-------------------------
1. **Инициализация класса `BS`:**
   - Создайте экземпляр класса `BS`, передав в конструктор опциональный URL или путь к файлу.
   - Пример: `parser = BS('https://example.com')` или `parser = BS('file:///path/to/local.html')`.
   - Если URL не передан, HTML-контент можно загрузить позже с помощью метода `get_url`.
2.  **Загрузка HTML-контента:**
    - Используйте метод `get_url(url)` для загрузки HTML-контента из URL или локального файла.
    - Пример: `parser.get_url('https://example.com')` или `parser.get_url('file:///path/to/local.html')`.
    - Метод обрабатывает пути как с `file://`, так и с `https://` протоколами.
    -  После успешной загрузки HTML-код сохраняется в атрибуте `html_content`.
    -  Метод возвращает `True`, если загрузка прошла успешно, `False` в противном случае.
3. **Выполнение локатора:**
   - Используйте метод `execute_locator(locator, url)` для выполнения XPath запроса к загруженному HTML-контенту.
   - Пример: 
     ```python
        locator = SimpleNamespace(by='ID', attribute='some_id', selector='//*[@id="some_id"]')
        elements = parser.execute_locator(locator)
     ```
   -   `locator` - это объект SimpleNamespace или словарь, содержащий параметры для поиска элемента:
        -   `by`: метод поиска элемента (`ID`, `CSS`, `TEXT` или `XPATH`).
        -   `attribute`: значение атрибута (например, id).
        -   `selector`: XPath селектор.
   -   `url` - опциональный параметр для перезагрузки HTML контента.
   -   Метод возвращает список элементов, соответствующих XPath-запросу.
   -   Если `html_content` пустой, метод возвращает пустой список.
4.  **Использование результатов:**
    -   Итерируйтесь по списку найденных элементов (если это необходимо).
    - Извлекайте текст или другие необходимые данные из элементов с помощью методов lxml.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver.bs.bs import BS
    from types import SimpleNamespace
    
    # Создаем экземпляр парсера и загружаем HTML
    parser = BS('https://example.com')
    
    # Создаем локатор для поиска элемента с id "example"
    locator = SimpleNamespace(
            by='ID',
            attribute='example',
            selector='//*[@id="example"]'
        )
    
    # Выполняем поиск элемента
    elements = parser.execute_locator(locator)
    
    # Вывод результатов
    if elements:
        print("Найдено элементов:")
        for element in elements:
           print(element.text if hasattr(element, 'text') else element)
    else:
        print("Элементы не найдены.")

    # Пример с CSS классом
    locator_css = SimpleNamespace(
        by='CSS',
        attribute='example-class',
        selector='//*[contains(@class, "example-class")]'
    )
    elements_css = parser.execute_locator(locator_css)
    
    if elements_css:
        print("Найдено элементов (CSS):")
        for element in elements_css:
            print(element.text if hasattr(element, 'text') else element)
    else:
         print("Элементы не найдены (CSS).")

    # Пример с текстовым полем
    locator_text = SimpleNamespace(
        by='TEXT',
        attribute='text',
        selector='//input[@type="text"]'
    )
    elements_text = parser.execute_locator(locator_text)
    if elements_text:
        print('Найдено текстовых полей:')
        for element in elements_text:
             print(element.text if hasattr(element, 'text') else element)
    else:
       print("Текстовые поля не найдены.")

    # Поиск с перезагрузкой страницы
    elements_url = parser.execute_locator(locator, url='https://example.com')
    if elements_url:
        print("Найдено элементов (после перезагрузки):")
        for element in elements_url:
            print(element.text if hasattr(element, 'text') else element)
    else:
         print("Элементы не найдены (после перезагрузки).")