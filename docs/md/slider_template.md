>[!IMPORTANT]
> This documentation is still under development. For a reference on how to use the component, please refer to the <a href="https://ui.shadcn.com/docs/components" target="_blank">Shadcn-ui documentation</a> and the source code below.

## Installation

Starting with the carousel, I will be attempting to seperate component styling and logic into its own bundle. This will allow you to simply copy and paste the components you need into your project, without needing to add the entire library/ javascript file.

## Source Code

```python
def Slider(cls=None, min=0, max=100, step=1, value=0, name=None, **kwargs):
    new_cls = "relative flex w-full touch-none select-none items-center"

    surreal_script = Script("""
proc_htmx('[data-ref="slider"]', slider => {
    const track = me('[data-ref="track"]', slider)
    const range = me('[data-ref="range"]', slider)
    const thumb = me('[data-ref="thumb"]', slider)
    const hiddenInput = me('[data-ref="hidden-input"]', slider)

    const {min, max, step, value} = slider.dataset
    let currentValue = parseInt(value) || 0

    function updateSlider() {
        const percentage = ((currentValue - min) / (max - min)) * 100
        range.style.width = `${percentage}%`
        thumb.style.left = `${percentage}%`
        hiddenInput.value = currentValue
    }

    function handleMove(clientX) {
        const rect = track.getBoundingClientRect()
        const percentage = (clientX - rect.left) / rect.width
        currentValue = Math.round((percentage * (max - min) + parseInt(min)) / step) * step
        currentValue = Math.max(min, Math.min(max, currentValue))
        updateSlider()
        slider.dispatchEvent(new CustomEvent('change', { detail: { value: currentValue } }))
    }

    function addDragListeners(startEvent) {
        startEvent.preventDefault()
        const moveHandler = moveEvent => handleMove(moveEvent.clientX)
        const upHandler = () => {
            document.removeEventListener('mousemove', moveHandler)
            document.removeEventListener('mouseup', upHandler)
        }
        document.addEventListener('mousemove', moveHandler)
        document.addEventListener('mouseup', upHandler)
    }

    track.on('mousedown', e => {
        handleMove(e.clientX)
        addDragListeners(e)
    })

    thumb.on('mousedown', addDragListeners)

    updateSlider()
})
""")

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    return Div(
        surreal_script,
        Div(
            Div(data_ref="range", cls="absolute h-full bg-primary"),
            data_ref="track",
            cls="relative h-2 w-full grow overflow-hidden rounded-full bg-secondary"
        ),
        Div(
            data_ref="thumb",
            cls="absolute top-1/2 -translate-x-1/2 -translate-y-1/2 block h-5 w-5 rounded-full border-2 border-primary bg-background ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
        ),
        Input(type="hidden", data_ref="hidden-input", name=name, value=value),
        data_max=max,
        data_step=step,
        data_value=value,
        role="slider",
        data_min=min,
        data_ref="slider",
        aria_valuemin=min,
        aria_valuemax=max,
        aria_valuenow=value,
        **kwargs
    )
```
