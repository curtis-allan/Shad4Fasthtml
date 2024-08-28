>[!IMPORTANT]
> This documentation is still under development. For a reference on how to use the component, please refer to the <a href="https://ui.shadcn.com/docs/components" target="_blank">Shadcn-ui documentation</a> and the source code below.

## Installation

Starting with the carousel, I will be attempting to seperate component styling and logic into its own bundle. This will allow you to simply copy and paste the components you need into your project, without needing to add the entire library/ javascript file.

## Source Code

```python
def RadioGroup(*c, cls=None, name=None, defaultValue=None, **kwargs):
    new_cls = "grid gap-2"
    
    surreal_script = Script("""
    proc_htmx('[data-ref="radio-group"]', group => {
        const items = any('[data-ref="radio-item"]', group)
        const hiddenInput = me('[data-ref="hidden-input"]', group)

        function updateRadioGroup(selectedValue) {
            items.run(item => {
                if (item.value === selectedValue) {
                    item.setAttribute('aria-checked', 'true')
                    item.dataset.state = 'checked'
                } else {
                    item.setAttribute('aria-checked', 'false')
                    item.dataset.state = 'unchecked'
                }
            })
            hiddenInput.value = selectedValue
            group.dispatchEvent(new CustomEvent('change', { detail: { value: selectedValue } }))
        }

        items.on('click', (event) => {
            const selectedValue = event.currentTarget.value
            updateRadioGroup(selectedValue)
        })

        // Set initial value if provided
        if (group.dataset.value) {
            updateRadioGroup(group.dataset.value)
        }
    })
    """)

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    return Div(
        surreal_script,
        *c,
        Input(type="hidden", data_ref="hidden-input", name=name, value=defaultValue),
        data_ref="radio-group",
        role="radiogroup",
        aria_required="false",
        style="outline:none;",
        data_value=defaultValue,
        **kwargs
    )

def RadioGroupItem(cls=None, value=None, **kwargs):
    new_cls = "group cursor-pointer aspect-square h-4 w-4 rounded-full border border-primary text-primary ring-offset-background focus:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
    indicator_cls = "hidden group-data-[state=checked]:flex items-center justify-center"
    circle_cls = "h-2.5 w-2.5 fill-current text-current"

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    return ft_hx('button',
        Span(
            Lucide(icon="circle", cls=circle_cls),
            cls=indicator_cls,
            data_state="unchecked",
        ),
        data_ref="radio-item",
        value=value,
        role="radio",
        type='button',
        aria_checked="false",
        tabindex="0",
        **kwargs
    )

```