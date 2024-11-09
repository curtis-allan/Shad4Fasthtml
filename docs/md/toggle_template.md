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

The `Toggle` component, similarly to a button, takes both an optional `variant` and `size` attribute. The variant can be either `default` or `outline`, and the size can be either `sm`, `default` or `lg`, all of which are displayed above.

Best practise for accessibility concerns is to include an `aria-label` attribute on custom elements. In the case of toggles, you can define a custom aria_label to describe what the actual element is, or simply omit it to have the `Toggle Button` label applied.

```py
Toggle(Lucide('bold'), aria_label="Toggle Bold", size="default", variant="default")
```

> [!TIP]
> All custom attributes are optional. Both the variant and size will render as `default` while the aria-label will be set to `Toggle Button`.

---

## Parameters

| Attribute | Type  | Description                                                                                                                          |
| --------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `variant` | `str` | Options for both a `default` and `outline` variant. Defaults to `default`, which renders similar to the `ghost` variant of a button. |
| `size`    | `str` | Changes the size of the rendered toggle. Options for either `sm`, `default` or `lg`. Defaults to `default`.                          |
