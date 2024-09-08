from fasthtml.components import Div, H1, P
from lucide_fasthtml import Lucide

__all__ = ["Alert", "AlertTitle", "AlertDescription"]

alert_cls = {
    "alert": "relative w-full rounded-lg border p-4 [&>svg~*]:pl-7 [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4",
    "title": "mb-1 font-medium leading-none tracking-tight",
    "description": "text-sm [&_p]:leading-relaxed",
}
alert_variants_cls = {
    "default": "bg-background text-foreground [&>svg]:text-foreground",
    "destructive": "border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive",
}

def AlertTitle(title: str = None, cls=None, **kwargs):
    new_cls = alert_cls["title"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return H1(title, **kwargs)


def AlertDescription(description: str = None, cls=None, **kwargs):
    new_cls = alert_cls["description"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return P(description, **kwargs)


def Alert(
    *c,
    title: str = None,
    description: str = None,
    variant: str = "default",
    cls=None,
    standard=False,
    icon: str = "chevrons-right",
    **kwargs,
):
    variants = tuple(alert_variants_cls.keys())
    assert variant in variants, f"`variant` not in {variants}"

    new_cls = f"{alert_cls['alert']} {alert_variants_cls[variant]}"
    headers = []
    if variant == "destructive":
        icon = "circle-alert"
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    if standard:
        return Div(*c, **kwargs)
    headers.append(Lucide(icon=icon, cls="size-4"))
    if title:
        headers.append(AlertTitle(title))
    if description:
        headers.append(AlertDescription(description))

    return Div(*headers, *c, **kwargs)