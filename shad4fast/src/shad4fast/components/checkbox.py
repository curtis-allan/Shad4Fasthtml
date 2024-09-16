from fasthtml.common import Span, Input, Div, ft_hx
from lucide_fasthtml import Lucide

__all__ = ["Checkbox"]

checkbox_base_cls = "peer cursor-pointer h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 peer-disabled:cursor-not-allowed peer-disabled:opacity-50 peer-checked:bg-primary peer-checked:text-primary-foreground peer-checked:[&>span]:flex"
checkbox_indicator_cls = (
    "preventdbclick items-center hidden justify-center text-current"
)


def Checkbox(cls=None, checked: bool = False, name=None, value="1", **kwargs):
    indicator = Div(
        Span(Lucide(icon="check", cls="size-4"), cls=checkbox_indicator_cls),
        cls=f"{checkbox_base_cls} {cls if cls else ''}",
    )
    value_holder = Input(
        type="checkbox",
        value=value,
        name=name,
        style="display: none;",
        checked=checked,
        cls="peer",
    )

    return ft_hx(
        "button",
        value_holder,
        indicator,
        type="button",
        onclick="this.querySelector('input').click()",
        **kwargs,
    )
