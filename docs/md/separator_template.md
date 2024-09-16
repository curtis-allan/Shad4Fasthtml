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

To use the Separator component, simply structure your code as with a normal FT method. The `orientation` parameter specifies which orientation of the separator to render, see the parameters table below for a full reference.

```python
Separator(orientation="horizontal")
```

> [!TIP]
> If the `orientation` attribute is not provided, the separator will be rendered with the `horizontal` orientation.

---

## Parameters

| Parameter     | Type  | Description                                                                                          |
| ------------- | ----- | ---------------------------------------------------------------------------------------------------- |
| `orientation` | `str` | The orientation of the separator. Options are `horizontal` and `vertical`. Defaults to `horizontal`. |
