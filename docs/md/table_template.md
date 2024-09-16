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

To use the table component, structure your code as with a normal FT method. Parameters follow the same logic as a standard `table` tag.

```python
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
    TableBody(
        TableRow(
                TableCell("INV001", cls="font-medium"),
                TableCell("Paid"),
                TableCell('Credit Card'),
                TableCell('$250.00', cls="text-right"),
            ),TableRow(
                TableCell('INV002', cls="font-medium"),
                TableCell('Pending'),
                TableCell('PayPal'),
                TableCell('$150.00', cls="text-right"),
            ),TableRow(
                TableCell('INV003', cls="font-medium"),
                TableCell('Unpaid'),
                TableCell('Bank Transfer'),
                TableCell('$350.00', cls="text-right"),
            )),
    TableFooter(
        TableRow(
            TableCell("Total", colSpan="3"),
            TableCell("$750.00", cls="text-right"),
        )
    ),
)
```

---

## Parameters

For a full reference for attribute options, check out the Mozilla docs for the input tag<a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table" target="_blank">here.</a>
