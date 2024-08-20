## Usage

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Switch
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

## Ft method

A relatively simple component, just structure your code as with a normal FT method. Parameters follow the same logic as a standard Input checkbox, except for the `state` attribute. For a full reference see the parameters table below.

```python+html
Switch(
    id="switch-toggle",
    name="switch-toggle",
    value="agree",
    state="uncheched",
)
```

When using the switch in a form, note that the `id`, `name`, and `value` attributes are passed on to the hidden input element. If you want to target the switch itself (either through htmx or javascript), you must use a class selector.

> **Note:** The state of the switch on initial render can be set via a 'state' attribute, either being `checked` or `unchecked`. The default state is `unchecked` when omitted.

## Parameters

| Parameter | Description |
| --- | --- |
| `id` | Passes the id to the hidden input element.
| `name` | Passes the name to the hidden input element.
| `value` | Sets the value of the hidden input element for access through a form submission.
| `state` | Controls how the switch is rendered on initial load. Options are `checked` or `unchecked`, with the default being `unchecked`.
