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

Functionally similar to the Shadcn-ui component, the `Avatar` component includes both an image and a fallback. The fallback will be shown until the image has loaded _and_ act as a full replacement if the image fails to render.

### FT Method

Using the FastHtml method, you can pass in the `src`, `alt`, and `fallback` attributes to the `Avatar` component. See the parameters table below for a full reference on the available attributes:

```python
Avatar(
    src="https://placecats.com/300/200",
    alt="Profile Image",
    fallback="CA",
)
```

> [!NOTE]
> The `fallback` and `alt` attributes are optional. If the `alt` attribute is not provided, the default value will be `Avatar Image`. The fallback will display without text if omitted.

### Standard Method

The `Avatar` component takes an `AvatarImage()` and an `AvatarFallback()` component as input:

```python
    Avatar(
        AvatarImage(
            src="https://placecats.com/300/200",
            alt="Profile Image",
        ),
        AvatarFallback("CA"),
        standard=True,
    )
```

---

## Parameters

| Parameter  | Type  | Description                                                 |
| ---------- | ----- | ----------------------------------------------------------- |
| `src`      | `str` | Sets the source of the image.                               |
| `alt`      | `str` | Sets the alt text of the image. Defaults to `Avatar Image`. |
| `fallback` | `str` | Sets the fallback text of the image.                        |
