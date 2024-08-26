## Setup

All component imports are included when using the default setup. If you wish to separately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Sheet, SheetTrigger
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```


---

## Usage

### Sheet Structure

The `Sheet` component in this implementation differs slightly from the original Shadcn-ui approach:

1. **SheetTrigger**: Requires a unique `sheet_id` to connect with its corresponding `Sheet` component.

2. **Sheet**: Needs a unique `id` that matches the `sheet_id` of its trigger and must **not** contain the `SheetTrigger` component.

### FT Method

Use the `FT` method to quickly and easily add a sheet to your page. 

```python+html
 Div(
        SheetTrigger("Toggle Sheet", sheet_id="demo-sheet"),
    ),
    Sheet(
    Div(
        P("This is where you'd enter your sheet content", cls="text-pretty"),
        cls="p-4",
    ),
    title="Demo Sheet",
    description="This is a demo sheet.",
    footer=Div(SheetCloseButton("Close")),
    content_cls="flex flex-col justify-between",
    id="demo-sheet",
    ),
```


### Components

- `SheetTrigger`: Button to open the sheet
- `Sheet`: Main container for the sheet content
- `SheetContent`: Content of the sheet
- `SheetHeader`: Header section of the sheet
- `SheetFooter`: Footer section of the sheet
- `SheetTitle`: Title of the sheet
- `SheetDescription`: Description of the sheet
- `SheetCloseButton`: Button to close the sheet

### Standard Method

As a reference with a real world example, here's the sheet navigation menu for this site, which uses the standard method to allow for more advances styling.

```python+html
Sheet(
    SheetContent(
        SheetHeader(
            SheetTitle(
                "Documentation",
                cls="tracking-tight select-none",
            ),
            Badge(
                "v1.0",
                variant="outline",
            ),
            cls="flex flex-col items-start w-full",
        ),
        Separator(),
        Div(
            Div(
                RenderNav(),
                cls="overflow-auto block min-h-max no-scrollbar",
            ),
            cls="overflow-hidden pl-2 w-full grid grow max-h-[calc(100vh-8rem)]",
        ),
        Separator(),
        SheetFooter(
            source_code(),
        ),
        side="left",
        cls="w-[215px] sm:w-[250px] flex flex-col h-svh items-start",
    ),
    id="mobile-nav",
    standard=True,
)
```

---

## Parameters

| Parameter | Type | Description|
| --- | --- | --- |
| `standard` | `bool` | If `True`, the sheet will be rendered as a standard sheet. |
| `id` | `str` | The unique identifier for the sheet. |
| `sheet_id` | `str` | The unique identifier for the sheet trigger. |
| `cls` | `str` | The class name for the sheet. |


