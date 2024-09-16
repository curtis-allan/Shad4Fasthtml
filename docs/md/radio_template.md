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

Implementing a radio group is simple. The `RadioGroup` component is used to wrap the radio buttons, and the `RadioGroupItem` component is used to create each radio button.

The `RadioGroup` takes an optional `default_value` parameter, which sets the initial value of the radio group. For a full list of parameters, see the parameters table below.

Each `RadioGroupItem` takes a `value` parameter, which sets the value of the radio button. You can link a `Label` component to each radio button via the `id` attribute to provide a label for each option, as shown here:

```python
RadioGroup(
    Div(
        RadioGroupItem(value="option1", id="option1"),
        Label("Claude 3.5 Sonnet", htmlFor="option1"),
        cls="flex items-center space-x-2",
    ),
    Div(
        RadioGroupItem(value="option2", id="option2"),
        Label("Gpt 4o", htmlFor="option2"),
        cls="flex items-center space-x-2",
    ),
    Div(
        RadioGroupItem(value="option3", id="option3"),
        Label("Gpt 4 Turbo", htmlFor="option3"),
        cls="flex items-center space-x-2",
    ),
    name="radio-demo",
    default_value="option1",
)
```

> [!NOTE]
> If the `default_value` parameter is not set, none of the radio buttons will be selected by default.

---

## Parameters

| Attribute       | Type  | Description                                                                                                     |
| --------------- | ----- | --------------------------------------------------------------------------------------------------------------- |
| `default_value` | `str` | The value of the radio button that is selected by default. Sets the `value` attribute of the hidden input also. |
| `name`          | `str` | Sets the `name` attribute of the hidden input.                                                                  |
| `value`         | `str` | Applies to the `RadioGroupItem` component. Sets the `value` attribute of the hidden input.                      |
