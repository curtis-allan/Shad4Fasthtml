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

Implementing the breadcrumb component is very straightforward. There are two main methods for implementing breadcrumb links. The first method, shown below, is a hard-coded approach. Structure your code as follows to render the exact layout you wish for:

```py
Breadcrumb(
    BreadcrumbList(
        BreadcrumbItem(
        BreadcrumbLink("Home", href="/")),
        BreadcrumbSeparator(),
        BreadcrumbItem(
            BreadcrumbEllipsis(),
        ),
        BreadcrumbSeparator(),
        BreadcrumbItem(
            BreadcrumbLink("Components", href="/components"),
        ),
        BreadcrumbSeparator(),
        BreadcrumbItem(
            BreadcrumbPage("Breadcrumb"),
        ),
    ),
    )
```

Alternatively, you can the entire `req` Request object from a given route to the `req` attribute of the breadcrumb component, which will automatically generate the breadcrumb links based on the path. To implement breadcrumbs in this way, structure your code as follows:

```py
@rt('/about/sponsors/contact')
def get(req: Request):
    return Body(Breadcrumb(req=req))
```

This will automatically generate the breadcrumb links based on the path of the request, including an ellipsis element if the path exceeds `4` links.

---

## Parameters

| Parameter | Type      | Description                                                                                                                               |
| --------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `req`     | `Request` | The request object from a given route.                                                                                                    |
| `href`    | `str`     | Relevant to the `BreadcrumbLink` component. Specifies the URL to link to. Automatically generated if implemented via the `req` attribute. |
