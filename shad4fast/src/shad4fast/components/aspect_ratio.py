from fasthtml.common import Div

def AspectRatio(*c, ratio: any = {1/1}, **kwargs):
    ratio = str(ratio).replace("{", "").replace("}", "")
    base_style = "position: relative; width: 100%;"
    return Div(Div(*c, style="position: absolute; inset: 0px;", **kwargs),cls="overflow-hidden", style=base_style + f" aspect-ratio:{ratio}")