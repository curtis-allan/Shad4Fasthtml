## Setup

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Label
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```
---

## Usage

To use the input component, structure your code as with a normal FT method. Parameters follow the same structure as the Shadcn variant. This includes all standard `label` attributes, along with the optional use of `htmlFor` instead of `for`.

```python+html
Label("Email", htmlFor="email")
```

>[!NOTE]
>The `htmlFor` attribute is purely to handle familiarity with the Shadcn component. It simply maps to a `for` attribute in the outputted HTML. In the future, this will have added benefits (eg. aria configuration).

---

## Parameters

| Attribute | Type | Description |
| --- | --- | --- |
| `htmlFor` | `str` | The `for` attribute of the label. Must match an `id` on an HTML tag for accessibility support.