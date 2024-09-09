from fasthtml.components import Div

__all__ = ["Separator"]

sep_cls = "shrink-0 bg-border"
sep_variant_cls = {
    "horizontal": "h-[1.5px] w-full",
    "vertical": "self-stretch w-[1.5px]",
}

def Separator(orientation="horizontal", cls=None, **kwargs):
    new_cls = f"{sep_cls} {sep_variant_cls[orientation]}"

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(decorative=True, **kwargs)