from fasthtml.common import Div


def Skeleton(**kwargs):
    base_cls = "animate-pulse rounded-md bg-muted"
    return Div(cls=f"{base_cls} {kwargs.pop('cls', '')}", **kwargs)
