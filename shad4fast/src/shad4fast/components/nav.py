from fasthtml.common import Div, Ul, Li, A
from .button import Button
from lucide_fasthtml import Lucide

__all__ = ["Nav", "NavItem", "NavLink"]

nav_cls = "flex items-center space-x-4 lg:space-x-6"
nav_item_cls = "relative"
nav_link_cls = "text-sm font-medium transition-colors hover:text-primary"
nav_link_active_cls = "text-primary"

def Nav(*c, cls=None, **kwargs):
    new_cls = nav_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Ul(*c, **kwargs)

def NavItem(*c, cls=None, **kwargs):
    new_cls = nav_item_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Li(*c, **kwargs)

def NavLink(*c, href="#", active=False, cls=None, **kwargs):
    new_cls = nav_link_cls
    if active:
        new_cls += f" {nav_link_active_cls}"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return A(*c, href=href, **kwargs)

def NavMenu(*c, cls=None, **kwargs):
    new_cls = "flex items-center"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)

def NavMenuTrigger(*c, cls=None, **kwargs):
    new_cls = "flex items-center space-x-1 text-sm font-medium"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(*c, variant="ghost", size="sm", **kwargs)

def NavMenuContent(*c, cls=None, **kwargs):
    new_cls = "absolute top-full left-0 mt-2 w-48 rounded-md bg-white shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)
