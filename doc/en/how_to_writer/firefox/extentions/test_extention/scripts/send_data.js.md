How to use this code block
=========================================================================================

Description
-------------------------
This JavaScript code is designed to be a content script for a browser extension. It is intended to be injected into web pages. Its purpose is to collect information from the page, including the title, URL, and HTML body content, and then send this data to a specified server endpoint using a POST request. It also includes logging of the response to the console.

Execution steps
-------------------------
1.  **Define the `onPageLoad` function**: The code defines a function called `onPageLoad` which encapsulates the logic to be executed when the page has finished loading.
    -  It extracts the page's title from `document.title`.
    - It extracts the current page's URL using `window.location.href`.
    -   It extracts the HTML content of the page body by using `document.body.innerHTML`.
    - It creates a `data` object to hold the extracted information with keys: `title`, `url`, and `body`.
    -   It then sends a POST request using the `fetch` function to the specified server endpoint with the constructed data, using `JSON.stringify()` to send payload.
    - It logs a success message if the request was successful, otherwise logs an error message to the console.
2.  **Set up the event listener**: The `window.addEventListener('load', onPageLoad);` line adds an event listener that waits for the `load` event, indicating that the entire page and all of its resources have loaded.
    -   When the event occurs, it executes the `onPageLoad` function, thus sending collected data after the page has fully loaded.

Usage example
-------------------------
```javascript
// contentScript.js

// Create an event handler for page loading
function onPageLoad() {
    // Collect page information
    var title = document.title;
    var url = window.location.href;
    var body = document.body.innerHTML;

    // Create an object with data to send
    var data = {
        title: title,
        url: url,
        body: body
    };

    // Send the data to the specified address
    fetch('http://127.0.0.1/hypotez.online/api/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(json => {
            console.log('Response:', json);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// Add an event listener for the page load event
window.addEventListener('load', onPageLoad);
```
```

## Changes
- Provided a detailed description of the JavaScript code, including its purpose and functionality.
- Outlined clear execution steps of the provided javascript code.
- Included a comprehensive usage example with comments.
- Used specific terms for descriptions to be precise.
- Formatted the response according to the `reStructuredText (RST)` structure.
- Added detailed explanation for  `document.title`, `window.location.href` and `document.body.innerHTML` properties, and how to use them for getting page info.
- Explained how the data is constructed and sent to a server with `fetch` method.
- Added a description about the usage of `window.addEventListener('load', onPageLoad)` method and what it does.
- Added clarification on where this code should be used and what actions are done by it on the page load.
- Added explanation for the fetch and exception handling.