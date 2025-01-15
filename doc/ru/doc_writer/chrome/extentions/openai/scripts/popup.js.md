# Документация модуля `popup.js`

## Обзор

Этот модуль `popup.js` является JavaScript-файлом, используемым для обработки логики взаимодействия во всплывающем окне расширения Chrome, предназначенного для взаимодействия с OpenAI API. Он содержит AngularJS-код для управления пользовательским интерфейсом и отправки запросов к серверу.

## Оглавление

-   [Обзор](#обзор)
-   [AngularJS Controller](#angularjs-controller)
    -   [Свойства `$scope`](#свойства-scope)
    -   [Функция `loadAssistants`](#функция-loadassistants)
    -   [Функция `$scope.sendMessage`](#функция-scopemessagesend)

## Обзор

Этот модуль `popup.js` является JavaScript-файлом, используемым для обработки логики взаимодействия во всплывающем окне расширения Chrome, предназначенного для взаимодействия с OpenAI API. Он содержит AngularJS-код для управления пользовательским интерфейсом и отправки запросов к серверу.

## AngularJS Controller

### Описание

Контроллер `MainController` управляет логикой всплывающего окна расширения. Он обрабатывает ввод сообщений, выбор ассистентов и взаимодействие с сервером.

### Свойства `$scope`

-   `message` (str): Текст сообщения, введенного пользователем.
-   `response` (str): Ответ от сервера OpenAI.
-   `assistants` (Array): Список ассистентов, полученный с сервера.
-   `selectedAssistant` (Object): Выбранный ассистент.

### Функция `loadAssistants`

```javascript
    function loadAssistants() {
        const url = 'http://localhost:8000/assistants';  // Создай новый endpoint для получения списка ассистентов
        alert("ASST")
        $http.get(url)
            .then(function (response) {
                $scope.assistants = response.data;  // Список ассистентов
            })
            .catch(function (error) {
                console.error('Ошибка загрузки ассистентов:', error);
            });
    }
```

**Описание**: Функция `loadAssistants` загружает список доступных ассистентов с сервера и сохраняет их в `$scope.assistants`.

**Описание работы:**

1.  Определяет URL для получения списка ассистентов.
2.  Использует `$http.get` для выполнения GET-запроса к серверу.
3.  При успешном ответе сохраняет полученный список ассистентов в `$scope.assistants`.
4.  В случае ошибки выводит сообщение об ошибке в консоль.

### Функция `$scope.sendMessage`

```javascript
    $scope.sendMessage = function () {
        const url = 'http://localhost:8000/ask';  // Адрес FastAPI сервера

        const data = {
            message: $scope.message,
            system_instruction: "You are a helpful assistant.",
            assistant_id: $scope.selectedAssistant.id  // Добавляем ID ассистента
        };

        // Отправка POST-запроса через $http (AJAX)
        $http.post(url, data)
            .then(function (response) {
                $scope.response = response.data.response;  // Ответ от сервера
            })
            .catch(function (error) {
                console.error('Ошибка:', error);
                $scope.response = 'Произошла ошибка. Попробуйте позже.';
            });
    };
```

**Описание**: Функция `$scope.sendMessage` отправляет сообщение пользователя на сервер OpenAI и отображает полученный ответ.

**Описание работы:**

1.  Определяет URL для отправки сообщения на сервер.
2.  Формирует объект `data` с сообщением пользователя, системными инструкциями и ID выбранного ассистента.
3.  Использует `$http.post` для отправки POST-запроса на сервер.
4.  При успешном ответе сохраняет ответ сервера в `$scope.response`.
5.  В случае ошибки выводит сообщение об ошибке в консоль и устанавливает `$scope.response` на сообщение об ошибке.