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

---

## Implementation

To use the Separator component, simply structure your code as with a normal FT method. The `orientation` parameter specifies which orientation of the separator to render, see the parameters table below for a full reference.

```python+html
Separator(orientation="horizontal")
```

> **Note:** If the `orientation` attribute is not provided, the separator will be rendered with the `horizontal` orientation.

---

## Parameters

| Parameter | Description |
| --- | --- |
| `orientation` | The orientation of the separator. Options are `horizontal` and `vertical`. Defaults to `horizontal`.
