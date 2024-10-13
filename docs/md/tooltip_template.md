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

To implement a tooltip, simply structure your code as shown below. The `Tooltip` component takes an optional `method` attribute, which sets the interaction method (hover or click).

The `TooltipContent` component takes an optional `state` attribute, which sets the initial view state of the tooltip (open or closed).

Further details of these attributes are outlined in the parameters table below.

> [!TIP]
> If not provided, the `state` attribute defaults to `closed` and the `method` attribute defaults to `hover`.

The `TooltipTrigger` component can take any valid FastHTML component, such as a `Button`, icon, or even some text:

```py
Tooltip(
    TooltipTrigger(Lucide("circle-help", cls="size-5 cursor-pointer")),
    TooltipContent("This is a tooltip!", state='closed'),
    method="hover",
)
```

Alternatively, you can simply enter a string to have it render as a regular Shad4Fast button component:

```python
Tooltip(
    TooltipTrigger("Click Me!"),
    TooltipContent("This is another tooltip.", state='open'),
    method="click",
)
```

---

## Parameters

| Attribute | Type  | Description                                                                                                                                                     |
| --------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `state`   | `str` | Applies to the `TooltipContent` component. Sets the initial view state of the tooltip. Can be either `open` or `closed`. Defaults to `closed`.                  |
| `method`  | `str` | Sets the interaction method of the tooltip. Can be either `hover` or `click`. Will throw an assertion error if not provided a valid value. Defaults to `hover`. |
