## Setup

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Checkbox
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```
---

## Usage

To use the checkbox component, structure your code as with a normal FT method. Parameters follow the same logic as a standard Input checkbox, except for the `state` attribute. For a full reference see the parameters table below.

```python+html
Checkbox(
    id="terms",
    name="terms",
    value="agree",
    state="unchecked"
    )
```

The state of the checkbox on initial render can be set via the `state` attribute. The default state is `unchecked` when omitted.

>[!WARNING]
>When provided, the `id`, `name`, and `value` attributes are passed on to the hidden input element. If you want to target the checkbox itself, you must use a class selector.

---

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `str` | Standard id arg. Passes the id to the hidden input element within.
| `name` | `str` | Standard name arg. Passes the name to the hidden input element within.
| `value` | `str` | Standard value arg. Sets the value of the hidden input element for access through a form submission.
| `state` | `str` | Sets the state of the checkbox on initial load. Options are `checked` or `unchecked`, with the default being `unchecked`.
