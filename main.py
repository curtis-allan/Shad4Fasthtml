import random

from starlette.responses import StreamingResponse

from docs.comp_demos import (
    ThemeToggle,
    alert_block,
    badge_block,
    button_block,
    card_block,
    checkbox_block,
    dialog_block,
    input_block,
    label_block,
    lucide_block,
    progress_block,
    select_block,
    separator_block,
    sheet_block,
    switch_block,
    table_block,
    textarea_block,
    toast_block,
    carousel_block,
    slider_block,
    tabs_block,
)
from fasthtml.common import *
from fasthtml.components import Zero_md
from shadcn import *

zeromd_headers = Script(
    type="module", src="https://cdn.jsdelivr.net/npm/zero-md@3?register"
)

social_headers = Socials(
    site_name="Shad4FastHtml",
    title="Shad4FastHtml",
    description="Open source Shadcn-ui components, made for FastHtml",
    url="www.shad4fasthtml.com",
    image="/public/social.png",
    card="summary_large_image",
)

favicon_headers = Favicon(
    light_icon="/public/light_favicon.ico", dark_icon="/public/dark_favicon.ico"
)

tw_output_link = Link(href="/output.css", rel="stylesheet")

app, rt = fast_app(
    pico=False,
    hdrs=(
        ShadHead(),
        zeromd_headers,
        social_headers,
        favicon_headers,
        tw_output_link,
    ),
    htmlkw={"lang": "en"},
)

toast_setup(app)


def MobileHeader():
    return Div(
        SheetTrigger(
            Lucide(icon="menu"),
            variant="outline",
            size="icon",
            sheet_id="mobile-nav",
        ),
        MobileNav(),
        A(
            H1(
                "Shad4FastHtml",
                cls="text-xl font-bold tracking-tighter select-none",
            ),
            href="/",
            hx_boost="true",
        ),
        ThemeToggle(cls="shrink-0"),
        cls="sm:hidden fixed flex top-0 z-50 items-center justify-between bg-background w-full px-4 py-2 shadow dark:shadow-border",
        tabindex="-1",
    )


def source_code():
    return (
        Div(
            Span(
                Lucide(icon="terminal", cls="size-4"),
                P(
                    "source code",
                    style="font-variant:small-caps; font-size:1.1rem; font-weight:600; letter-spacing:-0.05rem;"
                ),
                cls="text-center col-span-2 gap-1.5 flex items-center justify-start text-sm font-mono select-none dark:bg-slate-900 bg-slate-700 p-1 border border-inset border-accent text-green-400 dark:text-green-600",
            ),
            Span(
                Lucide(
                    icon="corner-down-right",
                    cls="w-5 h-7 text-muted-foreground skew-y-6",
                ),
                cls="justify-self-end w-fit select-none",
            ),
            A(
                Button(
                    Lucide(icon="github"),
                    size="icon",
                    variant="outline",
                ),
                href="https://github.com/curtis-allan/shadcn-fasthtml-framework",
                target="_blank",
                cls="self-start",
            ),
            cls="grid grid-flow-row-dense auto-cols-fr gap-1 w-[140px]",
        ),
    )


@rt("/")
def get():
    return (
        Body(
            Title("Shadcn components in FastHtml"),
            Main(
                Section(
                    MobileHeader(),
                    Header(
                        H1(
                            "Shadcn-ui components, made for FastHtml",
                            cls="sm:text-6xl text-5xl font-bold tracking-tight text-center",
                        ),
                        Nav(
                            Div(
                                A(
                                    Button(
                                        Lucide(icon="github"),
                                        size="icon",
                                        variant="ghost",
                                    ),
                                    href="https://github.com/curtis-allan/shadcn-fasthtml-framework",
                                    target="_blank",
                                ),
                                A(
                                    Button(
                                        Lucide(icon="twitter"),
                                        size="icon",
                                        variant="ghost",
                                    ),
                                    href="https://x.com/CurtisJAllan",
                                    target="_blank",
                                ),
                                cls="flex-grow flex gap-2",
                            ),
                            A(
                                Button(
                                    "Get Started",
                                    Lucide(icon="arrow-right"),
                                    variant="default",
                                ),
                                href="/getting-started/installation",
                                hx_boost="true",
                                hx_swap="outerHTML",
                            ),
                            cls="flex container max-w-md p-2 my-6 gap-4 justify-between border rounded-xl shadow-md",
                        ),
                        cls="flex flex-col text-balance max-w-3xl",
                    ),
                    Div(
                        H2(
                            "Click this button to change the theme",
                            cls="text-lg text-muted-foreground",
                        ),
                        Lucide(
                            icon="arrow-right",
                            cls="size-5 shrink-0 text-muted-foreground",
                        ),
                        ThemeToggle(cls="shrink-0"),
                        cls="container flex justify-center items-center gap-1.5",
                    ),
                    cls="flex flex-col justify-center gap-4 items-center container min-h-[calc(100svh-56px)]",
                ),
            ),
            cls="pt-[50px] sm:pt-0",
        ),
    )


def MobileNav():
    return (
        Sheet(
            SheetContent(
                SheetHeader(
                    SheetTitle(
                        "Documentation",
                        cls="tracking-tight select-none",
                    ),
                    Badge(
                        "v1.0",
                        variant="outline",
                    ),
                    cls="flex flex-col items-start w-full",
                ),
                Separator(),
                Div(
                    Div(
                        RenderNav(),
                        cls="overflow-auto block min-h-max no-scrollbar",
                    ),
                    cls="overflow-hidden pl-2 w-full grid grow max-h-[calc(100vh-8rem)]",
                ),
                Separator(),
                SheetFooter(
                    source_code(),
                ),
                side="left",
                cls="w-[215px] sm:w-[250px] flex flex-col h-svh items-start",
            ),
            id="mobile-nav",
            standard=True,
        ),
    )


def format_title(str: str):
    if "-" in str:
        words = str.split("-")
        cw = [word.capitalize() for word in words]
        formatted = " ".join(cw)
        return formatted
    res = str.capitalize()
    return res


link_groups = {
    "getting-started": ("installation", "tailwind-setup"),
    "components": (
        "card",
        "alert",
        "switch",
        "badge",
        "separator",
        "progress",
        "toast",
        "dialog",
        "button",
        "input",
        "textarea",
        "label",
        "table",
        "checkbox",
        "select",
        "sheet",
        "carousel",
        "slider",
        "tabs",
    ),
}


def NavItem(title, i):
    return (
        A(
            Button(
                format_title(
                    i,
                ),
                variant="link",
                cls="link-btn w-full tracking-tight !justify-start mt-2 !p-0 h-fit !text-muted-foreground text-sm tracking-tight !items-start",
            ),
            href=f"/{title}/{i}",
            hx_boost="true",
        ),
    )


def RenderNav():
    nav_items = []
    link_titles = link_groups.keys()
    for title in link_titles:
        link_group = (
            (
                (
                    (
                        Li(
                            H1(
                                format_title(title),
                                cls="font-semibold tracking-tight",
                            ),
                            Ul(
                                *[
                                    Li(
                                        NavItem(title, i),
                                    )
                                    for i in sorted(link_groups[title])
                                ],
                            ),
                        )
                    ),
                ),
            ),
        )
        nav_items += link_group
    return Ul(*nav_items, cls="space-y-2")


def Sidebar():
    return (
        Aside(
            Div(
                A(
                    H1(
                        "Shad4FastHtml",
                        cls="text-xl font-bold tracking-tighter select-none",
                    ),
                    href="/",
                    hx_boost="true",
                ),
                Span(
                    Badge("Version 1.0", variant="outline"),
                ),
                cls="flex flex-col justify-center gap-1 items-center",
            ),
            Separator(),
            Div(
                Div(
                    RenderNav(),
                    cls="w-full min-h-full",
                ),
                cls="flex flex-col overflow-x-hidden no-scrollbar overflow-y-scroll overscroll-y-contain w-full max-h-[calc(100vh-4rem)]",
            ),
            Separator(),
            source_code(),
            cls="hidden sm:flex fixed flex-col gap-2 items-start h-screen top-0 inset-x-0 border-r w-[180px] pl-6 pt-6",
        ),
    )


def DocsLayout(*c, title: str):
    name = format_title(title)
    return (
        Main(
            Section(
                Article(
                    H1(
                        name,
                        cls="text-4xl font-semibold tracking-tight text-center",
                    ),
                    *c,
                    cls="space-y-8",
                ),
                cls="max-w-4xl container my-14",
            ),
            cls="flex flex-col sm:ml-[180px]",
        ),
    )


def render_md(link):
    css = ".markdown-body{pre {position:relative; .copy-button{position:absolute;}} background-color:transparent} :host { display: block; position: relative; contain: content; } :host([hidden]) { display: none; }"
    css_template = Template(
        Link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.6.1/github-markdown-light.min.css",
            cls="light-theme",
        ),
        Link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.6.1/github-markdown-dark.min.css",
            media="(prefers-color-scheme: dark)",
            cls="dark-theme",
        ),
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@11/styles/github.min.css",
            cls="light-theme",
        ),
        Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/@highlightjs/cdn-assets@11/styles/github-dark.min.css",
            media="(prefers-color-scheme: dark)",
            cls="dark-theme",
        ),
        Style(css),
    )

    with open(f"{link}.md") as f:
        content = f.read()
    return Zero_md(
        css_template,
        Script(
            content,
            type="text/markdown",
        ),
    )


@rt("/getting-started/{title}")
def get(title: str):
    content = f"docs/md/{title}"
    print(content)
    if title == "installation":
        content = "README"
    name = format_title(title)
    return (
        Title(name),
        Body(
            Sidebar(),
            MobileHeader(),
            DocsLayout(
                Div(
                    render_md(content),
                ),
                title=title,
            ),
            cls="pt-[50px] sm:p-0",
        ),
    )


demo_comps = {
    "card": card_block,
    "select": select_block,
    "alert": alert_block,
    "toast": toast_block,
    "separator": separator_block,
    "badge": badge_block,
    "button": button_block,
    "progress": progress_block,
    "dialog": dialog_block,
    "input": input_block,
    "label": label_block,
    "tabel": table_block,
    "checkbox": checkbox_block,
    "switch": switch_block,
    "lucide": lucide_block,
    "textarea": textarea_block,
    "table": table_block,
    "sheet": sheet_block,
    "carousel": carousel_block,
    "slider": slider_block,
    "tabs": tabs_block,
}

@rt("/components/{title}")
def get(title: str):
    name = format_title(title)
    comp = demo_comps[title]
    return (
        Title(name),
        Body(
            Sidebar(),
            MobileHeader(),
            DocsLayout(
                Div(
                    H2(
                        "Demo",
                        cls="text-2xl font-semibold tracking-tight h-full border-b pb-1.5 mb-4",
                    ),
                    comp(),
                    render_md(f"docs/md/{title}_template"),
                    cls="flex flex-col gap-6",
                ),
                title=title,
            ),
            cls="pt-[50px] sm:p-0",
        ),
    )


@rt("/toast")
def get(sess):
    toast(sess=sess, title="Sent!", description="Email has been sent successfully.")


progress = 0


def ProgressBar(progress):
    return Progress(
        value=progress,
        hx_trigger="every 500ms",
        hx_target="this",
        hx_get="/progress",
        hx_swap="outerHTML",
        id="progress-bar",
    )


@rt("/start")
def post():
    global progress
    progress = 0
    return ProgressBar(progress)


@rt("/progress")
def get():
    global progress
    progress += random.randint(5, 25)
    if progress >= 100:
        return Div(
            Button(
                "Restart",
                hx_post="/start",
                cls="max-w-fit",
                hx_swap="innerHTML",
                hx_target="#progress-container",
            ),
            H2("Complete", cls="text-lg font-semibold tracking-tight"),
            cls="flex flex-col items-center justify-center gap-4",
            id="progress-bar",
        )

    return ProgressBar(progress)

serve()
