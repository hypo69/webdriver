Как использовать JavaScript-код для отправки URL из popup.js
=========================================================================================

Описание
-------------------------
Этот JavaScript-код предназначен для обработки события клика на кнопку во всплывающем окне расширения Chrome. Он извлекает URL текущей активной вкладки и отправляет его фоновому скрипту расширения через сообщение. Код также отображает уведомления пользователю об успехе или неудаче отправки.

Шаги выполнения
-------------------------
1.  **Получение кнопки:**
    -   Код начинается с прослушивания события `DOMContentLoaded`, чтобы убедиться, что весь HTML-документ загружен.
    -  Затем он находит кнопку на странице, используя `document.getElementById("sendUrlButton")`.
2.  **Установка прослушивателя кликов:**
    -  Код устанавливает прослушиватель события `click` на найденную кнопку.
    -  Когда кнопка будет нажата, выполняется переданная анонимная функция.
3. **Извлечение URL активной вкладки:**
   -   Внутри прослушивателя клика используется метод `chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => { ... })` для получения списка активных вкладок в текущем окне.
    -   Извлекается первый элемент массива `tabs` (`let activeTab = tabs[0]`) и его URL (`let activeTabUrl = activeTab.url`).
4. **Отправка сообщения фоновому скрипту:**
    -   URL активной вкладки и действие `sendUrl` отправляются фоновому скрипту расширения с помощью `chrome.runtime.sendMessage({ action: "sendUrl", url: activeTabUrl }, (response) => { ... })`.
    -   Метод отправляет сообщение и ждёт ответ.
5. **Обработка ответа:**
   -  В колбэке `chrome.runtime.sendMessage`, проверяется статус ответа.
    - Если статус `"success"`, то выводится сообщение `URL sent successfully!`.
    -  В случае неудачи выводится сообщение `Failed to send URL.`.

Пример использования
-------------------------
.. code-block:: javascript

    // popup.js
    document.addEventListener("DOMContentLoaded", function() {
      const sendUrlButton = document.getElementById("sendUrlButton");
    
       sendUrlButton.addEventListener("click", () => {
        //  alert("Hello, world!");
        chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
            let activeTab = tabs[0];
            let activeTabUrl = activeTab.url;
        
           chrome.runtime.sendMessage({ action: "sendUrl", url: activeTabUrl }, (response) => {
               if (response.status === "success") {
                   alert("URL sent successfully!");
               } else {
                   alert("Failed to send URL.");
                }
           });
        });
      });
    });
    
    
    // background.js (пример обработки сообщения)
    
    /*
    chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
        if (message.action === "sendUrl") {
            console.log("URL получен:", message.url);
            // Выполните необходимые действия здесь (например, отправьте на сервер)
            sendResponse({status: "success"})
            
        }
    });
    */
```