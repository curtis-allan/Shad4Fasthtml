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

The `Skeleton` component acts as a pre-styled placeholder. You can style the width/ size and anything else to ensure it resembles the type of content yet to be rendered in. By default, the skeleton method does not take any children. Instead, you can apply tailwind classes/ any styling to make it match the incoming HTML.

It also works great along with HTMX. If you make a call to the server that you expect to take a while to return (i.e an async generator), you can simply return a skeleton that matches the size/ layout of the incoming component.

You can give the parent element attributes like `hx_trigger='load'` and `hx_swap='outerHTML'` so that it triggers the long-timing server endpoint upon loading into the page, and automatically swaps out with the new content once it's ready (if configured correctly).

```py
Div(
    Skeleton(cls="h-12 w-12 !rounded-full"),
    Div(
        Skeleton(cls="h-4 w-[250px]"),
        Skeleton(cls="h-4 w-[250px]"),
        cls="space-y-2"
    ),
cls="flex items-center space-x-4"
)
```

---

## Parameters

The skeleton component takes any valid HTML kwargs by default, however it does not accept children elements.
