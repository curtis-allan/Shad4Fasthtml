from fasthtml.common import Div, Button, H3
from lucide_fasthtml import Lucide

__all__ = ["Accordion", "AccordionItem", "AccordionTrigger", "AccordionContent"]

accordion_cls = "w-full"
accordion_item_cls = "border-b"
accordion_trigger_cls = "flex w-full items-center justify-between py-4 text-sm font-medium transition-all hover:underline [&[data-state=open]>svg]:rotate-180"
accordion_content_cls = "overflow-hidden text-sm data-[state=closed]:animate-accordion-up data-[state=open]:animate-accordion-down"

def Accordion(*c, cls=None, **kwargs):
    new_cls = accordion_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)

def AccordionItem(*c, value, cls=None, **kwargs):
    new_cls = accordion_item_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, data_state="closed", data_value=value, **kwargs)

def AccordionTrigger(*c, cls=None, **kwargs):
    new_cls = accordion_trigger_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return H3(
        Button(
            *c,
            Lucide(icon="chevron-down", cls="h-4 w-4 shrink-0 transition-transform duration-200"),
            type="button",
            aria_expanded="false",
            data_state="closed",
            **kwargs
        )
    )

def AccordionContent(*c, cls=None, **kwargs):
    new_cls = accordion_content_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, data_state="closed", **kwargs)