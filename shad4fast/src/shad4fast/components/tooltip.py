from fasthtml.common import Div, Button
from typing import Literal
__all__ = ["Tooltip", "TooltipTrigger", "TooltipContent"]

tooltip_content_cls = "opacity-0 invisible absolute z-50 overflow-hidden rounded-md border bg-popover px-3 py-1.5 text-sm text-popover-foreground shadow-md transition-opacity duration-300"

def Tooltip(*c, method:str='hover', **kwargs):
    assert method in ['hover', 'click'], "Method must be either 'hover' or 'click'"
    return Div(*c, data_ref="tooltip", data_method=method, **kwargs)

def TooltipTrigger(c, **kwargs):
    if isinstance(c, str):
        return Button(c, data_ref="tooltip-trigger", **kwargs)
    return c(data_ref="tooltip-trigger", **kwargs)

def TooltipContent(*c, state='closed', **kwargs):
    return Div(*c, cls=f"{kwargs.get('cls', '')} {tooltip_content_cls}", data_state=state, data_ref="tooltip-content", **kwargs)
