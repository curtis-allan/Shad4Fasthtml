from fasthtml.components import Span, Input
from lucide_fasthtml import Lucide

__all__ = ["Checkbox"]

checkbox_base_cls = "cursor-pointer preventdbclick peer group h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground"
checkbox_indicator_cls = "preventdbclick items-center hidden justify-center text-current group-data-[state=checked]:flex"


def Checkbox(cls=None, checked: bool = False, name=None, value="1", id=None, **kwargs):
    new_cls = checkbox_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    indicator = Span(Lucide(icon="check", cls="size-4"), cls=checkbox_indicator_cls)
    value_holder = Input(
        type="checkbox",
        style="display: none;",
        value=value,
        id=id,
        name=name,
        checked=checked,
    )
    return Span(
        indicator,
        value_holder,
        aria_checked=checked,
        role="checkbox",
        data_state="checked" if checked else "unchecked",
        onclick="toggleCheckbox(this)",
        **kwargs,
    )
