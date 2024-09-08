from fasthtml.components import Input as OgInput

__all__ = ["Input"]

input_base_cls = "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"


def Input(*c, cls=None, **kwargs):
    new_cls = input_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return OgInput(*c, **kwargs)