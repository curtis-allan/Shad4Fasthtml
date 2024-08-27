import uuid
from docs.comp_code import code_dict, dummy_data
from fasthtml.common import *
from fasthtml.components import Zero_md
from shadcn import *

__all__ = [
    "card_block,carousel_block, select_block,ThemeToggle, alert_block, toast_block, separator_block, badge_block, progress_block, dialog_block, input_block, label_block, table_block, checkbox_block, button_block, lucide_block, textarea_block"
]


def ThemeToggle(variant="outline", cls=None, **kwargs):
    return Button(
        Lucide(icon="sun", id="theme-icon-sun"),
        Lucide(icon="moon", id="theme-icon-moon"),
        variant=variant,
        size="icon",
        cls=f"theme-toggle {cls}",
        **kwargs,
    )


def table_rows():
    results = []
    for i in dummy_data:
        results.append(
            TableRow(
                TableCell(i["invoice"], cls="font-medium"),
                TableCell(i["paymentStatus"]),
                TableCell(i["paymentMethod"]),
                TableCell(i["totalAmount"], cls="text-right"),
            )
        )
    return results


def Block(*c, id="default", name=None, **kwargs):
    header = None
    themeToggle = ThemeToggle(cls="absolute top-0 right-0")
    if name:
        header = H2(
            name,
            cls="text-xl font-semibold tracking-tight absolute top-2 inset-x-0 text-center",
        )

    cls = "relative max-w-xl mx-auto flex flex-col rounded-md bg-muted/40 shadow"
    return Div(
        Div(
            header,
            themeToggle,
            Div(
                *c,
                cls="block-content flex flex-col items-center h-[350px] justify-center",
            ),
            CodeContent(id=id),
            BlockChange(),
            cls=cls,
            id=id,
            **kwargs,
        ),
    )


def BlockChange():
    return (
        Button(
            Lucide(icon="arrow-left-right", cls="size-8 text-muted-foreground"),
            variant="outline",
            cls="flex w-full py-8",
            onclick=f"toggleView(this)",
        ),
        Script(
            """function toggleView(elt) {
                const block = elt.parentNode
                    block.querySelector('.block-content').classList.toggle('hidden');
                    block.querySelector('.code-content').classList.toggle('hidden');
            }"""
        ),
    )


def render_code(content):
    css = ".markdown-body{height:100%; overflow:hidden; pre {code {height:100%; box-sizing:border-box}height:100%;width:100%;box-sizing:border-box;}} :host {height:100%; width:100%; position: relative; contain: content;} :host([hidden]) { display: none; }"
    css_template = Template(
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
        Style(css),
    )

    return Zero_md(
        css_template,
        Script(
            f"```\n{content}\n```",
            type="text/markdown",
        ),
    )


def CodeContent(id: str = None):
    return Div(
        render_code(code_dict[id]),
        cls="code-content flex items-center justify-center h-[350px] hidden ",
    )


def card_block():
    return (
        Block(
            Card(
                Input(type="text", placeholder="Title", id="card1-input"),
                title="Create a post",
                description="Enter your post title below",
                footer=Div(
                    Button(
                        "Cancel",
                        variant="outline",
                    ),
                    Button("Submit"),
                    cls="flex w-full justify-end gap-2",
                ),
                cls="w-[80%]",
            ),
            id="card1",
        ),
    )


def CardAltBlock():
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
                cls="w-[90%]",
                standard=True,
            ),
            id="card2",
        ),
    )


def SelectAltBlock():
    return (
        Block(
            Select(
                SelectTrigger(
                    SelectValue(placeholder="Choose a coding language"),
                    cls="w-[250px]"
                ),
                SelectContent(
                    SelectGroup(
                        SelectLabel("Scripting Languages"),
                        SelectItem("JavaScript", value="javascript"),
                        SelectItem("TypeScript", value="typescript"),
                        SelectItem("Ruby", value="ruby"),
                        SelectItem("Lua", value="lua"),
                        SelectItem("PHP", value="php")
                    ),
                    SelectSeparator(),
                    SelectGroup(
                        SelectLabel("Mobile Development"),
                        SelectItem("Swift", value="swift"),
                        SelectItem("Kotlin", value="kotlin"),
                        SelectItem("Flutter", value="flutter"),
                        SelectItem("React Native", value="react-native"),
                        SelectItem("Xamarin", value="xamarin"),
                        SelectItem("Ionic", value="ionic")
                    ),
                    SelectSeparator(),
                    SelectGroup(
                        SelectLabel("Other Languages"),
                        SelectItem("Go", value="go"),
                        SelectItem("Rust", value="rust"),
                        SelectItem("C#", value="csharp"),
                        SelectItem("Java", value="java"),
                        SelectItem("Scala", value="scala"),
                        SelectItem("Haskell", value="haskell")
                    ),
                    id='select-alt',
                ),
                standard=True,
                id='select-alt',
                name="select-alt"
            ),
            id="select2",
        ),
    )

def select_block():
    return (
        Block(
            Select(
                placeholder="Pick a fruit",
                label="Fruits",
                items=["Apple", "Banana", "Blueberry", "Orange"],
                id="select-demo",
                name="select-demo",
                cls="[&>.select-trigger]:w-[180px]",
            ),
            id="select",
        ),
        H2("Scrolling & Seperators", cls="text-2xl font-semibold tracking-tight h-full border-b pb-1.5 mb-4"),
        SelectAltBlock(),
    )


def AlertAltBlock():
    return (
        Block(
            Alert(
                Lucide(icon="circle-alert", cls="size-4"),
                AlertTitle("Error"),
                AlertDescription("An error occurred while processing your request."),
                standard=True,
                variant="destructive",
                cls="max-w-[80%]",
            ),
            id="alert2",
        ),
    )


def button_block():
    return (
        Block(
            Button("Button"),
            id="button",
        ),
        H2(
            "Variants",
            cls="text-2xl font-semibold tracking-tight h-full border-b pb-1.5 mb-4",
        ),
        ButtonAltBlockVariants(),
        H2(
            "Sizes",
            cls="text-2xl font-semibold tracking-tight h-full border-b pb-1.5 mb-4",
        ),
        ButtonAltBlockSizes(),
        H2(
            "States",
            cls="text-2xl font-semibold tracking-tight h-full border-b pb-1.5 mb-4",
        ),
        ButtonAltBlockStates(),
    )


def ButtonAltBlockVariants():
    return (
        Block(
            Div(
                Button("Default", variant="default"),
                Button("Secondary", variant="secondary"),
                Button("Outline", variant="outline"),
                Button(
                    "Destructive",
                    variant="destructive",
                ),
                Button("Link", variant="link"),
                Button("Ghost", variant="ghost"),
                cls="grid grid-cols-2 sm:grid-cols-3 sm:grid-rows-2 gap-4 max-w-[90%]",
            ),
            id="button2",
        ),
    )


def ButtonAltBlockSizes():
    return (
        Block(
            Div(
                Button("Default", size="default"),
                Button("Small", size="sm"),
                Button("Large", size="lg"),
                Button(
                    Lucide(icon="settings"),
                    size="icon",
                ),
                cls="grid grid-flow-row gap-4 place-items-center auto-rows-auto max-w-[90%]",
            ),
            id="button3",
        ),
    )


def ButtonAltBlockStates():
    return (
        Block(
            Div(
                Span(
                    Label(
                        "Disabled:",
                        htmlFor="button-disabled",
                        cls="text-[15px] font-semibold",
                    ),
                    Button("Submit", id="button-secondary", disabled=True),
                    cls="flex items-center justify-between",
                ),
                Separator(),
                Span(
                    Label(
                        "Loading:",
                        htmlFor="button-loading",
                        cls="text-[15px] font-semibold",
                    ),
                    Button(
                        Lucide(icon="loader2", cls="size-4 mr-1.5 animate-spin"),
                        "Loading",
                        id="button-loading",
                        disabled=True,
                    ),
                    cls="flex items-center justify-between",
                ),
                cls="grid gap-3 w-[215px]",
            ),
            id="button4",
        ),
    )


def lucide_block():
    return Block(H1("Placeholder"), id="lucide")


def alert_block():
    return (
        Block(
            Alert(
                title="New message!",
                description="Open your messages to view more details.",
                cls="max-w-[80%]",
            ),
            id="alert1",
        ),
        H2(
            "Variants",
            cls="text-2xl font-semibold tracking-tight h-full border-b pb-1.5 mb-4",
        ),
        AlertAltBlock(),
    )


def toast_block():
    return (
        Block(
            Button("Send email", hx_get="/toast", hx_swap="none"),
            id="toast",
        ),
    )


def separator_block():
    return (
        Block(
            Div(
                H1(
                    "Welcome back",
                    cls="text-2xl sm:text-3xl font-bold tracking-tight",
                ),
                Separator(cls="my-2"),
                Div(
                    Button("Profile", variant="outline"),
                    Separator(orientation="vertical"),
                    Button("Settings", variant="outline"),
                    cls="flex gap-3 p-3",
                ),
                cls="container flex flex-col max-w-[80%] justify-center items-center",
            ),
            id="separator",
        ),
    )


def badge_block():
    return (
        Block(
            Div(
                H1(
                    "Shad4FastHtml",
                    cls="text-2xl font-semibold tracking-tight",
                ),
                Badge("v2.0"),
                cls="flex gap-1.5 items-center justify-center",
            ),
            id="badge",
        ),
        H2(
            "Variants",
            cls="text-2xl font-semibold tracking-tight h-full border-b pb-1.5 mb-4",
        ),
        BadgeAltBlock(),
    )


def BadgeAltBlock():
    return (
        Block(
            Div(
                Span(
                    Label("Default:", htmlFor="badge-default", cls="font-semibold"),
                    Badge("New Feature", variant="default", id="badge-default"),
                    cls="flex items-center justify-between",
                ),
                Separator(),
                Span(
                    Label("Secondary:", htmlFor="badge-secondary", cls="font-semibold"),
                    Badge("Updated", variant="secondary", id="badge-secondary"),
                    cls="flex items-center justify-between",
                ),
                Separator(),
                Span(
                    Label("Outline:", htmlFor="badge-outline", cls="font-semibold"),
                    Badge("Terms v1.03", variant="outline", id="badge-outline"),
                    cls="flex items-center justify-between",
                ),
                Separator(),
                Span(
                    Label(
                        "Destructive:", htmlFor="badge-destructive", cls="font-semibold"
                    ),
                    Badge("Invalid", variant="destructive", id="badge-destructive"),
                    cls="flex items-center justify-between",
                ),
                cls="flex flex-col gap-3 justify-center w-[180px]",
            ),
            id="badge2",
        ),
    )


def progress_block():
    return (
        Block(
            Div(
                Button(
                    "Start",
                    hx_post="/start",
                    cls="max-w-fit",
                    hx_swap="innerHTML",
                    hx_target="#progress-container",
                ),
                id="progress-container",
                cls="grid place-items-center w-[80%]",
            ),
            id="progress",
        ),
    )

def DialogAltBlock():
    return Block(
        Div(
            DialogTrigger("Toggle Dialog", dialog_id="demo-dialog"),
            Dialog(
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
                            ),
                            cls="grid grid-cols-4 items-center gap-4",
                        ),
                        Div(
                            Label("Email", cls="text-right"),
                            Input(
                                type="email",
                                value="johnsmith@email.com",
                                cls="col-span-3",
                            ),
                            cls="grid grid-cols-4 items-center gap-4",
                        ),
                        cls="grid gap-4 py-4",
                    ),
                    DialogFooter(DialogCloseButton("Save changes")),
                    cls="sm:max-w-[425px]",
                ),
                standard=True,
                id="demo-dialog",
            ),
        ),
        id="dialog2",
    )


def dialog_block():
    return Block(
        Div(
            DialogTrigger("Toggle Dialog", dialog_id="demo-dialog"),
            Dialog(
                Div(
                    Div(
                        Label("Name", cls="text-right"),
                        Input(
                            value="John",
                            cls="col-span-3",
                        ),
                        cls="grid grid-cols-4 items-center gap-4",
                    ),
                    Div(
                        Label("Email", cls="text-right"),
                        Input(
                            type="email",
                            value="johnsmith@email.com",
                            cls="col-span-3",
                        ),
                        cls="grid grid-cols-4 items-center gap-4",
                    ),
                    cls="grid gap-4 py-4",
                ),
                title="Edit Profile",
                description="Make changes to your profile here. Click save when you're done.",
                footer=Div(
                    DialogCloseButton("Save changes"), cls="flex w-full justify-end"
                ),
                id="demo-dialog",
            ),
        ),
        id="dialog",
    )


def label_block():
    return Block(
        Div(
            Label("Email", htmlFor="email"),
            Input(
                placeholder="Enter your email",
                type="email",
                id="email",
            ),
            cls="flex flex-col sm:flex-row gap-1.5 sm:items-center w-full max-w-sm container justify-center items-start",
        ),
        id="label",
    )


def input_block():
    return (
        Block(
            Input(
                placeholder="Enter something",
                type="text",
                id="title",
                cls="max-w-[80%]",
            ),
            id="input",
        ),
    )


def textarea_block():
    return Block(
        Div(
            Label(
                "Content",
                htmlFor="content",
            ),
            Textarea(
                placeholder="Enter some content.",
                cls="col-span-3",
                id="content",
            ),
            cls="space-y-5 max-w-[80%] w-full",
        ),
        id="textarea",
    )


def switch_block():
    return (
        Block(
            Div(
                Label(
                    "Agree to terms",
                    htmlFor="switch-toggle",
                ),
                Switch(
                    id="switch-toggle",
                ),
                cls="flex gap-1.5 items-center",
            ),
            id="switch",
        ),
        H2(
            "Within a form",
            cls="text-2xl font-semibold tracking-tight h-full border-b pb-1.5 mb-4",
        ),
        SwitchFormBlock(),
    )


def SwitchFormBlock():
    return (
        Block(
            Form(
                Div(
                    Label(
                        "Agree to terms",
                        htmlFor="switch-toggle2",
                    ),
                    Switch(
                        id="switch-toggle2",
                        name="switch-toggle2",
                        value="agree",
                    ),
                    cls="flex gap-1.5 items-center",
                ),
                Button("Submit", type="button"),
                cls="flex flex-col gap-4",
            ),
            id="switch2",
        ),
    )


def table_block():
    return (
        Block(
            Div(
                Table(
                    TableCaption("View your recent spending history."),
                    TableHeader(
                        TableRow(
                            TableHead("Payment", cls="w-[100px]"),
                            TableHead("Status"),
                            TableHead("Method"),
                            TableHead("Amount", cls="text-right"),
                        )
                    ),
                    TableBody(*table_rows()),
                    TableFooter(
                        TableRow(
                            TableCell("Total", colSpan="3"),
                            TableCell("$2,500.00", cls="text-right"),
                        )
                    ),
                ),
                cls="h-full container max-w-[80%] mt-4 overflow-auto",
            ),
            id="table",
        ),
    )

def carousel_block():
    return Block(
        Carousel(
            CarouselContent(
                CarouselItem(
                    Card(
                        Div(cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"),
                        title="Card #1",
                        description="Carousel demo card #1",
                        footer=Badge("@Shad4FastHtml", variant='default', cls="tracking-tighter"),
                    ),
                ),
                CarouselItem(
                    Card(
                        Div(cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"),
                        title="Card #2",
                        description="Carousel demo card #2",
                        footer=Badge("@Shad4FastHtml", variant='default', cls="tracking-tighter"),
                    ),
                ),
                CarouselItem(
                    Card(
                        Div(cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"),
                        title="Card #3",
                        description="Carousel demo card #3",
                        footer=Badge("@Shad4FastHtml", variant='default', cls="tracking-tighter"),
                    ),
                ),
                CarouselItem(
                    Card(
                        Div(cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"),
                        title="Card #4",
                        description="Carousel demo card #4",
                        footer=Badge("@Shad4FastHtml", variant='default', cls="tracking-tighter"),
                    ),
                ),
            ),
            CarouselPrevious(),
            CarouselNext(),
            cls="w-[65%] sm:w-1/2 mx-auto",
            autoplay=False,
            orientation="horizontal",
            id="carousel-demo"
        ),
        id="carousel",
    )

def slider_block():
    return Block(
        Slider(max='100', value='50', step='1', cls='max-w-64', min='0', id="demo-slider", name="demo-slider"),id="slider")
    


def sheet_block():
    return (
        Block(
            Div(
                SheetTrigger("Toggle Sheet", sheet_id="demo-sheet"),
            ),
            id="sheet",
        ),
        Sheet(
            Div(
                P("This is where you'd enter your sheet content", cls="text-pretty"),
                cls="p-4",
            ),
            title="Demo Sheet",
            description="This is a demo sheet.",
            footer=Div(SheetCloseButton("Close")),
            content_cls="flex flex-col justify-between",
            id="demo-sheet",
        ),
    )


def checkbox_block():
    return (
        Block(
            Div(
                Checkbox(id="terms1"),
                Div(
                    Label(
                        "Agree to the terms",
                        htmlFor="terms1",
                    ),
                    P(
                        "You agree to our Terms of Service and Privacy Policy.",
                        cls="text-sm text-muted-foreground",
                    ),
                    cls="grid gap-1.5 max-w-[300px]",
                ),
                cls="items-top justify-center flex space-x-2 container",
            ),
            id="checkbox",
        ),
    )
