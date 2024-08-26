## Setup

All component imports are included when using the default setup. If you wish to separately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Select, SelectTrigger, SelectValue, SelectContent, SelectItem
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

---

## Usage

The `Select` component in this implementation follows a structure similar to native HTML select elements but with enhanced customization and styling options.

### Select Structure

1. **Select**: The main wrapper component.
2. **SelectTrigger**: Contains the visible part of the select, including the current value and dropdown icon.
3. **SelectValue**: Displays the currently selected value or placeholder.
4. **SelectContent**: Contains the list of selectable options.
5. **SelectItem**: Individual selectable options.

### Behavior

- The Select component is client-side rendered, ensuring responsiveness and state preservation.
- When an item is selected, the value is updated in a hidden input field for form submissions.

>[!NOTE]
>The `Select` component uses a hidden input to store the selected value. Make sure to provide a `name` attribute if you intend to use it in a form.

### Example Usage

```python+html
Select(
    SelectTrigger(
        SelectValue(placeholder="Select a fruit")
    ),
    SelectContent(
        SelectItem("Apple", value="apple"),
        SelectItem("Banana", value="banana"),
        SelectItem("Orange", value="orange")
    ),
    name="fruit",
    id="fruit-select"
)
```

### Additional Components

- **SelectGroup**: Groups related items together.
- **SelectLabel**: Provides a label for a group of items.
- **SelectSeparator**: Adds a visual separator between items or groups.

Example with grouping:

```python+html
Select(
    SelectTrigger(
        SelectValue(placeholder="Select a fruit")
    ),
    SelectContent(
        SelectGroup(
            SelectLabel("Fruits"),
            SelectItem("Apple", value="apple"),
            SelectItem("Banana", value="banana"),
            SelectItem("Orange", value="orange")
        ),
        SelectSeparator(),
        SelectGroup(
            SelectLabel("Vegetables"),
            SelectItem("Carrot", value="carrot"),
            SelectItem("Broccoli", value="broccoli")
        )
    ),
    name="food",
    id="food-select"
)
```

>[!TIP]
>Use `SelectGroup` and `SelectLabel` to organize your options into logical categories, improving user experience for longer lists.

---

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `state` | `str` | Sets the initial state of the select. Can be either `"open"` or `"closed"`. Defaults to `"closed"`.
| `id` | `str` | Sets the id for the hidden input element.
| `name` | `str` | Sets the name for the hidden input element, used for form submissions.

>[!NOTE]
>The `value` of the selected item is stored in the hidden input element, which can be accessed through the `name` attribute in form submissions.