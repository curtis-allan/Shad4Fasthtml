# Nav Component

The Nav component provides a flexible navigation bar for your application. It includes support for basic navigation items and dropdown menus.

## Setup

Make sure the relevant packages are installed, and setup the imports as shown below.

> [!NOTE]
> If you wish to separately import components you can do so too. Make sure to import and setup `ShadHead()` as well.

from fasthtml import *
from shad4fast import *

app, rt = fast_app(pico=False, hdrs=(ShadHead(),))

---

## Usage

To use the Nav component, structure your code as follows:

from shad4fast.components.nav import Nav, NavItem, NavLink, NavMenu, NavMenuTrigger, NavMenuContent
from lucide_fasthtml import Lucide

```python
Nav(
    NavItem(NavLink("Home", href="/")),
    NavItem(NavLink("About", href="/about")),
    NavItem(NavLink("Contact", href="/contact")),
    NavItem(
        NavMenu(
            NavMenuTrigger(
                "More",
                Lucide(icon="chevron-down", cls="ml-1 h-4 w-4"),
            ),
            NavMenuContent(
                NavItem(NavLink("Blog", href="/blog")),
                NavItem(NavLink("FAQ", href="/faq")),
            ),
        )
    ),
    cls="mr-6",
)
```

> [!NOTE]
> The Nav component is typically used within a header or layout component for consistent navigation across your application.

---

## Components

### Nav

The main container for navigation items.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (NavItems)          |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### NavItem

Container for individual navigation items.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (NavLink or NavMenu)|
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### NavLink

The actual link within each navigation item.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| href      | `str`    | URL for the link                     |
| active    | `bool`   | Whether this link is currently active|
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (usually text)      |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### NavMenu

Container for dropdown menus.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (Trigger and Content)|
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### NavMenuTrigger

The button to toggle a dropdown menu.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (usually text and icon)|
| **kwargs  | `**kwargs` | Additional HTML attributes          |

### NavMenuContent

The content of a dropdown menu.

| Parameter | Type     | Description                          |
| --------- | -------- | ------------------------------------ |
| cls       | `str`    | Additional CSS classes for styling   |
| *c        | `*args`  | Child components (usually NavItems)  |
| **kwargs  | `**kwargs` | Additional HTML attributes          |

---

## Styling

The Nav component and its sub-components come with default styling using Tailwind CSS classes. You can customize the appearance by passing additional classes through the `cls` parameter or by modifying the default classes in the component definitions.

---

## Accessibility

The Nav component is designed with accessibility in mind. It uses semantic HTML elements and ARIA attributes where appropriate. However, you may need to add additional ARIA attributes depending on your specific implementation and requirements.

---

## JavaScript Interaction

For dropdown menus to function properly, you may need to add JavaScript for toggling the visibility of `NavMenuContent`. This is not included in the basic component and would need to be implemented separately, potentially using HTMX or custom JavaScript.
