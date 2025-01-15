Как использовать `popup.html` для отправки URL
=========================================================================================

Описание
-------------------------
Файл `popup.html` представляет собой HTML-страницу для всплывающего окна расширения Chrome. Основная его функция — предоставить пользователю кнопку для отправки URL текущей вкладки в фоновый скрипт расширения. Этот файл является частью расширения, использующего веб-драйверы для автоматизации и сбора данных.

Шаги выполнения
-------------------------
1. **Создание HTML-страницы:**
   - Файл `popup.html` содержит HTML-структуру для всплывающего окна расширения.
   -  Включает в себя:
     - Тег `<title>` для задания заголовка окна.
      -  Подключение внешнего скрипта `popup.js` для обработки событий.
    - Кнопку с `id="sendUrlButton"` для запуска отправки URL.
2.  **Подключение скрипта `popup.js`:**
    -  HTML-страница подключает файл `popup.js`, который содержит JavaScript код для обработки событий.
    -  Скрипт `popup.js` должен находится в той же директории.
3. **Использование кнопки для отправки URL:**
   - Когда пользователь нажимает на кнопку с `id="sendUrlButton"`, скрипт `popup.js` должен:
     -  Получить ID и URL текущей вкладки.
     -  Отправить сообщение на фоновый скрипт (`background.js`) с действием `collectData` и URL вкладки.
4.  **Обработка сообщения в `background.js`:**
   -  Фоновый скрипт `background.js` принимает сообщение, отправленное из `popup.js` и выполняет дальнейшие действия (например, собирает данные и отправляет их на сервер).
5.  **Настройка MODE:**
   - Переменная `MODE` предназначена для отладки. Возможные значения: `debug` или `prod`.
   - Если MODE="debug" скрипт может вести себя иначе чем в production.

Пример использования
-------------------------
.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>URL Sender</title>
        <script src="popup.js"></script>
    </head>
    <body>
        <button id="sendUrlButton">Send URL</button>
    </body>
    </html>
    
    <script>
        // popup.js
        document.addEventListener('DOMContentLoaded', function () {
            const sendUrlButton = document.getElementById('sendUrlButton');
            sendUrlButton.addEventListener('click', function () {
                chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                    if (tabs && tabs.length > 0) {
                         const currentTab = tabs[0];
                         chrome.runtime.sendMessage({ action: 'collectData', url: currentTab.url });
                     }
                });
            });
         });
    </script>

   
    <!-- //background.js

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
    -->
```