from fasthtml.components import Div, Thead, Tbody, Tfoot, Tr, Th, Td, Caption, Table as OgTable

__all__ = ["Table", "TableHeader", "TableBody", "TableRow", "TableHead", "TableCell", "TableCaption", "TableFooter"]

table_base_cls = "w-full caption-bottom text-sm"
table_head_cls = "[&_tr]:border-b"
table_body_cls = "[&_tr:last-child]:border-0"
table_footer_cls = "border-t bg-muted/50 font-medium [&>tr]:last:border-b-0"
table_row_cls = (
    "border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted"
)
table_head_cls = "h-12 px-4 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0"
table_cell_cls = "p-4 align-middle [&:has([role=checkbox])]:pr-0"

def Table(*c, cls=None, **kwargs):
    new_cls = table_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(OgTable(*c, **kwargs), cls="relative w-full overflow-auto")


def TableHeader(*c, cls=None, **kwargs):
    new_cls = table_head_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Thead(*c, **kwargs)


def TableBody(*c, cls=None, **kwargs):
    new_cls = table_body_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Tbody(*c, **kwargs)


def TableFooter(*c, cls=None, **kwargs):
    new_cls = table_footer_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Tfoot(*c, **kwargs)


def TableRow(*c, cls=None, **kwargs):
    new_cls = table_row_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Tr(*c, **kwargs)


def TableHead(*c, cls=None, **kwargs):
    new_cls = table_head_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Th(*c, **kwargs)


def TableCell(*c, cls=None, **kwargs):
    new_cls = table_cell_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Td(*c, **kwargs)


def TableCaption(*c, cls=None, **kwargs):
    new_cls = table_cell_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Caption(*c, **kwargs)