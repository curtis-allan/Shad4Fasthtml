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

To use the aspect ratio component, structure your code as with a normal FT method. The component takes a `ratio` parameter, which is the width by height of the aspect ratio you wish to create.

```python
AspectRatio(
    Img(
        src="/public/aspect.webp",
        cls="w-full h-full rounded-md object-cover",
        loading="lazy",
    ),
    ratio={16 / 9},
)
```

---

## Parameters

| Parameter | Type                                                                               | Description                             |
| --------- | ---------------------------------------------------------------------------------- | --------------------------------------- |
| ratio     | ratio value: either `{width / height}`, `height / width` or the ratio as a `float` | The width by height of the aspect ratio |
