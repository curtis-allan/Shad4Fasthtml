import random
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
    radio_block,
    avatar_block,
    aspect_ratio_block,
    scroll_area_block,
)
from fasthtml.common import *
from fasthtml.components import Zero_md
from shad4fast import *
from lucide_fasthtml import Lucide


link_groups = {
    "getting-started": (
        "installation",
        "tailwind-setup",
        "theme-config",
        "shad4fast-example",
        "ai-assistance",
    ),
    "components": (
        "card",
        "aspect-ratio",
        "avatar",
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
        "scroll-area",
        "carousel",
        "slider",
        "tabs",
        "radio",
    ),
}

zeromd_headers = Script(
    type="module", src="https://cdn.jsdelivr.net/npm/zero-md@3?register"
)

social_headers = Socials(
    site_name="Shad4FastHtml",
    title="Shad4FastHtml",
    description="Open source Shadcn-ui components, made for FastHtml",
    url="www.shad4fasthtml.com",
    image="/public/social.webp",
    card="summary_large_image",
)

favicon_headers = Favicon(
    light_icon="/public/light_favicon.ico", dark_icon="/public/dark_favicon.ico"
)

app, rt = fast_app(
    pico=False,
    hdrs=(
        ShadHead(theme_handle=True),
        zeromd_headers,
        social_headers,
        favicon_headers,
        ScriptX(fname="md_theme.js"),
    ),
    htmlkw={"lang": "en"},
)

app.static_route(".md", prefix="/docs",static_path="docs/md")

app.static_route(".py", prefix="/docs/demos", static_path="docs")

toast_setup(app)


def MobileHeader():
    return Div(
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
        cls="sm:hidden sticky flex top-0 z-50 items-center justify-between bg-background w-full px-4 py-2 shadow dark:shadow-border",
        tabindex="-1",
    )


def source_button():
    return Span(
        A(
            Button(
                Lucide(icon="github", cls="mr-2 size-5"),
                "Source",
                variant="outline",
                cls="w-full",
            ),
            href="https://github.com/curtis-allan/shadcn-fasthtml-framework",
            target="_blank",
            cls="w-full",
        ),
        cls="w-full flex justify-center items-center px-2",
    )


def carousel_items():
    carousel_items = ()
    for i in range(4):
        i += 1
        carousel_items += (
            Card(
                Div(cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"),
                title=f"Card {i}",
                description=f"Carousel demo card #{i}",
                footer=Badge(
                    "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                ),
            ),
        )
    return carousel_items


@rt("/")
def get():
    return (
        Title("Shad4Fast"),
        Body(
            Main(
                Section(
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
                            ),
                            cls="flex container max-w-md p-2 my-6 gap-4 justify-between border rounded-xl shadow-md",
                        ),
                        cls="flex flex-col text-balance max-w-3xl",
                    ),
                    cls="flex flex-col grow justify-center gap-4 items-center container h-full",
                ),
                cls="h-screen flex flex-col",
            ),
        ),
    )


def MobileNav():
    return (
        Sheet(
            SheetTrigger(
                Lucide(icon="menu"),
                variant="outline",
                size="icon",
            ),
            SheetContent(
                SheetHeader(
                    SheetTitle(
                        "Documentation",
                        cls="tracking-tight select-none",
                    ),
                    Badge(
                        "v1.2",
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
                    cls="overflow-hidden w-full grid grow max-h-[calc(100vh-8rem)]",
                ),
                Separator(),
                SheetFooter(
                    source_button(),
                ),
                side="left",
                cls="w-[215px] flex flex-col h-full",
            ),
            id="mobile-nav",
            standard=True,
        ),
    )


def format_title(str: str):
    if "-" or "_" in str:
        words = str.split("-") or str.split("_")
        cw = [word.capitalize() for word in words]
        formatted = " ".join(cw)
        return formatted
    res = str.capitalize()
    return res


def NavItem(title, i):
    return (
        A(
            Button(
                format_title(
                    i,
                ),
                variant="link",
                data_link=i,
                data_ref_navlink=True,
                cls="w-full sheet-close-button tracking-tight !justify-start mt-2 !p-0 !pl-6 h-fit !text-muted-foreground text-sm !items-start data-[state=active]:border-r-2 data-[state=active]:border-primary data-[state=active]:font-semibold data-[state=active]:rounded-none data-[state=active]:!text-accent-foreground",
            ),
            href=f"/{title}/{i}",
            hx_boost="true",
            hx_select="#docs-layout",
            target_id="docs-layout",
            hx_swap="outerHTML show:window:top",
        ),
    )


def RenderNav():
    nav_items = []
    link_titles = link_groups.keys()
    for title in link_titles:
        link_group = Li(
            H1(
                format_title(title),
                cls="font-semibold pl-5 tracking-tight",
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
                    Badge("Version 1.2", variant="outline"),
                ),
                cls="flex flex-col justify-center gap-1 items-center",
            ),
            Separator(),
            Div(
                Div(
                    RenderNav(),
                    cls="w-full min-h-full",
                ),
                cls="flex flex-col overflow-x-hidden overflow-y-scroll no-scrollbar overscroll-y-contain w-full h-full",
            ),
            Separator(),
            Span(
                source_button(),
                ThemeToggle(cls="shrink-0"),
                cls="w-full flex items-center gap-2 justify-center pr-2 pt-1",
            ),
            cls="hidden sm:flex fixed flex-col gap-2 items-center overflow-hidden h-screen top-0 inset-x-0 border-r w-[180px] pt-6 pb-2 m-0",
            id="sidebar",
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
            id="docs-layout",
        ),
    )


def render_md(link):
    if "-" in link:
        link = link.replace("-", "_")
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
        ),
    )


@rt("/components/{title}")
def get(title: str):
    name = format_title(title)
    return (
        (
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
                        globals()[f"{title.replace('-', '_')}_block"](),
                        render_md(f"docs/md/{title}_template"),
                        cls="flex flex-col gap-6",
                    ),
                    title=title,
                ),
            ),
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

def tid(id):
    return f"todo-{id}"

def edit_dialog(todo_id: int):
    edit = DialogTrigger(
        "Edit",
        hx_get=f"/example/edit/{todo_id}",
        target_id=f"edit-form-{todo_id}",
        hx_swap="outerHTML",
        variant="outline",
    )
    return Dialog(
        Div("Loading...", id=f"edit-form-{todo_id}"),
        trigger=edit,
        title="Edit Todo",
        description="Edit the todo item. Click the 'Save' button to save it.",
    )

def render_todo(todo):
    priority_cls = {
        "low": "",
        "medium": "bg-yellow-500/80",
        "high": "bg-red-500/80",
    }
    delete = Button(
       "Delete",
        hx_delete=f"/example/todos/{todo['id']}",
        target_id=tid(todo['id']),
        hx_swap="outerHTML",
        variant="destructive",
    )
    status_cls = "absolute top-1.5 right-1"
    checked = Badge(
        Lucide("check", stroke_width="3", cls="size-4 text-primary"),
        cls=f"!bg-green-600 text-primary {status_cls} {'invisible' if not todo['done'] else ''}",
    )

    return Card(
        CardHeader(
            checked,
            CardTitle(todo['title']),
            Div(
                "Priority level: ",
                Badge(
                    todo['priority'].title() if todo['priority'] else "Low",
                    variant="outline",
                    cls=f"{priority_cls[todo['priority']] if todo['priority'] else ''} w-fit",
                ),
                cls="flex items-center gap-1 text-muted-foreground text-sm pt-2",
            ),
        ),
        CardContent(
            P(todo['description'], cls="tracking-tight text-sm text-pretty line-clamp-3"),
            cls="grow",
        ),
        CardFooter(
              Div(
                delete,
                edit_dialog(todo_id=todo['id']),
                cls="flex items-center p-2 w-full justify-between self-end",
            ),
        ),
        cls="relative flex flex-col",
        standard=True,
        id=tid(todo['id']),
    )

def title_input(id=None, **kw):
    return Div(
        Label("Title", htmlFor=id),
        Input(
            id=id,
            name="title",
            placeholder="Enter a todo title",
             required=True,
        ),
        cls="space-y-1",
        id="title-block",
        **kw,
    )

def description_input(id=None, **kw):
    return Div(
        Label("Description", htmlFor=id),
        Textarea(
            id=id,
            name="description",
            placeholder="Enter a todo description",
            cls="resize-none",
            required=True,
        ),
        cls="space-y-1",
        id="description-block",
        **kw,
    )

def priority_input(**kw):
    return Div(
        Label(
            "Priority",
            Select(
                label="Priority",
                placeholder="Select a level of urgency",
                name="priority",
                items=["Low", "Medium", "High"],
                id="priority-select",
                cls="mt-1",
                default_value="high",
            ),
        ),
        id="priority-block",
        **kw,
    )

@rt("/example")
def get(sess):
    sess["todos"] = []
    sess["id_counter"] = 0
    todos = []
    add = Card(
        Form(
            title_input(id="new-title"),
            description_input(id="new-description"),
            priority_input(),
            Button(
                 "Add",
                cls="w-full !mt-6",
            ),
            hx_post="/example",
            target_id="todo-list",
            hx_swap="afterbegin",
            cls="px-4 space-y-3",
            id="todo-form",
        ),
        title="Create a Todo",
        description="Add a new todo item to your list. Click the 'Add' button to save it.",
        cls="w-full",
    )
    content = Div(
        id="todo-list",
        cls="grid sm:grid-cols-2 auto-rows-fr gap-3 w-full",
    )
    return Title("Todo list"), Body(
        H1(
            "Todo List - Shad4Fast",
            cls="text-4xl tracking-tighter font-semibold mt-10 text-center",
        ),
        Section(
            add,
            H1("Your Todos:", cls="text-3xl tracking-tight font-bold"),
            Separator(),
            content,
            cls="container max-w-4xl flex flex-col gap-4 items-center",
        ),
        cls="flex flex-col min-h-screen items-center gap-10 p-4",
    )


@rt("/example/todos/{id}")
def delete(id: int, sess):
    todos = [todo for todo in sess.get("todos") if todo['id'] != id]
    sess["todos"].pop(id)

@rt("/example")
def post(sess, title: str, description: str, priority: str):
    todos = sess.get("todos")
    id_counter = sess.get("id_counter")
    id_counter += 1
    new_todo = {
        'id': id_counter,
        'title': title,
        'description': description,
        'priority': priority,
        'done': False
    }
    todos.append(new_todo)
    sess["todos"].append(new_todo)
    sess["id_counter"] = id_counter
    return (
        render_todo(new_todo),
        title_input(id="new-title", hx_swap_oob="true"),
        description_input(id="new-description", hx_swap_oob="true"),
        priority_input(hx_swap_oob="true"),
    )

@rt("/example/edit/{id}")
def get(id: int, sess):
    todo = next((todo for todo in sess.get("todos") if todo['id'] == id), None)
    if not todo:
        return "Todo not found", 404
    
    res = Form(
        Div(
            title_input(id="edit-title"),
            description_input(id="edit-description"),
            cls="flex flex-col gap-2",
        ),
        Hidden(id="id", value=str(todo['id'])),
        Div(
            Hidden(name="done", value="", skip=True),
            Label("Complete", htmlFor="done"),
            Checkbox(id="done", name="done"),
            cls="flex items-center gap-1.5",
        ),
        DialogClose(
            "Save",
            cls="w-full !mt-6",
        ),
        hx_put="/example",
        target_id=tid(id),
        hx_swap="outerHTML",
        id=f"edit-form-{id}",
        cls="p-2 space-y-6",
    )
    return fill_form(res, todo)


@rt("/example")
def put(sess, id: int, title: str, description: str, done:bool=False):
    for todo in sess.get("todos"):
        if todo['id'] == id:
            todo.update({
                'title': title,
                'description': description,
                'done': done
            })
            return render_todo(todo)
    return "Todo not found", 404


serve()
