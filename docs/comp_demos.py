from docs.comp_code import code_dict, dummy_data
from fasthtml.common import *
from fasthtml.components import Zero_md
from shadcn import *

__all__ = [
    "card_block, select_block, alert_block, toast_block, separator_block, badge_block, progress_block, dialog_block, input_block, label_block, table_block, checkbox_block, button_block, lucide_block, textarea_block, render_copy_buttons"
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


def render_copy_buttons(app):
    app.router.hdrs += (
        Script(
            """function handleMdThemeChange(link) {
    const isDarkMode = localStorage.theme === 'dark' || document.documentElement.classList.contains('dark');
    const themeClass = isDarkMode ? 'dark-theme' : 'light-theme';
    link.disabled = !link.classList.contains(themeClass);
}

        document.addEventListener('zero-md-rendered', function(event) {
                const zeroMd = event.target;
                const shadowRoot = zeroMd.shadowRoot;

            if (shadowRoot) {
                const preElements = shadowRoot.querySelectorAll('pre');
                const content = shadowRoot.querySelector('.markdown-body');

                shadowRoot.querySelectorAll('link').forEach(link => handleMdThemeChange(link));
                
                preElements.forEach(pre => {
                    pre.style.position = 'relative';
                    pre.querySelector('code').style.padding = '1.5rem 0 ';
                    const button = document.createElement('button');
                    const clipboard = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" id="clipboard" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-clipboard"><rect width="8" height="4" x="8" y="2" rx="1" ry="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/></svg>';
                    const tick = '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" style="display:none;" id="tick" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-check"><path d="M20 6 9 17l-5-5"/></svg>';
                    button.innerHTML = clipboard + tick;
                    button.className = 'copy-button';
                    
                    button.addEventListener('click', function() {
                        const code = pre.querySelector('code');
                        const range = document.createRange();
                        range.selectNode(code);
                        window.getSelection().removeAllRanges();
                        window.getSelection().addRange(range);
                        
                        try {
                            document.execCommand('copy');
                            button.querySelector('#tick').style.display = 'block';
                            button.querySelector('#clipboard').style.display = 'none';
                            setTimeout(() => {
                                button.querySelector('#tick').style.display = 'none';
                                button.querySelector('#clipboard').style.display = 'block';
                            }, 2000);
                        } catch (err) {
                            console.error('Failed to copy text: ', err);
                        }
                        
                        window.getSelection().removeAllRanges();
                    });
                    pre.appendChild(button);
                });

                const style = document.createElement('style');
                style.textContent = `
                    .copy-button {
                        appearance: none;
                        position: absolute;
                        top: 5px;
                        right: 5px;
                        padding: 3px;
                        background-color: transparent;
                        border: 1px solid;
                        border-color: hsl(var(--border));
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    .copy-button:hover {
                        background-color: hsl(var(--muted));
                    }

                `;
                shadowRoot.appendChild(style);
            }
        });"""
        ),
    )


def render_code(content):
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
        cls="code-content flex items-center justify-center h-[350px] hidden",
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
            Div(
                Button(
                    Lucide(
                        icon="loader-circle",
                        cls="hidden size-4 animate-spin mr-1.5",
                        id="progress-loader",
                    ),
                    Span("Post"),
                    cls="max-w-fit",
                    id="progress-button",
                    disabled=True,
                ),
                Badge("Work in progress", variant="destructive"),
                # Progress(
                #     id="progress-bar-js",
                #     cls="data-[state=hidden]:hidden data-[state=visible]:animate-in data-[state=visible]:fade-in-0 data-[state=visible]:zoom-in-95",
                #     data_state="hidden",
                # ),
                # progress_script,
                cls="grid place-items-center w-[80%] gap-4",
                # hx_post="/job",
                # hx_swap="none",
                # hx_on__before_request="startProgress(this)",
            ),
            id="progress2",
        ),
    )


def dialog_block():
    return (
        Block(
            DialogTrigger("Toggle Dialog", dialog_id="demo-dialog"),
            id="dialog1",
        ),
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
                            type="email", value="johnsmith@email.com", cls="col-span-3"
                        ),
                        cls="grid grid-cols-4 items-center gap-4",
                    ),
                    cls="grid gap-4 py-4",
                ),
                DialogFooter(Button("Save changes")),
                cls="sm:max-w-[425px]",
            ),
            standard=True,
            id="demo-dialog",
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
