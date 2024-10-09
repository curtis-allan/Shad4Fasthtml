from fasthtml.common import Div, Ol, Li, A, Span
from lucide_fasthtml import Lucide

__all__ = ["Breadcrumb", "BreadcrumbItem", "BreadcrumbLink", "BreadcrumbSeparator"]

breadcrumb_cls = "flex"
breadcrumb_item_cls = "flex items-center"
breadcrumb_link_cls = "text-sm font-medium text-muted-foreground hover:text-foreground"
breadcrumb_separator_cls = "mx-2 text-muted-foreground"

def Breadcrumb(*c, cls=None, **kwargs):
    new_cls = breadcrumb_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Ol(*c, **kwargs)

def BreadcrumbItem(*c, cls=None, **kwargs):
    new_cls = breadcrumb_item_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Li(*c, **kwargs)

def BreadcrumbLink(*c, href="#", current=False, cls=None, **kwargs):
    new_cls = breadcrumb_link_cls
    if current:
        new_cls += " text-foreground font-semibold"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return A(*c, href=href, **kwargs)

def BreadcrumbSeparator(cls=None, **kwargs):
    new_cls = breadcrumb_separator_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Span(Lucide(icon="chevron-right", cls="h-4 w-4"), **kwargs)