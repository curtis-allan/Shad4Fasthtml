from fasthtml.components import Div

__all__ = ["Progress"]

progress_cls = "relative h-4 w-full overflow-hidden rounded-full bg-secondary"
progress_inner_cls = "progress-inner h-full w-full flex-1 bg-primary transition-all"

def Progress(value=0, id=None, cls=None, **kwargs):
    bar_comp = Div(
        style=f"transform: translateX(-{100-value}%)",
        id=f"{id}-inner",
        cls=progress_inner_cls,
    )
    new_cls = progress_cls
    if cls:
        new_cls += f" { cls}"
    kwargs["cls"] = new_cls
    return Div(
        bar_comp,
        role="progressbar",
        value=value,
        id=id,
        **kwargs,
    )