from docs.comp_code import code_dict, dummy_data
from fasthtml.common import *
from shadcn import *

__all__ = [
    "card_block, select_block, alert_block, toast_block, separator_block, badge_block, progress_block, dialog_block, input_block, label_block, table_block, checkbox_block, button_block, lucide_block, textarea_block"
]


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
            name, cls="text-xl font-semibold tracking-tight absolute top-2 inset-y-0"
        )

    cls = "relative max-w-xl mx-auto flex flex-col rounded-md bg-muted/40 shadow"
    return Div(
        Div(
            Div(
                header,
                themeToggle,
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


def CodeContent(id: str = None):
    return Div(
        Pre(
            Code(
                code_dict[id],
                cls="text-sm rounded-md h-[318px] w-full",
            ),
            cls="flex [&>button]:bg-muted-foreground/40 w-full",
        ),
        cls="code-content flex items-center justify-center p-4 flex-grow hidden",
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


def select_block():
    return (
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
        ),
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
            name="Destructive",
        ),
    )


def button_block():
    return (
        Block(
            Button("Default", variant="default"),
            id="button",
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
                    cls="text-2xl font-semibold tracking-tight leading-loose",
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
                    Label("Default:", htmlFor="badge-default"),
                    BadgeDefault(),
                    cls="flex items-center justify-between",
                ),
                Separator(),
                Span(
                    Label("Secondary:", htmlFor="badge-secondary"),
                    BadgeSecondary(),
                    cls="flex items-center justify-between",
                ),
                Separator(),
                Span(
                    Label("Outline:", htmlFor="badge-outline"),
                    BadgeOutline(),
                    cls="flex items-center justify-between",
                ),
                Separator(),
                Span(
                    Label("Destructive:", htmlFor="badge-destructive"),
                    BadgeDestructive(),
                    cls="flex items-center justify-between",
                ),
                cls="flex flex-col gap-3 justify-center w-[180px]",
            ),
            id="badge2",
        ),
    )


def BadgeDefault():
    return Badge("New Feature", variant="default", id="badge-default")


def BadgeSecondary():
    return Badge("Updated", variant="secondary", id="badge-secondary")


def BadgeDestructive():
    return Badge("Invalid", variant="destructive", id="badge-destructive")


def BadgeOutline():
    return Badge("Terms v1.03", variant="outline", id="badge-outline")


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
        H2(
            "Alternate Demo (JS + EventStream)",
            cls="text-2xl font-semibold tracking-tight h-full border-b pb-1.5 mb-4",
        ),
        ProgressAltBlock(),
    )


progress_script = Script(
    """function startProgress(elt) {
        const inner = elt.querySelector('#progress-bar-js-inner');
        const progress = elt.querySelector('#progress-bar-js');
        const button = elt.querySelector('#progress-button');
        const button_text = button.querySelector('span')
        const icon = elt.querySelector('#progress-loader');

        const eventSource = new EventSource('/progress-stream');

        progress.dataset.state = 'visible';

        icon.classList.remove('hidden');

        button_text.innerHTML = 'Posting';

        button.disabled = true;

        eventSource.onmessage = function(event) {
            const data = JSON.parse(event.data);

            inner.style.transform = `translateX(-${100 - (data.progress / data.total * 100)}%)`;

            if (data.progress === data.total) {
                icon.classList.add('hidden');
                button.disabled = false;
                button_text.innerHTML = 'Restart';
                eventSource.close();
            }
        };
        eventSource.onerror = function(error) {
            console.error('EventSource failed:', error);
            eventSource.close();
        };
    }
    """
)


def ProgressAltBlock():
    return (
        Block(
            Form(
                Button(
                    Lucide(
                        icon="loader-circle",
                        cls="hidden size-4 animate-spin mr-1.5",
                        id="progress-loader",
                    ),
                    Span("Post"),
                    cls="max-w-fit",
                    id="progress-button",
                ),
                Progress(
                    id="progress-bar-js",
                    cls="data-[state=hidden]:hidden data-[state=visible]:animate-in data-[state=visible]:fade-in-0 data-[state=visible]:zoom-in-95",
                    data_state="hidden",
                ),
                progress_script,
                cls="grid place-items-center w-[80%] gap-4",
                hx_post="/job",
                hx_swap="beforeend",
                hx_on__before_request="startProgress(this)",
            ),
            id="progress2",
        ),
    )


def dialog_block():
    return (
        Block(
            DialogTrigger("Toggle Dialog", target="modal"),
            id="dialog1",
        ),
    )


def DialogAltBlock():
    return (
        Block(
            DialogTrigger("Toggle Dialog", target="modal-standard"),
            id="dialog2",
        ),
    )


def label_block():
    return Block(
        Div(
            Label(
                "Email",
                htmlFor="email",
            ),
            Input(type="email", id="email"),
            cls="space-y-5 max-w-[80%] w-full",
        ),
        id="label",
    )


def input_block():
    return (
        Block(
            Div(
                Label("Title", htmlFor="title"),
                Input(placeholder="Enter a title", type="text", id="title"),
                cls="space-y-5 max-w-[80%] w-full",
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
                        cls="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70",
                    ),
                    P(
                        "You agree to our Terms of Service and Privacy Policy.",
                        cls="text-sm text-muted-foreground",
                    ),
                    cls="grid gap-1.5 leading-none",
                ),
                cls="items-top flex space-x-2 max-w-[80%] mx-auto",
            ),
            id="checkbox",
        ),
    )
