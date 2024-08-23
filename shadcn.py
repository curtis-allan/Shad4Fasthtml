import sys

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
    "ThemeToggle",
    "Sheet",
    "SheetHeader",
    "SheetFooter",
    "SheetTitle",
    "SheetDescription",
    "SheetContent",
    "SheetTrigger",
    "SheetCloseButton",
]


def ShadHead(lucide_link=True, tw_link=False):

    shad_scripts = """
    function swapTheme() {
        const sunIcons = document.querySelectorAll('#theme-icon-sun');
        const moonIcons = document.querySelectorAll('#theme-icon-moon');

        if (localStorage.theme === 'dark' || document.documentElement.classList.contains('dark')) {
            if(sunIcons && moonIcons) {
                sunIcons.forEach(icon => icon.style.display = 'block')
                moonIcons.forEach(icon => icon.style.display = 'none')
                }
    } else {
            if(sunIcons && moonIcons) {
                sunIcons.forEach(icon => icon.style.display = 'none')
                moonIcons.forEach(icon => icon.style.display = 'block')
            }
        }
    }

    function handleThemeChange() {
    if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", () => {
                swapTheme()
                document.body.addEventListener("htmx:afterSwap", () => {
                    swapTheme()
                });
            });
        } else {
            swapTheme()
            document.body.addEventListener("htmx:afterSwap", () => {
                swapTheme()
            });
        }
    }

    if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
        document.documentElement.classList.add('dark')
        handleThemeChange()
    } else {
        document.documentElement.classList.remove('dark')
        handleThemeChange()
    }


    function toggleCheckbox(e) {
    e.dataset.state = e.dataset.state === 'unchecked' ? 'checked' : 'unchecked';
    e.querySelector('input').checked = e.dataset.state === 'checked';
    }

  function proc_htmx(sel, func) {
  htmx.onLoad(elt => {
    const elements = any(sel, elt, false);
    if (elt.matches && elt.matches(sel)) elements.unshift(elt);
    elements.forEach(func);
  });
}

  proc_htmx('.theme-toggle', elt => {
    elt.addEventListener('mousedown', event => {
        const sunIcon = elt.querySelector('#theme-icon-sun');
        const moonIcon = elt.querySelector('#theme-icon-moon');
        event.preventDefault();
        const zeroMd = document.querySelectorAll('zero-md');

        if(localStorage.theme === 'dark' || document.documentElement.classList.contains('dark')) {
            localStorage.theme = 'light'
            document.documentElement.classList.remove('dark');
        } else {
            localStorage.theme = 'dark'
            document.documentElement.classList.add('dark');
        }
        swapTheme();
        zeroMd.forEach(zeroMd => {
            if (zeroMd.shadowRoot) {
                const links = zeroMd.shadowRoot.querySelectorAll('link');
                links.forEach(link => handleMdThemeChange(link));
            } else {
            console.log('No shadow roots found');
            }
        });
    })
  })

  proc_htmx('.preventdbclick', elt => {
    elt.addEventListener('mousedown', event => {
    if (event.detail > 1) event.preventDefault();
    })
  })

  proc_htmx('.select', select => {
    content = select.querySelector('.select-content');

    function toggleClose() {
      select.dataset.state = 'closed'
      content.dataset.state= 'closed'
    }

   document.body.addEventListener('mousedown', event => {
    if (!select.contains(event.target) && select.dataset.state === 'open') {
      toggleClose();
    }
  })

    const scrollUpBtn = select.querySelector('.scroll-up');
    const scrollDownBtn = select.querySelector('.scroll-down');
    viewport = select.querySelector('.viewport')
    let scrollInterval;

    function scrollContent(direction) {
        const scrollAmount = direction === 'up' ? -5 : 5;
        viewport.scrollTop += scrollAmount;
    }

    function startScrolling(direction) {
        scrollInterval = setInterval(() => scrollContent(direction), 10);
    }

    function stopScrolling() {
        clearInterval(scrollInterval);
    }

    function updateButtonVisibility() {
        const isAtTop = viewport.scrollTop === 0;
        const isAtBottom = viewport.scrollHeight - viewport.clientHeight <= viewport.scrollTop + 1;

        scrollUpBtn.style.visibility = isAtTop ? 'hidden' : 'visible'
        scrollDownBtn.style.visibility = isAtBottom ? 'hidden' : 'visible'
    }

    scrollUpBtn.addEventListener('mouseenter', () => startScrolling('up'));
    scrollUpBtn.addEventListener('mouseleave', stopScrolling);

    scrollDownBtn.addEventListener('mouseenter', () => startScrolling('down'));
    scrollDownBtn.addEventListener('mouseleave', stopScrolling);

    viewport.addEventListener('scroll', updateButtonVisibility);

  select.addEventListener('mousedown', event => {
    event.preventDefault();
    trigger = select.querySelector('.select-trigger');
    
    inputval = select.querySelector('input').value;

    newState = select.dataset.state === 'open' ? 'closed':'open';

    if(trigger.contains(event.target)) {
      openSide = select.getBoundingClientRect();
      distBottom = window.innerHeight - openSide.bottom
      switch(openSide.top > distBottom) {
        case true:
          content.dataset.side = 'top'
          break;
        case false:
          content.dataset.side = 'bottom'
          break;
      }
      select.dataset.state = newState
      content.dataset.state=newState
      return
    } 

    if(event.target.classList.contains('select-item')) {
      const item = event.target;
      if(inputval === item.getAttribute('value')) {
        toggleClose();
        return;
      }

      if(inputval !== 'undefined') {
        const oldItem = content.querySelector(`.select-item[value="${inputval}"]`);
        oldItem.dataset.checked = 'false';
        oldItem.querySelector('span').dataset.checked = 'false';
      }

      item.dataset.checked = 'true';
      item.querySelector('span').dataset.checked = 'true';

      select.querySelector('.select-value').innerHTML = item.textContent;
      select.querySelector('input').value= item.getAttribute('value');
      trigger.focus();
      toggleClose();
    }
  })
  })

  function openSheet(button) {
    const sheet = document.querySelector(`#${button.getAttribute('sheet-id')}`);
    sheet.dataset.state = 'open'
    sheet.style.display = 'block';
  }

  proc_htmx('.sheet', elt => {
    var fragment = document.createDocumentFragment();

    fragment.appendChild(elt);

    document.body.appendChild(fragment);

    const overlay = elt.querySelector('.sheet-overlay');
    const closeIcon = elt.querySelector('.sheet-close-x');
    const closeBtn = elt.querySelector('.sheet-close-button');

    function toggleClose() {
    elt.dataset.state = 'closed'
    setTimeout(() => elt.style.display = 'none', 110);
  }

    if (overlay) overlay.addEventListener('mousedown', toggleClose)
    if (closeBtn) closeBtn.addEventListener('mousedown', toggleClose)
    if (closeIcon) closeIcon.addEventListener('mousedown', toggleClose)

  });

function openDialog(button) {
    const dialog = document.querySelector(`#${button.getAttribute('dialog-id')}`);
    dialog.dataset.state = 'open'
    dialog.style.display = 'block';
  }

  proc_htmx('.dialog', dialog => {
    var fragment = document.createDocumentFragment();

    fragment.appendChild(dialog);

    document.body.appendChild(fragment);

    const overlay = dialog.querySelector('.dialog-overlay');
    const closeIcon = dialog.querySelector('.dialog-close-btn');
    const closeBtn = dialog.querySelector('.dialog-close-button');

    function toggleClose() {
        dialog.dataset.state = 'closed'
        setTimeout(() => dialog.style.display = 'none', 110);
    }

    if (overlay) overlay.addEventListener('mousedown', toggleClose)
    if (closeBtn) closeBtn.addEventListener('mousedown', toggleClose)
    if (closeIcon) closeIcon.addEventListener('mousedown', toggleClose)
  });

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

    load_lucide = """
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
    """

    tw_import = """"https://cdn.tailwindcss.com"""

    headers = [
        Script(shad_scripts),
    ]

    if lucide_link:
        headers.append(Script(load_lucide, type="module"))
    if tw_link:
        headers.append(Script(src=tw_import))

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
select_trigger_cls = "select-trigger cursor-pointer flex h-10 items-center justify-between rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background focus:outline-none focus:ring-2 focus:ring-ring focus:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
select_scrollup_cls = "scroll-up flex cursor-default items-center justify-center py-1"
select_scrolldown_cls = (
    "scroll-down flex cursor-default items-center justify-center py-1"
)
select_content_cls = "absolute min-w-full h-fit w-fit data-[side=top]:bottom-11 data-[side=bottom]:top-11 select-content data-[state=open]:no-bg-scroll z-50 max-h-96 rounded-md border bg-popover text-popover-foreground shadow-md data-[state=closed]:hidden data-[state=open]:animate-in data-[state=closed]:animate-out data-[state=closed]:fade-out-0 data-[state=open]:fade-in-0 data-[state=closed]:zoom-out-95 data-[state=open]:zoom-in-95 data-[side=bottom]:slide-in-from-top-2 data-[side=left]:slide-in-from-right-2 data-[side=right]:slide-in-from-left-2 data-[side=top]:slide-in-from-bottom-2 data-[side=bottom]:translate-y-1 data-[side=left]:-translate-x-1 data-[side=right]:translate-x-1 data-[side=top]:-translate-y-1"
select_label_cls = "py-1.5 pl-8 pr-2 text-sm font-semibold"
select_item_cls = "select-item relative flex w-full cursor-default select-none hover:bg-muted items-center rounded-sm py-1.5 pl-8 pr-2 text-sm outline-none focus:bg-accent focus:text-accent-foreground data-[disabled]:pointer-events-none data-[checked=true]:bg-muted data-[disabled]:opacity-50"
select_separator_cls = "-mx-1 my-1 h-px bg-muted"
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


def ThemeToggle(variant="outline", cls=None, **kwargs):
    return Button(
        Lucide(icon="sun", id="theme-icon-sun"),
        Lucide(icon="moon", id="theme-icon-moon"),
        variant=variant,
        size="icon",
        cls=f"theme-toggle + {cls}",
        **kwargs,
    )


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
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    if standard:
        return Div(overlay, style="display: none;", data_state=state, *c, **kwargs)

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
        SheetContent(header, *c, footer, variant=side, cls=content_cls),
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


def SheetContent(*c, cls=None, variant, **kwargs):
    new_cls = f"{sheet_content_cls} {sheet_variants_cls[variant]}"
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


def Checkbox(cls=None, state="unchecked", name=None, id=None, **kwargs):
    curr_state = "true" if state == "checked" else None
    new_cls = checkbox_base_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    indicator = Span(Lucide(icon="check", cls="size-4"), cls=checkbox_indicator_cls)
    value_holder = Input(
        type="checkbox", style="display: none;", id=id, name=name, checked=curr_state
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
    return Div(*c, ico, tabindex=-1, **kwargs)


def SelectValue(placeholder=None, cls=None, **kwargs):
    new_cls = "select-value overflow-hidden text-ellipsis"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Span(placeholder, **kwargs)


def SelectScrollUpButton(cls=None, **kwargs):
    new_cls = select_scrollup_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    ico = Lucide(icon="chevron-up", cls="h-4 w-4")
    return Span(ico, style="visibility:hidden", **kwargs)


def SelectScrollDownButton(cls=None, **kwargs):
    new_cls = select_scrolldown_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    ico = Lucide(icon="chevron-down", cls="h-4 w-4")
    return Span(ico, **kwargs)


def SelectContent(*c, cls=None, **kwargs):
    new_cls = select_content_cls
    scrollUp = SelectScrollUpButton()
    scrollDown = SelectScrollDownButton()
    viewport = Div(
        *c,
        cls="viewport overflow-y-scroll p-1 h-[188px] w-full min-w-[8rem] no-scrollbar",
    )

    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(scrollUp, viewport, scrollDown, data_state="closed", **kwargs)


def SelectGroup(*c, **kwargs):
    return Optgroup(*c, **kwargs)


def SelectLabel(*c, cls=None, **kwargs):
    new_cls = select_label_cls
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Label(*c, **kwargs)


def SelectItem(*c, cls=None, checked="false", value=None, **kwargs):
    new_cls = select_item_cls
    span_cls = "absolute left-2 flex h-3.5 w-3.5 items-center justify-center data-[checked=false]:hidden"
    ico = Lucide(icon="check", cls=f"h-4 w-4")
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    return Div(
        Span(ico, cls=span_cls, data_checked=checked),
        value=value,
        *c,
        data_checked=checked,
        **kwargs,
    )


def SelectSeparator(**kwargs):
    return Hr(cls=select_separator_cls, **kwargs)


def Select(*c, cls=None, state="closed", id=None, name=None, **kwargs):
    new_cls = "select relative w-fit"
    if cls:
        new_cls += f" {cls}"
    kwargs["cls"] = new_cls
    value_holder = Hidden(value="undefined", name=name, id=id)
    return Div(value_holder, *c, data_state=state, **kwargs)


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
