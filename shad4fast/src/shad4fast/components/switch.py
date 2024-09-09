from fasthtml.components import Div, Span, Input

__all__ = ["Switch"]

switch_base_cls = "group peer inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=unchecked]:bg-input"
switch_thumb_cls = "pointer-events-none block h-5 w-5 rounded-full bg-background shadow-lg ring-0 transition-transform group-data-[state=checked]:translate-x-5 group-data-[state=unchecked]:translate-x-0"

def Switch(state="unchecked", cls=None, id=None, name=None, value=None, **kwargs):
    curr_state = "true" if state == "checked" else None
    assert state in ("checked", "unchecked"), '`state` not in ("checked", "unchecked")'

    new_cls = switch_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    thumb = Span(cls=switch_thumb_cls)
    value_holder = Input(
        type="checkbox",
        style="display: none;",
        id=id,
        name=name,
        value=value,
        checked=curr_state,
    )
    return Div(
        thumb, value_holder, data_state=state, onclick="toggleCheckbox(this)", **kwargs
    )