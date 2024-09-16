from fasthtml.common import Img, Div, Span

__all__ = ["Avatar", "AvatarImage", "AvatarFallback"]

base_cls = "relative flex h-10 w-10 shrink-0 overflow-hidden rounded-full"
img_cls = "aspect-square h-full w-full hidden"
fallback_cls = "flex h-full w-full items-center justify-center rounded-full bg-muted"


def Avatar(
    *c,
    cls="",
    standard=False,
    src: str = None,
    alt: str = "Avatar Image",
    fallback: str = None,
    **kwargs,
):
    if standard:
        return Div(*c, cls=f"{base_cls} {cls}", **kwargs)
    return Div(
        AvatarImage(src=src, alt=alt),
        AvatarFallback(fallback),
        cls=f"{base_cls} {cls}",
        **kwargs,
    )


def AvatarImage(src: str = None, cls="", alt: str = "Avatar Image", **kwargs):
    return Img(
        src=src,
        alt=alt,
        cls=f"{img_cls} {cls}",
        onerror="this.remove()",
        onload="this.classList.remove('hidden')",
        **kwargs,
    )


def AvatarFallback(*c, cls="", **kwargs):
    return Span(*c, cls=f"{fallback_cls} {cls}", **kwargs)
