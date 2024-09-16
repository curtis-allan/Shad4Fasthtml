from fasthtml.common import Script, Style, Link
import os

__all__ = ["ShadHead"]


def ShadHead(tw_cdn=False, theme_handle=False):
    tw_config = Script("""
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
}""")

    tw_styles = Style(
        """
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
}""",
        type="text/tailwindcss",
    )

    with open(os.path.join(os.path.dirname(__file__), "js/main_scripts.js")) as main:
        main_scr = main.read()

    tw_output_link = Link(href="/output.css", rel="stylesheet")

    script = Script(main_scr)

    headers = [
        script,
    ]
    if tw_cdn:
        headers.append(Script(src="https://cdn.tailwindcss.com"))
        headers.append(tw_config)
        headers.append(tw_styles)

    else:
        headers.append(tw_output_link)

    if theme_handle:
        with open(os.path.join(os.path.dirname(__file__), "js/theme.js")) as theme:
            theme_scr = theme.read()
        headers.append(Script(theme_scr))

    return (*headers,)
