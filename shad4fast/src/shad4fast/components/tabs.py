from fasthtml.common import Div, Script, ft_hx
import os

__all__ = ["Tabs", "TabsList", "TabsTrigger", "TabsContent"]

with open(os.path.join(os.path.dirname(__file__), '../js/tabs.js')) as tabs:
    tabs_scr = tabs.read()

script = Script(tabs_scr, _async=True, defer=True)

def Tabs(*c, default_value=None, **kwargs):

    return Div(*c, script, data_ref="tabs", data_default_value=default_value, **kwargs)

def TabsList(*c, cls=None, **kwargs):
    new_cls = "inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, role="tablist", **kwargs, tabindex=0)

def TabsTrigger(*c, cls=None, value=None, **kwargs):
    new_cls = "inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return ft_hx('button', type='button',*c, role="tab", data_tab_trigger=True, data_value=value, **kwargs)

def TabsContent(*c, cls=None, value=None, **kwargs):
    new_cls = "mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, role="tabpanel", data_tab_content=True, data_value=value, hidden=True, **kwargs)