from fasthtml.components import Div, Input, Span, Script, NotStr
from lucide_fasthtml import Lucide
from fasthtml.common import ft_hx
import os

__all__ = ["RadioGroup", "RadioGroupItem"]

with open(os.path.join(os.path.dirname(__file__), '../js/radio.js')) as radio:
    radio_scr = radio.read()

script = Script(NotStr(radio_scr), _async=True, defer=True)

def RadioGroup(*c, cls=None, name=None, defaultValue=None, **kwargs):
    new_cls = "grid gap-2"

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    return Div(
        script,
        *c,
        Input(type="hidden", data_ref="hidden-input", name=name, value=defaultValue),
        data_ref="radio-group",
        role="radiogroup",
        aria_required="false",
        style="outline:none;",
        data_value=defaultValue,
        **kwargs
    )

def RadioGroupItem(cls=None, value=None, **kwargs):
    new_cls = "group cursor-pointer aspect-square h-4 w-4 rounded-full border border-primary text-primary ring-offset-background focus:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
    indicator_cls = "hidden group-data-[state=checked]:flex items-center justify-center"
    circle_cls = "h-2.5 w-2.5 fill-current text-current"

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    return ft_hx('button',
        Span(
            Lucide(icon="circle", cls=circle_cls),
            cls=indicator_cls,
            data_state="unchecked",
        ),
        data_ref="radio-item",
        value=value,
        role="radio",
        type='button',
        aria_checked="false",
        tabindex="0",
        **kwargs
    )