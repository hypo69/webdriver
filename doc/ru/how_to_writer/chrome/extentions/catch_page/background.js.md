Как использовать `background.js` для сбора и отправки данных
=========================================================================================

Описание
-------------------------
Файл `background.js` представляет собой скрипт, который выполняется в фоновом режиме расширения Chrome. Он предназначен для перехвата событий клика по иконке расширения, сбора данных с текущей вкладки и отправки этих данных на сервер. Скрипт использует API Chrome для прослушивания событий и взаимодействия с вкладками и хранилищем расширения.

Шаги выполнения
-------------------------
1.  **Прослушивание клика по иконке расширения:**
    - Функция `chrome.action.onClicked.addListener` устанавливает прослушиватель для события клика по иконке расширения.
    -  Когда пользователь нажимает на иконку, выполняется переданная анонимная функция.
2.  **Отправка сообщения на вкладку:**
    -  Анонимная функция в `chrome.action.onClicked.addListener` отправляет сообщение на текущую вкладку с помощью `chrome.tabs.sendMessage`.
    -  Сообщение содержит:
        -  `action`: `'collectData'`, указывающее на действие сбора данных.
        -  `url`: URL текущей вкладки.
    - Это сообщение инициирует сбор данных на странице.
3.  **Прослушивание сообщений от других частей расширения:**
    -  `chrome.runtime.onMessage.addListener` устанавливает прослушиватель для сообщений, отправленных из других частей расширения (например, content scripts).
    -   Переданная анонимная функция выполняется при получении сообщения.
4.  **Проверка типа сообщения:**
    -   Функция проверяет, что полученное сообщение имеет `action` равное `'collectData'`.
    -   Это позволяет отфильтровать сообщения для дальнейшей обработки.
5.  **Отправка данных на сервер:**
    -  Если действие равно `'collectData'`, вызывается функция `sendDataToServer(message.url)`.
    -   Функция `sendDataToServer` делает следующее:
        -   Получает данные из локального хранилища расширения с ключом `collectedData` через `chrome.storage.local.get()`.
        - Если данные есть:
           - Выполняет POST запрос к серверу `http://127.0.0.1/hypotez/catch_request.php`.
           -   Отправляет данные в формате JSON.
           -   Логирует успешную отправку в консоль или ошибку при отправке.
        -   Если данных нет, логирует ошибку в консоль.
6. **Настройка URL сервера:**
    - Установите корректный URL сервера в константе `serverUrl` функции `sendDataToServer`.

Пример использования
-------------------------
.. code-block:: javascript

    // background.js
    
    // Прослушивание клика по иконке расширения
    chrome.action.onClicked.addListener((tab) => {
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
        const serverUrl = 'http://127.0.0.1/hypotez/catch_request.php';
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