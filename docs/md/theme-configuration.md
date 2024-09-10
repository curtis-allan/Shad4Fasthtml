
## Changing the theme

Shad4FastHtml follows a similar structure to the original Shadcn theme configuration. Changing your theme is as easy as it is within the original package. If using the Tailwindcss standalone setup, simply open the `globals.css` file and replace these values: 

```css
@layer base {
    :root {
        --background: 0 0% 100%;
        --foreground: 240 10% 3.9%;
        --card: 0 0% 100%;
        --card-foreground: 240 10% 3.9%;
        --popover: 0 0% 100%;
        --popover-foreground: 240 10% 3.9%;
        --primary: 240 5.9% 10%;
        --primary-foreground: 0 0% 98%;
        --secondary: 240 4.8% 95.9%;
        --secondary-foreground: 240 5.9% 10%;
        --muted: 240 4.8% 95.9%;
        --muted-foreground: 240 3.8% 46.1%;
        --accent: 240 4.8% 95.9%;
        --accent-foreground: 240 5.9% 10%;
        --destructive: 0 84.2% 60.2%;
        --destructive-foreground: 0 0% 98%;
        --border: 240 5.9% 90%;
        --input: 240 5.9% 90%;
        --ring: 240 5.9% 10%;
        --radius: 0.5rem;
        --chart-1: 12 76% 61%;
        --chart-2: 173 58% 39%;
        --chart-3: 197 37% 24%;
        --chart-4: 43 74% 66%;
        --chart-5: 27 87% 67%;
    }

    .dark {
        --background: 240 10% 3.9%;
        --foreground: 0 0% 98%;
        --card: 240 10% 3.9%;
        --card-foreground: 0 0% 98%;
        --popover: 240 10% 3.9%;
        --popover-foreground: 0 0% 98%;
        --primary: 0 0% 98%;
        --primary-foreground: 240 5.9% 10%;
        --secondary: 240 3.7% 15.9%;
        --secondary-foreground: 0 0% 98%;
        --muted: 240 3.7% 15.9%;
        --muted-foreground: 240 5% 64.9%;
        --accent: 240 3.7% 15.9%;
        --accent-foreground: 0 0% 98%;
        --destructive: 0 62.8% 30.6%;
        --destructive-foreground: 0 0% 98%;
        --border: 240 3.7% 15.9%;
        --input: 240 3.7% 15.9%;
        --ring: 240 4.9% 83.9%;
        --chart-1: 220 70% 50%;
        --chart-2: 160 60% 45%;
        --chart-3: 30 80% 55%;
        --chart-4: 280 65% 60%;
        --chart-5: 340 75% 55%;
    }
}
```

You can adjust the colours/styles however you wish. For ease of use, you can simply go <a href="https://ui.shadcn.com/themes" target="_blank">here</a>, choose a theme configuration you like and copy/paste the config over the matching section.

>[!NOTE]
> If using tailwind via cdn, you can still change the default theme configuration. To do this, locate the `headers.py` file within the shad4fast installation and locate the matching styles. Then you can simply replace them as shown above.

## Setting up light/dark mode

Theme handling can be a useful addition to any web application and is becoming more prevalent in modern sites. To simplify the usage of a light/dark mode system, Shad4Fast includes an optional script that can be toggled in the header as shown here:

```python
app, rt = fast_app(
    pico=False,
    hdrs=(ShadHead(theme_handle=True),),
)
```

Both of the in-built Tailwind setup methods include the default Shadcn theme for both light and dark mode by default. Setting the `theme_handle` attribute in the header will include a script within the `head` tag of your website that provides the bare essentials:

* System theme detection, using the `@media` css query.
* Caching of prefered theme in local browser storage.
* `Dark` class toggling of the html tag.

By simply setting the theme_handle to true, users with a preferred system theme of `dark` will have the dark colourscheme applied and vice versa.

## Theme Toggle

The `theme_handle` headers also include javascript that allows for the manual swapping of the pages theme. This can be done by adding the class `theme-toggle` to a button (or component). When this is clicked, both the `dark` class of the html tag and the `theme` setting saved in local browser storage will be toggled. This allows for users to change the theme manually, and maintain that current theme across page navigations (including refreshes and browser exiting). 

Below is the theme toggle component used in this site. Using pure tailwindcss to toggle the visible icon and the `theme-toggle` class, this allows for a simple yet fully functioning and reactive theme toggle button:

```python
from shad4fast import Button
from lucide_fasthtml import Lucide

def ThemeToggle(variant="outline", cls=None, **kwargs):
    return Button(
        Lucide("sun", cls="dark:flex hidden"),
        Lucide("moon", cls="dark:hidden"),
        variant=variant,
        size="icon",
        cls=f"theme-toggle {cls}",
        **kwargs,
    )
```
