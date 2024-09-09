from fasthtml.components import Label as OgLabel

__all__ = ["Label"]

label_cls = "preventdbclick text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"

def Label(*c, htmlFor=None, cls=None, **kwargs):
    new_cls = label_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return OgLabel(*c, _for=htmlFor, **kwargs)