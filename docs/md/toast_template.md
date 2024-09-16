## Setup

Make sure the relevant packages are installed, and setup the imports as shown below.

> [!NOTE]
> If you wish to seperately import components you can do so too. Make sure to import and setup `ShadHead()` as well.

```python
from fasthtml import *
from shad4fast import *

app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```

---

## Usage

To use a toast, you must return it as a response to a route call. For a full reference to available attribute options, see the parameter table below:

```python
// Setup the toast handler function under the app setup

    toast_setup(app)

// Use a button to trigger the toast route

    Button("Send email", hx_get="/toast", hx_swap="none")

// Add a toast function to the route return statement

    @rt("/toast")
    def get(sess):
        toast(sess=sess, title="Sent!", description="Email has been sent successfully.")
```

---

## Parameters

| Parameter     | Type  | Description                                                                        |
| ------------- | ----- | ---------------------------------------------------------------------------------- |
| `variant`     | `str` | The variant of the toast. Can be `default` or `destructive`. Default is `default`. |
| `sess`        | `str` | The current session object.                                                        |
| `title`       | `str` | The title of the toast.                                                            |
| `description` | `str` | The description of the toast.                                                      |
