from fasthtml.common import Div, P, H1, Span, ft_hx
from lucide_fasthtml import Lucide
from .button import Button

__all__ = [
    "Sheet",
    "SheetClose",
    "SheetContent",
    "SheetHeader",
    "SheetTitle",
    "SheetDescription",
    "SheetFooter",
    "SheetTrigger",
]

sheet_overlay_cls = "group-data-[state=open]:no-bg-scroll fixed inset-0 z-50 bg-black/80 group-data-[state=open]:animate-in group-data-[state=closed]:animate-out group-data-[state=closed]:fade-out-0 group-data-[state=open]:fade-in-0"
sheet_variants_cls = {
    "top": "inset-x-0 top-0 border-b group-data-[state=closed]:slide-out-to-top group-data-[state=open]:slide-in-from-top",
    "bottom": "inset-x-0 bottom-0 border-t group-data-[state=closed]:slide-out-to-bottom group-data-[state=open]:slide-in-from-bottom",
    "left": "inset-y-0 left-0 h-full w-3/4 border-r group-data-[state=closed]:slide-out-to-left group-data-[state=open]:slide-in-from-left sm:max-w-sm",
    "right": "inset-y-0 right-0 h-full w-3/4 border-l group-data-[state=closed]:slide-out-to-right group-data-[state=open]:slide-in-from-right sm:max-w-sm",
}
sheet_closeBtn_cls = "sheet-close-button absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none"
sheet_content_cls = "fixed z-50 gap-4 bg-background p-6 shadow-lg transition ease-in-out group-data-[state=open]:animate-in group-data-[state=closed]:animate-out group-data-[state=closed]:duration-300 group-data-[state=open]:duration-500"
sheet_header_cls = "flex flex-col space-y-2 text-center sm:text-left"
sheet_footer_cls = "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2"
sheet_title_cls = "text-lg font-semibold text-foreground"
sheet_description_cls = "text-sm text-muted-foreground"


def Sheet(
    *c,
    side="right",
    title=None,
    description=None,
    footer=None,
    standard=False,
    trigger=None,
    state="closed",
    cls=None,
    **kwargs,
):
    header_content = []
    sheet_trigger = None

    new_cls = None
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    if standard:
        return Div(*c, data_ref="sheet", role="dialog", tabindex="-1", **kwargs)

    if title:
        header_content.append(SheetTitle(title))
    if description:
        header_content.append(SheetDescription(description))
    if header_content:
        header = SheetHeader(
            *header_content,
        )
    else:
        header = None
    if footer:
        footer = SheetFooter(footer)
    else:
        footer = None
    if trigger and isinstance(trigger, str):
        sheet_trigger = SheetTrigger(trigger)
    elif trigger:
        sheet_trigger = trigger

    return Div(
        sheet_trigger,
        SheetContent(header, *c, footer, side=side, state=state),
        data_state=state,
        role="dialog",
        data_ref="sheet",
        tabindex="-1",
        **kwargs,
    )


def SheetClose(*c, cls=None, **kwargs):
    new_cls = "sheet-close-button"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(
        *c,
        **kwargs,
    )


def SheetContent(*c, cls=None, state: str = "closed", side="right", **kwargs):
    overlay = Div(data_ref="sheet-overlay", cls=sheet_overlay_cls)
    new_cls = f"{sheet_content_cls} {sheet_variants_cls[side]}"
    closeBtn = ft_hx(
        "button",
        Span("Close", cls="sr-only"),
        Lucide(icon="x", cls="size-4"),
        cls=sheet_closeBtn_cls,
        type="button",
        tabindex=0,
    )
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(
        overlay,
        Div(*c, closeBtn, data_ref="sheet-content", **kwargs),
        data_ref="sheet-portal",
        style=f"display:{'block' if state=='open' else 'none'};",
        data_state=state,
        cls="group",
    )


def SheetTitle(*c, cls=None, **kwargs):
    new_cls = sheet_title_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return H1(*c, **kwargs)


def SheetDescription(*c, cls=None, **kwargs):
    new_cls = sheet_description_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return P(*c, **kwargs)


def SheetHeader(*c, cls=None, **kwargs):
    new_cls = sheet_header_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def SheetTrigger(*c, **kwargs):
    return Button(
        *c,
        type="button",
        data_ref="sheet-trigger",
        **kwargs,
    )


def SheetFooter(*c, cls=None, **kwargs):
    new_cls = sheet_footer_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)
