from fasthtml.common import *
from shadcn import *

app, rt = fast_app(
    pico=False,
    hdrs=(
        ShadHead(),
        HighlightJS(),
        MarkdownJS(),
    ),
    live=True,
    debug=True,
)

toast_setup(app)


dummy_data = data = [
    {
        "invoice": "INV001",
        "paymentStatus": "Paid",
        "totalAmount": "$250.00",
        "paymentMethod": "Credit Card",
    },
    {
        "invoice": "INV002",
        "paymentStatus": "Pending",
        "totalAmount": "$150.00",
        "paymentMethod": "PayPal",
    },
    {
        "invoice": "INV003",
        "paymentStatus": "Unpaid",
        "totalAmount": "$350.00",
        "paymentMethod": "Bank Transfer",
    },
    {
        "invoice": "INV004",
        "paymentStatus": "Paid",
        "totalAmount": "$450.00",
        "paymentMethod": "Credit Card",
    },
    {
        "invoice": "INV005",
        "paymentStatus": "Paid",
        "totalAmount": "$550.00",
        "paymentMethod": "PayPal",
    },
    {
        "invoice": "INV006",
        "paymentStatus": "Pending",
        "totalAmount": "$200.00",
        "paymentMethod": "Bank Transfer",
    },
    {
        "invoice": "INV007",
        "paymentStatus": "Unpaid",
        "totalAmount": "$300.00",
        "paymentMethod": "Credit Card",
    },
]

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
    "progress": """Div(
    Button(
        "Start",
        onclick="handleClick()",
        cls="max-w-fit",
    ),
    Progress(
        ProgressInner(id="progress-inner"),
        ),
        cls="flex flex-col gap-3 w-[80%] items-center justify-center",
    ),""",
    "toast": """
    // import statements + app setup

    toast_setup(app)

    // route setup

    Button("Send email", hx_get="/toast", hx_swap="none"),

    // rest of code
    
    @rt("/toast")
    def get(sess):
        toast(sess=sess, title="Sent!", description="Email has been sent successfully.")
""",
    "dialog1": """
// import statements + app setup

@rt('/')
def get():
    return DialogTrigger("Toggle Dialog", target="modal"),
    id="dialog1",
    ),

@rt('/modal')
def get():
    return
        Dialog(
            Div(
                P(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam fringilla viverra orci, non ullamcorper quam rhoncus eget. Proin finibus turpis a sapien egestas eleifend.",
                    cls="text-pretty",
                ),
            cls="sm:max-w-[425px]",
            ),
            title="Dialog example",
            description="An example of a dialog component, press 'x' to close.",
            footer=P(
                "Powered by htmx, fasthtml, and vanillaJS",
                cls="text-center text-sm text-muted-foreground tracking-tight w-full",
            ),
        )""",
    "dialog2": """
// import statements + app setup

@rt('/')
def get():
    return DialogTrigger("Toggle Dialog", target="modal-standard"),
    id="dialog2",
    ),

@rt("/modal-standard")
def get():
    return (Dialog(
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
)
""",
    "input": """
    // Example usage of the Input, Button, Label & Textarea components

    Div(
        H1("Create a post", cls="text-2xl font-semibold tracking-tight"),
        Div(
            Label("Title", htmlFor="title"),
            Input(placeholder="Enter a title", id="title"),
            Label(
                "Content",
                htmlFor="content",
            ),
            Textarea(
                placeholder="Enter some content...",
                cls="col-span-3",
                id="content",
            ),
            Button("Submit", cls="mt-5 self-end"),
            cls="flex flex-col gap-1.5",
        ),
        cls="space-y-5 max-w-[80%] w-full",
    ),
""",
    "switch": """
    Div(
    Label(
        "Agree to terms",
        htmlFor="switch",
        ),
        Switch(
            id="switch",
        ),
         cls="flex gap-1.5 items-center",
    ),""",
    "table": """
    // Dummy table data to indicate mapping
    
    dummy_data = data = [
    {
        "invoice": "INV001",
        "paymentStatus": "Paid",
        "totalAmount": "$250.00",
        "paymentMethod": "Credit Card",
    },
    {
        "invoice": "INV002",
        "paymentStatus": "Pending",
        "totalAmount": "$150.00",
        "paymentMethod": "PayPal",
    },
    {
        "invoice": "INV003",
        "paymentStatus": "Unpaid",
        "totalAmount": "$350.00",
        "paymentMethod": "Bank Transfer",
    },
    {
        "invoice": "INV004",
        "paymentStatus": "Paid",
        "totalAmount": "$450.00",
        "paymentMethod": "Credit Card",
    },
    {
        "invoice": "INV005",
        "paymentStatus": "Paid",
        "totalAmount": "$550.00",
        "paymentMethod": "PayPal",
    },
    {
        "invoice": "INV006",
        "paymentStatus": "Pending",
        "totalAmount": "$200.00",
        "paymentMethod": "Bank Transfer",
    },
    {
        "invoice": "INV007",
        "paymentStatus": "Unpaid",
        "totalAmount": "$300.00",
        "paymentMethod": "Credit Card",
    },
    ]

    // Mapping function for FT components with data

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

    // Final composition

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
                TableCell("Total", colSpan="3"), TableCell("$2,500.00")
            )
        ),
        cls="max-w-[80%] mx-auto mt-5",
    ),""",
    "select": """Select(
    SelectTrigger(
        SelectValue(placeholder="Pick a fruit"),
        cls="w-[180px]",
    ),
    SelectContent(
        SelectLabel("Fruits"),
        SelectItem("Apple", value="apple"),
        SelectItem("Banana", value="banana"),
        SelectItem("Blueberry", value="blueberry"),
        SelectItem("Pineapple", value="pineapple"),
        SelectItem("Orange", value="orange"),
        SelectItem("Mango", value="mango"),
        SelectItem("Guava", value="guava"),
        SelectItem("Watermelon", value="watermelon"),
    ),
),""",
    "checkbox": """Div(
        Checkbox(id="terms1"),
        Div(
            Label(
                "Agree to the terms",
                htmlFor="terms1",
                cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
            ),
            P(
                "You agree to our Terms of Service and Privacy Policy.",
                cls="text-sm text-muted-foreground",
            ),
            cls="grid gap-1.5 leading-none",
        ),
        cls="items-top flex space-x-2",
    ),""",
}


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


def Block(*c, name=None, id="default", **kwargs):
    cls = "relative mx-auto w-full max-w-xl flex flex-col rounded-md bg-muted/40 shadow"
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
            size="icon",
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


def CodeContent(id: str = None):
    return (
        Div(
            Pre(
                Code(
                    code[id],
                    cls="text-sm rounded-md bg-muted h-[318px]",
                ),
                cls="flex [&>button]:bg-primary/50",
            ),
            cls="code-content flex items-center justify-center w-full p-4 flex-grow hidden",
        ),
    )


@rt("/")
def get():
    return Title("Shadcn components in FastHtml"), Main(
        Header(
            H1(
                "Shadcn-ui components, made for FastHtml",
                cls="relative text-6xl font-bold tracking-tight text-center",
            ),
            Nav(
                A(
                    Button(
                        Lucide(icon="github"),
                        size="icon",
                        variant="outline",
                    ),
                    href="https://github.com/curtis-allan/shadcn-fasthtml-framework",
                    target="_blank",
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
            cls="flex flex-col pt-20 text-balance ",
        ),
        Section(
            Div(
                H1(
                    "Click this button to change the theme",
                    cls="text-lg text-muted-foreground",
                ),
                Lucide(
                    icon="arrow-right",
                    cls="size-5 min-w-max text-muted-foreground",
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
                cls="container flex justify-center items-center gap-1.5",
            ),
            Block(
                Card(
                    Input(
                        type="text", placeholder="Enter some text...", id="card1-input"
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
                Select(
                    SelectTrigger(
                        SelectValue(placeholder="Pick a fruit"),
                        cls="w-[180px]",
                    ),
                    SelectContent(
                        SelectLabel("Fruits"),
                        SelectItem("Apple", value="apple"),
                        SelectItem("Banana", value="banana"),
                        SelectItem("Blueberry", value="blueberry"),
                        SelectItem("Pineapple", value="pineapple"),
                        SelectItem("Orange", value="orange"),
                        SelectItem("Mango", value="mango"),
                        SelectItem("Guava", value="guava"),
                        SelectItem("Watermelon", value="watermelon"),
                    ),
                ),
                id="select",
                name="Select",
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
                Button("Send email", hx_get="/toast", hx_swap="none"),
                name="Toast",
                id="toast",
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
            Block(
                Div(
                    Button(
                        "Start",
                        onclick="handleClick()",
                        cls="max-w-fit",
                    ),
                    Progress(
                        ProgressInner(id="progress-inner"),
                    ),
                    cls="flex flex-col gap-3 w-[80%] items-center justify-center",
                ),
                name="Progress Bar",
                id="progress",
            ),
            Block(
                DialogTrigger("Toggle Dialog", target="modal"),
                id="dialog1",
                name="Dialog",
            ),
            Block(
                DialogTrigger("Toggle Dialog", target="modal-standard"),
                id="dialog2",
                name="Dialog: standard",
            ),
            Block(
                Div(
                    H1("Create a story", cls="text-2xl font-semibold tracking-tight"),
                    Div(
                        Label("Title", htmlFor="title"),
                        Input(placeholder="Enter a title", id="title"),
                        Label(
                            "Content",
                            htmlFor="content",
                        ),
                        Textarea(
                            placeholder="Enter some content.",
                            cls="col-span-3",
                            id="content",
                        ),
                        Button("Submit", cls="mt-5 self-end"),
                        cls="flex flex-col gap-1.5",
                    ),
                    cls="space-y-5 max-w-[80%] w-full",
                ),
                id="input",
                name="Input & Textarea",
            ),
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
                name="Switch & Label",
            ),
            Block(
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
                    cls="max-w-[80%] mx-auto mt-5",
                ),
                id="table",
                name="Table",
            ),
            Block(
                Div(
                    Checkbox(id="terms1"),
                    Div(
                        Label(
                            "Agree to the terms",
                            htmlFor="terms1",
                            cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                        ),
                        P(
                            "You agree to our Terms of Service and Privacy Policy.",
                            cls="text-sm text-muted-foreground",
                        ),
                        cls="grid gap-1.5 leading-none",
                    ),
                    cls="items-top flex space-x-2",
                ),
                id="checkbox",
                name="Checkbox",
            ),
            cls="flex flex-col gap-6 p-8",
        ),
        cls="max-w-4xl container",
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
    "getting-started": ("installation", "using-components"),
    "components": ("card", "alert", "switch"),
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
                    cls="w-full",
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
                cls="max-w-4xl container mt-14",
            ),
            cls="flex flex-col pl-[180px] flex-grow",
        ),
        cls="min-h-screen flex flex-col",
    )


def content():
    f = open("README.md")
    return f.read()


@rt("/getting-started/{title}")
def get(title: str):
    return DocsLayout(
        Div(content(), cls="marked"),
        title=title,
    )


@rt("/components/{title}")
def get(title: str):
    return DocsLayout(Div("component here"), title=title)


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


serve()
