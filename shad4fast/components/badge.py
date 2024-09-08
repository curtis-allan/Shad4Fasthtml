from fasthtml.components import Div

__all__ = ["Badge"]

badge_cls = "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2"
badge_variants_cls = {
    "default": "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
    "secondary": "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
    "destructive": "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
    "outline": "text-foreground",
}

def Badge(*c, variant: str = "default", cls=None, **kwargs):
    variants = tuple(badge_variants_cls.keys())
    assert variant in variants, f"`variant` not in {variants}"
    new_cls = badge_cls
    new_cls += f" {badge_variants_cls[variant]}"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)