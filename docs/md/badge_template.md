## Usage

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Badge
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

## Ft method

To use the Badge component, structure your code as with a normal FT method. Attributes follow the standard Shadcn Badge structure, for a full reference see the parameters table below.

```python+html
Div(
    H1(
        "Shad4FastHtml",
        cls="text-2xl font-semibold tracking-tight leading-loose",
    ),
    Badge("v2.0", variant="default"),
    cls="flex gap-1.5 items-center justify-center",
)
```

> **Note:** If the `variant` attribute is not provided, the badge will be rendered with the `default` variant.

## Parameters

| Parameter | Description |
| --- | --- |
| `variant` | The variant of the badge. Options are `default`, `secondary`, `outline`, and `destructive`. Defaults to `default`.
