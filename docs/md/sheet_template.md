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

The sheet component has two methods of implementation. The first method is the FastHtml method for a simpler implementation, and the second method is the standard method for a more Shadcn-ui like implementation.

If you wish to use a button to close the dialog from within, you can use the `SheetClose` component, or simply apply the `sheet-close-button` class to a component.

### FT Method

Using the FastHtml method, you can pass in a `trigger`, `title`, `description` and `footer` attribute to the `Sheet` component.

Along with these, you can pass a `state` attribute to indicate whether the sheet is rendered open or closed on initial load _and_ a `side` attribute to indicate which side of the screen the sheet should appear from.

The `trigger` attribute can take either a string (sets the text of the trigger button) or a component. If supplying a component, make sure to set the `data-ref` attribute to `sheet-trigger` so the sheet can be opened via Javascript.

```python
Sheet(
    Div(
        P("This is where you'd enter your sheet content"),
        cls="h-[85%]",
    ),
    title="Demo Sheet",
    description="This is a demo sheet.",
    footer=SheetClose("Close", cls="w-full"),
    trigger="Toggle Sheet",
)
```

> [!NOTE]
> The sheet `state` attribute is not required, and will default to `closed` if not specified.

### Standard Method

The standard method is similar to the FastHtml method, but follows the original Shadcn-ui method of passing in the `SheetContent`, `SheetHeader`, `SheetTitle`, `SheetDescription`, and `SheetFooter` components.

> [!IMPORTANT]
> To ensure the component is rendered correctly, you must pass in the `standard` attribute as `True`. To change the default `open` state, pass the `state` attribute as `open` or `closed` to the _DialogContent()_ method.

```python
Sheet(
    SheetTrigger("Toggle Sheet"),
    SheetContent(
        SheetHeader(
            SheetTitle("Demo Sheet"),
            SheetDescription("This is a demo sheet."),
        ),
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
        SheetFooter(SheetClose("Close")),
    ),
    standard=True,
)
```

> [!IMPORTANT]
> The `SheetTrigger` component must be a direct child of the `Sheet` component. This is done by default in the FT method. If using the standard method, make sure the `SheetTrigger` is: a child of the `Sheet` component _and_ not inside the `SheetContent` component.

---

## Parameters

| Parameter     | Type                      | Description                                                                                                                                                                                          |
| ------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `trigger`     | `str` _or_ `FT Component` | Sets the text of the dialog trigger component. Only needed in the FT method.                                                                                                                         |
| `title`       | `str`                     | Sets the title of the card. Only needed in the FT method.                                                                                                                                            |
| `description` | `str`                     | Sets the description of the card. Only needed in the FT method.                                                                                                                                      |
| `footer`      | `any`                     | Sets the footer of the card. Can be any valid FT component/components. Only needed in the FT method.                                                                                                 |
| `side`        | `str`                     | Sets the side of the screen the sheet should appear from. Can be either `left`, `right`, `top` or `bottom`. Defaults to `right`. Apply to the `SheetContent` component if using the standard method. |
| `state`       | `str`                     | Sets the state of the dialog. Can be either `open` or `closed`. Defaults to `closed`. Apply to the `SheetContent` component if using the standard method.                                            |
| `standard`    | `bool`                    | A boolean attribute to indicate if the component is rendered in the standard method. Defaults to `False`. Only needed if using the standard method.                                                  |
