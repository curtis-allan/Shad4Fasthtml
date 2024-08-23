## Usage

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Progress
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

---

## Implementation

Progress bars can be a little tricky to implement. Depending on your use case, you may need a different approach when handling progress updates. By default, the progress bar takes a `value` attribute in the form of a percentage value of the total.

> **Note:** Make sure not to include the % symbol in your value, just a value representing the completion percentage: (33 for 33%). This value can be either an integer or a float.

Here are two possible implementations you can use depending on your use case:

---

### HTMX Approach

The first example above uses htmx to update the progress bar using a global value in place of an actual callback value. In a real scenario, you would want to use an actual callback value, such as an XHR progress event value, instead. Refer to the htmx <a href="https://htmx.org/reference/#events" target="_blank">documentation</a> for more information on how to handle progress updates with htmx.

For further references, refer to these resources:

*   <a href="https://gallery.fastht.ml/widgets/progress_bar/display" target="_blank">FastHtml Gallery Progress Bar</a>
*   <a href="https://htmx.org/examples/progress-bar/" target="_blank">Official HTMX Example</a>

```python+html

// Button + Container to handle initial progress bar swap and subsequent updates.

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

// To save code lines, we can define a simple function to return the progress bar
// with our unique params.

def ProgressBar(progress):
    return Progress(
        value=progress,
        hx_trigger="every 500ms",
        hx_target="this",
        hx_get="/progress",
        hx_swap="outerHTML",
        id="progress-bar",
    )

// For this example, we define a global variable to store the progress
// value for demonstration purposes.

progress = 0

// Then, we can define our routes to handle the progress bar updates.

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

    return ProgressBar(progress)
```

> **Note:** To ensure a smooth transition, the progress bar requires an `id` attribute. The id is passed on automatically to the inner bar element as `id='{id}-inner'`. For example, `Progress(id='progress-bar')` would set the inner Div id to `'progress-bar-inner`.

### JavaScript Approach

The second example above uses a combination of JavaScript and Slarlette's `StreamingResponse` response class to update the progress bar. Using this streaming response and an async generator, we can continuously stream the progress updates to the client. 

To handle these responses, we can instantiate a new `EventSource` object, which behaves a bit like a WebSocket connection, only its unilateral (Server -> Client). Using this object, we can listen for events that are sent from the async generator and update the progress bar. 

Firstly, we can setup a form component which sends a standard hx-post request. The example above utilises tailwind animations to showcase a real-world implementation of responsive form handling on the client.

```python+html
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
    Script(progress_script),
    cls="grid place-items-center w-[80%] gap-4",
    hx_post="/job",
    hx_swap="beforeend",
    hx_on__before_request="startProgress(this)",
),
```

>**Note:** The `hx_on__before_request` attribute is used to trigger the `startProgress()` function as soon as the form is submitted.

Next, we can define a script to handle the progress bar updates and attach it to our form. Then, we can envoke the `startProgress()` function to instantiate the event source and listen for loading events.

```javascript
function startProgress(elt) {
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
```

Once the form is submitted, the `startProgress()` function will create a new connection to our route `/progress-stream` and listen for any events sent from the server (in the form of `onmessage` events). This is useful in our case, as we can use it to dynamically update the progress bar's inner element `#progress-bar-js-inner` directly. 

Since the inner element of the progress bar has a style set to `translateX(-100%)` initially, we can return the progress state and total amount from our server route and use them to calculate the percentage loaded for each update. Once the progress reaches 100% of the total being served, we can update our components to reflect this, as shown above.

>**Note:** The `eventSource.close()` function is used to close the connection. It should be utilised when the connection is no longer needed *AND* within error handling functions, to ensure the connection is closed and resources are freed!

Finally, we can define our routes. In the case of this example, dummy methods and global variables are defined to simulate a real-world scenario duration.

```python+html
loaded = 0
total = 8000


@rt("/progress-stream")
async def get():
    global loaded
    global total

    async def event_stream():
        while loaded <= total:
            yield f"data: {json.dumps({'progress': loaded, 'total': total})}\n\n"
            await asyncio.sleep(0.4)

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@rt("/job")
async def post():
    global total
    global loaded
    loaded = 0

    while loaded < total:
        loaded += 200
        await asyncio.sleep(0.05)

    return Response(status_code=204)
```

Our form component sends a request to the `/job` route, and invoked the `startProgress()` function to create a new connection to the `/progress-stream` route. The job route simulates a long-running process by incrementing the `loaded` variable by a set amount and sleeping for a short period of time. 

Since both the total and loaded variables are global, they can be accessed by both the progress-stream and job routes. This allows us to create an asyncronous generator, in the form of a loop, that can send the relevant data to the client.

>**Note:** Both `loaded` and `total` globals can be set to anything. In this example, we have set them to dummy values of 8000 and 0 respectively. In a real-world scenario, these values would be replaced with the relevant total and loaded values from the server.

By using a a `sleep()` function, we can throttle the requests that the stream sends to the client, in this case it retrieves the new `loaded` value every 0.05 seconds. This ensures that the stream is not overwhelmed with requests, and the client can receive the updates in a timely manner, but can be altered as needed.

The flow is as follows:

1. The `startProgress()` function is called when the form is submitted.
2. A new connection is created to the `/progress-stream` route using the `EventSource` object.
3. The `/job` route begins 'working', incrementing the global `loaded` variable every 0.05 seconds.
4. Relevant data is streamed to the client every 400ms via the `eventSource.onmessage` function.
5. Our JS script reads the data from the stream and updates both the progress bar and form components.
6. On completion, the `eventSource.close()` function is called to close the connection and the form state is updated.

This documentation is still a work in progress, and will be updated as I continue to work on this project. Feel free to play around with the methods outlined and hopefully they can be useful to you in some way.

---

## Parameters

| Parameter | Description |
| --- | --- |
| `value` | The value of the progress bar. Defaults to `0`. Used in styling the inner bar element. Can be set to any value between `0` and `100`.
| `id` | The id of the progress bar. Automatically generates an `id` attribute for the inner bar element in the form of `id='{Progress bar's id}-inner'`.
