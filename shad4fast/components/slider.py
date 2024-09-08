from fasthtml.components import Div, Input
from fasthtml.xtend import ScriptX

__all__ = ["Slider"]

def Slider(cls=None, min=0, max=100, step=1, value=0, name=None, **kwargs):
    new_cls = "relative flex w-full touch-none select-none items-center"

    slider_script = ScriptX('shad4fast/js/slider.js', _async=True, defer=True)

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    return Div(
        slider_script,
        Div(
            Div(data_ref="range", cls="absolute h-full bg-primary"),
            data_ref="track",
            cls="relative h-2 w-full grow overflow-hidden rounded-full bg-secondary"
        ),
        Div(
            data_ref="thumb",
            cls="absolute top-1/2 -translate-x-1/2 -translate-y-1/2 block h-5 w-5 rounded-full border-2 border-primary bg-background ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
        ),
        Input(type="hidden", data_ref="hidden-input", name=name, value=value),
        data_max=max,
        data_step=step,
        data_value=value,
        role="slider",
        data_min=min,
        data_ref="slider",
        aria_valuemin=min,
        aria_valuemax=max,
        aria_valuenow=value,
        **kwargs
    )