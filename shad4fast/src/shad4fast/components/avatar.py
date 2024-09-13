from fasthtml.common import Img, Div, Span

__all__ = ["Avatar", "AvatarImage", "AvatarFallback"]

base_cls = ("relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full",)
img_cls = "aspect-square h-full w-full"
fallback_cls = "flex h-full w-full items-center justify-center rounded-full bg-muted"


def Avatar(*c, **kwargs):
    return Div(*c, cls=kwargs.pop("cls") + base_cls**kwargs)


def AvatarImage(src: str = None, alt: str = None, **kwargs):
    return Img(src=src, alt=alt, cls=kwargs.pop("cls") + img_cls, **kwargs)


def AvatarFallback(*c, **kwargs):
    return Span(*c, cls=kwargs.pop("cls") + fallback_cls, **kwargs)
