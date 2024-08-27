>[!IMPORTANT]
> This documentation is still under development. For a reference on how to use the component, please refer to the <a href="https://ui.shadcn.com/docs/components" target="_blank">Shadcn-ui documentation</a> and the source code below.

## Installation

Starting with the carousel, I will be attempting to seperate component styling and logic into its own bundle. This will allow you to simply copy and paste the components you need into your project, without needing to add the entire library/ javascript file.

## Source Code

```python
def Carousel(*c, cls=None, orientation:str='horizontal', autoplay:bool=False, duration:str='500', **kwargs):
    new_cls = "relative w-full"

    surreal_script = Script("""
    proc_htmx('[data-ref="carousel"]', carousel => {
    const items = any('[data-carousel-item]', carousel)
    const content = me('[data-ref="content"]', carousel)
    const prevButton = me('[data-ref="prevButton"]', carousel)
    const nextButton = me('[data-ref="nextButton"]', carousel)

    const {autoplay, orientation, duration} = carousel.dataset

    let currentIndex = 0;

            if (orientation === 'vertical') {
                items.run(item => {
                    item.classAdd('pt-4');
                });
                content.classAdd('-mt-4', 'flex-col')
                prevButton.classList.add('-top-12', 'left-1/2', '-translate-x-1/2', 'rotate-90');
                nextButton.classList.add('-bottom-12', 'left-1/2', '-translate-x-1/2', 'rotate-90');

            } else {
                items.run(item => {
                    item.classAdd('pl-4');
                });
                content.classAdd('-ml-4');
                prevButton.classList.add('-left-12', 'top-1/2', '-translate-y-1/2');
                nextButton.classList.add('-right-12', 'top-1/2', '-translate-y-1/2');
            }

            function updateCarousel() {
                content.style.transform = `translateX(-${currentIndex * 100}%)`;
            }

            prevButton.on('click', () => {
                currentIndex = (currentIndex - 1 + items.length) % items.length;
                updateCarousel();
            });

    nextButton.on('click', () => {
        currentIndex = (currentIndex + 1) % items.length;
        updateCarousel();
    });


    if (autoplay === 'true') {
        setInterval(() => {
            currentIndex = (currentIndex + 1) % items.length;
            updateCarousel();
        }, 5000);
        }
    })""")

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] =new_cls

    return Div(
            surreal_script,
            *c,
            data_autoplay='true' if autoplay else 'false',
            data_orientation=orientation,
            data_duration=duration,
            data_ref="carousel",
            role="region",
            aria_roledescription="carousel",
            **kwargs
        )

def CarouselContent(*c, cls=None, **kwargs):
    new_cls = "flex transition-transform ease-in-out duration-500"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(Div(*c, data_ref="content", **kwargs), cls="overflow-hidden")

def CarouselItem(*c, cls=None, **kwargs):
    new_cls = "min-w-0 shrink-0 grow-0 basis-full",
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, data_carousel_item=True, **kwargs)

def CarouselPrevious(icon='arrow-left', cls=None, **kwargs):
    new_cls = "absolute h-8 w-8 !rounded-full"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(Lucide(icon=icon, cls='size-4'),
                variant="outline",
                size="icon", data_ref="prevButton", **kwargs)

def CarouselNext(icon='arrow-right', cls=None, **kwargs):
    new_cls = "absolute h-8 w-8 !rounded-full"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(Lucide(icon=icon, cls='size-4'),
                variant="outline",
                size="icon", data_ref="nextButton", **kwargs)
```