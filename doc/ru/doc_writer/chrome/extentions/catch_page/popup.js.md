# Документация модуля `popup.js`

## Обзор

Этот модуль `popup.js` представляет собой JavaScript-файл, используемый для обработки логики взаимодействия во всплывающем окне расширения Chrome. Он содержит код для обработки клика по кнопке и отправки URL текущей вкладки в фоновый скрипт.

## Оглавление

-   [Обзор](#обзор)
-   [Функции](#функции)
    -   [Обработчик события `click`](#обработчик-события-click)

## Функции

### Обработчик события `click`

```javascript
document.getElementById("sendUrlButton").addEventListener("click", () => {
    alert("Hello, world!");
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
```

**Описание**: Этот код добавляет обработчик события `click` к элементу с `id="sendUrlButton"`. При клике на кнопку выполняются следующие действия:

1.  Выводит сообщение `Hello, world!` с помощью `alert`.
2.  Использует `chrome.tabs.query`, чтобы получить информацию о текущей активной вкладке.
3.  Извлекает URL активной вкладки.
4.  Использует `chrome.runtime.sendMessage`, чтобы отправить сообщение в фоновый скрипт расширения с действием `sendUrl` и URL активной вкладки.
5.  Получает ответ от фонового скрипта и показывает соответствующее сообщение (успешное или нет) через `alert`.