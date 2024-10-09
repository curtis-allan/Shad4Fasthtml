from fasthtml.common import Div, P, H1, Span, ft_hx
from lucide_fasthtml import Lucide
from .button import Button

__all__ = [
    "Dialog",
    "DialogHeader",
    "DialogFooter",
    "DialogTitle",
    "DialogClose",
    "DialogDescription",
    "DialogContent",
    "DialogTrigger",
]

dialog_portal_cls = "hidden fixed inset-0 z-50"
dialog_content_cls = "fixed left-[50%] top-[50%] grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 group-data-[state=open]:animate-in group-data-[state=closed]:animate-out group-data-[state=open]:fade-in-0 group-data-[state=open]:zoom-in-95 group-data-[state=open]:slide-in-from-left-1/2 group-data-[state=open]:slide-in-from-top-[48%] group-data-[state=closed]:slide-out-to-left-1/2 group-data-[state=closed]:slide-out-to-top-[48%] group-data-[state=closed]:zoom-out-95 group-data-[state=closed]:fade-out-0 sm:rounded-lg"
dialog_closeBtn_cls = "dialog-close-button absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none"
dialog_title_cls = "text-lg font-semibold leading-none tracking-tight"
dialog_description_cls = "text-sm text-muted-foreground"
dialog_header_cls = "flex flex-col space-y-1.5 text-center sm:text-left"
dialog_footer_cls = "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2"


def DialogHeader(*c, cls=None, **kwargs):
    new_cls = dialog_header_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def DialogFooter(*c, cls=None, **kwargs):
    new_cls = dialog_footer_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def DialogTitle(*c, cls=None, **kwargs):
    new_cls = dialog_title_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return H1(*c, **kwargs)


def DialogClose(*c, cls=None, **kwargs):
    new_cls = "dialog-close-button"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(*c, **kwargs)


def DialogDescription(*c, cls=None, **kwargs):
    new_cls = dialog_description_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return P(*c, **kwargs)


def DialogContent(*c, cls=None, **kwargs):
    closeBtn = ft_hx(
        "button",
        Lucide(icon="x", cls="size-4"),
        Span("Close", cls="sr-only"),
        type="button",
        tabindex=0,
        cls=dialog_closeBtn_cls,
    )
    new_cls = dialog_content_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(Div(*c, closeBtn, data_ref="dialog-content", **kwargs), cls=dialog_portal_cls, tabindex="-1", data_ref="dialog-portal")


def DialogTrigger(*c, **kwargs):
    return Button(
        *c,
        data_ref="dialog-trigger",
        type="button",
        **kwargs,
    )


def Dialog(
    *c,
    footer: str = None,
    title: str = None,
    description: str = None,
    standard: bool = False,
    trigger: str = None,
    cls=None,
    **kwargs,
):
    new_cls = "group"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    if standard:
        return Div(*c, data_ref="dialog", tabindex="-1", **kwargs)

    header_content = []
    if title:
        header_content.append(DialogTitle(title))
    if description:
        header_content.append(DialogDescription(description))
    if footer:
        footer = DialogFooter(footer)
    dialog_trigger = None
    if trigger and isinstance(trigger, str):
        dialog_trigger = DialogTrigger(trigger)
    elif trigger:
        dialog_trigger = trigger

    if header_content:
        header = DialogHeader(
            *header_content,
        )

    return Div(
        dialog_trigger,
        DialogContent(
            header,
            *c,
            footer,
        ),
        data_ref="dialog",
        tabindex="-1",
        **kwargs,
    )
