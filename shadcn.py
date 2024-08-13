import sys
import uuid

from fasthtml.common import *
from fasthtml.components import Button as OgButton
from fasthtml.components import Input as OgInput
from fasthtml.components import Label as OgLabel
from fasthtml.components import Textarea as OgTextarea
from fasthtml.toaster import *

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
    "Badge",
    "Separator",
    "Progress",
    "ProgressInner",
    "toast",
    "Toaster",
    "toast_setup",
    "Dialog",
    "DialogHeader",
    "DialogTitle",
    "DialogDescription",
    "DialogContent",
    "DialogFooter",
    "DialogTrigger",
    "Button",
    "Input",
    "Textarea",
    "Label",
    "Switch",
]


def ShadHead(lucid=True):
    tw_import = "https://cdn.tailwindcss.com"

    lucide_import = "https://unpkg.com/lucide@latest/dist/umd/lucide.js"

    tw_config = """
    function filterDefault(values) {
	return Object.fromEntries(
		Object.entries(values).filter(([key]) => key !== "DEFAULT"),
	)
}

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
        animation: {
        "accordion-down": "accordion-down 0.2s ease-out",
        "accordion-up": "accordion-up 0.2s ease-out",
      },
        animationDelay: ({ theme }) => ({
					...theme("transitionDelay"),
				}),
				animationDuration: ({ theme }) => ({
					0: "0ms",
					...theme("transitionDuration"),
				}),
				animationTimingFunction: ({ theme }) => ({
					...theme("transitionTimingFunction"),
				}),
				animationFillMode: {
					none: "none",
					forwards: "forwards",
					backwards: "backwards",
					both: "both",
				},
				animationDirection: {
					normal: "normal",
					reverse: "reverse",
					alternate: "alternate",
					"alternate-reverse": "alternate-reverse",
				},
				animationOpacity: ({ theme }) => ({
					DEFAULT: 0,
					...theme("opacity"),
				}),
				animationTranslate: ({ theme }) => ({
					DEFAULT: "100%",
					...theme("translate"),
				}),
				animationScale: ({ theme }) => ({
					DEFAULT: 0,
					...theme("scale"),
				}),
				animationRotate: ({ theme }) => ({
					DEFAULT: "30deg",
					...theme("rotate"),
				}),
				animationRepeat: {
					0: "0",
					1: "1",
					infinite: "infinite",
				},
				keyframes: {
					enter: {
						from: {
							opacity: "var(--tw-enter-opacity, 1)",
							transform:
								"translate3d(var(--tw-enter-translate-x, 0), var(--tw-enter-translate-y, 0), 0) scale3d(var(--tw-enter-scale, 1), var(--tw-enter-scale, 1), var(--tw-enter-scale, 1)) rotate(var(--tw-enter-rotate, 0))",
						},
					},
					exit: {
						to: {
							opacity: "var(--tw-exit-opacity, 1)",
							transform:
								"translate3d(var(--tw-exit-translate-x, 0), var(--tw-exit-translate-y, 0), 0) scale3d(var(--tw-exit-scale, 1), var(--tw-exit-scale, 1), var(--tw-exit-scale, 1)) rotate(var(--tw-exit-rotate, 0))",
						},
					},
          "accordion-down": {
          from: { height: "0" },
          to: { height: "var(--radix-accordion-content-height)" },
        },
        "accordion-up": {
          from: { height: "var(--radix-accordion-content-height)" },
          to: { height: "0" },
        },
				},
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
  plugins: [
	function ({ addUtilities, matchUtilities, theme }) {
		addUtilities({
			"@keyframes enter": theme("keyframes.enter"),
			"@keyframes exit": theme("keyframes.exit"),
			".animate-in": {
				animationName: "enter",
				animationDuration: theme("animationDuration.DEFAULT"),
				"--tw-enter-opacity": "initial",
				"--tw-enter-scale": "initial",
				"--tw-enter-rotate": "initial",
				"--tw-enter-translate-x": "initial",
				"--tw-enter-translate-y": "initial",
			},
			".animate-out": {
				animationName: "exit",
				animationDuration: theme("animationDuration.DEFAULT"),
				"--tw-exit-opacity": "initial",
				"--tw-exit-scale": "initial",
				"--tw-exit-rotate": "initial",
				"--tw-exit-translate-x": "initial",
				"--tw-exit-translate-y": "initial",
			},
		})

		matchUtilities(
			{
				"fade-in": (value) => ({ "--tw-enter-opacity": value }),
				"fade-out": (value) => ({ "--tw-exit-opacity": value }),
			},
			{ values: theme("animationOpacity") },
		)

		matchUtilities(
			{
				"zoom-in": (value) => ({ "--tw-enter-scale": value }),
				"zoom-out": (value) => ({ "--tw-exit-scale": value }),
			},
			{ values: theme("animationScale") },
		)

		matchUtilities(
			{
				"spin-in": (value) => ({ "--tw-enter-rotate": value }),
				"spin-out": (value) => ({ "--tw-exit-rotate": value }),
			},
			{ values: theme("animationRotate") },
		)

		matchUtilities(
			{
				"slide-in-from-top": (value) => ({
					"--tw-enter-translate-y": `-${value}`,
				}),
				"slide-in-from-bottom": (value) => ({
					"--tw-enter-translate-y": value,
				}),
				"slide-in-from-left": (value) => ({
					"--tw-enter-translate-x": `-${value}`,
				}),
				"slide-in-from-right": (value) => ({
					"--tw-enter-translate-x": value,
				}),
				"slide-out-to-top": (value) => ({
					"--tw-exit-translate-y": `-${value}`,
				}),
				"slide-out-to-bottom": (value) => ({
					"--tw-exit-translate-y": value,
				}),
				"slide-out-to-left": (value) => ({
					"--tw-exit-translate-x": `-${value}`,
				}),
				"slide-out-to-right": (value) => ({
					"--tw-exit-translate-x": value,
				}),
			},
			{ values: theme("animationTranslate") },
		)

		matchUtilities(
			{ duration: (value) => ({ animationDuration: value }) },
			{ values: filterDefault(theme("animationDuration")) },
		)

		matchUtilities(
			{ delay: (value) => ({ animationDelay: value }) },
			{ values: theme("animationDelay") },
		)

		matchUtilities(
			{ ease: (value) => ({ animationTimingFunction: value }) },
			{ values: filterDefault(theme("animationTimingFunction")) },
		)

		addUtilities({
			".running": { animationPlayState: "running" },
			".paused": { animationPlayState: "paused" },
		})

		matchUtilities(
			{ "fill-mode": (value) => ({ animationFillMode: value }) },
			{ values: theme("animationFillMode") },
		)

		matchUtilities(
			{ direction: (value) => ({ animationDirection: value }) },
			{ values: theme("animationDirection") },
		)

		matchUtilities(
			{ repeat: (value) => ({ animationIterationCount: value }) },
			{ values: theme("animationRepeat") },
		)
	},
  ],
}"""

    tw_globals = """
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    

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
@layer base {
  * {
    @apply border-border antialiased;
  }
  body {
    @apply bg-background text-foreground;
    font-feature-settings: "rlig" 1, "calt" 1;
  }
}
"""
    shad_scripts = """
    function toggleTheme() { 

    const html = document.documentElement;
    const theme = html.getAttribute('class');
    const icon = document.getElementById("theme-toggle-icon");

    html.setAttribute('class', theme === 'light' ? 'dark' : 'light');
    }
    """
    load_lucide="""htmx.onLoad(() => lucide.createIcons());"""

    if lucid:
        return (
            Script(src=tw_import),
            Script(src=lucide_import),
            Script(tw_config),
            Style(tw_globals, type="text/tailwindcss"),
            Script(code=shad_scripts),
            Script(code=load_lucide),
            Script(code=dialog_script),)
    else:
        return (
            Script(src=tw_import),
            Script(tw_config),
            Style(tw_globals, type="text/tailwindcss"),
            Script(code=shad_scripts),
            Script(code=dialog_script),)


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
badge_cls = "inline-flex items-center rounded-full border px-2.5 py-0.5 text-xs font-semibold transition-colors focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2"
badge_variants_cls = {
        "default":
          "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
        "secondary":
          "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
        "destructive":
          "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
        "outline": "text-foreground",
}
sep_cls = "shrink-0 bg-border"
sep_variant_cls={"horizontal": "h-[1.5px] w-full", "vertical": "self-stretch w-[1.5px]"}
progress_cls = "relative h-4 w-full overflow-hidden rounded-full bg-secondary"
progress_inner_cls = "h-full w-full flex-1 bg-primary transition-all"
toast_container_cls = "fixed top-0 z-[100] flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-0 sm:right-0 sm:top-auto sm:flex-col md:max-w-[420px] transition-transform duration-300"
toast_base_cls = "group pointer-events-auto relative flex w-full items-center justify-between space-x-4 overflow-hidden rounded-md border p-6 pr-8 shadow-lg toast"
toast_variants_cls = {"default": "border bg-background text-foreground", "destructive":"destructive group border-destructive bg-destructive text-destructive-foreground"}
toast_closeBtn_cls = "toast-close-button cursor-pointer active:ring absolute right-2 top-2 rounded-md p-1 text-foreground/50 opacity-0 transition-opacity hover:text-foreground focus:opacity-100 focus:outline-none focus:ring-2 group-hover:opacity-100 group-[.destructive]:text-red-300 group-[.destructive]:hover:text-red-50 group-[.destructive]:focus:ring-red-400 group-[.destructive]:focus:ring-offset-red-600"
toast_title_cls = "text-sm font-semibold"
toast_description_cls = "text-sm opacity-90"
dialog_overlay_cls = "dialog-overlay fixed inset-0 z-50 bg-black/80 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0"
dialog_content_cls= "dialog-content fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[state=closed]:slide-out-to-left-1/2 data-[state=closed]:slide-out-to-top-[48%] data-[state=open]:slide-in-from-left-1/2 data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg"
dialog_closeBtn_cls = "dialog-close-btn cursor-pointer active:ring absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none data-[state=open]:bg-accent data-[state=open]:text-muted-foreground"
dialog_title_cls = "text-lg font-semibold leading-none tracking-tight"
dialog_description_cls = "text-sm text-muted-foreground"
dialog_header_cls = "flex flex-col space-y-1.5 text-center sm:text-left"
dialog_footer_cls =  "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2"
textarea_cls = "flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
label_cls = "select-none text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
switch_base_cls = "peer inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=unchecked]:bg-input"
switch_thumb_cls="pointer-events-none block h-5 w-5 rounded-full bg-background shadow-lg ring-0 transition-transform data-[state=checked]:translate-x-5 data-[state=unchecked]:translate-x-0"


def Button(*c, size='default', variant='default', cls=None, **kwargs):
    new_cls = btn_base_cls

    new_cls += f" {btn_variants[variant]} {btn_sizes[size]}"

    # If cls was provided, append it to the new_cls
    if cls:
        new_cls += f" {cls}"

    # Update the kwargs with the new cls
    kwargs["cls"] = new_cls
    return OgButton(*c, **kwargs)

def Input(*c, cls=None, **kwargs):
    new_cls = input_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return OgInput(*c, **kwargs)

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
        headers.append(Lucide(icon=icon, cls="size-4", id=f"alert-icon-{uuid.uuid4()}"))
    else:
        headers.append(Lucide(icon=icon_v, cls="size-4", id=f"alert-icon-{uuid.uuid4()}"))
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

def Badge(*c, variant:str=None, cls=None, **kwargs):
    new_cls = badge_cls
    if cls:
        new_cls += f" {cls}"
    if variant == 'default' or variant == None:
        new_cls += f" {badge_variants_cls['default']}"
    if variant == 'secondary':
        new_cls += f" {badge_variants_cls['secondary']}"
    if variant == 'destructive':
        new_cls += f" {badge_variants_cls['destructive']}"
    if variant == 'outline':
        new_cls += f" {badge_variants_cls['outline']}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)

def Separator(orientation:str='horizontal', cls=None, **kwargs):
    new_cls = sep_cls

    if orientation == 'horizontal' or orientation == None:
        new_cls += f" {sep_variant_cls["horizontal"]}"
    if orientation == 'vertical':
        new_cls += f" {sep_variant_cls['vertical']}"

    if cls:
        new_cls += f" {cls}"
    
    kwargs["cls"] = new_cls
    return Div(decorative=True, **kwargs)

def ProgressInner(id:str=None):
    style = "transform: translateX(-101%)"
    return Div(style=style, id=id, cls=progress_inner_cls)

def Progress(*c,id:str=None,cls=None, **kwargs):
    new_cls = progress_cls
    script = Script("""function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function handleClick() {
    const total = 100;
    const progress = htmx.find("#progress-inner");
    for (let i = 20; i <= total; i+=20) {
        progress.style.transform = `translateX(-${100-i}%)`;
        await sleep(700);
    }
}""")
    if cls:
        new_cls += f" { cls}"
    kwargs["cls"] = new_cls
    return Div(*c, script, id=id, **kwargs)

toast_script = """
export function proc_htmx(sel, func) {
  htmx.onLoad(elt => {
    const elements = any(sel, elt, false);
    if (elt.matches && elt.matches(sel)) elements.unshift(elt);
    elements.forEach(func);
  });
}

proc_htmx('#toast-container', function(toast) {
  let dismissTimeout;
  const closeButton = toast.querySelector('.toast-close-button');
  const duration = 6000;

  function dismissToast() {
    clearTimeout(dismissTimeout);
    toast.style.transform = 'translateX(100%)';
    setTimeout(() => toast.remove(), 300);
  }

  function resetTimer() {
    clearTimeout(dismissTimeout);
    dismissTimeout = setTimeout(dismissToast, duration);
  }

  // Mouse drag functionality
  let isDragging = false;
  let startX;
  let originalTransform;
  const threshold = 100;

  toast.addEventListener('mousedown', e => {
    e.preventDefault(); // Prevent text selection
    toast.style.transition = 'none';
    isDragging = true;
    startX = e.clientX;
    originalTransform = window.getComputedStyle(toast).transform;

  });

  toast.addEventListener('mousemove', e => {
    if (!isDragging) return
    resetTimer();
    let deltaX = e.clientX - startX;
    if (deltaX > 0) {
      toast.style.transform = `translateX(${deltaX}px)`;
    }
  });

  toast.addEventListener('mouseup', e => {
    if (!isDragging) return;
    toast.style.transition = 'transform 0.2s';
    isDragging = false;
    let deltaX = e.clientX - startX;
    if (deltaX >= threshold) {
      dismissToast();
    } else {
      toast.style.transform = 'translateX(0)';
    }
  });

if (closeButton) closeButton.addEventListener('click', dismissToast);

  toast.addEventListener('mouseleave', resetTimer);

  resetTimer();
});
"""

toast_styles = """@keyframes slideInFromTop {
  from { transform: translateY(-100%); }
  to { transform: translateY(0); }
}

@keyframes slideInFromBottom {
  from { transform: translateY(100%); }
  to { transform: translateY(0); }
}

.toast {
  animation-duration: 0.2s;
  animation-fill-mode: forwards;
}

@media (max-width: 640px) {
  .toast {
    animation-name: slideInFromTop;
  }
}

@media (min-width: 641px) {
  .toast {
    animation-name: slideInFromBottom;
  }
}
"""

def toast(sess, title, description, variant="default"):
    assert variant in ("default", "destructive"), '`variant` not in ("default", "destructive")'
    sess.setdefault(sk, []).append((title, description, variant))

def Toaster(sess):
    closeBtn = Div(Lucide(icon="x", cls="size-4"), cls=toast_closeBtn_cls)
    toasts = [Div(P(title, cls=toast_title_cls),P(description, cls=toast_description_cls), closeBtn, cls=f"{toast_base_cls} {toast_variants_cls[variant]}") for title,description,variant in sess.pop(sk, [])]
    return Div(Div(*toasts, cls=toast_container_cls, id="toast-container"),
               hx_swap_oob="afterbegin:body")

def toast_setup(app):
    app.router.hdrs += (Style(toast_styles), Script(toast_script, type="module"))
    app.router.after.append(after_toast)

def after_toast(resp, req, sess):
    if sk in sess: req.injects.append(Toaster(sess))

def DialogHeader(*c,cls=None, **kwargs):
    new_cls = dialog_header_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)

def DialogFooter(*c, cls=None, **kwargs):
    new_cls = dialog_footer_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)

def DialogTitle(*c,cls=None, **kwargs):
    new_cls = dialog_title_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return H1(*c, **kwargs)

def DialogDescription(*c,cls=None, **kwargs):
    new_cls = dialog_description_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return P(*c, **kwargs)

def DialogContent(*c,cls=None, **kwargs):
    closeBtn = Div(Lucide(icon='x', cls=f'size-4'), Span("Close", cls='sr-only'),cls=dialog_closeBtn_cls)
    new_cls = dialog_content_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c,closeBtn, data_state='open', **kwargs)

def DialogTrigger(*c, target=None, cls=None, **kwargs):
    new_cls = ''
    if cls:
      new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(*c ,hx_get=f"/{target}", hx_swap="beforeend", hx_target="body", **kwargs)

dialog_script = """
  function proc_htmx(sel, func) {
  htmx.onLoad(elt => {
    const elements = any(sel, elt, false);
    if (elt.matches && elt.matches(sel)) elements.unshift(elt);
    elements.forEach(func);
  });
}

  proc_htmx('.dialog', function(dialog) {
    const overlay = dialog.querySelector('.dialog-overlay');
    const closeBtn = dialog.querySelector('.dialog-close-btn');
    const content = dialog.querySelector('.dialog-content');

    function toggleClose() {
    content.dataset.state = 'closed';
    overlay.dataset.state = 'closed';
    setTimeout(() => dialog.remove(), 110);
    }

    if(closeBtn) closeBtn.addEventListener('click', toggleClose);
    if(overlay) overlay.addEventListener('click', toggleClose);
  })
"""

def Dialog(*c,footer=None, title=None, description=None, standard=False,cls=None, **kwargs):
    overlay = Div(cls=dialog_overlay_cls, data_state="open")

    new_cls = 'dialog'
    if cls:
      new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    if standard:
        return Div(overlay, *c, **kwargs)

    header_content = []
    if title:
      header_content.append(DialogTitle(title))
    if description:
      header_content.append(DialogDescription(description))
    if footer:
        footer = DialogFooter(footer)

    if header_content:
        header = DialogHeader(
            *header_content,
        )

    return Div(overlay, DialogContent(header, *c, footer), **kwargs)

def Textarea(*c, cls=None, **kwargs):
    new_cls = textarea_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return OgTextarea(*c, **kwargs)
  
def Label(*c, htmlFor=None, cls=None, **kwargs):
    new_cls = label_cls
    if cls:
      new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return OgLabel(*c, **{'for': htmlFor}, **kwargs)

def Switch(state="unchecked",cls=None, id=None, name=None, **kwargs):
    assert state in ("checked", "unchecked"), '`state` not in ("checked", "unchecked")'

    new_cls = switch_base_cls
    if cls:
      new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    thumb = Span(cls=switch_thumb_cls)
    return Div(thumb,Input(type='checkbox', style="display: none;", id=id, name=name, checked='false'), data_state=state, onclick="const checked = this.dataset.state === 'unchecked' ? 'checked' : 'unchecked'; this.dataset.state = checked; this.querySelector('span').dataset.state = checked; this.querySelector('input').checked=(checked === 'checked' ? true : false)", **kwargs)

component_map = [Button, Input, Card, Progress, Dialog, Textarea, Label]

def override_components():
    module_name = "fasthtml.common"
    module = sys.modules[module_name]
    for component in component_map:
        component_name = component.__name__
        setattr(module, component_name, component)


override_components()
