from fasthtml.common import Div
from .button import Button
from lucide_fasthtml import Lucide

__all__ = [
    "Carousel",
    "CarouselContent",
    "CarouselItem",
    "CarouselPrevious",
    "CarouselNext",
]


def Carousel(
    *c,
    cls=None,
    items=[],
    orientation: str = "horizontal",
    autoplay: bool = False,
    duration: str = "500",
    index: int = 0,
    standard: bool = False,
    **kwargs,
):
    new_cls = "relative w-full"

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    if standard:
        return Div(
            *c,
            data_autoplay="true" if autoplay else "false",
            data_orientation=orientation,
            data_ref="carousel",
            data_index=index,
            role="region",
            aria_roledescription="carousel",
            **kwargs,
        )

    carousel_items = ()
    for i in items:
        carousel_items += (CarouselItem(i),)

    return Div(
        CarouselContent(*carousel_items, duration=duration),
        CarouselPrevious(),
        CarouselNext(),
        data_autoplay="true" if autoplay else "false",
        data_orientation=orientation,
        data_ref="carousel",
        data_index=index,
        role="region",
        aria_roledescription="carousel",
        **kwargs,
    )


def CarouselContent(*c, cls=None, duration: str = "500", **kwargs):
    new_cls = "flex transition-transform ease-in-out"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(
        Div(
            *c,
            data_ref="content",
            style=f"transform:translate3d(0px, 0px, 0px);transition-duration:{duration}ms",
            **kwargs,
        ),
        cls="overflow-hidden",
    )


def CarouselItem(*c, cls=None, **kwargs):
    new_cls = ("min-w-0 shrink-0 grow-0 basis-full",)
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, data_carousel_item=True, **kwargs)


def CarouselPrevious(icon="arrow-left", cls=None, **kwargs):
    new_cls = "absolute h-8 w-8 !rounded-full"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(
        Lucide(icon=icon, cls="size-4"),
        variant="outline",
        size="icon",
        data_ref="prevButton",
        type="button",
        **kwargs,
    )


def CarouselNext(icon="arrow-right", cls=None, **kwargs):
    new_cls = "absolute h-8 w-8 !rounded-full"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(
        Lucide(icon=icon, cls="size-4"),
        variant="outline",
        size="icon",
        type="button",
        data_ref="nextButton",
        **kwargs,
    )
