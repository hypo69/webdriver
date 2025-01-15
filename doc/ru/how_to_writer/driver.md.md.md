Как использовать модуль `src.webdriver.driver`
=========================================================================================

Описание
-------------------------
Модуль `driver.py` предоставляет класс `Driver` для взаимодействия с веб-драйверами Selenium. Этот модуль инкапсулирует логику инициализации драйвера, навигации, прокрутки, определения языка страницы, управления куки и загрузки HTML-контента.

Шаги выполнения
-------------------------
1. **Инициализация драйвера:**
   - Создайте экземпляр класса `Driver`, передав класс веб-драйвера (например, `Chrome`, `Firefox`) и необходимые аргументы.
   - Пример: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`.
   - Класс проверяет, что переданный `webdriver_cls` имеет метод `get`, и создает объект драйвера.
2. **Инициализация подкласса:**
   - Если вы создаете подкласс `Driver`, убедитесь, что передаете аргумент `browser_name`.
   - Пример: `class CustomDriver(Driver, browser_name='Chrome'): ...`
   - `browser_name` сохраняется как атрибут подкласса.
3. **Доступ к атрибутам драйвера:**
   - Для доступа к атрибутам веб-драйвера используйте атрибуты экземпляра `Driver`.
   - Пример: `driver.page_source` (обращается к `self.driver.page_source`).
4. **Прокрутка страницы:**
   - Используйте метод `scroll(scrolls, frame_size, direction, delay)` для прокрутки страницы в заданном направлении.
   - Пример: `driver.scroll(scrolls=2, direction='down')`.
   - `scrolls` - количество прокруток, `frame_size` - размер прокрутки, `direction` - направление ('forward', 'down', 'backward', 'up', 'both'), `delay` - задержка между прокрутками.
5. **Определение языка страницы:**
   - Получите язык страницы, используя свойство `locale`.
   - Пример: `language = driver.locale`.
   - Свойство извлекает язык из мета-тегов или с помощью JavaScript (если реализован).
6. **Навигация по URL:**
   - Используйте метод `get_url(url)`, чтобы перейти по указанному URL.
   - Пример: `driver.get_url('https://example.com')`.
   - Сохраняет предыдущий URL, ждет загрузки страницы, сохраняет куки и обрабатывает исключения.
7. **Открытие новой вкладки:**
   - Используйте метод `window_open(url)`, чтобы открыть новую вкладку и перейти по указанному URL (необязательно).
   - Пример: `driver.window_open('https://newtab.com')`.
8. **Ожидание:**
   - Используйте метод `wait(delay)` для приостановки выполнения на заданное время.
   - Пример: `driver.wait(2)`.
9. **Сохранение куки:**
   - Используйте метод `_save_cookies_localy()` для сохранения куки в локальный файл.
   - Пример: `driver._save_cookies_localy()`.
   - В текущей версии возвращает `True` для отладки, нужно использовать `pickle.dump()` для сохранения.
10. **Загрузка HTML-контента:**
    - Используйте метод `fetch_html(url)` для загрузки HTML-контента из файла или по URL.
    - Пример: `driver.fetch_html('file:///path/to/local.html')` или `driver.fetch_html('https://example.com')`.
    - Поддерживает протоколы `file://`, `http://` и `https://`.

Пример использования
-------------------------
.. code-block:: python

    from selenium.webdriver import Chrome
    from src.webdriver.driver import Driver

    # Инициализация драйвера Chrome
    driver = Driver(Chrome, executable_path='/path/to/chromedriver')
    
    # Переход по URL
    driver.get_url('https://example.com')
    
    # Прокрутка страницы вниз 2 раза
    driver.scroll(scrolls=2, direction='down')
    
    # Получение языка страницы
    language = driver.locale
    print(f"Язык страницы: {language}")

    # Открытие новой вкладки
    driver.window_open('https://newtab.com')
    
    # Получение HTML контента
    if driver.fetch_html('https://example.com'):
        print(f'HTML content {driver.html_content[:100]}...')

    # Получение заголовка страницы
    print(f'Заголовок страницы: {driver.title}')

    # Ожидание 1 секунду
    driver.wait(1)

    # Закрытие драйвера
    driver.quit()