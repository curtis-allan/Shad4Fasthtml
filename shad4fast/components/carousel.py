from fasthtml.components import Div, Script
from shad4fast.shadcn import Button, Lucide

__all__ =     ["Carousel",
    "CarouselContent",
    "CarouselItem",
    "CarouselPrevious",
    "CarouselNext",]

def carousel_script():
    return Script(src="/shad4fast/js/carousel.js", defer=True)

def Carousel(*c, cls=None, orientation:str='horizontal', autoplay:bool=False, duration:str='500', **kwargs):
    new_cls = "relative w-full"

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] =new_cls

    return Div(
            *c,
            carousel_script(),
            data_autoplay='true' if autoplay else 'false',
            data_orientation=orientation,
            data_duration=duration,
            data_ref="carousel",
            role="region",
            aria_roledescription="carousel",
            **kwargs
        )

def CarouselContent(*c, cls=None, **kwargs):
    new_cls = "flex transition-transform ease-in-out duration-500"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(Div(*c, data_ref="content", **kwargs), cls="overflow-hidden")

def CarouselItem(*c, cls=None, **kwargs):
    new_cls = "min-w-0 shrink-0 grow-0 basis-full",
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, data_carousel_item=True, **kwargs)

def CarouselPrevious(icon='arrow-left', cls=None, **kwargs):
    new_cls = "absolute h-8 w-8 !rounded-full"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(Lucide(icon=icon, cls='size-4'),
                variant="outline",
                size="icon", data_ref="prevButton", **kwargs)

def CarouselNext(icon='arrow-right', cls=None, **kwargs):
    new_cls = "absolute h-8 w-8 !rounded-full"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(Lucide(icon=icon, cls='size-4'),
                variant="outline",
                size="icon", data_ref="nextButton", **kwargs)