>[!IMPORTANT]
> This documentation is still under development. For a reference on how to use the component, please refer to the <a href="https://ui.shadcn.com/docs/components" target="_blank">Shadcn-ui documentation</a> and the source code below.

## Installation

Starting with the carousel, I will be attempting to seperate component styling and logic into its own bundle. This will allow you to simply copy and paste the components you need into your project, without needing to add the entire library/ javascript file.

## Source Code

```python
def Tabs(*c, default_value=None, **kwargs):

    surreal_script = Script("""
    proc_htmx('[data-ref="tabs"]', tabs => {
        const triggers = any('[data-tab-trigger]', tabs)
        const contents = any('[data-tab-content]', tabs)
        
        function setActiveTab(value) {
            triggers.run(trigger => {
                if (trigger.dataset.value === value) {
                    trigger.dataset.state = 'active'
                    trigger.setAttribute('aria-selected', 'true')
                } else {
                    trigger.dataset.state = ''
                    trigger.setAttribute('aria-selected', 'false')
                }
            })
            
            contents.run(content => {
                if (content.dataset.value === value) {
                    content.dataset.state = 'active'
                    content.removeAttribute('hidden')
                } else {
                    content.dataset.state = ''
                    content.setAttribute('hidden', '')
                }
            })
        }
        
        triggers.on('click', (event) => {
            const value = event.currentTarget.dataset.value
            setActiveTab(value)
        })
        
        // Set initial active tab
        const defaultValue = tabs.dataset.defaultValue
        if (defaultValue) {
            setActiveTab(defaultValue)
        } else if (triggers.length > 0) {
            setActiveTab(triggers[0].dataset.value)
        }
    })
    """)

    return Div(*c,surreal_script, data_ref="tabs", data_default_value=default_value, **kwargs)

def TabsList(*c, cls=None, **kwargs):
    new_cls = "inline-flex h-10 items-center justify-center rounded-md bg-muted p-1 text-muted-foreground"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, role="tablist", **kwargs, tabindex=0)

def TabsTrigger(*c, cls=None, value=None, **kwargs):
    new_cls = "inline-flex items-center justify-center whitespace-nowrap rounded-sm px-3 py-1.5 text-sm font-medium ring-offset-background transition-all focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 data-[state=active]:bg-background data-[state=active]:text-foreground data-[state=active]:shadow-sm"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return ft_hx('button', type='button',*c, role="tab", data_tab_trigger=True, data_value=value, **kwargs)

def TabsContent(*c, cls=None, value=None, **kwargs):
    new_cls = "mt-2 ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, role="tabpanel", data_tab_content=True, data_value=value, hidden=True, **kwargs)
```