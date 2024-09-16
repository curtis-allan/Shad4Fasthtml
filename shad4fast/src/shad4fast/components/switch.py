from fasthtml.common import Span, Input, ft_hx, Div

__all__ = ["Switch"]

switch_base_cls = "group peer inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 peer-checked:bg-primary bg-input peer-checked:[&>span]:translate-x-5 [&>span]:translate-x-0"
switch_thumb_cls = "pointer-events-none block h-5 w-5 rounded-full bg-background shadow-lg ring-0 transition-transform"


def Switch(checked: bool = False, cls=None, name=None, value="1", **kwargs):
    thumb = Div(
        Span(cls=switch_thumb_cls), cls=f"{switch_base_cls} {cls if cls else ''}"
    )
    value_holder = Input(
        type="checkbox",
        style="display: none;",
        name=name,
        value=value,
        checked=checked,
        cls="peer",
    )

    return ft_hx(
        "button",
        value_holder,
        thumb,
        type="button",
        onclick="this.querySelector('input').click()",
        role="switch",
        **kwargs,
    )
