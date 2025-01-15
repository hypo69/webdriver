# Документация модуля `contentScript.js`

## Обзор

Этот модуль `contentScript.js` является контентным скриптом для расширения браузера, предназначенным для сбора данных со страниц и их отправки на сервер.

## Оглавление

-   [Обзор](#обзор)
-   [Функции](#функции)
    -   [Обработчик события загрузки страницы (`onPageLoad`)](#обработчик-события-загрузки-страницы-onpageload)

## Функции

### Обработчик события загрузки страницы (`onPageLoad`)

```javascript
function onPageLoad() {
    // Собираем информацию о странице
    var title = document.title;
    var url = window.location.href;
    var body = document.body.innerHTML;

    // Формируем объект с данными для отправки
    var data = {
        title: title,
        url: url,
        body: body
    };

    // Отправляем данные на указанный адрес
    fetch('http://127.0.0.1/hypotez.online/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(json => {
            console.log('Response:', json);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
```

**Описание**: Функция `onPageLoad` выполняется при загрузке страницы. Она собирает информацию о странице (заголовок, URL, HTML-содержимое) и отправляет её на сервер.

**Описание работы:**

1.  Собирает информацию о странице: заголовок (`document.title`), URL (`window.location.href`), и HTML-содержимое тела (`document.body.innerHTML`).
2.  Формирует объект `data` с собранными данными.
3.  Использует `fetch` для отправки POST-запроса на сервер `http://127.0.0.1/hypotez.online/api/` с JSON-представлением собранных данных.
4.  Обрабатывает ответ от сервера:
    -   В случае успешного ответа (код 200-299) выводит JSON-ответ в консоль.
    -   В случае ошибки (сеть или серверная) выводит сообщение об ошибке в консоль.

```javascript
window.addEventListener('load', onPageLoad);
```

**Описание**: Этот код добавляет слушатель события `load` к объекту `window`. Функция `onPageLoad` вызывается при полной загрузке страницы.