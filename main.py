from fasthtml.common import *
from shadcn import *

app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(),),
    live=True,
    debug=True,
    htmlkw={"cls": "dark"},
)


@rt("/")
def get():
    return Title("Shadcn components in FastHtml"), Main(
        Header(
            H1(
                "Shadcn-ui components, made for FastHtml",
                cls="text-6xl font-bold tracking-loose text-center",
            ),
            cls="py-6",
        ),
        Section(
            Div(
                H1(
                    "Click this button to change the theme",
                    cls="text-2xl text-muted-foreground",
                ),
                Lucide(icon="chevron-right", cls="size-7 text-muted-foreground"),
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
                ),
                cls="flex justify-center items-center p-6 gap-1.5",
            ),
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
            ),
            Card(
                CardHeader(
                    CardTitle("New Card :)"), CardDescription("This is a new card :0")
                ),
                CardContent(
                    P("Lots of awesome content aka oanwdo woadn owndiaonwi"),
                    I(**{"data-lucide": "x"}),
                ),
                CardFooter(
                    P(
                        "This is the footer :D",
                        cls="text-muted-foreground text-center text-sm",
                    ),
                ),
                standard=True,
            ),
            Alert(
                Lucide(icon="chevrons-right", cls="size-4"),
                AlertTitle("New message!"),
                AlertDescription("Open your messages section to view more details."),
                standard=True,
            ),
            Alert(
                title="Error",
                variant="destructive",
                description="Your session has expired. Please log in again.",
            ),
            cls="flex flex-col gap-6 p-8",
        ),
    )


@rt("/{prevIcon}")
def get(prevIcon: str):
    newIcon = ""
    if prevIcon == "sun":
        newIcon = "moon"
    if prevIcon == "moon":
        newIcon = "sun"
    return (
        Button(
            Lucide(
                icon=newIcon,
                cls="size-6",
                id="theme-toggle-icon",
            ),
            size="icon",
            variant="outline",
            onclick="toggleTheme()",
            hx_swap="outerHTML",
            hx_get=f"/{newIcon}",
        ),
    )


serve()
