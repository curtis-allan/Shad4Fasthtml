from functools import partial
from fasthtml.components import Div, Span
from lucide_fasthtml import Lucide
from .button import Button

def CollapsibleTrigger(*c, **kwargs):
    sr = Span("Toggle", cls="sr-only")
    return Button(Lucide("chevrons-up-down", cls="size-4"),sr, variant="ghost", size="icon", cls="w-9 p-0", data_ref="collapse-trigger", **kwargs)

def Collapsible(*c, state="closed", **kwargs):
    cls = f"{kwargs.pop('cls', '')} group"
    return Div(*c, data_ref="collapse",  data_state=state, cls=cls,  **kwargs)

def CollapsibleContent(*c, **kwargs):
    cls = f"{kwargs.pop('cls', '')} group-data-[state=closed]:hidden"
    return Div(*c, cls=cls,  data_ref="collapse-content", **kwargs)