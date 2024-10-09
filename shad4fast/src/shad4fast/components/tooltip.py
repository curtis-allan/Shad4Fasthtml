from fasthtml.common import Div, Span

__all__ = ["Tooltip", "TooltipTrigger", "TooltipContent"]

tooltip_cls = "relative inline-block"
tooltip_content_cls = "absolute z-10 px-2 py-1 text-sm font-medium text-white bg-gray-900 rounded-md shadow-sm dark:bg-gray-700"

def Tooltip(*c, cls=None, **kwargs):
    new_cls = tooltip_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)

def TooltipTrigger(*c, cls=None, **kwargs):
    return Span(*c, cls=cls, **kwargs)

def TooltipContent(*c, position="top", cls=None, **kwargs):
    new_cls = tooltip_content_cls
    if position == "top":
        new_cls += " bottom-full left-1/2 transform -translate-x-1/2 mb-1"
    elif position == "bottom":
        new_cls += " top-full left-1/2 transform -translate-x-1/2 mt-1"
    elif position == "left":
        new_cls += " right-full top-1/2 transform -translate-y-1/2 mr-1"
    elif position == "right":
        new_cls += " left-full top-1/2 transform -translate-y-1/2 ml-1"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)