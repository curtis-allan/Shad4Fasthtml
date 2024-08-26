## Setup

All component imports are included when using the default setup. If you wish to seperately import components you can do so too. 

```python
from fasthtml import *
from shadcn import ShadHead, Input
```

Just make sure to import and setup `ShadHead()` as well:

```python
app, rt = fast_app(pico=False, hdrs=(ShadHead(),))
```
---

## Usage

To use the input component, structure your code as with a normal FT method. Parameters follow the same structure as a normal `<input>` tag. For a full usage guide, check out the Mozilla docs <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input" target="_blank">here.</a> 

```python+html
Input(placeholder="Enter something", type="text", id="title")
```

The state of the checkbox on initial render can be set via the `state` attribute. The default state is `unchecked` when omitted.