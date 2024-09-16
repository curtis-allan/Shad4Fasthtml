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

The `Slider` component takes a set of attributes associated with a standard slider. These are:

- `min`: The minimum value of the slider.
- `max`: The maximum value of the slider.
- `step`: The step size of the slider.
- `value`: The initial value of the slider.
- `name`: The name of the slider. Used for form submission.

For a full list of parameters, see the parameters table below.

```python
Slider(
    min=0,
    max=100,
    name="demo-slider",
    value=0,
    step=1,
    cls="max-w-64",
)
```

> [!NOTE]
> All attributes are optional. To see their default values, see the parameters table below.

---

## Parameters

| Attribute | Type  | Description                                                                     |
| --------- | ----- | ------------------------------------------------------------------------------- |
| `min`     | `int` | The minimum value of the slider. Defaults to `0`.                               |
| `max`     | `int` | The maximum value of the slider. Defaults to `100`.                             |
| `step`    | `int` | The step size of the slider. Defaults to `1`.                                   |
| `value`   | `int` | The initial value of the slider. Defaults to `0`.                               |
| `name`    | `str` | The name of the slider. Used for form submission. Passed onto the hidden input. |
