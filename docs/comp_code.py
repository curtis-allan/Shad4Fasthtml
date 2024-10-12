dummy_data = [
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

code_dict = {
    "avatar": """
Avatar(
    src="https://placecats.com/300/200",
    alt="Profile Image", 
    fallback="CA"
)
""",
    "aspect_ratio": """
Div(
    AspectRatio(
        Img(
            src="/public/aspect.webp",
            cls="w-full h-full rounded-md object-cover",
            loading="lazy",
        ),
        ratio={16 / 9},
    ),
    cls="w-[80%]",
)
""",
    "scroll_area": """
def fake_data():
    results = []
    for i in range(50):
        results.append(Div(f"Item Entry #{i}", cls="text-sm"))
    return results

ScrollArea(
    Div(
        H4("Entries", cls="mb-4 text-sm font-medium leading-none"),
        *fake_data(),
        cls="p-4",
    ),
    cls="h-72 w-48 rounded-md border",
)
""",
    "scroll_area2": """
def fake_data_horizontal():
    results = ()
    data = [
        {
            "artist": "Ornella Binni",
            "art": "https://images.unsplash.com/photo-1465869185982-5a1a7522cbcb?auto=format&fit=crop&w=300&q=80",
        },
        {
            "artist": "Tom Byrom",
            "art": "https://images.unsplash.com/photo-1548516173-3cabfa4607e9?auto=format&fit=crop&w=300&q=80",
        },
        {
            "artist": "Vladimir Malyavko",
            "art": "https://images.unsplash.com/photo-1494337480532-3725c85fd2ab?auto=format&fit=crop&w=300&q=80",
        },
    ]
    for i in data:
        results += (
            Figure(
                Div(
                    Img(
                        src=i["art"],
                        alt=f"Photo by {i['artist']}",
                        cls="aspect-[3/4] h-fit w-fit object-cover",
                    ),
                ),
                Figcaption(
                    "Photo by ",
                    Span(i["artist"], cls="font-semibold text-foreground"),
                    cls="pt-2 text-xs text-muted-foreground",
                ),
                cls="shrink-0",
            ),
        )
    return results

ScrollArea(
    Div(*fake_data_horizontal(), cls="flex w-max space-x-4 p-4"),
    cls="w-96 whitespace-nowrap rounded-md border",
    orientation="horizontal",
)
""",
    "aspect_ratio2": """
 Div(
    AspectRatio(
        Img(
            src="/public/aspect2.webp",
            cls="w-full h-full rounded-md object-cover",
            loading="lazy",
        ),
        ratio={9 / 16},
    ),
    cls="min-w-[200px] py-3",
)
""",
    "card1": """
Card(
    Input(
        type="text",
        placeholder="Title",
        ),
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
    )""",
    "alert2": """
Alert(
    Lucide(icon="circle-alert", cls="size-4"),
    AlertTitle("Error"),
    AlertDescription("An error occurred while processing your request."),
    standard=True,
    variant="destructive",
    cls="max-w-[80%]",
)
""",
    "alert1": """
Alert(
    title="New message!",
    description="Open your messages to view more details.",
    cls="max-w-[80%]",
)
""",
    "separator": """
H1(
    "Welcome back",
    cls="text-3xl font-bold tracking-tight leading-loose",
),
Separator(cls="my-2 max-w-[90%]"),
Div(
    Button("Profile", variant="outline"),
    Separator(orientation="vertical"),
    Button("Messages", variant="outline"),
    Separator(orientation="vertical"),
    Button("Settings", variant="outline"),
    cls="flex gap-3 p-3",
)
""",
    "badge": """
Div(
    H1(
        "Shad4FastHtml",
        cls="text-2xl font-semibold tracking-tight",
    ),
    Badge("v2.0"),
    cls="flex gap-1.5 items-center justify-center",
)
""",
    "badge2": """
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
)""",
    "progress": """
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
)

def ProgressBar(progress):
    return Progress(
        value=progress,
        hx_trigger="every 500ms",
        hx_target="this",
        hx_get="/progress",
        hx_swap="outerHTML",
        id="progress-bar",
    )

progress = 0
    
@rt("/start")
def post():
    global progress
    progress = 0
    return ProgressBar(progress)


@rt("/progress")
def get():
    global progress
    progress += random.randint(1, 25)
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

    return ProgressBar(progress)""",
    "progress2": """Div(
    Button(
        "Start",
        hx_post="/start",
        cls="max-w-fit",
        hx_swap="innerHTML",
        hx_target="#progress-container",
    ),
    id="progress-container",
    cls="grid place-items-center w-[80%]",
)""",
    "toast": """
// Setup the toast handler function under the app setup

    toast_setup(app)

// Use a button to trigger the toast route

    Button("Send email", hx_get="/toast", hx_swap="none")

// Add a toast function to the route return statement
    
    @rt("/toast")
    def get(sess):
        toast(sess=sess, title="Sent!", description="Email has been sent successfully.")
""",
    "dialog": """
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
            DialogClose("Save changes"), cls="flex w-full justify-end"
        ),
        id="demo-dialog",
    )""",
    "dialog2": """
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
            DialogFooter(DialogClose("Save changes")),
            cls="sm:max-w-[425px]",
        ),
        standard=True,
        id="demo-dialog",
    )
""",
    "input": """
Input(
    placeholder="Enter something",
    type="text", 
    id="title", 
    cls="max-w-[80%]"
)
""",
    "switch": """
Div(
    Label(
        "Agree to terms",
        htmlFor="switch-toggle",
    ),
    Switch(
        id="switch-toggle",
        name="switch-toggle",
    ),
    cls="flex gap-1.5 items-center",
),""",
    "switch2": """Form(
Div(
    Label(
        "Agree to terms",
        htmlFor="switch-toggle",
    ),
    Switch(
        id="switch-toggle",
        name="switch-toggle",
        value="agree",
    ),
    Button("Submit"),
    cls="flex flex-col gap-4",
    ),
    cls="flex gap-1.5 items-center",
)

""",
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
    placeholder="Pick a fruit",
    label="Fruits",
    items=["Apple", "Banana", "Blueberry", "Pineapple", "Orange", "Mango", "Guava", "Watermelon"],
    )""",
    "checkbox": """
Div(
    Checkbox(id="terms1", name="terms1"),
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
)""",
    "button": """
Button("Button")
    """,
    "lucide": """
Lucide(icon='home', cls='size-6')""",
    "textarea": """
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
)""",
    "label": """
Div(
    Label("Email", htmlFor="email"),
    Input(
        placeholder="Enter your email",
        type="email",
        id="email",
    ),
    cls="flex flex-col sm:flex-row gap-1.5 sm:items-center w-full max-w-sm container justify-center items-start",
)""",
    "sheet": """
Sheet(
    Div(
        P("This is where you'd enter your sheet content"),
        cls="h-[85%]",
    ),
    title="Demo Sheet",
    description="This is a demo sheet.",
    footer=SheetClose("Close", cls="w-full"),
    trigger="Toggle Sheet",
    id="demo-sheet",
)""",
    "sheet2": """
Sheet(
    SheetTrigger("Toggle Sheet"),
    SheetContent(
        SheetHeader(
            SheetTitle("Demo Sheet"),
            SheetDescription("This is a demo sheet."),
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
        SheetFooter(SheetClose("Close")),
    ),
    standard=True,
)""",
"accordion":"""
Accordion(
    AccordionItem(
        AccordionTrigger("What is FastHTML?"),
        AccordionContent(
            P("FastHTML is a Python library for building web applications using a component-based approach, similar to React but with Python syntax.")
        )
    ),
    AccordionItem(
        AccordionTrigger("How does Shad4Fast relate to FastHTML?"),
        AccordionContent(
            P("Shad4Fast is a component library built on top of FastHTML, providing pre-styled UI components inspired by Shadcn UI for rapid development.")
        )
    ),
    AccordionItem(
        AccordionTrigger("What are the benefits of using Shad4Fast?"),
        AccordionContent(
            P("Shad4Fast offers easy-to-use, customizable UI components that are accessible and responsive, speeding up development while maintaining a professional look and feel.")
        )
    ),
    cls="!w-[80%]",
)""",
    "button2": """
Div(
    Button("Default", variant="default"),

    Button("Secondary", variant="secondary"),

    Button("Outline", variant="outline"),

    Button("Destructive", variant="destructive"),

    Button("Link", variant="link"),

    Button("Ghost", variant="ghost"),

    cls="grid grid-cols-2 sm:grid-cols-3 sm:grid-rows-2 gap-4 max-w-[90%]",
)""",
    "button3": """
Div(
    Button("Default", size="default"),

    Button("Small", size="sm"),

    Button("Large", size="lg"),

    Button(Lucide(icon="settings"),size="icon"),

    cls="grid grid-flow-row gap-4 place-items-center auto-rows-auto max-w-[90%]",
)""",
    "button4": """
Div(
    Span(
        Label("Disabled:", htmlFor="button-disabled",cls="text-[15px] font-semibold"),
        Button("Submit", id="button-secondary", disabled=True),
        cls="flex items-center justify-between",
    ),
    Separator(),
    Span(
        Label("Loading:", htmlFor="button-loading",cls="text-[15px] font-semibold"),
        Button(
            Lucide(icon="loader2", cls="size-4 mr-1.5 animate-spin"),
            "Loading",
            id="button-loading",
            disabled=True,
        ),
        cls="flex items-center justify-between",
    ),
    cls="grid gap-3 w-[215px]",
)""",
    "select2": """Select(
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
)""",
    "carousel": """
def carousel_items():
items = ()
for i in range(4):
    i += 1
    items += (
        Card(
            Div(cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"),
            title=f"Card {i}",
            description=f"Carousel demo card #{i}",
            footer=Badge(
                "@Shad4FastHtml", variant="default", cls="tracking-tighter"
            ),
        ),
    )
return items

Carousel(
    items=carousel_items(),
    cls="max-w-[65%] mx-auto",
)
""",
    "carousel2": """
Carousel(
    CarouselContent(
        CarouselItem(
            Card(
                Div(
                    cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"
                ),
                title="Card #1",
                description="Carousel demo card #1",
                footer=Badge(
                    "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                ),
            ),
        ),
        CarouselItem(
            Card(
                Div(
                    cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"
                ),
                title="Card #2",
                description="Carousel demo card #2",
                footer=Badge(
                    "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                ),
            ),
        ),
        CarouselItem(
            Card(
                Div(
                    cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"
                ),
                title="Card #3",
                description="Carousel demo card #3",
                footer=Badge(
                    "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                ),
            ),
        ),
        CarouselItem(
            Card(
                Div(
                    cls="h-24 w-full mx-auto bg-primary/40 rounded-sm animate-pulse"
                ),
                title="Card #4",
                description="Carousel demo card #4",
                footer=Badge(
                    "@Shad4FastHtml", variant="default", cls="tracking-tighter"
                ),
            ),
        ),
        duration="1000",
    ),
    cls="max-w-xs",
    autoplay=True,
    orientation="vertical",
    standard=True,
)
""",
    "slider": """
Slider(min=0, max=100, cls="max-w-64")
""",
    "tabs": """Tabs(
    TabsList(
        TabsTrigger("Post", value="tab1"),
        TabsTrigger("Settings", value="tab2"),
        cls="grid w-full grid-cols-2"
    ),
    TabsContent(Card(Div(Label("Username", htmlFor="tab-title"),Input(type="text", placeholder="Title", id="tab-title"),),
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
            ), value="tab1"),
    TabsContent(Card(
                Div(Label("Username", htmlFor="tab-settings"),Input(type="text", value="@JohnDoe", disabled='true', id="tab-settings"),),
                title="Settings",
                description="Change your settings here",
                footer=Div(
                    Button(
                        "Cancel",
                        variant="outline",
                    ),
                    Button("Submit"),
                    cls="flex w-full justify-end gap-2",
                ),
            ), value="tab2"),
            default_value="tab1",
            cls="max-w-[80%] w-full mx-auto"
        )
""",
    "radio": """RadioGroup(
    Div(RadioGroupItem(value="option1", id="option1"), Label("Claude 3.5 Sonnet", htmlFor="option1"), cls="flex items-center space-x-2"),
    Div(RadioGroupItem(value="option2", id="option2"), Label("Gpt 4o", htmlFor="option2"), cls="flex items-center space-x-2"),
    Div(RadioGroupItem(value="option3", id="option3"), Label("Gpt 4 Turbo", htmlFor="option3"), cls="flex items-center space-x-2"),
    name="my-radio-group",
    defaultValue="option1",
)
""",
}
