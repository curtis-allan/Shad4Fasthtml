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

Implementing an accordion is very straightforward. Simply structure your code as shown below, ensuring that each item is wrapped in an `AccordionItem` component, consisting of an `AccordionTrigger` and `AccordionContent`:

```py
Accordion(
    AccordionItem(
        AccordionTrigger("Heading 1"),
        AccordionContent(
            P("Content 1")
        )
    ),
    AccordionItem(
        AccordionTrigger("Heading 2"),
        AccordionContent(
            P("Content 2")
        )
    ),
    AccordionItem(
        AccordionTrigger("Heading 3"),
        AccordionContent(
            P("Content 3")
        )
    ),
)
```

---

## Parameters

The accordion component takes the standard attributes as a default FastHTML component.
