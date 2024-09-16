## Setup

Make sure the relevant packages are installed, and setup the imports as shown below.

> [!NOTE]
> If you wish to seperately import components you can do so too. Make sure to import and setup `ShadHead()` as well.

```python
from fasthtml import *
from shad4fast import *

app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

---

## Usage

To use the textarea component, structure your code as with a normal FT method. Parameters follow the same structure as a normal `textarea` tag.

```python
Textarea(placeholder="Enter something", id="content")
```

> [!TIP]
> To make the textarea component resizable, set the class value to `resize-none`, or options include `resize-vertical`, or `resize-horizontal`.

---

## Parameters

For a full reference for attribute options, check out the Mozilla docs for the input tag<a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea" target="_blank">here.</a>
