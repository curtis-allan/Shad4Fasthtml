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

To use the scroll area component, structure your code as with a normal FT method. The component takes an `orientation` parameter, which is the orientation of the scroll area.

```python
def fake_data():
    results = ()
    for i in range(50):
        results += (Div(f"Item Entry #{i}", cls="text-sm"), Separator(cls="my-2"))
    return results

ScrollArea(
    Div(
        H4("Entries", cls="mb-4 text-sm font-medium leading-none"),
        *fake_data(),
        cls="p-4",
    ),
    cls="h-72 w-48 rounded-md border",
)
```

> [!NOTE]
> If not set, the orientation will default to `vertical`.

---

## Parameters

| Parameter   | Type  | Description                                                |
| ----------- | ----- | ---------------------------------------------------------- |
| orientation | `str` | The orientation of the scroll area. Defaults to `vertical` |
