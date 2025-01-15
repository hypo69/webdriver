# JavaScript Documentation: `popup.js`

This document provides an overview of the `popup.js` script, which is responsible for handling interactions within the popup of a browser extension, specifically sending the current tab's URL to the background script.

## Table of Contents

1.  [Overview](#overview)
2.  [Event Listener](#event-listener)
3. [Functionality](#functionality)

## Overview

The `popup.js` script is an essential part of a browser extension's popup that runs when the popup is opened. Its main purpose is to listen for user actions (specifically, clicking the "Send URL" button) and then send the current page's URL to the background script for further processing.

## Event Listener

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

**Description**: This event listener is triggered when the HTML button with the ID `sendUrlButton` is clicked.

**Functionality**:

-   An alert `"Hello, world!"` appears as a simple test.
-   It uses `chrome.tabs.query()` to get information about the active tab in the current window.
-   It extracts the URL (`activeTabUrl`) from the active tab.
-   It uses `chrome.runtime.sendMessage` to send a message to the background script.
-  The message has the following properties:
    -   `action`: Set to `"sendUrl"`.
    -  `url`: The URL of the current tab (`activeTabUrl`).
-   It sets up a callback function to handle the response from the background script.
-   The callback function:
    -  Displays an alert saying "URL sent successfully!" if the response status is "success".
    -  Displays an alert saying "Failed to send URL." if the response status is not "success".

This documentation provides an overview of the `popup.js` script and its interactions for developers.