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

To use the switch component, structure your code as with a normal FT method. Parameters follow the same logic as a standard Input checkbox. For a full reference see the parameters table below.

```python
Switch(
    id="terms",
    name="terms",
    value="on",
    checked=False,
    )
```

> [!NOTE]
> The state of the switch on initial render can be set via the `checked` attribute. The default state is `False` when omitted.

---

## Parameters

| Parameter | Type   | Description                                                                                                           |
| --------- | ------ | --------------------------------------------------------------------------------------------------------------------- |
| `name`    | `str`  | Standard name arg. Passes the name to the hidden input element within for use with forms.                             |
| `value`   | `str`  | Standard value arg. Sets the value of the hidden input element for access through a form submission. Defaults to `1`. |
| `checked` | `bool` | Sets the state of the switch on initial load. The default is `False` when omitted.                                    |
