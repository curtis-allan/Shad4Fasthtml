## Setup

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Button
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

---

## Usage

To use the Button component, structure your code as with a normal FT method. The parameters follow the same structure as the original Shadcn-ui method, see the parameters table below for a full reference.

```python+html
Button("Button", variant="default", size="default")
```

> [!NOTE]
>If the `variant` or `size` attribute are omitted, the button will be rendered with the `default` variant or size.

---

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `variant` | `str` | Sets the variant of the Button. Options are `default`, `secondary`, `outline`, `destructive`, `link` and `ghost`. Defaults to `default`.
| `size` | `str` | Sets the size of the Button. Options are `default`, `sm`, `lg` and `icon`. Defaults to `default`.

