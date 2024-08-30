
from fasthtml.common import NotStr, ft_hx, Script
from .core import get_icon

def Lucide(icon, size='24', color='currentColor', stroke_width='2', absolute_sw=False, **kwargs):
    icon_content, is_cdn = get_icon(icon)
    sw = stroke_width
    if absolute_sw:
        sw = f'{float(stroke_width) * 24 / float(size)}'

    
    svg_attrs = {'width': size,'height': size,'xmlns': "http://www.w3.org/2000/svg",'viewBox': '0 0 24 24','fill': kwargs.pop('fill', 'none'),'stroke': color,'stroke-width': sw,'stroke-linecap': kwargs.pop('strokeLinecap', 'round'),'stroke-linejoin': kwargs.pop('strokeLinejoin', 'round'),'cls': f"lucide lucide-{icon} {kwargs.pop('cls', '')}"
    }

    if is_cdn:
        repl_script=Script(f"""htmx.onLoad(function(content) {{fetch('{icon_content}').then(r=>r.text()).then(text=>{{const parser = new DOMParser();const svgDoc = parser.parseFromString(text.trim(),'text/html');const contents=svgDoc.querySelector('svg').innerHTML;htmx.findAll("[data-icon='{icon}']").forEach(e=>e.innerHTML=contents);}}).catch(error=>console.error('Error loading SVG:',error));}});""".strip(), _async=True, defer=True)

        return ft_hx('svg', repl_script, **svg_attrs, **kwargs, data_icon=icon)
    
    return ft_hx('svg', NotStr(icon_content), **svg_attrs, **kwargs)