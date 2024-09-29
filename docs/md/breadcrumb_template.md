
# Breadcrumb Component

The Breadcrumb component provides a navigation aid that helps users understand their current location within a hierarchical structure of the website.

## Setup

Make sure the relevant packages are installed, and setup the imports as shown below.

> [!NOTE]
> If you wish to separately import components you can do so too. Make sure to import and setup `ShadHead()` as well.

from fasthtml import *
from shad4fast import *

app, rt = fast_app(pico=False, hdrs=(ShadHead(),))

---

## Usage

To use the Breadcrumb component, structure your code as follows:

from shad4fast.components.breadcrumb import Breadcrumb, BreadcrumbItem, BreadcrumbLink, BreadcrumbSeparator

```python
Breadcrumb(
    BreadcrumbItem(BreadcrumbLink("Home", href="/")),
    BreadcrumbItem(BreadcrumbSeparator()),
    BreadcrumbItem(BreadcrumbLink("Products", href="/products")),
    BreadcrumbItem(BreadcrumbSeparator()),
    BreadcrumbItem(BreadcrumbLink("Laptops", href="/products/laptops", current=True)),
)
```

---

## Components

### Breadcrumb

The main container for breadcrumb items.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (BreadcrumbItems)   |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### BreadcrumbItem

Container for individual breadcrumb items.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (Link or Separator) |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### BreadcrumbLink

The actual link within each breadcrumb item.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| href      | `str`    | URL for the link                     |
| current   | `bool`   | Whether this is the current page     |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (usually text)      |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### BreadcrumbSeparator

The separator between breadcrumb items.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| **kwargs  | `**kwargs` | Additional HTML attributes          |
