# JavaScript Documentation: `popup.js` (OpenAI Model Interface)

This document provides an overview of the `popup.js` script, which is responsible for managing the logic and interactions within the popup of the OpenAI Model Interface extension, utilizing AngularJS.

## Table of Contents

1.  [Overview](#overview)
2.  [AngularJS Module and Controller](#angularjs-module-and-controller)
    -   [`openaiApp`](#openaiapp)
    -   [`MainController`](#maincontroller)
        -   [Scope Variables](#scope-variables)
        -   [Functions](#functions)
            -   [`loadAssistants`](#loadassistants)
            -   [`sendMessage`](#sendmessage)

## Overview

The `popup.js` script initializes an AngularJS application (`openaiApp`) and defines the `MainController`. This controller manages the user interface logic for interacting with the OpenAI Model. It includes fetching assistants, sending messages, and updating the view with the model's response.

## AngularJS Module and Controller

### `openaiApp`

```javascript
const app = angular.module('openaiApp', []);
```

**Description**: Initializes the AngularJS application module named `openaiApp`.

-   This sets up the AngularJS application, creating a module that will contain the application's components and logic.

### `MainController`

```javascript
app.controller('MainController', function ($scope, $http) {
    // ... controller logic ...
});
```

**Description**: Defines the `MainController` which manages the UI for interacting with the OpenAI Model.

-   This controller handles the functionality of both the "Chat" and "Model" tabs in the popup.
-   It is responsible for fetching available assistants, sending messages to the model, and processing the received data.
#### Scope Variables
-   `$scope.message`: Stores the user's input message.
-   `$scope.response`: Stores the response from the OpenAI model.
-  `$scope.assistants`: Stores a list of available assistants.
-   `$scope.selectedAssistant`: Stores the currently selected assistant.

#### Functions

##### `loadAssistants`

```javascript
function loadAssistants() {
    const url = 'http://localhost:8000/assistants';  // Create a new endpoint to receive the list of assistants
    alert("ASST")
    $http.get(url)
        .then(function (response) {
            $scope.assistants = response.data;  // List of assistants
        })
        .catch(function (error) {
            console.error('Error loading assistants:', error);
        });
}
```

**Description**: Fetches the list of available assistants from a server endpoint.

-   It makes a GET request to `http://localhost:8000/assistants`.
-   Upon successful response, it updates the `$scope.assistants` with the data received from the server.
-   If an error occurs during the request, it logs the error message to the console.

##### `sendMessage`

```javascript
$scope.sendMessage = function () {
    const url = 'http://localhost:8000/ask';  // Address of FastAPI server

    const data = {
        message: $scope.message,
        system_instruction: "You are a helpful assistant.",
        assistant_id: $scope.selectedAssistant.id  // Add the ID of the assistant
    };

    // Sending POST request via $http (AJAX)
    $http.post(url, data)
        .then(function (response) {
            $scope.response = response.data.response;  // Response from the server
        })
        .catch(function (error) {
            console.error('Error:', error);
            $scope.response = 'An error occurred. Please try again later.';
        });
};
```

**Description**: Sends a message to the OpenAI model and updates the UI with the response.

-   It makes a POST request to `http://localhost:8000/ask`.
-   The request includes the user's input message (`$scope.message`), a default system instruction, and the ID of the selected assistant (`$scope.selectedAssistant.id`).
-   Upon a successful response, it updates the `$scope.response` with the response from the server.
-  If an error occurs during the request, it logs the error message to the console and sets an error message to `$scope.response`.

This documentation provides a detailed explanation of how `popup.js` handles the user interface logic within the OpenAI Model Interface extension.