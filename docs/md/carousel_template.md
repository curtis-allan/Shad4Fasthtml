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

### FT Method

Using the FastHtml method, you can pass in the `items`, `orientation`, `autoplay`, and `duration` attributes to the `Carousel` component.

1. items: Takes a list of FT components to be rendered as carousel items.
2. orientation: Sets the orientation of the carousel.
3. autoplay: Sets the autoplay state of the carousel.
4. duration: Sets the duration of the carousel transition in ms.

> For a full attribute reference see the parameters table below.

To get started using the FT method, simply structure your code using the example below for reference. For ease of this example, I've included a `carousel_items()` function that returns a list of `Card` components:

```python
def carousel_items():
    items = ()
    for i in range(4):
        i += 1
        items += (
            Card(
                Div(cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"),
                title=f"Card {i}",
                description=f"Carousel demo card #{i}",
                footer=Badge(
                    "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                ),
            ),
        )
    return items

Carousel(
    items=carousel_items(),
    orientation="horizontal",
    autoplay=False,
    duration="500",
)
```

> [!NOTE]
> By default, the carousel will be rendered with the `horizontal` orientation, autoplay disabled and will have a duration of 500ms. If the attributes are omitted, the default values will be used.

### Standard Method

The standard method is similar to the FastHtml method, but follows the original Shadcn-ui method of passing in the `CarouselContent`, `CarouselItem`, `CarouselPrevious`, and `CarouselNext` components. To ensure the component is rendered correctly, you must pass in the `standard` attribute as `True`.

```python
        Carousel(
            CarouselContent(
                CarouselItem(
                    Card(
                        Div(
                            cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"
                        ),
                        title="Card #1",
                        description="Carousel demo card #1",
                        footer=Badge(
                            "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                        ),
                    ),
                ),
                CarouselItem(
                    Card(
                        Div(
                            cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"
                        ),
                        title="Card #2",
                        description="Carousel demo card #2",
                        footer=Badge(
                            "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                        ),
                    ),
                ),
                CarouselItem(
                    Card(
                        Div(
                            cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"
                        ),
                        title="Card #3",
                        description="Carousel demo card #3",
                        footer=Badge(
                            "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                        ),
                    ),
                ),
                CarouselItem(
                    Card(
                        Div(
                            cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"
                        ),
                        title="Card #4",
                        description="Carousel demo card #4",
                        footer=Badge(
                            "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                        ),
                    ),
                ),
            ),
            CarouselPrevious(),
            CarouselNext(),
            autoplay=False,
            duration="500",
            orientation="horizontal",
            standard=True,
        )
```

---

## Parameters

| Parameter     | Type   | Description                                                                                              |
| ------------- | ------ | -------------------------------------------------------------------------------------------------------- |
| `items`       | `list` | A list of FT components to be rendered as carousel items.                                                |
| `orientation` | `str`  | Sets the orientation of the carousel. Options are `horizontal` and `vertical`. Defaults to `horizontal`. |
| `autoplay`    | `bool` | Sets the autoplay state of the carousel. Defaults to `False`.                                            |
| `duration`    | `str`  | Sets the duration of the carousel transition in ms. Defaults to `500`.                                   |
