## Todo List, using Shad4Fast

To assist with understanding how to use Shad4Fast within a FastHTML app, I've enhanced a simple `Todo List` application created by the founder of FastHTML.

Instead of the default Picocss style & components that ship with FastHtml by default, the app now uses the Shad4FastHtml framework.

To try it out, a live version of the app can be found <a href="https://www.shad4fasthtml.com/example" target="_blank">here</a>.

```python
from fasthtml.common import *
from shad4fast import *
from lucide_fasthtml import Lucide

app, rt, todos, Todo = fast_app(
    "data/todos.db",
    id=int,
    title=str,
    description=str,
    done=bool,
    priority=str,
    pk="id",
    pico=False,
    hdrs=(ShadHead(theme_handle=True),),
)


def tid(id):
    return f"todo-{id}"


def edit_dialog(todo_id: str):
    edit = DialogTrigger(
        "Edit",
        hx_get=f"/edit/{todo_id}",
        target_id=f"edit-form-{todo_id}",
        hx_swap="outerHTML",
        variant="outline",
    )
    return Dialog(
        Div("Loading...", id=f"edit-form-{todo_id}"),
        trigger=edit,
        title="Edit Todo",
        description="Edit the todo item. Click the 'Save' button to save it.",
    )


@patch
def __ft__(self: Todo):
    priority_cls = {
        "low": "",
        "medium": "bg-yellow-500/80",
        "high": "bg-red-500/80",
    }
    delete = Button(
        "Delete",
        hx_delete=f"/todos/{self.id}",
        target_id=tid(self.id),
        hx_swap="outerHTML",
        variant="destructive",
    )
    status_cls = "absolute top-1.5 right-1"
    checked = Badge(
        Lucide("check", stroke_width="3", cls="size-4 text-primary"),
        cls=f"!bg-green-600 text-primary {status_cls} {'invisible' if not self.done else ''}",
    )

    return Card(
        CardHeader(
            checked,
            CardTitle(self.title),
            Div(
                "Priority level: ",
                Badge(
                    self.priority.title() if self.priority else "Low",
                    variant="outline",
                    cls=f"{priority_cls[self.priority] if self.priority else ''} w-fit",
                ),
                cls="flex items-center gap-1 text-muted-foreground text-sm pt-2",
            ),
        ),
        CardContent(
            P(self.description, cls="tracking-tight text-sm text-pretty line-clamp-3"),
            cls="grow",
        ),
        CardFooter(
            Div(
                delete,
                edit_dialog(todo_id=self.id),
                cls="flex items-center p-2 w-full justify-between self-end",
            ),
        ),
        cls="relative flex flex-col",
        standard=True,
        id=tid(self.id),
    )


def title_input(id=None, **kw):
    return Div(
        Label("Title", htmlFor=id),
        Input(
            id=id,
            name="title",
            placeholder="Enter a todo title",
            required=True,
        ),
        cls="space-y-1",
        id="title-block",
        **kw,
    )


def description_input(id=None, **kw):
    return Div(
        Label("Description", htmlFor=id),
        Textarea(
            id=id,
            name="description",
            placeholder="Enter a todo description",
            cls="resize-none",
            required=True,
        ),
        cls="space-y-1",
        id="description-block",
        **kw,
    )


def priority_input(**kw):
    return Div(
        Label(
            "Priority",
            Select(
                label="Priority",
                placeholder="Select a level of urgency",
                name="priority",
                items=["Low", "Medium", "High"],
                id="priority-select",
                cls="mt-1",
                default_value="high",
            ),
        ),
        id="priority-block",
        **kw,
    )


@rt("/")
def get():
    add = Card(
        Form(
            title_input(id="new-title"),
            description_input(id="new-description"),
            priority_input(),
            Button(
                "Add",
                cls="w-full !mt-6",
            ),
            hx_post="/",
            target_id="todo-list",
            hx_swap="afterbegin",
            cls="px-4 space-y-3",
            id="todo-form",
        ),
        title="Create a Todo",
        description="Add a new todo item to your list. Click the 'Add' button to save it.",
        cls="w-full",
    )
    content = Div(
        *todos(order_by="id desc"),
        id="todo-list",
        cls="grid sm:grid-cols-2 auto-rows-fr gap-3 w-full",
    )
    return Title("Todo list"), Body(
        H1(
            "Todo List - Shad4Fast",
            cls="text-4xl tracking-tighter font-semibold mt-10 text-center",
        ),
        Section(
            add,
            H1("Your Todos:", cls="text-3xl tracking-tight font-bold"),
            Separator(),
            content,
            cls="container max-w-4xl flex flex-col gap-4 items-center",
        ),
        cls="flex flex-col min-h-screen items-center gap-10 p-4",
    )


@rt("/todos/{id}")
def delete(id: int):
    todos.delete(id)


@rt("/")
def post(todo: Todo):
    return (
        todos.insert(todo),
        title_input(id="new-title", hx_swap_oob="true"),
        description_input(id="new-description", hx_swap_oob="true"),
        priority_input(hx_swap_oob="true"),
    )


@rt("/edit/{id}")
def get(id: int):
    todo = todos.get(id)
    res = Form(
        Div(
            title_input(id="edit-title"),
            description_input(id="edit-description"),
            cls="flex flex-col gap-2",
        ),
        Hidden(id="id"),
        Div(
            Hidden(name="done", value="", skip=True),
            Label("Complete", htmlFor="done"),
            Checkbox(id="done", name="done"),
            cls="flex items-center gap-1.5",
        ),
        DialogClose(
            "Save",
            cls="w-full !mt-6",
        ),
        hx_put="/",
        target_id=tid(id),
        hx_swap="outerHTML",
        id=f"edit-form-{id}",
        cls="p-2 space-y-6",
    )
    return fill_form(res, todo)


@rt("/")
def put(todo: Todo):
    return todos.upsert(todo)


serve()
```
