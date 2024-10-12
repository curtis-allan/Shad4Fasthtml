from fasthtml.common import Div, ft_hx, H3
from lucide_fasthtml import Lucide

__all__ = ["Accordion", "AccordionItem", "AccordionTrigger", "AccordionContent"]

accordion_cls = "w-full"
accordion_item_cls = "border-b"
accordion_trigger_cls = "flex flex-1 items-center justify-between py-4 font-medium transition-all hover:underline"
accordion_content_cls = "hidden overflow-hidden text-sm transition-all peer-data-[state=closed]:animate-accordion-up peer-data-[state=open]:animate-accordion-down"
inner_content_cls = "pb-4 pt-0"

def Accordion(*c, cls=None, **kwargs):
    new_cls = accordion_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, data_ref="accordion", **kwargs)

def AccordionItem(*c, cls=None, **kwargs):
    new_cls = accordion_item_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, data_ref="accordion-item", **kwargs)

def AccordionTrigger(*c, cls=None, **kwargs):
    new_cls = "peer group flex"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return H3(ft_hx('button',
            *c,
            Lucide(icon="chevron-down", cls="h-4 w-4 shrink-0 transition-transform duration-200 group-data-[state=open]:rotate-180"),
            type="button",
            cls=accordion_trigger_cls,
        ),
        data_ref="accordion-trigger",
        aria_expanded="false",
        data_state="closed",
        **kwargs
    )

def AccordionContent(*c, cls=None, **kwargs):
    new_cls = accordion_content_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(Div(*c, cls=inner_content_cls), data_ref="accordion-content", role="region", **kwargs)
