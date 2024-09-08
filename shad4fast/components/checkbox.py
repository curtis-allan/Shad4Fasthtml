from fasthtml.components import Span, Input
from lucide_fasthtml import Lucide

__all__ = ["Checkbox"]

checkbox_base_cls = "cursor-pointer preventdbclick peer group h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground"
checkbox_indicator_cls = "preventdbclick flex items-center justify-center text-current group-data-[state=unchecked]:hidden"

def Checkbox(cls=None, state="unchecked", name=None, value=None, id=None, **kwargs):
    curr_state = "true" if state == "checked" else None
    assert state in ("checked", "unchecked"), '`state` not in ("checked", "unchecked")'

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
        checked=curr_state,
    )
    return Span(
        indicator,
        value_holder,
        data_state=state,
        onclick="toggleCheckbox(this)",
        **kwargs,
    )