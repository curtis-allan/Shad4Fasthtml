from typing import Any, List, Optional
from fasthtml.components import Div, Span, Hr, Script

def select_script() -> Script: ...

def SelectTrigger(*c: Any, cls: Optional[str] = None, **kwargs: Any) -> Any: ...

def SelectValue(placeholder: Optional[str] = None, cls: Optional[str] = None, **kwargs: Any) -> Span: ...

def SelectScrollUpButton(cls: Optional[str] = None, **kwargs: Any) -> Div: ...

def SelectScrollDownButton(cls: Optional[str] = None, **kwargs: Any) -> Div: ...

def SelectContent(*c: Any, cls: Optional[str] = None, id: str, **kwargs: Any) -> Any: ...

def SelectGroup(*c: Any, **kwargs: Any) -> Div: ...

def SelectLabel(*c: Any, cls: Optional[str] = None, **kwargs: Any) -> Div: ...

def SelectItem(*c: Any, cls: Optional[str] = None, checked: str = "false", value: Optional[str] = None, **kwargs: Any) -> Div: ...

def SelectSeparator(id: Optional[str] = None, cls: Optional[str] = None, **kwargs: Any) -> Hr: ...

def Portal(*c: Any, id: str, **kwargs: Any) -> Div: ...

def Select(
    *c: Any,
    cls: Optional[str] = None,
    state: str = "closed",
    placeholder: Optional[str] = None,
    label: Optional[str] = None,
    items: Optional[List[str]] = None,
    id: str,
    name: Optional[str] = None,
    standard: bool = False,
    **kwargs: Any
) -> Div: ...

# Constants
select_cls: dict
select_content_styles: str

# Exported names
__all__: List[str]