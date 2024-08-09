import uuid

from fasthtml.common import *
from shadcn import *

HtmxStyles = Style(
    """
    @keyframes fade-in {
     from { opacity: 0; }
   }

   @keyframes fade-out {
     to { opacity: 0; }
   }

   @keyframes slide-to-right {
     from { transform: translateX(-90px); }
   }

    @keyframes slide-from-right {
     from { transform: translateX(90px); }
   }

   .slide-it {
     view-transition-name: slide-it;
   }

   ::view-transition-old(slide-it) {
     animation: 180ms cubic-bezier(0.4, 0, 1, 1) both fade-out,
     600ms cubic-bezier(0.4, 0, 0.2, 1) both slide-to-right;
   }
   ::view-transition-new(slide-it) {
     animation: 420ms cubic-bezier(0, 0, 0.2, 1) 90ms both fade-in,
     600ms cubic-bezier(0.4, 0, 0.2, 1) both slide-to-right;
   }"""
)

app, rt = fast_app(
    pico=False,
    hdrs=(
        ShadHead(),
        HighlightJS(langs=["python"]),
    ),
    live=True,
    debug=True,
    htmlkw={"cls": "dark"},
)

setup_toasts(app)

code = {
    "card1": """Card(
    Input(
        type="text",
        placeholder="Enter some text...",
        ),
    title="Create a post",
    description="Enter your post related information below",
    footer=Div(
        Button(
            "Cancel",
            variant="outline",
            ),
        Button("Submit"),
            cls="flex w-full justify-end gap-2",
            ),
            cls="w-[90%]",
        ),""",
    "card2": """Card(
    CardHeader(
        CardTitle("New Card!"),
        CardDescription("This is a new card :0"),
    ),
    CardContent(
        P("Lots of awesome content aka oanwdo woadn
        owndiaonwi. wodn wodin donwd onida ondwoai",
        cls="text-balance",
        ),
    ),
    CardFooter(
        P("This is the footer :D",
            cls="text-muted-foreground text-center 
            text-sm",
        ),
    ),
    cls="w-[90%]",
    standard=True,
)
""",
    "alert1": """Alert(
    Lucide(icon="chevrons-right", cls="size-4"),
    AlertTitle("New message!"),
    AlertDescription(
        "Open your messages section to view more details."
    ),
    standard=True,
    cls="max-w-[90%]",
)
""",
    "alert2": """Alert(
    title="Error",
    variant="destructive",
    description="Your session has expired. Please log in again.",
    cls="max-w-[90%]",
)
""",
    "separator": """H1(
    "Welcome back",
    cls="text-3xl font-bold tracking-tight leading-loose",
    ),
    Separator(cls="my-2 max-w-[90%]"),
    Div(
        Button("Profile", variant="secondary"),
        Separator(orientation="vertical"),
        Button("Messages", variant="secondary"),
        Separator(orientation="vertical"),
        Button("Settings", variant="secondary"),
        cls="flex gap-3 p-3",
    ),
""",
    "badge": """Div(
    H1(
        "Shad4FastHtml",
        cls="text-2xl font-semibold tracking-tight leading-loose",
    ),
    Badge("v2.0", variant="default"),
    cls="flex gap-1.5 items-center justify-center",
),
""",
}

state = {
    "card1": False,
    "card2": False,
    "alert1": False,
    "alert2": False,
    "toast1": False,
    "separator": False,
    "badge": False,
}


def Block(*c, name=None, id="default", **kwargs):
    cls = "relative mx-auto w-full max-w-xl flex flex-col rounded-md bg-muted/40 shadow"
    if name == None:
        return (
            Div(
                Div(
                    *c,
                    cls="flex flex-col items-center h-[350px] justify-center",
                ),
                BlockChange(target=id),
                cls=cls,
                id=id,
                **kwargs,
            ),
        )

    title = Div(
        H1(
            name,
            cls="text-3xl font-semibold text-muted-foreground tracking-tight leading-loose",
        ),
        cls="flex items-center justify-center",
    )
    return Article(
        title,
        Div(
            Div(
                *c,
                cls="flex flex-col items-center h-[350px] justify-center",
            ),
            BlockChange(target=id),
            cls=cls,
            id=id,
            **kwargs,
        ),
    )


def BlockChange(target: str):
    icon = "arrow-right"
    if state[target] == True:
        icon = "arrow-left"
    return (
        Button(
            Lucide(icon=icon, cls="size-8 text-muted-foreground"),
            variant="outline",
            size="icon",
            cls="flex w-full py-8",
            hx_target=f"#{target}",
            hx_swap="outerHTML transition:true",
            hx_get=f"/switch/{target}",
        ),
    )


def CodeBlock(id: str = None):
    return (
        Block(
            Div(
                Pre(
                    Code(
                        code[id],
                        cls="text-sm rounded-md bg-muted text-foreground h-[318px]",
                    ),
                    cls="flex",
                ),
                cls="flex items-center justify-center w-full p-4 flex-grow",
            ),
            id=id,
        ),
    )


@rt("/")
def get():
    return Title("Shadcn components in FastHtml"), Main(
        Header(
            H1(
                "Shadcn-ui components, made for FastHtml",
                cls="text-6xl font-bold tracking-tight text-center",
            ),
            cls="pt-20 text-balance",
        ),
        Section(
            Div(
                H1(
                    "Click this button to change the theme",
                    cls="text-2xl text-muted-foreground",
                ),
                Lucide(
                    icon="arrow-right",
                    cls="size-8 min-w-max text-muted-foreground",
                ),
                Button(
                    Lucide(
                        icon="sun",
                        cls="size-6",
                        id="theme-toggle-icon",
                    ),
                    size="icon",
                    variant="outline",
                    onclick="toggleTheme()",
                    hx_swap="outerHTML",
                    hx_get="/sun",
                    cls="flex-none",
                ),
                cls="flex justify-center items-center py-6 gap-1.5",
            ),
            Block(
                Card(
                    Input(
                        type="text",
                        placeholder="Enter some text...",
                    ),
                    title="Create a post",
                    description="Enter your post related information below",
                    footer=Div(
                        Button(
                            "Cancel",
                            variant="outline",
                        ),
                        Button("Submit"),
                        cls="flex w-full justify-end gap-2",
                    ),
                    cls="w-[90%]",
                ),
                name="Card",
                id="card1",
            ),
            Block(
                Card(
                    CardHeader(
                        CardTitle("New Card :)"),
                        CardDescription("This is a new card :0"),
                    ),
                    CardContent(
                        P(
                            "Lots of awesome content aka oanwdo woadn owndiaonwi. wodn wodin donwd onida ondwoai",
                            cls="text-balance",
                        ),
                    ),
                    CardFooter(
                        P(
                            "This is the footer :D",
                            cls="text-muted-foreground text-center text-sm",
                        ),
                    ),
                    cls="w-[90%]",
                    standard=True,
                ),
                name="Card: Standard",
                id="card2",
            ),
            Block(
                Alert(
                    title="Error",
                    variant="destructive",
                    description="Your session has expired. Please log in again.",
                    cls="!w-[90%]",
                ),
                id="alert1",
                name="Alert",
            ),
            Block(
                Alert(
                    Lucide(icon="chevrons-right", cls="size-4"),
                    AlertTitle("New message!"),
                    AlertDescription(
                        "Open your messages section to view more details."
                    ),
                    standard=True,
                    cls="!w-[90%]",
                ),
                id="alert2",
                name="Alert: Standard",
            ),
            Block(
                Button("Add email", hx_get="/toast", hx_swap="none"),
                name="Toast",
                id="toast1",
            ),
            Block(
                H1(
                    "Welcome back",
                    cls="text-3xl font-bold tracking-tight leading-loose",
                ),
                Separator(cls="my-2 max-w-[90%]"),
                Div(
                    Button("Profile", variant="secondary"),
                    Separator(orientation="vertical"),
                    Button("Messages", variant="secondary"),
                    Separator(orientation="vertical"),
                    Button("Settings", variant="secondary"),
                    cls="flex gap-3 p-3",
                ),
                name="Separator",
                id="separator",
            ),
            Block(
                Div(
                    H1(
                        "Shad4FastHtml",
                        cls="text-2xl font-semibold tracking-tight leading-loose",
                    ),
                    Badge("v2.0"),
                    cls="flex gap-1.5 items-center justify-center",
                ),
                name="Badge",
                id="badge",
            ),
            render_toasts,
            cls="flex flex-col gap-6 p-8",
        ),
        cls="max-w-4xl container",
    )


@rt("/toast")
def get(session):
    if "id" not in session:
        session["id"] = str(uuid.uuid4())
    add_toast(session, typ="info", message="WORKED!")


@rt("/{prevIcon}")
def get(prevIcon: str):
    newIcon = ""
    if prevIcon == "sun":
        newIcon = "moon"
    if prevIcon == "moon":
        newIcon = "sun"
    return (
        Button(
            Lucide(icon=newIcon, cls="size-6", id="theme-toggle-icon"),
            size="icon",
            variant="outline",
            onclick="toggleTheme()",
            hx_swap="outerHTML",
            hx_get=f"/{newIcon}",
            cls="flex-none",
        ),
    )


@rt("/switch/{id}")
def get(id: str):
    if id == "alert1":
        if not state[id]:
            state[id] = True
            return CodeBlock(id)
        else:
            state[id] = False
            return (
                Block(
                    Alert(
                        title="Error",
                        variant="destructive",
                        description="Your session has expired. Please log in again.",
                        cls="!w-[400px]",
                    ),
                    id=id,
                ),
            )
    if id == "alert2":
        if not state[id]:
            state[id] = True
            return CodeBlock(id)
        else:
            state[id] = False
            return Block(
                Alert(
                    Lucide(icon="chevrons-right", cls="size-4"),
                    AlertTitle("New message!"),
                    AlertDescription(
                        "Open your messages section to view more details."
                    ),
                    standard=True,
                    cls="!w-[400px]",
                ),
                id=id,
            )
    if id == "card1":
        if not state[id]:
            state[id] = True
            return CodeBlock(id)
        else:
            state[id] = False
            return Block(
                Card(
                    Input(
                        type="text",
                        placeholder="Enter some text...",
                    ),
                    title="Create a post",
                    description="Enter your post related information below",
                    footer=Div(
                        Button(
                            "Cancel",
                            variant="outline",
                        ),
                        Button("Submit"),
                        cls="flex w-full justify-end gap-2",
                    ),
                    cls="w-[400px]",
                ),
                id=id,
            )
    if id == "card2":
        if not state[id]:
            state[id] = True
            return CodeBlock(id)
        else:
            state[id] = False
            return (
                Block(
                    Card(
                        CardHeader(
                            CardTitle("New Card :)"),
                            CardDescription("This is a new card :0"),
                        ),
                        CardContent(
                            P(
                                "Lots of awesome content aka oanwdo woadn owndiaonwi. wodn wodin donwd onida ondwoai",
                                cls="text-balance",
                            ),
                        ),
                        CardFooter(
                            P(
                                "This is the footer :D",
                                cls="text-muted-foreground text-center text-sm",
                            ),
                        ),
                        standard=True,
                        cls="w-[400px]",
                    ),
                    id=id,
                ),
            )
    if id == "separator":
        if not state[id]:
            state[id] = True
            return CodeBlock(id)
        else:
            state[id] = False
            return (
                Block(
                    H1(
                        "Welcome back",
                        cls="text-3xl font-bold tracking-tight leading-loose",
                    ),
                    Separator(cls="my-2 max-w-[90%]"),
                    Div(
                        Button("Profile", variant="secondary"),
                        Separator(orientation="vertical"),
                        Button("Messages", variant="secondary"),
                        Separator(orientation="vertical"),
                        Button("Settings", variant="secondary"),
                        cls="flex gap-3 p-3",
                    ),
                    id="separator",
                ),
            )
    if id == "badge":
        if not state[id]:
            state[id] = True
            return CodeBlock(id)
        else:
            state[id] = False
            return (
                Block(
                    Div(
                        H1(
                            "Shad4FastHtml",
                            cls="text-2xl font-semibold tracking-tight leading-loose",
                        ),
                        Badge("v2.0", variant="default"),
                        cls="flex gap-1.5 items-center justify-center",
                    ),
                    id="badge",
                ),
            )
    return H1("Didnt work :()")


serve()
