from fasthtml.components import ft_hx


def Toggle(*c, variant="default", toggled=False, size="default", **kwargs):
    variants = {
        "default": "bg-transparent",
        "outline": "border border-input bg-transparent hover:bg-accent hover:text-accent-foreground"
    }
    sizes = {
        "default": "h-10 px-3 min-w-10",
        "sm": "h-9 px-2.5 min-w-9",
        "lg": "h-11 px-5 min-w-11"
    }

    if not isinstance(variant, str) or variant not in variants:
        raise ValueError(f"variant must be one of: {', '.join(variants.keys())}")
    if not isinstance(size, str) or size not in sizes:
        raise ValueError(f"size must be one of: {', '.join(sizes.keys())}")

    base_cls = " ".join([
        "inline-flex items-center justify-center rounded-md text-sm font-medium",
        "ring-offset-background transition-colors hover:bg-muted",
        "hover:text-muted-foreground focus-visible:outline-none focus-visible:ring-2",
        "focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none",
        "disabled:opacity-50 data-[on]:bg-accent data-[on]:text-accent-foreground",
        "[&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 gap-2"
    ])

    onclick = "this.value = this.toggleAttribute('data-on');"

    cls = f"{base_cls} {variants[variant]} {sizes[size]} {kwargs.pop('cls', '')}"

    return ft_hx('button',*c, cls=cls.strip(), onclick=onclick,
data_on=toggled, aria_label=kwargs.pop('aria_label', 'Toggle Button'), **kwargs)
