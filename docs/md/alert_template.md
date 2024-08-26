## Setup

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Alert
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

---

## Usage

### FT Method

Using the FastHtml method, you can pass in the `title`, `description`, `variant` and `icon` attributes to the `Alert` component. See the parameters section for all possible attributes.

```python+html
Alert(
    title="New message!",
    description="Open your messages to view more details.",
    variant="default",
    icon="chevrons-right",
    cls="max-w-[80%]",
)
```

> [!NOTE] 
>The 'variant' attribute will be set to 'default' if not provided.
    
If lucide is set to `True` in the `ShadHead()` function and the icon attribute is not added, a default icon will be rendered, depending on the `variant` attribute. If you wish to use an alert with no icon, you can set the `icon` attribute to `None` or use the `standard` method.

### Standard Method

The standard method is similar to the FastHtml method, but follows the original Shadcn-ui method of passing in the `AlertTitle` and `AlertDescription` components. To ensure the component is rendered correctly, you must pass in the `standard` attribute as `True`.

```python+html
Alert(
    Lucide(icon="circle-alert", cls="size-4"),
    AlertTitle("Error"),
    AlertDescription("An error occurred while processing your request."),
    standard=True,
    variant="destructive",
    cls="max-w-[80%]",
)
```

> [!TIP] 
>The `Standard` method does not include an `icon` by default. You can use the `Lucide` component to add an icon to the alert as shown above to render a valid lucide icon.

---

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `title` | `str` | Sets the title of the alert.
| `description` | `str` | Sets the description of the alert.
| `variant` | `str` | Sets the variant of the alert. Options are `default` or `destructive`.
| `icon` | `str` | Sets a Lucide icon to be displayed in the alert. Only used when `standard` is false. Defaults to `chevrons-right` if variant is `default` or omitted or `circle-alert` if variant is `destructive`.
| `standard` | `bool` | A boolean attribute to indicate if the component is rendered in the standard method. Defaults to `False`.
