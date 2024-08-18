from docs.comp_demos import (
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
    switch_block,
    table_block,
    textarea_block,
    toast_block,
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
)

favicon_headers = Favicon(
    light_icon="/public/light_favicon.ico", dark_icon="/public/dark_favicon.ico"
)

app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(), HighlightJS(), zeromd_headers, social_headers, favicon_headers),
)

toast_setup(app)


@rt("/")
def get():
    return (
        Title("Shadcn components in FastHtml"),
        Body(
            Header(
                H1(
                    "Shadcn-ui components, made for FastHtml",
                    cls="relative text-6xl font-bold tracking-tight text-center",
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
                    ),
                    cls="flex container max-w-md p-2 my-6 gap-4 justify-between border rounded-xl shadow-md",
                ),
                cls="flex flex-col text-balance ",
            ),
            Div(
                H1(
                    "Click this button to change the theme",
                    cls="text-lg text-muted-foreground",
                ),
                Lucide(
                    icon="arrow-right",
                    cls="size-5 min-w-max text-muted-foreground",
                ),
                ThemeToggle(cls="shrink-0"),
                cls="container flex justify-center items-center gap-1.5",
            ),
            cls="max-w-4xl container min-h-screen flex flex-col justify-center items-center",
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
    "getting-started": ("installation",),
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
        "lucide",
        "input",
        "textarea",
        "label",
        "switch",
        "table",
        "checkbox",
        "select",
    ),
}


def Sidebar():
    nav_items = []
    link_titles = link_groups.keys()
    for title in link_titles:
        link_group = (
            (
                Li(
                    H1(
                        format_title(title),
                        cls="font-semibold tracking-tight text-md pb-1",
                    ),
                    Ul(
                        *[
                            Li(
                                A(
                                    Button(
                                        format_title(i),
                                        variant="link",
                                        cls="w-full !justify-start !text-muted-foreground tracking-tight !p-0 pl-2 h-fit my-1.5",
                                    ),
                                    href=f"/{title}/{i}",
                                    hx_boost="true",
                                ),
                            )
                            for i in link_groups[title]
                        ],
                    ),
                )
            ),
        )

        nav_items += link_group
    return Aside(
        Nav(
            A(
                Button(
                    Lucide(icon="arrow-left", cls="size-4 mr-1.5"),
                    "Home",
                    variant="ghost",
                    cls="w-full !justify-start pl-0",
                ),
                href="/",
                hx_boost="true",
            ),
            Ul(*nav_items, cls="space-y-2"),
            cls="space-y-4",
        ),
        cls="fixed h-screen top-0 inset-x-0 border-r w-[180px] p-6",
    )


def DocsLayout(*c, title: str):
    name = format_title(title)
    return Title(name), Body(
        Sidebar(),
        Main(
            Section(
                Article(H1(name, cls="text-3xl font-bold"), *c, cls="space-y-8"),
                cls="max-w-4xl container my-14",
            ),
            cls="flex flex-col pl-[180px] flex-grow",
        ),
        cls="min-h-screen flex flex-col",
    )


def render_md(link):
    css = ".markdown-body {background-color: unset !important; color: unset !important; margin: 2rem auto;}"
    css_template = Template(Style(css), data_append=True)

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
    return DocsLayout(
        Div(
            render_md("README"),
        ),
        title=title,
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
}


@rt("/components/{title}")
def get(title: str):
    comp = demo_comps[title]
    return DocsLayout(
        Div(
            comp(),
            render_md(f"docs/md/{title}_template"),
        ),
        title=title,
    )


@rt("/toast")
def get(sess):
    toast(sess=sess, title="Sent!", description="Email has been sent successfully.")


@rt("/modal")
def get():
    return Dialog(
        Div(
            P(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam fringilla viverra orci, non ullamcorper quam rhoncus eget. Proin finibus turpis a sapien egestas eleifend.",
                cls="text-pretty",
            ),
            cls="sm:max-w-[425px]",
        ),
        title="Dialog example",
        description="Click the 'x' or anywhere outside the dialog to close.",
        footer=P(
            "Powered by htmx, fasthtml, and vanillaJS",
            cls="text-center text-sm text-muted-foreground tracking-tight w-full",
        ),
    )


@rt("/{fname:path}.{ext:static}")
async def get(fname: str, ext: str):
    return FileResponse(f"public/{fname}.{ext}")


@rt("/modal-standard")
def get():
    return Dialog(
        DialogContent(
            DialogHeader(
                DialogTitle("Edit Profile"),
                DialogDescription(
                    "Make changes to your profile here. Click save when you're done."
                ),
            ),
            Div(
                Div(
                    Label("Name", cls="text-right"),
                    Input(
                        value="John",
                        cls="col-span-3",
                        autofocus="true",
                        onfocus="this.select()",
                    ),
                    cls="grid grid-cols-4 items-center gap-4",
                ),
                Div(
                    Label("Email", cls="text-right"),
                    Input(type="email", value="john@gmail.com", cls="col-span-3"),
                    cls="grid grid-cols-4 items-center gap-4",
                ),
                cls="grid gap-4 py-4",
            ),
            DialogFooter(Button("Save changes")),
            cls="sm:max-w-[425px]",
        ),
        standard=True,
    )


serve()
