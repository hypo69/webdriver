# Документация модуля `background.js`

## Обзор

Этот модуль `background.js` является фоновым скриптом для расширения Chrome, который обрабатывает сообщения, связанные со сбором данных, и отправляет их на сервер.

## Оглавление

-   [Обзор](#обзор)
-   [Функции](#функции)
    -   [Слушатель кликов по иконке расширения](#слушатель-кликов-по-иконке-расширения)
    -   [Слушатель сообщений](#слушатель-сообщений)
    -   [`sendDataToServer`](#senddatatoserver)

## Функции

### Слушатель кликов по иконке расширения

```javascript
chrome.browserAction.onClicked.addListener(tab => {
    chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
});
```

**Описание**: Этот код устанавливает слушатель для события клика по иконке расширения. При клике он отправляет сообщение с действием `'collectData'` и URL текущей вкладки контентному скрипту на этой вкладке.

### Слушатель сообщений

```javascript
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === 'collectData') {
        sendDataToServer(message.url);
    }
});
```

**Описание**: Этот код устанавливает слушатель для сообщений, отправленных из других частей расширения (контентных или фоновых скриптов). При получении сообщения с действием `'collectData'` он вызывает функцию `sendDataToServer()` с URL из сообщения.

### `sendDataToServer`

```javascript
function sendDataToServer(url) {
    const serverUrl = 'http://127.0.0.1/hypotez.online/api/'; // Change to your server endpoint
    chrome.storage.local.get('collectedData', (result) => {
        const collectedData = result.collectedData;
        if (collectedData) {
            fetch(serverUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(collectedData)
            })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Failed to send data to server');
                    }
                    console.log('Data sent to server successfully');
                })
                .catch(error => {
                    console.error('Error sending data to server:', error);
                });
        } else {
            console.error('No collected data found');
        }
    });
}
```

**Описание**: Функция `sendDataToServer` извлекает данные из локального хранилища Chrome под ключом `'collectedData'` и отправляет их на сервер по указанному URL (`serverUrl`).

**Параметры**:

-   `url` (string): URL текущей вкладки, отправленной из контентного скрипта.

**Описание работы:**

1.  Извлекает данные из локального хранилища Chrome под ключом `'collectedData'`.
2.  Проверяет наличие данных.
3.  Если данные есть, отправляет POST-запрос на сервер с JSON-представлением этих данных.
4.  Регистрирует сообщение об успешной отправке или ошибку в консоли.