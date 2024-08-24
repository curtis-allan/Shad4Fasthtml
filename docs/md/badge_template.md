## Setup

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Badge
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

---

## Usage

To use the Badge component, structure your code as with a normal FT method. The `variant` parameter specifies which variant of the badge to render, see the parameters table below for a full reference.

```python+html
Badge("v2.0", variant="default")
```

> [!NOTE]
>If the `variant` attribute is not provided, the badge will be rendered with the `default` variant.

---

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `variant` | `str` | Sets the variant of the badge. Options are `default`, `secondary`, `outline`, and `destructive`. Defaults to `default`.
