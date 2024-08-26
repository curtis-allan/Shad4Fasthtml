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

The `Select` component in this implementation follows the exact same structure as Shadcn's Select component. Both a standard and FT method are provided. I recommend using the `Standard` method when you need advanced functionality (groups, targetted styling etc.) and the `FT` method when you just need a simple select.


### FT Method

The FT Method is simplified and ideal for small, standard dropdowns. It's designed to be a quick and easy way to add a select dropdown to your page.

```python+html
Select(
    placeholder="Pick a fruit",
    label="Fruits",
    items=["Apple", "Banana", "Blueberry", "Orange"],
    id="select-demo",
    name="select-demo",
    cls="[&>.select-trigger]:w-[180px]",
)
```

For the case of ease of use, the FT method takes a list of items in string format and will render a new `SelectItem` option for each. The string option you enter is used for the select item displayed name, and its value and name attribute are automatically generated (a lower case version of the string).

>[!WARNING]
>The `Select` component will not be functional without a valid `id` being assigned to both the `Select` and `SelectContent` components. This is due to their functionality, if an id isnt provided they will both raise a `ValueError`.

## Standard Method

The standard method mimics Shadcn's system and allows for a more advanced and customizable version of the select component. I recommend using this method when you need more control over the select component, particularly applying `kwargs` and functionality to the inner items. For those unfamiliar with Shadcn's system, the following components are used to structure the select component:

- **SelectGroup**: Groups related items together.
- **SelectLabel**: Provides a label for a group of items.
- **SelectSeparator**: Adds a visual separator between items or groups.

Example with grouping & the standard method:

```python+html
Select(
    SelectTrigger(
        SelectValue(placeholder="Choose a coding language"),
        cls="w-[250px]"
    ),
    SelectContent(
        SelectGroup(
            SelectLabel("Scripting Languages"),
            SelectItem("JavaScript", value="javascript"),
            SelectItem("TypeScript", value="typescript"),
            SelectItem("Ruby", value="ruby"),
            SelectItem("Lua", value="lua"),
            SelectItem("PHP", value="php")
        ),
        SelectSeparator(),
        SelectGroup(
            SelectLabel("Mobile Development"),
            SelectItem("Swift", value="swift"),
            SelectItem("Kotlin", value="kotlin"),
            SelectItem("Flutter", value="flutter"),
            SelectItem("React Native", value="react-native"),
            SelectItem("Xamarin", value="xamarin"),
            SelectItem("Ionic", value="ionic")
        ),
        SelectSeparator(),
        SelectGroup(
            SelectLabel("Other Languages"),
            SelectItem("Go", value="go"),
            SelectItem("Rust", value="rust"),
            SelectItem("C#", value="csharp"),
            SelectItem("Java", value="java"),
            SelectItem("Scala", value="scala"),
            SelectItem("Haskell", value="haskell")
        ),
        id='select-alt',
    ),
    standard=True,
    id='select-alt',
)
```

>[!TIP]
>Use `SelectGroup` and `SelectLabel` to organize your options into logical categories, improving user experience for longer lists.

---

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `items` | `list` | *FT Method Only* A list of items to be displayed in the select component. |
| `placeholder` | `str` | *FT Method Only* The placeholder text to be displayed in the select trigger component. |
| `label` | `str` | *FT Method Only* The label text to be displayed above the select component. |
| `id` | `str` | **Required** Sets the select id, and in the case of the standard method, will set the id of its descendant components accordingly. |
| `name` | `str` | Sets the name of the hidden input element. |
| `standard` | `bool` | If set to `True`, the select component will be rendered using the standard method. |
>[!NOTE]
>The `value` of the selected item is stored in a hidden input element, which can be accessed through the `name` attribute given in the FT method, or assigning a custom name to to your `SelectItems` components in the standard approach.
