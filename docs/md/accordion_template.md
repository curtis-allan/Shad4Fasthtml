
# Accordion Component

The Accordion component is a vertically stacked set of interactive headings that each reveal an associated section of content.

## Setup

Make sure the relevant packages are installed, and setup the imports as shown below.

> [!NOTE]
> If you wish to separately import components you can do so too. Make sure to import and setup `ShadHead()` as well.

from fasthtml import *
from shad4fast import *

app, rt = fast_app(pico=False, hdrs=(ShadHead(),))

---

## Usage

To use the Accordion component, structure your code as follows:

from shad4fast.components.accordion import Accordion, AccordionItem, AccordionTrigger, AccordionContent

```python
Accordion(
    AccordionItem(
        AccordionTrigger("Is it accessible?"),
        AccordionContent(
            P("Yes. It adheres to the WAI-ARIA design pattern.")
        ),
        value="item-1"
    ),
    AccordionItem(
        AccordionTrigger("Is it styled?"),
        AccordionContent(
            P("Yes. It comes with default styles that matches the other components' aesthetic.")
        ),
        value="item-2"
    ),
)
```

---

## Components

### Accordion

The main container for accordion items.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (AccordionItems)    |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### AccordionItem

Container for individual accordion items.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| value     | `str`    | Unique identifier for the item       |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (Trigger and Content)|
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### AccordionTrigger

The clickable header of an accordion item.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (usually text)      |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### AccordionContent

The content revealed when an accordion item is expanded.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (content)           |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

