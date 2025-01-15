Как использовать модуль `src.webdriver.driver`
=========================================================================================

Описание
-------------------------
Модуль `driver.py` предназначен для работы с веб-драйверами Selenium. Класс `Driver` предоставляет унифицированный интерфейс для взаимодействия с веб-драйверами, включая инициализацию, навигацию, управление куки, обработку исключений и другие операции.

Шаги выполнения
-------------------------
1. **Инициализация драйвера:**
   - Создайте экземпляр класса `Driver`, передав класс веб-драйвера (например, `Chrome`, `Firefox`) и необходимые аргументы.
   - Пример: `driver = Driver(Chrome, executable_path='/path/to/chromedriver')`.
2. **Навигация по URL:**
   - Используйте метод `get_url(url)`, чтобы перейти по указанному URL.
   - Пример: `driver.get_url('https://example.com')`.
3. **Прокрутка страницы:**
   - Используйте метод `scroll(scrolls, frame_size, direction, delay)` для прокрутки страницы в нужном направлении.
   - Пример: `driver.scroll(scrolls=2, direction='down')`.
4. **Определение языка страницы:**
   - Получите язык страницы, используя свойство `locale`.
   - Пример: `language = driver.locale`.
5. **Открытие новой вкладки:**
   - Используйте метод `window_open(url)` для открытия новой вкладки и перехода по указанному URL (опционально).
   - Пример: `driver.window_open('https://newtab.com')`.
6. **Получение HTML контента:**
   - Используйте метод `fetch_html(url)` для получения HTML контента из файла или URL.
   - Пример: `driver.fetch_html('https://example.com')`.
7. **Использование атрибутов драйвера:**
   - Для доступа к атрибутам, используйте метод `__getattr__`, например: `driver.title` (возвращает заголовок страницы)

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

    # Закрытие драйвера
    driver.quit()