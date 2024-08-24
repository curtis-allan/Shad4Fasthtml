## Setup

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Card
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

---
## Usage

### FT Method

Using the FastHtml method, you can pass in the `title`, `description`, and `footer` attributes to the `Card` component. For a full attribute reference see the parameters table below.

```python+html
Card(
    Input(type="text", placeholder="Enter some text..."),
    title="Create a post",
    description="Enter your post title below.",
    footer=Div(
        Button("Cancel", variant="outline"),
        Button("Submit"),
        cls="flex w-full justify-end gap-2",
    ),
    cls="w-[80%]",
)
```

### Standard Method

The standard method is similar to the FastHtml method, but follows the original Shadcn-ui method of passing in the `CardHeader`, `CardTitle`, `CardDescription`, `CardContent`, and `CardFooter` components. To ensure the component is rendered correctly, you must pass in the `standard` attribute as `True`.

```python+html
Card(
    CardHeader(
        CardTitle("Create a post"),
        CardDescription("Enter your post title below."),
    ),
    CardContent(Input(type="text", placeholder="Enter some text..."),),
    CardFooter(
        Div(
            Button("Cancel", variant="outline"),
            Button("Submit"),
            cls="flex w-full justify-end gap-2",
        ),
    ),
    standard=True,
    cls="w-[80%]",
)
```

---

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `title` | `str` | Sets the title of the card.
| `description` | `str` | Sets the description of the card.
| `footer` | `any` | Sets the footer of the card. Can be any valid FT component/components.
| `standard` | `bool` | A boolean attribute to indicate if the component is rendered in the standard method. Defaults to `False`.
