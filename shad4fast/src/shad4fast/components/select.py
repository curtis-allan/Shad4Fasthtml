from fasthtml.common import Div, ft_hx, Span, Hr, Script
from fasthtml.xtend import Hidden
from lucide_fasthtml import Lucide
import os

__all__ = [
    "Select",
    "SelectContent",
    "SelectLabel",
    "SelectItem",
    "SelectSeparator",
    "SelectTrigger",
    "SelectGroup",
    "SelectValue",
]


select_cls = {
    "trigger": "flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 [&>span]:line-clamp-1",
    "scroll-up-btn": "flex cursor-default items-center justify-center py-1",
    "scroll-down-btn": "flex cursor-default items-center justify-center py-1",
    "content": "relative z-50 max-h-96 min-w-[8rem] overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1",
    "item": "group relative flex w-full cursor-default select-none items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[disabled]:opacity-50",
    "separator": "-mx-1 my-1 h-px bg-muted",
    "label": "py-1.5 pl-8 pr-2 text-sm font-semibold",
    "base": "group relative data-[state=open]:no-bg-scroll",
    "viewport": "p-1 h-[var(--radix-select-trigger-height)] w-full min-w-[var(--radix-select-trigger-width)] no-scrollbar",
}

select_content_styles = "box-sizing: border-box; display: flex; flex-direction: column; outline: none; --radix-select-content-transform-origin: var(--radix-popper-transform-origin); --radix-select-content-available-width: var(--radix-popper-available-width); --radix-select-content-available-height: var(--radix-popper-available-height); --radix-select-trigger-width: var(--radix-popper-anchor-width); --radix-select-trigger-height: var(--radix-popper-anchor-height); pointer-events: auto;"

with open(os.path.join(os.path.dirname(__file__), "../js/select.js")) as select:
    select_scr = select.read()

script = Script(select_scr)


def SelectTrigger(*c, cls=None, **kwargs):
    ico = Lucide(icon="chevron-down", cls="h-4 w-4 opacity-50 shrink-0")
    new_cls = select_cls["trigger"]
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return ft_hx("button", *c, ico, type="button", data_ref="select-trigger", **kwargs)


def SelectValue(placeholder=None, cls=None, **kwargs):
    new_cls = "pointer-events-none"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Span(placeholder, data_ref="select-value", **kwargs)


def SelectScrollUpButton(cls=None, **kwargs):
    new_cls = select_cls["scroll-up-btn"]
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    ico = Lucide(icon="chevron-up", cls="h-4 w-4 hidden sm:flex")
    return Div(ico, aria_hidden="true", data_ref="select-scroll-up", **kwargs)


def SelectScrollDownButton(cls=None, **kwargs):
    new_cls = select_cls["scroll-down-btn"]
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    ico = Lucide(icon="chevron-down", cls="h-4 w-4 hidden sm:flex")
    return Div(ico, aria_hidden="true", data_ref="select-scroll-down", **kwargs)


def SelectContent(*c, cls=None, id=None, **kwargs):
    if not id:
        raise ValueError("`id` is required")
    new_cls = select_cls["content"]
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Portal(
        Div(
            SelectScrollUpButton(),
            Div(
                *c,
                style="position:relative;flex:1 1 0%;overflow: auto;",
                cls=select_cls["viewport"],
                role="listbox",
                id=f"{id}-viewport",
                data_ref="select-viewport",
            ),
            SelectScrollDownButton(),
            tabindex="-1",
            style=select_content_styles,
            id=f"{id}-content",
            data_ref="select-content",
            data_state="closed",
            **kwargs,
        ),
        id=id,
    )


def SelectGroup(*c, **kwargs):
    return Div(*c, role="group", **kwargs)


def SelectLabel(*c, cls=None, **kwargs):
    new_cls = select_cls["label"]
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def SelectItem(*c, cls=None, checked="false", value=None, **kwargs):
    new_cls = select_cls["item"]
    span_cls = "absolute left-2 hidden h-3.5 w-3.5 items-center justify-center group-data-[checked=true]:flex"
    ico = Lucide(icon="check", cls="h-4 w-4")
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(
        Span(ico, cls=span_cls),
        Span(*c),
        data_checked=checked,
        value=value,
        role="option",
        tabindex=-1,
        data_ref="select-item",
        aria_selected=checked,
        **kwargs,
    )


def SelectSeparator(**kwargs):
    cls = f"{kwargs.pop('cls', '')} {select_cls['separator']}"
    return Hr(cls=cls, **kwargs)


def Portal(*c, id=None, **kwargs):
    if not id:
        raise ValueError("`id` is required")
    return Div(
        *c,
        id=f"{id}-portal",
        style="position:fixed;left:0;top:0;display:none;",
        **kwargs,
    )


def Select(
    *c,
    cls=None,
    state="closed",
    placeholder: str = None,
    label: str = None,
    items: list = None,
    id=None,
    name=None,
    standard=False,
    **kwargs,
):
    if not id:
        raise ValueError("`id` is required")
    new_cls = select_cls["base"]
    value_holder = Hidden(value="", name=name, id=f"{id}-input")
    render_items = ()

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    if standard:
        return Div(
            value_holder,
            *c,
            script,
            data_ref="select",
            data_state=state,
            id=id,
            role="combobox",
            aria_controls=f"{id}-content",
            aria_expanded="false",
            aria_haspopup="listbox",
            **kwargs,
        )

    if items:
        render_items = (
            SelectItem(item, value=item.lower(), name=item) for item in items
        )

    select_trigger = SelectTrigger(SelectValue(placeholder))
    select_content = (
        SelectContent(SelectGroup(SelectLabel(label), *render_items), id=id),
    )

    return Div(
        value_holder,
        select_trigger,
        select_content,
        script,
        data_state=state,
        data_ref="select",
        id=id,
        role="combobox",
        aria_controls=f"{id}-content",
        aria_expanded="false",
        aria_haspopup="listbox",
        **kwargs,
    )
