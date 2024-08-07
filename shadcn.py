import sys
import uuid
from functools import wraps

from fasthtml.common import *
from fasthtml.components import Button as OgButton
from fasthtml.components import Input as OgInput

__all__ = [
    "CardHeader",
    "CardFooter",
    "CardTitle",
    "CardDescription",
    "CardContent",
    "ShadHead",
    "Alert",
    "AlertTitle",
    "AlertDescription",
    "Lucide",
]


def ShadHead():
    tw_import = "https://cdn.tailwindcss.com"

    lucide_import = "https://unpkg.com/lucide@latest/dist/umd/lucide.js"

    tw_config = """
    tailwind.config = {
    darkMode: 'selector',
    theme: {
    container: {
      center: true,
      padding: "2rem",
      screens: {
        "2xl": "1400px",
      },
    },
    extend: {
      colors: {
        border: "hsl(var(--border))",
        input: "hsl(var(--input))",
        ring: "hsl(var(--ring))",
        background: "hsl(var(--background))",
        foreground: "hsl(var(--foreground))",
        primary: {
          DEFAULT: "hsl(var(--primary))",
          foreground: "hsl(var(--primary-foreground))",
        },
        secondary: {
          DEFAULT: "hsl(var(--secondary))",
          foreground: "hsl(var(--secondary-foreground))",
        },
        destructive: {
          DEFAULT: "hsl(var(--destructive))",
          foreground: "hsl(var(--destructive-foreground))",
        },
        muted: {
          DEFAULT: "hsl(var(--muted))",
          foreground: "hsl(var(--muted-foreground))",
        },
        accent: {
          DEFAULT: "hsl(var(--accent))",
          foreground: "hsl(var(--accent-foreground))",
        },
        popover: {
          DEFAULT: "hsl(var(--popover))",
          foreground: "hsl(var(--popover-foreground))",
        },
        card: {
          DEFAULT: "hsl(var(--card))",
          foreground: "hsl(var(--card-foreground))",
        },
      },
      borderRadius: {
        lg: `var(--radius)`,
        md: `calc(var(--radius) - 2px)`,
        sm: "calc(var(--radius) - 4px)",
      },
      },
  },
}"""

    tw_globals = """
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    
@layer base {
    :root {
    --background: 0 0% 100%;
    --foreground: 224 71.4% 4.1%;
    --card: 0 0% 100%;
    --card-foreground: 224 71.4% 4.1%;
    --popover: 0 0% 100%;
    --popover-foreground: 224 71.4% 4.1%;
    --primary: 220.9 39.3% 11%;
    --primary-foreground: 210 20% 98%;
    --secondary: 220 14.3% 95.9%;
    --secondary-foreground: 220.9 39.3% 11%;
    --muted: 220 14.3% 95.9%;
    --muted-foreground: 220 8.9% 46.1%;
    --accent: 220 14.3% 95.9%;
    --accent-foreground: 220.9 39.3% 11%;
    --destructive: 0 84.2% 60.2%;
    --destructive-foreground: 210 20% 98%;
    --border: 220 13% 91%;
    --input: 220 13% 91%;
    --ring: 224 71.4% 4.1%;
    --radius: 0.5rem;
    --chart-1: 12 76% 61%;
    --chart-2: 173 58% 39%;
    --chart-3: 197 37% 24%;
    --chart-4: 43 74% 66%;
    --chart-5: 27 87% 67%;
}

.dark {
    --background: 224 71.4% 4.1%;
    --foreground: 210 20% 98%;
    --card: 224 71.4% 4.1%;
    --card-foreground: 210 20% 98%;
    --popover: 224 71.4% 4.1%;
    --popover-foreground: 210 20% 98%;
    --primary: 210 20% 98%;
    --primary-foreground: 220.9 39.3% 11%;
    --secondary: 215 27.9% 16.9%;
    --secondary-foreground: 210 20% 98%;
    --muted: 215 27.9% 16.9%;
    --muted-foreground: 217.9 10.6% 64.9%;
    --accent: 215 27.9% 16.9%;
    --accent-foreground: 210 20% 98%;
    --destructive: 0 62.8% 30.6%;
    --destructive-foreground: 210 20% 98%;
    --border: 215 27.9% 16.9%;
    --input: 215 27.9% 16.9%;
    --ring: 216 12.2% 83.9%;
    --chart-1: 220 70% 50%;
    --chart-2: 160 60% 45%;
    --chart-3: 30 80% 55%;
    --chart-4: 280 65% 60%;
    --chart-5: 340 75% 55%;
}
}
@layer base {
  * {
    @apply border-border;
  }
  body {
    @apply bg-background text-foreground;
    font-feature-settings: "rlig" 1, "calt" 1;
  }
}
"""
    theme_toggle = """
    function toggleTheme() { 

    const html = document.documentElement;
    const theme = html.getAttribute('class');
    const icon = document.getElementById("theme-toggle-icon");

    html.setAttribute('class', theme === 'light' ? 'dark' : 'light');
    icon.setAttribute('data-lucide', theme === 'light' ? 'moon' : 'sun');
    }

    setTimeout(lucide.createIcons(), 200);
    """
    load_lucide="""window.addEventListener('DOMContentLoaded', function() {lucide.createIcons(); document.body.addEventListener('htmx:afterSettle', function(evt) {lucide.createIcons(); console.log("htmxSettle:fired")})});"""
    return (
        Script(src=tw_import),
        Script(src=lucide_import),
        Script(tw_config),
        Style(tw_globals, type="text/tailwindcss"),
        Script(code=theme_toggle),
        Script(code=load_lucide))


btn_variants = {
    "default": "bg-primary text-primary-foreground hover:bg-primary/90",
    "destructive": "bg-destructive text-destructive-foreground hover:bg-destructive/90",
    "outline": "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
    "secondary": "bg-secondary text-secondary-foreground hover:bg-secondary/80",
    "ghost": "hover:bg-accent hover:text-accent-foreground",
    "link": "text-primary underline-offset-4 hover:underline",
}
btn_sizes = {
    "default": "h-10 px-4 py-2",
    "sm": "h-9 rounded-md px-3",
    "lg": "h-11 rounded-md px-8",
    "icon": "h-10 w-10",
}
btn_base_cls = "inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50"
input_base_cls = "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
card_cls = {
    "card": "rounded-lg border bg-card text-card-foreground shadow-sm",
    "head": "flex flex-col space-y-1.5 p-6",
    "title": "text-2xl font-semibold leading-none tracking-tight",
    "description": "text-sm text-muted-foreground",
    "content": "p-6 pt-0",
    "footer": "flex items-center p-6 pt-0",
}
alert_cls = {
    "alert": "relative w-full rounded-lg border p-4 [&>svg~*]:pl-7 [&>svg+div]:translate-y-[-3px] [&>svg]:absolute [&>svg]:left-4 [&>svg]:top-4",
    "title": "mb-1 font-medium leading-none tracking-tight",
    "description": "text-sm [&_p]:leading-relaxed",
}
alert_variants_cls = {
    "default": "bg-background text-foreground [&>svg]:text-foreground",
    "destructive": "border-destructive/50 text-destructive dark:border-destructive [&>svg]:text-destructive",
}


@wraps(OgButton)
def Button(*c, size=None, variant=None, cls=None, **kwargs):
    new_cls = btn_base_cls

    # Add variant class
    new_cls += f" {btn_variants.get(variant, btn_variants['default'])}"

    # Add size class
    new_cls += f" {btn_sizes.get(size, btn_sizes['default'])}"

    # If cls was provided, append it to the new_cls
    if cls:
        new_cls += f" {cls}"

    # Update the kwargs with the new cls
    kwargs["cls"] = new_cls
    return OgButton(*c, **kwargs)


@wraps(OgInput)
def Input(*c, cls=None, **kwargs):
    new_cls = input_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return OgInput(*c, **kwargs)


# Used for the structing of the card element, can be used as you would in structuring
# a shadcn-ui card normally or by using the
# title, description and footer variables on the Card FT itself.


def CardHeader(*c, cls=None, **kwargs):
    new_cls = card_cls["head"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def CardTitle(*c, cls=None, **kwargs):
    new_cls = card_cls["title"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return H1(*c, **kwargs)


def CardDescription(*c, cls=None, **kwargs):
    new_cls = card_cls["description"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return P(*c, **kwargs)


def CardContent(*c, cls=None, **kwargs):
    new_cls = card_cls["content"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def CardFooter(*c, cls=None, **kwargs):
    new_cls = card_cls["footer"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def Card(
    *c,
    title: str = None,
    description: str = None,
    footer=None,
    cls=None,
    standard=False,
    **kwargs,
):
    new_cls = card_cls["card"]

    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls

    if standard:
        return Div(*c, **kwargs)

    header_content = []
    if title:
        header_content.append(CardTitle(title))
    if description:
        header_content.append(CardDescription(description))

    if footer:
        footer = CardFooter(footer)

    if header_content:
        header = CardHeader(
            *header_content,
        )

    return Div(header, CardContent(*c), footer, **kwargs)


def AlertTitle(title: str = None, cls=None, **kwargs):
    new_cls = alert_cls["title"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return H1(title, **kwargs)


def AlertDescription(description: str = None, cls=None, **kwargs):
    new_cls = alert_cls["description"]
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    return P(description, **kwargs)


def Alert(
    *c,
    title: str = None,
    description: str = None,
    variant: str = None,
    cls=None,
    standard=False,
    icon:str=None,
    **kwargs,
):
    new_cls = alert_cls["alert"]
    icon_v = "chevrons-right"
    headers = []
    if variant == "default" or variant == None:
        new_cls += f" {alert_variants_cls["default"]}"
    if variant == "destructive":
        icon_v = "circle-alert"
        new_cls += f" {alert_variants_cls["destructive"]}"

    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    if standard:
        return Div(*c, **kwargs)
    if icon:
        headers.append(Lucide(icon=icon_v, cls="size-4", id=f"alert-icon-{uuid.uuid4()}"))
    else:
        headers.append(Lucide(icon=icon, cls="size-4", id=f"alert-icon-{uuid.uuid4()}"))
    if title:
        headers.append(AlertTitle(title))
    if description:
        headers.append(AlertDescription(description))


    return Div(*headers, *c, **kwargs)


def Lucide(icon:str=None ,cls=None, id=None, **kwargs):
    df_id=None
    df_cls=None

    if id == None:
        df_id=f"icon-{uuid.uuid4()}"

    if cls==None:
        df_cls="size-5"

    df_id=id
    df_cls=cls
    kwargs["cls"] = df_cls
    if icon:
        return I(**{'data-lucide':icon},id=df_id, **kwargs)
    else:
        return I(**{'data-lucide':"accessibility"}, id=df_id, **kwargs)


component_map = [Button, Input, Card]


def override_components():
    module_name = "fasthtml.common"
    module = sys.modules[module_name]
    for component in component_map:
        component_name = component.__name__
        setattr(module, component_name, component)


override_components()
