Как использовать `background.js` для сбора и отправки данных
=========================================================================================

Описание
-------------------------
Файл `background.js` представляет собой фоновый скрипт расширения Chrome, который отвечает за сбор данных с веб-страниц и их отправку на сервер. Он использует API Chrome для прослушивания событий и взаимодействия с вкладками и хранилищем. Скрипт ждет клика на иконку расширения, после чего отправляет сообщение на активную вкладку для инициирования сбора данных, а затем отправляет полученные данные на сервер.

Шаги выполнения
-------------------------
1.  **Прослушивание клика по иконке расширения:**
    -   `chrome.browserAction.onClicked.addListener(tab => { ... })` устанавливает прослушиватель события клика по иконке расширения.
    -   При клике на иконку выполняется переданная анонимная функция.
2. **Отправка сообщения на вкладку:**
    -  Внутри обработчика клика, `chrome.tabs.sendMessage(tab.id, { action: 'collectData', url: tab.url });` отправляет сообщение на текущую активную вкладку.
    - Сообщение содержит:
       - `action`: `'collectData'` (для идентификации типа сообщения).
        - `url`: URL активной вкладки.
3.  **Прослушивание сообщений от других частей расширения:**
    -  `chrome.runtime.onMessage.addListener((message, sender, sendResponse) => { ... })` устанавливает прослушиватель для сообщений, приходящих из других частей расширения (например, из content scripts).
    -  Когда сообщение с действием `collectData` получено, выполняется анонимная функция.
4.  **Отправка данных на сервер:**
    -   Функция `sendDataToServer(url)` получает URL страницы как аргумент и выполняет следующие действия:
        -  Получает данные из локального хранилища расширения по ключу `'collectedData'` с помощью `chrome.storage.local.get('collectedData', (result) => { ... })`.
        -  Отправляет POST-запрос на сервер по адресу `http://127.0.0.1/hypotez.online/api/` с полученными данными в формате JSON.
        - При успешной отправке данные логируются в консоль.
        -   В случае ошибки отправки в консоль также выводится сообщение об ошибке.
    -  Если данных в хранилище не обнаружено, выводится сообщение об ошибке.
5. **Настройка URL сервера:**
    -   Измените константу `serverUrl` в функции `sendDataToServer` на URL вашего сервера.

Пример использования
-------------------------
.. code-block:: javascript

    // background.js
    
    // Прослушивание клика по иконке
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