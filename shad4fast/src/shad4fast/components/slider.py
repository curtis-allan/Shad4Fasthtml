from fasthtml.common import Div, Input, Script
import os

__all__ = ["Slider"]

with open(os.path.join(os.path.dirname(__file__), '../js/slider.js')) as slider:
    slider_scr = slider.read()

script = Script(slider_scr, _async=True, defer=True)

def Slider(cls=None, min=0, max=100, step=1, value=0, name=None, **kwargs):
    new_cls = "relative flex w-full touch-none select-none items-center"

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    return Div(
        script,
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