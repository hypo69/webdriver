# Модуль `login`

## Обзор

Модуль `login` предназначен для автоматизации процесса авторизации на сайте Amazon с использованием веб-драйвера. Он содержит функцию `login`, которая принимает объект поставщика (`Supplier`) в качестве аргумента и использует его для выполнения шагов авторизации, таких как ввод электронной почты, пароля и нажатие кнопок.

## Подробней

Этот модуль является частью процесса автоматизации работы с поставщиками на платформе Amazon. Он использует локаторы, хранящиеся в объекте поставщика, для поиска и взаимодействия с элементами веб-страницы. В случае неуспешной авторизации, модуль выполняет логирование ошибки.

## Функции

### `login`

```python
def login(s) -> bool:
    """ Функция логин. 
   @param
        s - Supplier
    @returns
        True if login else False

   """
```

**Назначение**:
Функция `login` автоматизирует процесс входа пользователя на сайт Amazon. Она использует объект `Supplier` для получения необходимых локаторов и управления веб-драйвером.

**Параметры**:
- `s` (Supplier): Объект поставщика, содержащий информацию о локаторах элементов страницы и драйвере веб-браузера.

**Возвращает**:
- `bool`: `True`, если вход выполнен успешно, и `False` в противном случае.

**Как работает функция**:

1.  **Инициализация**: Функция извлекает локаторы для элементов страницы входа из объекта `Supplier` и получает доступ к веб-драйверу.
2.  **Переход на страницу Amazon**: Функция переходит по URL-адресу Amazon.
3.  **Взаимодействие с элементами страницы**:
    *   Нажимает кнопку открытия формы входа. В случае неудачи пытается обновить страницу и повторить попытку.
    *   Вводит адрес электронной почты.
    *   Нажимает кнопку продолжения.
    *   Вводит пароль.
    *   Кликает на чекбокс "оставаться в системе".
    *   Нажимает кнопку подтверждения входа.
4.  **Проверка успешности входа**: Проверяет текущий URL страницы после попытки входа. Если URL указывает на страницу входа, функция логирует ошибку и завершается.
5.  **Логирование и завершение**: В случае успешного входа, функция логирует информацию об этом и возвращает `True`.

**ASCII Flowchart**:

```
    Supplier (s)
    |
    V
    Извлечение локаторов и драйвера (_l, _d)
    |
    V
    Переход на страницу Amazon (_d.get_url)
    |
    V
    Попытка открытия формы входа (_d.click)
    |
    V
    Успешно?
    |   Y  -> Ввод email (_d.execute_locator)
    |   N  -> Обновление страницы (_d.refresh) -> Попытка открытия формы входа
    |
    V
    Ввод email (_d.execute_locator)
    |
    V
    Нажатие кнопки "Продолжить" (_d.execute_locator)
    |
    V
    Ввод пароля (_d.execute_locator)
    |
    V
    Клик на чекбокс "оставаться в системе" (_d.execute_locator)
    |
    V
    Нажатие кнопки "Войти" (_d.execute_locator)
    |
    V
    Проверка URL (_d.current_url)
    |
    V
    Успешно?
    |   Y  -> Логирование и возврат True
    |   N  -> Логирование ошибки
    |
    V
    Конец
```

**Примеры**:

```python
# Предположим, что у нас есть объект Supplier 'supplier'
success = login(supplier)
if success:
    print("Вход выполнен успешно")
else:
    print("Вход не удался")