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

To use the tabs component, structure your code as with a normal FT method. The `Tabs` component takes a `default_value` attribute that sets the default tab on initial render.

Each `TabsContent` component requires a `value` attribute that corresponds to the value of the `TabsTrigger` component. To use the component, structure your code as shown below:

```python
Tabs(
    TabsList(
        TabsTrigger("Post", value="tab1"),
        TabsTrigger("Settings", value="tab2"),
        cls="grid w-full grid-cols-2",
    ),
    TabsContent(
        Card(
            Div(
                Label("Username", htmlFor="tab-title"),
                Input(type="text", placeholder="Title", id="tab-title"),
            ),
            title="Create a post",
            description="Enter your post title below",
            footer=Div(
                Button(
                    "Cancel",
                    variant="outline",
                ),
                Button("Submit"),
                cls="flex w-full justify-end gap-2",
            ),
        ),
        value="tab1",
    ),
    TabsContent(
        Card(
            Div(
                Label("Username", htmlFor="tab-settings"),
                Input(
                    type="text",
                    value="@JohnDoe",
                    disabled="true",
                    id="tab-settings",
                ),
            ),
            title="Settings",
            description="Change your settings here",
            footer=Div(
                Button(
                    "Cancel",
                    variant="outline",
                ),
                Button("Submit"),
                cls="flex w-full justify-end gap-2",
            ),
        ),
        value="tab2",
    ),
    default_value="tab1",
    cls="sm:max-w-[80%] w-full max-w-[70%] mx-auto",
)
```

> [!NOTE]
> If the `default_value` attribute is not set, the first tab will be selected by default.

---

## Parameters

| Parameter       | Type  | Description                                                                                                                              |
| --------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `default_value` | `str` | Sets the default tab on initial render. Default to the first tab if not set.                                                             |
| `value`         | `str` | Sets the value of the tab/ tab trigger to match which tab is opened. Must be unique. Applies to both the content and trigger components. |
