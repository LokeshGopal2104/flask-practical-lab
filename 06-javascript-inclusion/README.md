
## JavaScript Integration

JavaScript is stored separately from HTML in the Flask static directory.

### File Location

`static/js/script.js`

### Including JavaScript

The JavaScript file is included in `base.html` using:

```html
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

### Features Implemented

- Loading an external JavaScript file.
- Displaying messages in the browser console.
- Handling button clicks using a JavaScript function.
- Displaying an alert popup.
- Sharing JavaScript across multiple pages through template inheritance.

### Testing

1. Open the Home page.
2. Click the `Click Me` button.
3. Verify that the alert popup appears.
4. Open browser Developer Tools using F12.
5. Select Console and verify the JavaScript log message.
6. Repeat the check on the About page.

### Key Takeaway

Flask can serve JavaScript files from its `static` directory, just as it serves CSS and images. The `url_for()` function generates the correct URL to the JavaScript file.
