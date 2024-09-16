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

Used the same as a normal label tag, with styling and an extra `htmlFor` attribute. Parameters follow the same structure as the Shadcn variant. This includes all standard `label` attributes, along with the optional use of `htmlFor` instead of `for`.

```python
Label("Email", htmlFor="email")
```

> [!NOTE]
> The `htmlFor` attribute is purely to handle familiarity with the Shadcn component. It simply maps to a `for` attribute in the outputted HTML. In the future, this will have added benefits (eg. aria configuration).

---

## Parameters

| Attribute | Type  | Description                                                                                    |
| --------- | ----- | ---------------------------------------------------------------------------------------------- |
| `htmlFor` | `str` | The `for` attribute of the label. Must match an `id` on an HTML tag for accessibility support. |
