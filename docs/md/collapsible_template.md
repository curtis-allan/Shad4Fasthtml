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

To use the collapsible component, simply setup your code as follows. The main `Collapsible` container takes a single custom parameter, `state`, which sets the initial open state of the collapsible content. All content you wish to be collapsible is passed into the `CollapsibleContent` function.

The `CollapsibleTrigger` can be passed into any function within the main `Collapsible` container:

```python
Collapsible(
    Div(H4("Header"), CollapsibleTrigger()),
    Div("Uncollapsed Content"),
    CollapsibleContent(
        Div("Collapsed 1"),
        Div("Collapsed 2"),
        cls="space-y-2"),
    cls="space-y-2",
)
```

---

## Parameters

| Parameter | Type                     | Description                                                                                                                 |
| --------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `state`   | `str ['open', 'closed']` | Applies to the `Collapsible` container. A string defining the open state of the collapsible content. Defaults to `'closed'` |
