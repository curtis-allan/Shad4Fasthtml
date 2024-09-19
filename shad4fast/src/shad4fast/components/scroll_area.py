from fasthtml.common import Div

viewport_styles = "scrollbar-width: none; -ms-overflow-style: none; -webkit-overflow-scrolling: touch;"

scrollbar_cls = "flex touch-none select-none transition-colors p-[1px]"


def ScrollArea(*c, cls=None, orientation="vertical", **kwargs):
    new_cls = "relative overflow-hidden"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    content = Div(
        Div(*c, style="min-width:100%;display:table;"),
        style=f"overflow: {'hidden scroll' if orientation == 'vertical' else 'scroll'}; {viewport_styles}",
        cls="w-full h-full rounded-[inherit]",
        data_ref="viewport",
    )

    scrollbar = Div(
        Div(cls="bg-border rounded-full hidden relative flex-1", data_ref="thumb"),
        cls=f"{scrollbar_cls} flex-col h-2.5 w-full border-t border-t-transparent"
        if orientation == "horizontal"
        else f"{scrollbar_cls} w-2.5 h-full border-l border-l-transparent",
        data_ref="scrollbar",
        style=f"position: absolute;{'right:0; top:0;' if orientation == 'vertical' else 'bottom:0; left:0;'}",
    )

    return Div(
        content,
        scrollbar,
        role="region",
        tabindex="0",
        data_orientation=orientation,
        data_ref_scrollarea=True,
        aria_label="Scrollable content",
        **kwargs,
    )
