from fasthtml.common import Ol, Nav, Li, A, Span
from fasthtml.common import Request
from lucide_fasthtml import Lucide

__all__ = ["Breadcrumb", "BreadcrumbItem", "BreadcrumbLink", "BreadcrumbSeparator", "BreadcrumbEllipsis", "BreadcrumbPage", "BreadcrumbList"]

breadcrumb_item_cls = "inline-flex items-center gap-1.5"
breadcrumb_link_cls = "transition-colors hover:text-foreground"
breadcrumb_list_cls = "flex flex-wrap items-center gap-1.5 break-words text-sm text-muted-foreground sm:gap-2.5"
breadcrumb_page_cls = "font-normal text-foreground"
breadcrumb_ellipsis_cls = "flex h-9 w-9 items-center justify-center"

def Breadcrumb(*c, req:Request=None, **kwargs):
    if req:
        path = req.url.path
        parts = path.strip('/').split('/')
        items = [(BreadcrumbItem(BreadcrumbLink("Home", href="/")), BreadcrumbSeparator())]
        for i, part in enumerate(parts):
            if i == len(parts) - 1:
                items.append(BreadcrumbItem(BreadcrumbPage(part.capitalize())))
                break
            else:
                link = '/' + '/'.join(parts[:i+1])
                items.append((BreadcrumbItem(BreadcrumbLink(part.capitalize(), href=link)), BreadcrumbSeparator()))

        if len(items) >= 4:
            items[1] = (BreadcrumbItem(BreadcrumbEllipsis()), BreadcrumbSeparator())
        return Nav(BreadcrumbList(*items), aria_label="breadcrumb", **kwargs)
    return Nav(*c, aria_label="breadcrumb", **kwargs)   

def BreadcrumbItem(*c, **kwargs):
    return Li(*c,cls=f"{kwargs.pop('cls', '')} {breadcrumb_item_cls}", **kwargs)

def BreadcrumbLink(*c, **kwargs):
    return A(*c, cls=f"{kwargs.pop('cls', '')} {breadcrumb_link_cls}", **kwargs)

def BreadcrumbEllipsis(**kwargs):
    return Span(Lucide(icon="ellipsis", cls="h-4 w-4"), Span("More", cls="sr-only"), cls=f"{kwargs.pop('cls', '')} {breadcrumb_ellipsis_cls}", **kwargs)

def BreadcrumbSeparator(icon="chevron-right", **kwargs):
    return Li(Lucide(icon=icon), role="presentation", aria_hidden="true", **kwargs)

def BreadcrumbList(*c, **kwargs):
    return Ol(*c, cls=f"{kwargs.pop('cls', '')} {breadcrumb_list_cls}", **kwargs)

def BreadcrumbPage(*c, **kwargs):
    return Span(*c, role="link", aria_disabled="true", aria_current="page", cls=f"{kwargs.pop('cls', '')} {breadcrumb_page_cls}", **kwargs)