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

To use the Button component, structure your code as with a normal FT component. The parameters follow the same structure as the original Shadcn-ui method, see the parameters table below for a full reference.

```python
Button("Button", variant="default", size="default")
```

> [!NOTE]
> If the `variant` or `size` attribute are omitted, the button will be rendered with the `default` variant or size.

---

## Parameters

| Parameter | Type  | Description                                                                                                                              |
| --------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `variant` | `str` | Sets the variant of the Button. Options are `default`, `secondary`, `outline`, `destructive`, `link` and `ghost`. Defaults to `default`. |
| `size`    | `str` | Sets the size of the Button. Options are `default`, `sm`, `lg` and `icon`. Defaults to `default`.                                        |
