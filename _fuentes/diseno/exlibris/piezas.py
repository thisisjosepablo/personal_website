"""Genera las piezas del logo a partir de boceto-jpst.png (tinta = currentColor):

  exlibris-jpst.svg   ex libris completo
  cartela-jpst.svg    cartela JPST con las bandas de triángulos (horizontal)
  cartela-corta.svg   solo el recuadro JPST (navbar)
  favicon-j.svg       la J en su recuadro (favicon)

Uso: python piezas.py   (necesita potracer, numpy y pillow)
"""
import numpy as np
import potrace
from PIL import Image, ImageFilter, ImageOps

ESCALA, UMBRAL = 2, 120

gris = ImageOps.grayscale(Image.open("boceto-jpst.png"))
W, H = gris.size
grande = gris.resize((W * ESCALA, H * ESCALA), Image.Resampling.LANCZOS)
grande = grande.filter(ImageFilter.GaussianBlur(0.9 * ESCALA))
TINTA = np.asarray(grande) < UMBRAL          # True = tinta, en coordenadas x2


def trazar(tinta, ox=0, oy=0, motas=12):
    """Calca una máscara de tinta (coords x2) y devuelve el atributo d en coords del boceto,
    desplazado para que (ox, oy) sea el origen."""
    curvas = potrace.Bitmap(~tinta).trace(      # potracer toma False como tinta
        turdsize=motas * ESCALA * ESCALA, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY,
        alphamax=1.0, opticurve=True, opttolerance=0.25)
    k = 1 / ESCALA
    p = lambda q: f"{q.x * k - ox:.1f} {q.y * k - oy:.1f}"
    d = []
    for c in curvas:
        d.append("M" + p(c.start_point))
        for s in c.segments:
            d.append("L" + p(s.c) + "L" + p(s.end_point) if s.is_corner
                     else "C" + p(s.c1) + " " + p(s.c2) + " " + p(s.end_point))
        d.append("Z")
    return "".join(d)


def svg(nombre, d, w, h, etiqueta):
    open(nombre, "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" role="img" '
        f'aria-label="{etiqueta}"><path fill="currentColor" d="{d}"/></svg>')
    print(f"{nombre}: {len(d) / 1024:.0f} KB")


def region(*rects):
    """Máscara con solo la tinta dentro de los rectángulos (x0, y0, x1, y1) en coords del boceto."""
    m = np.zeros_like(TINTA)
    for x0, y0, x1, y1 in rects:
        m[y0 * ESCALA:y1 * ESCALA, x0 * ESCALA:x1 * ESCALA] = True
    return TINTA & m


# 1 · Ex libris completo, recortado a la tinta con un pequeño margen
ys, xs = np.where(TINTA)
x0, y0 = xs.min() // ESCALA - 6, ys.min() // ESCALA - 6
x1, y1 = xs.max() // ESCALA + 6, ys.max() // ESCALA + 6
svg("exlibris-jpst.svg", trazar(TINTA, x0, y0), x1 - x0, y1 - y0,
    "Ex libris de José Pablo Soriano Torres")

# 2 · Cartela con bandas de triángulos
svg("cartela-jpst.svg", trazar(region((395, 742, 1275, 860), (634, 710, 1036, 860)), 395, 710),
    1275 - 395, 860 - 710, "JPST")

# 3 · Solo el recuadro JPST
svg("cartela-corta.svg", trazar(region((634, 710, 1036, 860)), 634, 710), 1036 - 634, 860 - 710, "JPST")

# 4 · Favicon: la J (en papel) sobre un recuadro de tinta cuadrado
jx0, jy0, jx1, jy1 = 652, 728, 740, 849             # caja de la J en el boceto
j = ~TINTA[jy0 * ESCALA:jy1 * ESCALA, jx0 * ESCALA:jx1 * ESCALA]   # True = papel (la letra)
lado = (jy1 - jy0 + 28) * ESCALA
lienzo = np.zeros((lado, lado), bool)               # False = tinta de fondo
oy = (lado - j.shape[0]) // 2
ox = (lado - j.shape[1]) // 2
lienzo[oy:oy + j.shape[0], ox:ox + j.shape[1]] = j
# esquinas ligeramente redondeadas, como un taco de madera
yy, xx = np.mgrid[:lado, :lado]
r = 10 * ESCALA
for cy, cx in ((r, r), (r, lado - r), (lado - r, r), (lado - r, lado - r)):
    esquina = ((yy < r) | (yy >= lado - r)) & ((xx < r) | (xx >= lado - r))
    lienzo |= esquina & (((yy - cy) ** 2 + (xx - cx) ** 2) > r * r) & \
        (np.sign(yy - lado / 2) == np.sign(cy - lado / 2)) & (np.sign(xx - lado / 2) == np.sign(cx - lado / 2))
svg("favicon-j.svg", trazar(~lienzo, motas=4), lado / ESCALA, lado / ESCALA, "J")
