from fasthtml.components import Textarea as OgTextarea

__all__ = ["Textarea"]

textarea_cls = "flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"

def Textarea(*c, cls=None, **kwargs):
    new_cls = textarea_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return OgTextarea(*c, **kwargs)