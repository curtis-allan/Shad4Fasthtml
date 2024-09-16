from fasthtml.components import Div, P
from lucide_fasthtml import Lucide
from fasthtml.toaster import *

__all__ = ["toast", "Toaster", "toast_setup"]

toast_container_cls = "fixed top-0 z-[100] flex max-h-screen w-full flex-col-reverse p-4 sm:bottom-0 sm:right-0 sm:top-auto sm:flex-col md:max-w-[420px] transition-transform duration-300"
toast_base_cls = "group pointer-events-auto relative flex w-full items-center justify-between space-x-4 overflow-hidden rounded-md border p-6 pr-8 shadow-lg toast"
toast_variants_cls = {
    "default": "border bg-background text-foreground",
    "destructive": "destructive group border-destructive bg-destructive text-destructive-foreground",
}
toast_closeBtn_cls = "toast-close-button cursor-pointer active:ring absolute right-2 top-2 rounded-md p-1 text-foreground/50 opacity-0 transition-opacity hover:text-foreground focus:opacity-100 focus:outline-none focus:ring-2 group-hover:opacity-100 group-[.destructive]:text-red-300 group-[.destructive]:hover:text-red-50 group-[.destructive]:focus:ring-red-400 group-[.destructive]:focus:ring-offset-red-600"
toast_title_cls = "text-sm font-semibold"
toast_description_cls = "text-sm opacity-90"


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
    app.after.append(after_toast)


def after_toast(resp, req, sess):
    if sk in sess:
        req.injects.append(Toaster(sess))
