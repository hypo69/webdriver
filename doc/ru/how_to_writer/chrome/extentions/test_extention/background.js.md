Как использовать `background.js` для сбора и отправки данных
=========================================================================================

Описание
-------------------------
Файл `background.js` является фоновым скриптом расширения Chrome, который отвечает за перехват кликов по иконке расширения, получение URL активной вкладки, сбор данных и их отправку на сервер. Он использует Chrome API для взаимодействия с вкладками, хранилищем и отправки запросов.

Шаги выполнения
-------------------------
1. **Установка прослушивателя клика по иконке:**
   -  `chrome.browserAction.onClicked.addListener(tab => { ... })` устанавливает прослушиватель события клика по иконке расширения.
   -  Когда пользователь кликает на иконку, выполняется анонимная функция, переданная в качестве аргумента.
2. **Отправка сообщения на вкладку:**
    -  Внутри обработчика клика, `chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });` отправляет сообщение на активную вкладку.
    -  Сообщение содержит:
       -  `action`: `'collectData'` (указывает на запрос сбора данных).
       -  `url`: URL активной вкладки.
3. **Прослушивание сообщений из других частей расширения:**
   - `chrome.runtime.onMessage.addListener((message, sender, sendResponse) => { ... })` устанавливает прослушиватель для сообщений, приходящих из других частей расширения (например, content script).
   - Когда приходит сообщение, выполняется анонимная функция.
4.  **Обработка сообщения `collectData`:**
    -   Внутри прослушивателя проверяется поле `message.action`. Если оно равно `'collectData'`, вызывается функция `sendDataToServer(message.url)`.
5.  **Отправка данных на сервер:**
    - Функция `sendDataToServer(url)` получает данные из локального хранилища расширения по ключу `collectedData` с помощью `chrome.storage.local.get('collectedData', (result) => { ... })`.
    -   После получения данных:
         -  Выполняет `fetch` запрос методом POST на адрес `http://127.0.0.1/hypotez.online/api/`.
         -   Отправляет данные в формате JSON.
       -   В случае успешной отправки в консоль выводится сообщение `'Data sent to server successfully'`.
       - При ошибке в консоль выводится сообщение `Error sending data to server:`.
    - Если в локальном хранилище нет данных, выводится сообщение `No collected data found`.
6.  **Настройка URL сервера:**
   -  Измените константу `serverUrl` в функции `sendDataToServer` на URL вашего сервера.

Пример использования
-------------------------
.. code-block:: javascript

    // background.js
    
    // Прослушивание клика по иконке расширения
    chrome.browserAction.onClicked.addListener(tab => {
        chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });
    });
    
    // Прослушивание сообщений от других частей расширения
    chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
        if (message.action === 'collectData') {
            sendDataToServer(message.url);
        }
    });
    
    // Функция отправки данных на сервер
    function sendDataToServer(url) {
        const serverUrl = 'http://127.0.0.1/hypotez.online/api/';
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