from fasthtml.components import Div, P, H1, Span, Script, NotStr
from lucide_fasthtml import Lucide
from .button import Button
import os

__all__ = ["Dialog", "DialogHeader", "DialogFooter", "DialogTitle", "DialogCloseButton", "DialogDescription", "DialogContent", "DialogTrigger"]

dialog_overlay_cls = "group-data-[state=open]:no-bg-scroll dialog-overlay fixed inset-0 z-50 bg-black/80 group-data-[state=open]:animate-in group-data-[state=closed]:animate-out group-data-[state=closed]:fade-out-0 group-data-[state=open]:fade-in-0"
dialog_content_cls = "dialog-content fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 group-data-[state=open]:animate-in group-data-[state=closed]:animate-out group-data-[state=closed]:fade-out-0 group-data-[state=open]:fade-in-0 group-data-[state=closed]:zoom-out-95 group-data-[state=open]:zoom-in-95 group-data-[state=closed]:slide-out-to-left-1/2 group-data-[state=closed]:slide-out-to-top-[48%] group-data-[state=open]:slide-in-from-left-1/2 group-data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg"
dialog_closeBtn_cls = "dialog-close-btn cursor-pointer active:ring absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none group-data-[state=open]:bg-accent group-data-[state=open]:text-muted-foreground"
dialog_title_cls = "text-lg font-semibold leading-none tracking-tight"
dialog_description_cls = "text-sm text-muted-foreground"
dialog_header_cls = "flex flex-col space-y-1.5 text-center sm:text-left"
dialog_footer_cls = "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2"

with open(os.path.join(os.path.dirname(__file__), '../js/dialog.js')) as dialog:
    dialog_scr = dialog.read()

script = Script(NotStr(dialog_scr), _async=True, defer=True)

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


def DialogCloseButton(*c, cls=None, **kwargs):
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
    closeBtn = Div(
        Lucide(icon="x", cls="size-4"),
        Span("Close", cls="sr-only"),
        cls=dialog_closeBtn_cls,
    )
    new_cls = dialog_content_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, closeBtn, **kwargs)


def DialogTrigger(*c, dialog_id=None, **kwargs):
    return Button(
        *c,
        data_dialog_id=dialog_id,
        **kwargs,
    )


def Dialog(
    *c,
    footer=None,
    title=None,
    description=None,
    standard=False,
    state="closed",
    cls=None,
    **kwargs,
):
    overlay = Div(cls=dialog_overlay_cls)

    new_cls = "dialog group"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    if standard:
        return Div(overlay, style="display: none;", data_state=state, *c, **kwargs)

    header_content = []
    if title:
        header_content.append(DialogTitle(title))
    if description:
        header_content.append(DialogDescription(description))
    if footer:
        footer = DialogFooter(footer)

    if header_content:
        header = DialogHeader(
            *header_content,
        )

    return Div(script,
        overlay,
        DialogContent(header, *c, footer),
        style="display: none;",
        data_state=state,
        tabindex="-1",
        **kwargs,
    )
