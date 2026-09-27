"""Genera propuestas.html con las variantes del ex libris a partir de contornos.py."""
from contornos import paths

P = paths(width=200, y_at_top=80)          # paisaje algo más ancho que el círculo

def paisaje(stroke="var(--linea)", lago="var(--lago)", w=1.6, colina=True):
    s = f'<g fill="none" stroke-linecap="round" stroke-linejoin="round">'
    s += f'<path d="{P["sierra"]}" stroke="{stroke}" stroke-width="{w}"/>'
    if colina:
        s += f'<path d="{P["colina"]}" stroke="{stroke}" stroke-width="{w*0.6}" opacity=".7"/>'
    s += f'<path d="{P["ladera_izq"]}" stroke="{stroke}" stroke-width="{w}"/>'
    s += f'<path d="{P["ladera_der"]}" stroke="{stroke}" stroke-width="{w}"/>'
    # embalse: orillas + rayado horizontal de grabado, recortado a la forma del agua
    s += f'<clipPath id="agua"><path d="{P["lago"]}"/></clipPath>'
    s += f'<path d="{P["orilla_izq"]}" stroke="{lago}" stroke-width="{w*0.7}"/>'
    s += f'<path d="{P["orilla_der"]}" stroke="{lago}" stroke-width="{w*0.7}"/>'
    s += '<g clip-path="url(#agua)">' + "".join(
        f'<path d="M0 {y:.1f} H200" stroke="{lago}" stroke-width="{w*0.45}"/>' for y in [162 + i * 3.6 for i in range(10)]) + '</g>'
    return s + '</g>'

def clip(id_, r):
    return f'<clipPath id="{id_}"><circle cx="100" cy="100" r="{r}"/></clipPath>'

# A · Clásico: anillo con texto, JP en el cielo
A = f'''<svg viewBox="0 0 200 200"><defs>{clip("cA",76)}
<path id="arcoSup" d="M 22 100 A 78 78 0 0 1 178 100"/>
<path id="arcoInf" d="M 14 100 A 86 86 0 0 0 186 100"/></defs>
<circle cx="100" cy="100" r="96" fill="none" stroke="var(--linea)" stroke-width="1.6"/>
<circle cx="100" cy="100" r="76" fill="none" stroke="var(--linea)" stroke-width=".9"/>
<text class="anillo"><textPath href="#arcoSup" startOffset="50%" text-anchor="middle">EX · LIBRIS</textPath></text>
<text class="anillo"><textPath href="#arcoInf" startOffset="50%" text-anchor="middle">JOSÉ PABLO SORIANO TORRES</textPath></text>
<g clip-path="url(#cA)">{paisaje()}</g>
<text x="100" y="74" class="jp" text-anchor="middle" font-size="44">JP</text>
</svg>'''

# B · Integrado: la J se hunde en el embalse, la P se apoya en la sierra
B = f'''<svg viewBox="0 0 200 200"><defs>{clip("cB",88)}</defs>
<circle cx="100" cy="100" r="92" fill="none" stroke="var(--linea)" stroke-width="1.6"/>
<g clip-path="url(#cB)">{paisaje()}</g>
<text x="100" y="112" class="jp integrado" text-anchor="middle" font-size="84">J<tspan dx="-5">P</tspan></text>
</svg>'''

# C · Mínimo: solo la sierra y el agua, JP pequeño; pensado para favicon/navbar
C = f'''<svg viewBox="0 0 200 200"><defs>{clip("cC",86)}</defs>
<circle cx="100" cy="100" r="92" fill="none" stroke="var(--linea)" stroke-width="5"/>
<g clip-path="url(#cC)">
  <path d="{P["sierra"]}" fill="none" stroke="var(--linea)" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <clipPath id="aguaC"><path d="{P["lago"]}"/></clipPath><g clip-path="url(#aguaC)"><path d="M0 166 H200 M0 176 H200 M0 186 H200" stroke="var(--lago)" stroke-width="5"/></g>
</g>
<text x="100" y="72" class="jp" text-anchor="middle" font-size="54" font-weight="600">JP</text>
</svg>'''

html = open("plantilla.html").read()
html = html.replace("{{A}}", A).replace("{{B}}", B).replace("{{C}}", C)
open("../exlibris.html", "w").write(html)
print("ok")
