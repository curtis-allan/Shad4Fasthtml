import sys
import uuid

from fasthtml.common import *
from fasthtml.components import Button as OgButton
from fasthtml.components import Input as OgInput
from fasthtml.components import Label as OgLabel
from fasthtml.components import Table as OgTable
from fasthtml.components import Textarea as OgTextarea
from fasthtml.toaster import *

__all__ = [
    "CardHeader",
    "CardFooter",
    "CardTitle",
    "CardDescription",
    "CardContent",
    "Card",
    "ShadHead",
    "Alert",
    "AlertTitle",
    "AlertDescription",
    "Lucide",
    "Badge",
    "Separator",
    "Progress",
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
    "DialogCloseButton",
    "Button",
    "Input",
    "Textarea",
    "Label",
    "Switch",
    "Table",
    "TableHeader",
    "TableBody",
    "TableFooter",
    "TableHead",
    "TableRow",
    "TableCell",
    "TableCaption",
    "Checkbox",
    "Select",
    "SelectContent",
    "SelectLabel",
    "SelectItem",
    "SelectSeparator",
    "SelectTrigger",
    "SelectGroup",
    "SelectValue",
    "Sheet",
    "SheetHeader",
    "SheetFooter",
    "SheetTitle",
    "SheetDescription",
    "SheetContent",
    "SheetTrigger",
    "SheetCloseButton",
    "Carousel",
    "CarouselContent",
    "CarouselItem",
    "CarouselPrevious",
    "CarouselNext",
    "Slider",
    "Tabs",
    "TabsTrigger",
    "TabsContent",
    "TabsList",
    "RadioGroup",
    "RadioGroupItem",
]


def ShadHead(lucide_link=True, tw_link=False):

    tw_config = Script("""
    function filterDefault(values) {
	return Object.fromEntries(
		Object.entries(values).filter(([key]) => key !== "DEFAULT"),
	)
}

tailwind.config = {
  darkMode: ["selector"],
  content: ["./**/*.{py,js}", "./docs/**/*.py"],
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
}
""")

    tw_styles = Style("""
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
    :root:has(.no-bg-scroll) {
        overflow: hidden;
    }

    * {
        @apply border-border;
    }

    body {
        @apply bg-background text-foreground antialiased min-h-screen;
        font-feature-settings: "rlig" 1, "calt" 1;
    }
}

@layer utilities {

    /* Hide scrollbar for Chrome, Safari and Opera */
    .no-scrollbar::-webkit-scrollbar {
        display: none;
    }
    /* Hide scrollbar for IE, Edge and Firefox */
    .no-scrollbar {
        -webkit-overflow-scrolling:touch;
        -ms-overflow-style: none;
        /* IE and Edge */
        scrollbar-width: none;
        /* Firefox */
    }
}

@keyframes slideInFromTop {
    from {
        transform: translateY(-100%);
    }

    to {
        transform: translateY(0);
    }
}

@keyframes slideInFromBottom {
    from {
        transform: translateY(100%);
    }

    to {
        transform: translateY(0);
    }
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
}""", type="text/tailwindcss")

    with open('shadscripts.js', 'r') as file:
        shad_scripts = file.read()

    load_lucide = Script("""
    import 'https://unpkg.com/lucide@latest';

    const loadLucide = () => {
            lucide.createIcons();
            document.body.addEventListener("htmx:afterSwap", function() {
                lucide.createIcons();
        });
    }
    
    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", loadLucide);
    } else {
        loadLucide();   
    }
    """, type="module")

    headers = [
        Script(shad_scripts),
    ]

    if lucide_link:
        headers.append(load_lucide)
    if tw_link:
        headers.append(Script(src="https://cdn.tailwindcss.com"))
        headers.append(tw_styles)
        headers.append(tw_config)


    return (*headers,)


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
    "default": "border-transparent bg-primary text-primary-foreground hover:bg-primary/80",
    "secondary": "border-transparent bg-secondary text-secondary-foreground hover:bg-secondary/80",
    "destructive": "border-transparent bg-destructive text-destructive-foreground hover:bg-destructive/80",
    "outline": "text-foreground",
}
sep_cls = "shrink-0 bg-border"
sep_variant_cls = {
    "horizontal": "h-[1.5px] w-full",
    "vertical": "self-stretch w-[1.5px]",
}
progress_cls = "relative h-4 w-full overflow-hidden rounded-full bg-secondary"
progress_inner_cls = "progress-inner h-full w-full flex-1 bg-primary transition-all"
toast_container_cls = "fixed top-0 z-[100] flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-0 sm:right-0 sm:top-auto sm:flex-col md:max-w-[420px] transition-transform duration-300"
toast_base_cls = "group pointer-events-auto relative flex w-full items-center justify-between space-x-4 overflow-hidden rounded-md border p-6 pr-8 shadow-lg toast"
toast_variants_cls = {
    "default": "border bg-background text-foreground",
    "destructive": "destructive group border-destructive bg-destructive text-destructive-foreground",
}
toast_closeBtn_cls = "toast-close-button cursor-pointer active:ring absolute right-2 top-2 rounded-md p-1 text-foreground/50 opacity-0 transition-opacity hover:text-foreground focus:opacity-100 focus:outline-none focus:ring-2 group-hover:opacity-100 group-[.destructive]:text-red-300 group-[.destructive]:hover:text-red-50 group-[.destructive]:focus:ring-red-400 group-[.destructive]:focus:ring-offset-red-600"
toast_title_cls = "text-sm font-semibold"
toast_description_cls = "text-sm opacity-90"
dialog_overlay_cls = "group-data-[state=open]:no-bg-scroll dialog-overlay fixed inset-0 z-50 bg-black/80 group-data-[state=open]:animate-in group-data-[state=closed]:animate-out group-data-[state=closed]:fade-out-0 group-data-[state=open]:fade-in-0"
dialog_content_cls = "dialog-content fixed left-[50%] top-[50%] z-50 grid w-full max-w-lg translate-x-[-50%] translate-y-[-50%] gap-4 border bg-background p-6 shadow-lg duration-200 group-data-[state=open]:animate-in group-data-[state=closed]:animate-out group-data-[state=closed]:fade-out-0 group-data-[state=open]:fade-in-0 group-data-[state=closed]:zoom-out-95 group-data-[state=open]:zoom-in-95 group-data-[state=closed]:slide-out-to-left-1/2 group-data-[state=closed]:slide-out-to-top-[48%] group-data-[state=open]:slide-in-from-left-1/2 group-data-[state=open]:slide-in-from-top-[48%] sm:rounded-lg"
dialog_closeBtn_cls = "dialog-close-btn cursor-pointer active:ring absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none group-data-[state=open]:bg-accent group-data-[state=open]:text-muted-foreground"
dialog_title_cls = "text-lg font-semibold leading-none tracking-tight"
dialog_description_cls = "text-sm text-muted-foreground"
dialog_header_cls = "flex flex-col space-y-1.5 text-center sm:text-left"
dialog_footer_cls = "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2"
textarea_cls = "flex min-h-[80px] w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
label_cls = "preventdbclick text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
switch_base_cls = "group peer inline-flex h-6 w-11 shrink-0 cursor-pointer items-center rounded-full border-2 border-transparent transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=unchecked]:bg-input"
switch_thumb_cls = "pointer-events-none block h-5 w-5 rounded-full bg-background shadow-lg ring-0 transition-transform group-data-[state=checked]:translate-x-5 group-data-[state=unchecked]:translate-x-0"
table_base_cls = "w-full caption-bottom text-sm"
table_head_cls = "[&_tr]:border-b"
table_body_cls = "[&_tr:last-child]:border-0"
table_footer_cls = "border-t bg-muted/50 font-medium [&>tr]:last:border-b-0"
table_row_cls = (
    "border-b transition-colors hover:bg-muted/50 data-[state=selected]:bg-muted"
)
table_head_cls = "h-12 px-4 text-left align-middle font-medium text-muted-foreground [&:has([role=checkbox])]:pr-0"
table_cell_cls = "p-4 align-middle [&:has([role=checkbox])]:pr-0"
checkbox_base_cls = "preventdbclick peer group h-4 w-4 shrink-0 rounded-sm border border-primary ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 data-[state=checked]:bg-primary data-[state=checked]:text-primary-foreground"
checkbox_indicator_cls = "preventdbclick flex items-center justify-center text-current group-data-[state=unchecked]:hidden"
select_trigger_cls = "select-trigger flex h-10 w-full items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 [&>span]:line-clamp-1"
select_scrollup_cls = "scroll-up flex cursor-default items-center justify-center py-1"
select_scrolldown_cls = "scroll-down flex cursor-default items-center justify-center py-1"
select_content_cls = "select-content relative z-50 max-h-96 min-w-[8rem] overflow-hidden rounded-md border bg-popover text-popover-foreground shadow-md data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1"
select_item_cls = "group select-item relative flex w-full cursor-default select-none hover:bg-muted items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[checked=true]:bg-muted data-[disabled]:opacity-50"
select_separator_cls = "-mx-1 my-1 h-px bg-muted"
select_label_cls = "py-1.5 pl-8 pr-2 text-sm font-semibold"
sheet_overlay_cls = "sheet-overlay group-data-[state=open]:no-bg-scroll fixed inset-0 z-50 bg-black/80 group-data-[state=open]:animate-in group-data-[state=closed]:animate-out group-data-[state=closed]:fade-out-0 group-data-[state=open]:fade-in-0"
sheet_variants_cls = {
    "top": "inset-x-0 top-0 border-b group-data-[state=closed]:slide-out-to-top group-data-[state=open]:slide-in-from-top",
    "bottom": "inset-x-0 bottom-0 border-t group-data-[state=closed]:slide-out-to-bottom group-data-[state=open]:slide-in-from-bottom",
    "left": "inset-y-0 left-0 h-full w-3/4 border-r group-data-[state=closed]:slide-out-to-left group-data-[state=open]:slide-in-from-left sm:max-w-sm",
    "right": "inset-y-0 right-0 h-full w-3/4 border-l group-data-[state=closed]:slide-out-to-right group-data-[state=open]:slide-in-from-right sm:max-w-sm",
}
sheet_closeBtn_cls = "sheet-close-x absolute right-4 top-4 rounded-sm opacity-70 ring-offset-background transition-opacity hover:opacity-100 focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:pointer-events-none"
sheet_content_cls = "fixed z-50 gap-4 bg-background p-6 shadow-lg transition ease-in-out group-data-[state=open]:animate-in group-data-[state=closed]:animate-out group-data-[state=closed]:duration-300 group-data-[state=open]:duration-500"
sheet_header_cls = "flex flex-col space-y-2 text-center sm:text-left"
sheet_footer_cls = "flex flex-col-reverse sm:flex-row sm:justify-end sm:space-x-2"
sheet_title_cls = "text-lg font-semibold text-foreground"
sheet_description_cls = "text-sm text-muted-foreground"
select_content_styles_ = "box-sizing: border-box; display: flex; flex-direction: column; outline: none; --radix-select-content-transform-origin: var(--radix-popper-transform-origin); --radix-select-content-available-width: var(--radix-popper-available-width); --radix-select-content-available-height: var(--radix-popper-available-height); --radix-select-trigger-width: var(--radix-popper-anchor-width); --radix-select-trigger-height: var(--radix-popper-anchor-height); pointer-events: auto;"
select_viewport_cls = "viewport p-1 h-[var(--radix-select-trigger-height)] w-full min-w-[var(--radix-select-trigger-width)] no-scrollbar"


def Button(*c, size="default", variant="default", cls=None, **kwargs):
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
    variant: str = "default",
    cls=None,
    standard=False,
    icon: str = "chevrons-right",
    **kwargs,
):
    variants = tuple(alert_variants_cls.keys())
    assert variant in variants, f"`variant` not in {variants}"

    new_cls = f"{alert_cls['alert']} {alert_variants_cls[variant]}"
    headers = []
    if variant == "destructive":
        icon = "circle-alert"
    if cls:
        new_cls += f" {cls}"

    kwargs["cls"] = new_cls
    if standard:
        return Div(*c, **kwargs)
    headers.append(Lucide(icon=icon, cls="size-4"))
    if title:
        headers.append(AlertTitle(title))
    if description:
        headers.append(AlertDescription(description))

    return Div(*headers, *c, **kwargs)


def Lucide(icon: str = "x", cls="size-5", **kwargs):
    kwargs["cls"] = f"lucide {cls}"
    return I(data_lucide=icon, **kwargs)


def Badge(*c, variant: str = "default", cls=None, **kwargs):
    variants = tuple(badge_variants_cls.keys())
    assert variant in variants, f"`variant` not in {variants}"
    new_cls = badge_cls
    new_cls += f" {badge_variants_cls[variant]}"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def Separator(orientation="horizontal", cls=None, **kwargs):
    new_cls = f"{sep_cls} {sep_variant_cls[orientation]}"

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(decorative=True, **kwargs)


def Progress(value=0, id=None, cls=None, **kwargs):

    bar_comp = Div(
        style=f"transform: translateX(-{100-value}%)",
        id=f"{id}-inner",
        cls=progress_inner_cls,
    )
    new_cls = progress_cls
    if cls:
        new_cls += f" { cls}"
    kwargs["cls"] = new_cls
    return Div(
        bar_comp,
        role="progressbar",
        value=value,
        id=id,
        **kwargs,
    )


def toast(sess, title, description, variant="default"):
    assert variant in (
        "default",
        "destructive",
    ), '`variant` not in ("default", "destructive")'
    sess.setdefault(sk, []).append((title, description, variant))


def Toaster(sess):
    closeBtn = Div(Lucide(icon="x", cls="size-4"), cls=toast_closeBtn_cls)
    toasts = [
        Div(
            P(title, cls=toast_title_cls),
            P(description, cls=toast_description_cls),
            closeBtn,
            cls=f"{toast_base_cls} {toast_variants_cls[variant]}",
        )
        for title, description, variant in sess.pop(sk, [])
    ]
    return Div(
        Div(*toasts, cls=toast_container_cls, id="toast-container"),
        hx_swap_oob="afterbegin:body",
    )


def toast_setup(app):
    app.router.after.append(after_toast)


def after_toast(resp, req, sess):
    if sk in sess:
        req.injects.append(Toaster(sess))


def DialogHeader(*c, cls=None, **kwargs):
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


def DialogTitle(*c, cls=None, **kwargs):
    new_cls = dialog_title_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return H1(*c, **kwargs)


def DialogCloseButton(*c, cls=None, **kwargs):
    new_cls = "dialog-close-button"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(*c, **kwargs)


def DialogDescription(*c, cls=None, **kwargs):
    new_cls = dialog_description_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return P(*c, **kwargs)


def DialogContent(*c, cls=None, **kwargs):
    closeBtn = Div(
        Lucide(icon="x", cls=f"size-4"),
        Span("Close", cls="sr-only"),
        cls=dialog_closeBtn_cls,
    )
    new_cls = dialog_content_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, closeBtn, **kwargs)


def DialogTrigger(*c, dialog_id=None, **kwargs):
    return Button(
        *c,
        dialog_id=dialog_id,
        onclick="event.preventDefault();openDialog(this)",
        **kwargs,
    )


def Dialog(
    *c,
    footer=None,
    title=None,
    description=None,
    standard=False,
    state="closed",
    cls=None,
    **kwargs,
):
    overlay = Div(cls=dialog_overlay_cls)

    new_cls = "dialog group"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    if standard:
        return Div(overlay, style="display: none;", data_state=state, *c, **kwargs)

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

    return Div(
        overlay,
        DialogContent(header, *c, footer),
        style="display: none;",
        data_state=state,
        tabindex="-1",
        **kwargs,
    )


def Sheet(
    *c,
    cls=None,
    side="right",
    title=None,
    description=None,
    footer=None,
    standard=False,
    state="closed",
    content_cls=None,
    **kwargs,
):
    new_cls = "group sheet"
    overlay = Div(cls=sheet_overlay_cls)
    header_content = []
    header = None
    footer = None

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    if standard:
        return Div(overlay, *c, style="display: none;", data_state=state, **kwargs)

    if title:
        header_content.append(SheetTitle(title))
    if description:
        header_content.append(SheetDescription(description))
    if header_content:
        header = SheetHeader(
            *header_content,
        )
    if footer:
        footer = SheetFooter(footer)

    return Div(
        overlay,
        SheetContent(header, *c, footer, side=side, cls=content_cls),
        data_state=state,
        role="dialog",
        tabindex="-1",
        style="display: none;",
        **kwargs,
    )


def SheetCloseButton(*c, cls=None, **kwargs):
    new_cls = "sheet-close-button"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(
        *c,
        **kwargs,
    )


def SheetContent(*c, cls=None, side="right", **kwargs):
    new_cls = f"{sheet_content_cls} {sheet_variants_cls[side]}"
    closeBtn = ft_hx(
        "button",
        Span("Close", cls="sr-only"),
        Lucide(icon="x", cls="size-4"),
        cls=sheet_closeBtn_cls,
        type="button",
    )
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(closeBtn, *c, **kwargs)


def SheetTitle(*c, cls=None, **kwargs):
    new_cls = sheet_title_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return H1(*c, **kwargs)


def SheetDescription(*c, cls=None, **kwargs):
    new_cls = sheet_description_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return P(*c, **kwargs)


def SheetHeader(*c, cls=None, **kwargs):
    new_cls = sheet_header_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def SheetTrigger(*c, cls=None, sheet_id: str = None, **kwargs):
    new_cls = "sheet-trigger"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Button(
        *c,
        onclick="event.preventDefault();openSheet(this)",
        sheet_id=sheet_id,
        **kwargs,
    )


def SheetFooter(*c, cls=None, **kwargs):
    new_cls = sheet_footer_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


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
    return OgLabel(*c, _for=htmlFor, **kwargs)


def Switch(state="unchecked", cls=None, id=None, name=None, value=None, **kwargs):
    curr_state = "true" if state == "checked" else None
    assert state in ("checked", "unchecked"), '`state` not in ("checked", "unchecked")'

    new_cls = switch_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    thumb = Span(cls=switch_thumb_cls)
    value_holder = Input(
        type="checkbox",
        style="display: none;",
        id=id,
        name=name,
        value=value,
        checked=curr_state,
    )
    return Div(
        thumb, value_holder, data_state=state, onclick="toggleCheckbox(this)", **kwargs
    )


def Table(*c, cls=None, **kwargs):
    new_cls = table_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(OgTable(*c, **kwargs), cls="relative w-full overflow-auto")


def TableHeader(*c, cls=None, **kwargs):
    new_cls = table_head_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Thead(*c, **kwargs)


def TableBody(*c, cls=None, **kwargs):
    new_cls = table_body_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Tbody(*c, **kwargs)


def TableFooter(*c, cls=None, **kwargs):
    new_cls = table_footer_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Tfoot(*c, **kwargs)


def TableRow(*c, cls=None, **kwargs):
    new_cls = table_row_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Tr(*c, **kwargs)


def TableHead(*c, cls=None, **kwargs):
    new_cls = table_head_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Th(*c, **kwargs)


def TableCell(*c, cls=None, **kwargs):
    new_cls = table_cell_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Td(*c, **kwargs)


def TableCaption(*c, cls=None, **kwargs):
    new_cls = table_cell_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Caption(*c, **kwargs)


def Checkbox(cls=None, state="unchecked", name=None, value=None, id=None, **kwargs):
    curr_state = "true" if state == "checked" else None
    assert state in ("checked", "unchecked"), '`state` not in ("checked", "unchecked")'

    new_cls = checkbox_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    indicator = Span(Lucide(icon="check", cls="size-4"), cls=checkbox_indicator_cls)
    value_holder = Input(
        type="checkbox",
        style="display: none;",
        value=value,
        id=id,
        name=name,
        checked=curr_state,
    )
    return Span(
        indicator,
        value_holder,
        data_state=state,
        onclick="toggleCheckbox(this)",
        **kwargs,
    )


def SelectTrigger(*c, cls=None, **kwargs):
    ico = Lucide(icon="chevron-down", cls="h-4 w-4 opacity-50 shrink-0")
    new_cls = select_trigger_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return ft_hx('button', *c, ico, **kwargs)


def SelectValue(placeholder=None, cls=None, **kwargs):
    new_cls = "select-value pointer-events-none"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Span(placeholder, **kwargs)


def SelectScrollUpButton(cls=None, **kwargs):
    new_cls = select_scrollup_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    ico = Lucide(icon="chevron-up", cls="h-4 w-4 hidden sm:flex")
    return Div(ico, aria_hidden="true",**kwargs)


def SelectScrollDownButton(cls=None, **kwargs):
    new_cls = select_scrolldown_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    ico = Lucide(icon="chevron-down", cls="h-4 w-4 hidden sm:flex")
    return Div(ico,aria_hidden="true", **kwargs)


def SelectContent(*c, cls=None, id=None, **kwargs):
    if not id:
        raise ValueError("`id` is required")
    new_cls = select_content_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Portal(Div(SelectScrollUpButton(),
            Div(*c,
            cls=select_viewport_cls,
            role="listbox",
            style="position:relative;flex:1 1 0%;overflow: auto;",
            id=f"{id}-viewport"
        ),
        SelectScrollDownButton(),
        tabindex="-1",
        style=select_content_styles_,
        id=f"{id}-content",
        **kwargs
    ), 
    id=id,
    )

def SelectGroup(*c, **kwargs):
    return Div(*c, role="group", **kwargs)


def SelectLabel(*c, cls=None, **kwargs):
    new_cls = select_label_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(*c, **kwargs)


def SelectItem(*c, cls=None, checked="false", value=None, **kwargs):
    new_cls = select_item_cls
    span_cls = "absolute left-2 hidden h-3.5 w-3.5 items-center justify-center group-data-[checked=true]:flex"
    ico = Lucide(icon="check", cls="h-4 w-4")
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(
        Span(ico, cls=span_cls),
        Span(*c),
        data_checked=checked,
        value=value,
        role="option",
        tabindex=-1,
        aria_selected=checked,
        **kwargs
    )

def SelectSeparator(id=None, cls=None, **kwargs):   
    new_cls = select_separator_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Hr(id=f"{id}-separator", **kwargs)

def Portal(*c, id=None, **kwargs):
    if not id:
        raise ValueError("`id` is required")
    return Div(*c, id=f"{id}-portal", style="position:fixed;left:0;top:0;display:none;",cls="select-portal", **kwargs)

def Select(*c, cls=None, state="closed", placeholder:str=None, label:str=None, items: list = None, id=None, name=None, standard=False, **kwargs):
    if not id:
        raise ValueError("`id` is required")
    new_cls = "select group relative data-[state=open]:no-bg-scroll"
    value_holder = Hidden(value="", name=name, id=f"{id}-input")
    render_items = ()

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls

    if standard:
        return Div(value_holder, *c, data_state=state, id=id, role="combobox", aria_controls=f"{id}-content", aria_expanded="false", aria_haspopup="listbox", **kwargs)

    if items:
        render_items = (SelectItem(item, value=item.lower(), name=item) for item in items)

    select_trigger = SelectTrigger(SelectValue(placeholder))
    select_content = SelectContent(
            SelectGroup(SelectLabel(label), *render_items),
            id=id
        ),

    return Div(
        value_holder,
        select_trigger,
        select_content,
        data_state=state,
        id=id,
        role="combobox",
        aria_controls=f"{id}-content",
        aria_expanded="false",
        aria_haspopup="listbox",
        **kwargs
    )


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
        if (startEvent.button !== 0 && startEvent.type !== 'touchstart') return; // Only proceed for left mouse button or touch
        startEvent.preventDefault()
        const moveHandler = moveEvent => handleMove(moveEvent.clientX || moveEvent.touches[0].clientX)
        const upHandler = () => {
            document.removeEventListener('mousemove', moveHandler)
            document.removeEventListener('mouseup', upHandler)
            document.removeEventListener('touchmove', moveHandler)
            document.removeEventListener('touchend', upHandler)
        }
        document.addEventListener('mousemove', moveHandler)
        document.addEventListener('mouseup', upHandler)
        document.addEventListener('touchmove', moveHandler)
        document.addEventListener('touchend', upHandler)
    }

    track.on('mousedown', e => {
        if (e.button === 0) { // Only proceed for left mouse button
            handleMove(e.clientX)
            addDragListeners(e)
        }
    })

    track.on('touchstart', e => {
        handleMove(e.touches[0].clientX)
        addDragListeners(e)
    })

    thumb.on('mousedown', e => {
        if (e.button === 0) addDragListeners(e) // Only proceed for left mouse button
    })

    thumb.on('touchstart', e => {
        addDragListeners(e)
    })

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

component_map = [
    Button,
    Input,
    Card,
    Progress,
    Dialog,
    Textarea,
    Label,
    Checkbox,
    Select,
]


def override_components():
    module_name = "fasthtml.common"
    module = sys.modules[module_name]
    for component in component_map:
        component_name = component.__name__
        setattr(module, component_name, component)


override_components()
