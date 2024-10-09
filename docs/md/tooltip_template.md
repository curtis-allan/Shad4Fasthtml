
# Tooltip Component

The Tooltip component displays additional information when a user hovers over or focuses on an element.

## Setup

Make sure the relevant packages are installed, and setup the imports as shown below.

> [!NOTE]
> If you wish to separately import components you can do so too. Make sure to import and setup `ShadHead()` as well.

from fasthtml import *
from shad4fast import *

app, rt = fast_app(pico=False, hdrs=(ShadHead(),))

---

## Usage

To use the Tooltip component, structure your code as follows:

from shad4fast.components.tooltip import Tooltip, TooltipTrigger, TooltipContent

```python
Tooltip(
    TooltipTrigger(Button("Hover me")),
    TooltipContent("This is a tooltip!"),
)
```

---

## Components

### Tooltip

The main container for the tooltip.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (Trigger and Content)|
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### TooltipTrigger

The element that triggers the tooltip on hover or focus.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (usually a button or text)|
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### TooltipContent

The content of the tooltip that appears when triggered.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| position  | `str`    | Position of the tooltip (top, bottom, left, right)|
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (tooltip content)   |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

---

## Styling

All components come with default styling using Tailwind CSS classes. You can customize the appearance by passing additional classes through the `cls` parameter or by modifying the default classes in the component definitions.

---

## Accessibility

These components are designed with accessibility in mind. They use semantic HTML elements and ARIA attributes where appropriate. However, you may need to add additional ARIA attributes depending on your specific implementation and requirements.

---

## JavaScript Interaction

For the Accordion and Tooltip components to function properly, you may need to add JavaScript for toggling visibility and managing interactions. This is not included in the basic components and would need to be implemented separately, potentially using HTMX or custom JavaScript.
