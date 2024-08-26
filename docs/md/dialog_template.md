## Setup

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Dialog
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

---

## Usage

### Dialog Structure

The `Dialog` component in this implementation differs slightly from the original Shadcn-ui approach:

1. **DialogTrigger**: Requires a unique `dialog_id` to connect with its corresponding `Dialog` component.

2. **Dialog**: Needs a unique `id` that matches the `dialog_id` of its trigger and must **not** contain the `DialogTrigger` component.

### Behavior

- Similar to the `Sheet` component, `Dialog` is client-side rendered, preserving state across toggles and ensuring responsiveness.
- **Placement**: 
  - `DialogTrigger` can be placed where you want the trigger to appear.
  - `Dialog` can be positioned anywhere within the body of your HTML but must **not** be a parent of `DialogTrigger`. Post-rendering, `Dialog` components are moved to the end of the `<body>` via a script to ensure correct overlay behavior.

>[!WARNING]
>The `DialogTrigger` must *not* be a child of the `Dialog`. This will cause the trigger to be hidden and untargetable.


### FT Method

Using the FastHtml method, you can pass in the `title`, `description`, and `footer` attributes to the `Dialog` component. Along with these, you can pass a `state` attribute to indicate whether the dialog is rendered open or closed on initial load.

```python+html
DialogTrigger("Toggle Dialog", dialog_id="demo-dialog"),
Dialog(
    Div(
        Div(
            Label("Name", cls="text-right"),
            Input(
                value="John",
                cls="col-span-3",
            ),
            cls="grid grid-cols-4 items-center gap-4",
        ),
        Div(
            Label("Email", cls="text-right"),
            Input(
                type="email",
                value="johnsmith@email.com",
                cls="col-span-3",
            ),
            cls="grid grid-cols-4 items-center gap-4",
        ),
        cls="grid gap-4 py-4",
    ),
    title="Edit Profile",
    description="Make changes to your profile here. Click save when you're done.",
    footer=Div(
        DialogCloseButton("Save changes"), cls="flex w-full justify-end"
    ),
    id="demo-dialog",
)
```

>[!NOTE] 
>The `state` attribute is optional and defaults to `closed`.

### Standard Method

The standard method is similar to the FastHtml method, but follows the original Shadcn-ui method of passing in the `DialogContent`, `DialogHeader`, `DialogTitle`, `DialogDescription`, and `DialogFooter` components. To ensure the component is rendered correctly, you must pass in the `standard` attribute as `True`.

```python+html
DialogTrigger("Toggle Dialog", dialog_id="demo-dialog"),
Dialog(
    DialogContent(
        DialogHeader(
            DialogTitle("Edit Profile"),
            DialogDescription(
                "Make changes to your profile here. Click save when you're done."
            ),
        ),
        Div(
            Div(
                Label("Name", cls="text-right"),
                Input(value="John", cls="col-span-3"),
                cls="grid grid-cols-4 items-center gap-4",
            ),
            Div(
                Label("Email", cls="text-right"),
                Input(
                    type="email", value="johnsmith@email.com", cls="col-span-3"
                ),
                cls="grid grid-cols-4 items-center gap-4",
            ),
            cls="grid gap-4 py-4",
        ),
        DialogFooter(DialogCloseButton("Save changes")),
        cls="sm:max-w-[425px]",
    ),
    standard=True,
    id="demo-dialog",
)
```

> [!TIP] 
>Make sure the `DialogContent` component wraps around the `DialogHeader`, `DialogTitle`, `DialogDescription`, and `DialogFooter` components for proper rendering.

---

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `str` | **Required**. Unique identifier, must match `dialog_id` from `DialogTrigger`.
| `title` | `str` | Sets the title of the card.
| `description` | `str` | Sets the description of the card.
| `footer` | `any` | Sets the footer of the card. Can be any valid FT component/components.
| `state` | `str` | Sets the state of the dialog. Can be either `open` or `closed`. Defaults to `closed`.
| `standard` | `bool` | A boolean attribute to indicate if the component is rendered in the standard method. Defaults to `False`.