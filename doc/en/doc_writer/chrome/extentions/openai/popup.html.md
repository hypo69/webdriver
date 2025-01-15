# HTML Documentation: `popup.html` (OpenAI Model Interface)

This document provides an overview of the `popup.html` file, which serves as the main user interface for the OpenAI Model Interface extension popup.

## Table of Contents

1.  [Overview](#overview)
2.  [HTML Structure](#html-structure)
    -   [Header](#header)
    -   [Navigation Tabs](#navigation-tabs)
    -   [Chat Tab Content](#chat-tab-content)
    -   [Model Tab Content](#model-tab-content)
3.  [JavaScript Interaction](#javascript-interaction)

## Overview

The `popup.html` file is the primary HTML document for the extension popup. It uses AngularJS to create a dynamic and interactive user interface, allowing users to interact with the OpenAI Model. The interface includes tabs for chatting with the model and managing its training status. It is set up for potential debugging purposes with a `MODE` variable.

## HTML Structure

The HTML structure is divided into several parts:

### Header

-   A `<!DOCTYPE html>` declaration to define the document type.
-   An `<html>` tag with `lang="en"` attribute to define the root element.
-  A `<head>` tag containing:
    - A `<title>` tag with the text "OpenAI Model Interface".
    -   `<script>` tags to include AngularJS, jQuery, and the `popup.js` file.
    -  A `<link>` tag to include external style sheet file.

### Navigation Tabs

-   A `<ul>` element with the class `tabs` to create horizontal navigation tabs:
    -   A `<li>` element with `ng-class` and `ng-click` directives for the "Chat" tab.
    -   A `<li>` element with `ng-class` and `ng-click` directives for the "Model" tab.

### Chat Tab Content

-  A `<div>` element with the `ng-show` directive to display the content of the Chat tab:
    -   An `<h2>` tag with the text "Chat with Model".
    -   A `<label>` element for selecting an assistant from a dropdown list.
    -   A `<select>` element with `ng-model` and `ng-options` directives for choosing an assistant.
    -   A `<textarea>` element with the `ng-model` directive for entering a message.
    -  A `<button>` with the `ng-click` directive to send the message.
    -   A `<div>` element with the id `response` to display the model's response.
        -   An `<h3>` tag with the text "Response:".
        -   A `<p>` tag with the `{{response}}` to dynamically render the response.

### Model Tab Content

-  A `<div>` element with the `ng-show` directive to display the content of the Model tab:
    -  An `<h2>` tag with the text "Model Training and Status".
    -   A `<p>` tag with a brief description.
    -   A `<label>` element for entering training data in a text area.
    -  A `<textarea>` element with the `ng-model` directive for entering training data.
    -  A `<button>` with the `ng-click` directive to start model training.
     -   An `<h3>` tag with the text "Training Status:".
    - A `<p>` tag with `{{trainingStatus}}` to display the training status.

## JavaScript Interaction

The `<script src="popup.js"></script>` tag includes the JavaScript file `popup.js`, which is expected to handle the following:

-   Initializes AngularJS module named `openaiApp` and a controller named `MainController`.
-   Manages the tab switching logic using `isTabActive` and `setActiveTab`.
-   Handles fetching data for `assistants` dropdown menu, updating `selectedAssistant`, and the main logic for sending message to the model.
-   It may contains the functionality for getting and processing responses.
-  It may also includes the logic for training model, updating the training status and fetching data for training data.

This document provides a clear overview of the `popup.html` file and its structure for developers working on the OpenAI Model Interface extension.