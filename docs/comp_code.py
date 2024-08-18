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
    "input": """Div(
        Label("Title", htmlFor="title"),
        Input(placeholder="Enter a title", type="text", id="title"),
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
    "button": """Button("Default", variant='default')
    """,
    "lucide": """Lucide(icon='home', cls='size-6')""",
    "textarea": """Div(
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
    "label": """Div(
    Label(
        "Enter your email",
        htmlFor="email",
    ),
    Input(type="email", id="email"),
    cls="space-y-5 max-w-[80%] w-full",
),""",
}
