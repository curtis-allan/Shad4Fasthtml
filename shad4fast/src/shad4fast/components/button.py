from fasthtml.components import Button as OgButton

__all__ = ["Button"]

btn_variants = {
    "default": "bg-primary text-primary-foreground hover:bg-primary/90",
    "destructive": "bg-destructive text-destructive-foreground hover:bg-destructive/90",
    "outline": "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
    "secondary": "bg-secondary text-secondary-foreground hover:bg-secondary/80",
    "ghost": "hover:bg-accent hover:text-accent-foreground",
    "link": "text-primary underline-offset-4 hover:underline",
}
btn_sizes = {
    "default": "h-10 px-4 py-2",
    "sm": "h-9 rounded-md px-3",
    "lg": "h-11 rounded-md px-8",
    "icon": "h-10 w-10",
}
btn_base_cls = "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"


def Button(*c, size="default", variant="default", cls=None, **kwargs):
    new_cls = btn_base_cls

    new_cls += f" {btn_variants[variant]} {btn_sizes[size]}"

    # If cls was provided, append it to the new_cls
    if cls:
        new_cls += f" {cls}"

    # Update the kwargs with the new cls
    kwargs["cls"] = new_cls
    return OgButton(*c, **kwargs)