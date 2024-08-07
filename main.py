from fasthtml.common import *
from shadcn import *

app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(),),
    live=True,
    debug=True,
    htmlkw={"data-theme": "light"},
)


@rt("/")
def get():
    return Main(
        H1(
            "Shadcn-ui styled components for FastHTML",
            cls="text-6xl my-6 font-bold tracking-loose text-center",
        ),
        Section(
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
                        onclick="toggleTheme()",
                    ),
                    Button("Submit"),
                    cls="flex w-full justify-end gap-2",
                ),
            ),
            Card(
                CardHeader(
                    CardTitle("New Card :)"), CardDescription("This is a new card :0")
                ),
                CardContent(P("Lots of awesome content aka oanwdo woadn owndiaonwi")),
                CardFooter(
                    P(
                        "This is the footer :D",
                        cls="text-muted-foreground text-center text-sm",
                    ),
                ),
                standard=True,
            ),
            Alert(
                title="Error",
                variant="destructive",
                description="Your session has expired. Please log in again.",
                icon=True,
            ),
            cls="flex flex-col gap-6 p-8",
        ),
    )


serve()
