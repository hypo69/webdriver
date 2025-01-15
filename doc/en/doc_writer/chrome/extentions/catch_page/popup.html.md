# HTML Documentation: `popup.html`

This document provides an overview of the `popup.html` file, which is part of a Chrome extension designed to send the current page URL.

## Table of Contents

1.  [Overview](#overview)
2.  [HTML Structure](#html-structure)
3.  [JavaScript Interaction](#javascript-interaction)

## Overview

The `popup.html` file defines the user interface for a popup within a Chrome extension. It includes a button that, when clicked, triggers the sending of the current page's URL. The script is set up for potential debugging purposes with a `MODE` variable.

## HTML Structure

The HTML structure is straightforward and includes:

-   A `<!DOCTYPE html>` declaration to define the document type.
-   A `<html>` tag that is the root element.
-  A `<head>` tag containing:
    - A `<title>` tag with the text "URL Sender".
    - A `<script>` tag to include the `popup.js` file.
-   A `<body>` tag containing:
    - A `<button>` with the id `sendUrlButton` and the text "Send URL".



## JavaScript Interaction

The `<script src="popup.js"></script>` tag includes the JavaScript file `popup.js`, which is expected to handle the following:

-   Adding an event listener to the button with the id `sendUrlButton`.
-  Sending the URL of the current tab to a background script upon button click.

This simple HTML structure provides a basic interface for an extension, which is then enhanced by the javascript functionality described in `popup.js`.