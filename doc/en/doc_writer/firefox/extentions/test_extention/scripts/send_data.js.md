# JavaScript Documentation: Anonymous Script

This document provides an overview of the anonymous JavaScript code snippet, which is designed to collect page information and send it to a server after the page loads.

## Table of Contents

1.  [Overview](#overview)
2.  [Event Listener](#event-listener)
3.  [Function](#function)
    -   [`onPageLoad`](#onpageload)

## Overview

The anonymous JavaScript code provided is designed to be executed within a web page context. It is responsible for collecting specific information about the page (title, URL, and body content) and sending this data to a predefined server endpoint after the page has fully loaded.

## Event Listener

### `window.addEventListener('load', onPageLoad);`

```javascript
window.addEventListener('load', onPageLoad);
```

**Description**: This event listener is triggered when the web page has fully loaded.

-   It sets up a listener for the `load` event on the `window` object.
-   When the event is triggered, it executes the `onPageLoad` function.

## Function

### `onPageLoad`

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

**Description**: This function is responsible for collecting page data and sending it to a server.

**Functionality**:

-   It retrieves the page's `title`, `url` (using `window.location.href`), and the full `innerHTML` of the `<body>` element.
-  It creates a data object with these properties.
-   It sends a POST request to the specified URL (`http://127.0.0.1/hypotez.online/api/`) with collected data using the `fetch` API.
-   Sets the `Content-Type` header to `application/json`.
-    Parses the JSON response upon success.
-   Logs the response data using `console.log`.
-   If an error occurs during the request, it catches and logs the error message using `console.error`.

This documentation explains how the anonymous JavaScript code operates, collecting data and sending it to a server after the page has finished loading.