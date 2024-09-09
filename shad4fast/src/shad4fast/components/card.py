from fasthtml.components import Div, H1, P

__all__ = ["Card", "CardHeader", "CardTitle", "CardDescription", "CardContent", "CardFooter"]

card_cls = {
    "card": "rounded-lg border bg-card text-card-foreground shadow-sm",
    "head": "flex flex-col space-y-1.5 p-6",
    "title": "text-2xl font-semibold leading-none tracking-tight",
    "description": "text-sm text-muted-foreground",
    "content": "p-6 pt-0",
    "footer": "flex items-center p-6 pt-0",
}

def CardHeader(*c, cls=None, **kwargs):
    new_cls = card_cls["head"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def CardTitle(*c, cls=None, **kwargs):
    new_cls = card_cls["title"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return H1(*c, **kwargs)


def CardDescription(*c, cls=None, **kwargs):
    new_cls = card_cls["description"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return P(*c, **kwargs)


def CardContent(*c, cls=None, **kwargs):
    new_cls = card_cls["content"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def CardFooter(*c, cls=None, **kwargs):
    new_cls = card_cls["footer"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def Card(
    *c,
    title: str = None,
    description: str = None,
    footer=None,
    cls=None,
    standard=False,
    **kwargs,
):
    new_cls = card_cls["card"]

    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls

    if standard:
        return Div(*c, **kwargs)

    header_content = []
    if title:
        header_content.append(CardTitle(title))
    if description:
        header_content.append(CardDescription(description))

    if footer:
        footer = CardFooter(footer)

    if header_content:
        header = CardHeader(
            *header_content,
        )

    return Div(header, CardContent(*c), footer, **kwargs)
