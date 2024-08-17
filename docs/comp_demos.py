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


def Block(*c, name=None, id="default", **kwargs):
    cls = "relative mx-auto w-full max-w-xl flex flex-col rounded-md bg-muted/40 shadow"
    return Article(
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
                    code_dict[id],
                    cls="text-sm rounded-md bg-muted h-[318px]",
                ),
                cls="flex [&>button]:bg-primary/50",
            ),
            cls="code-content flex items-center justify-center w-full p-4 flex-grow hidden",
        ),
    )


def card_block():
    return (
        Block(
            Card(
                Input(type="text", placeholder="Enter some text...", id="card1-input"),
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
            name="Card: Standard",
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
            name="Select",
        ),
    )


def AlertAltBlock():
    return (
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
    )


def button_block():
    return (
        Block(
            Button("Default", variant="default"),
            id="button",
            name="Button",
        ),
    )


def lucide_block():
    return Block(Lucide(icon="home", cls="size-6"), id="lucide", name="Lucide")


def alert_block():
    return (
        Block(
            Alert(
                Lucide(icon="chevrons-right", cls="size-4"),
                AlertTitle("New message!"),
                AlertDescription("Open your messages section to view more details."),
                standard=True,
                cls="!w-[90%]",
            ),
            id="alert2",
            name="Alert: Standard",
        ),
    )


def toast_block():
    return (
        Block(
            Button("Send email", hx_get="/toast", hx_swap="none"),
            name="Toast",
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
            name="Badge",
            id="badge",
        ),
    )


def progress_block():
    return (
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
    )


def dialog_block():
    return (
        Block(
            DialogTrigger("Toggle Dialog", target="modal"),
            id="dialog1",
            name="Dialog",
        ),
    )


def DialogAltBlock():
    return (
        Block(
            DialogTrigger("Toggle Dialog", target="modal-standard"),
            id="dialog2",
            name="Dialog: standard",
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
        name="Label",
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
            name="Input",
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
        name="Textarea",
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
            name="Switch & Label",
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
            name="Table",
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
                cls="items-top flex space-x-2",
            ),
            id="checkbox",
            name="Checkbox",
        ),
    )
