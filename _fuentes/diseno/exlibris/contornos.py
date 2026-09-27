"""Contornos trazados sobre _fuentes/fotos/perfil_sierra.heic (coordenadas en la foto reducida a 1000x418)
y generación de las propuestas de ex libris en SVG."""

# --- Contornos (x, y) ---
SIERRA = [(200, 172), (225, 170), (248, 166), (275, 156), (300, 148), (330, 138), (360, 131),
          (385, 128), (405, 129), (425, 134), (450, 136), (480, 135), (520, 133), (555, 131),
          (590, 134), (615, 131), (628, 134), (655, 136), (690, 142), (720, 152), (745, 154),
          (765, 151), (790, 155), (815, 161), (840, 167), (880, 166), (920, 169), (945, 172)]
LADERA_IZQ = [(150, 150), (165, 158), (190, 172), (225, 186), (265, 201), (305, 216), (350, 232),
              (400, 248), (440, 258), (478, 264)]
COLINA_MEDIA = [(372, 214), (410, 208), (450, 216), (495, 230), (530, 238), (556, 246)]
LADERA_DER = [(552, 266), (585, 250), (625, 229), (670, 215), (720, 210), (760, 211), (800, 204),
              (850, 187), (900, 174), (950, 167), (1000, 163)]
ORILLA_IZQ = [(478, 264), (430, 272), (350, 282), (305, 296), (318, 310), (362, 322), (374, 338),
              (372, 352), (395, 368), (445, 385), (500, 402), (545, 418)]
ORILLA_DER = [(552, 266), (566, 276), (592, 292), (598, 305), (584, 322), (568, 340), (572, 352),
              (620, 360), (690, 366), (700, 378), (760, 398), (805, 418)]


def catmull_rom(pts, t=0.5):
    """Convierte una polilínea en curvas Bézier suaves (Catmull-Rom)."""
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    p = [pts[0]] + pts + [pts[-1]]
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 3, p1[1] + (p2[1] - p0[1]) * t / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 3, p2[1] - (p3[1] - p1[1]) * t / 3)
        d += f" C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f}"
    return d


def to_logo(pts, x0=150, x1=900, y_top=128, cx=100, width=184, y_at_top=98,
            relieve=2.2, y_agua=266, agua=0.8):
    """Lleva coordenadas de la foto al viewBox 0 0 200 200 del sello.
    `relieve` exagera la altura de las montañas (como en un grabado) y `agua` comprime el embalse."""
    s = width / (x1 - x0)
    def y_map(y):
        if y <= y_agua:
            return y_at_top + (y - y_top) * s * relieve
        return y_at_top + (y_agua - y_top) * s * relieve + (y - y_agua) * s * agua
    return [(cx - width / 2 + (x - x0) * s, y_map(y)) for x, y in pts]


def lago(**kw):
    """Embalse como forma cerrada: orilla izquierda hacia abajo y derecha de vuelta hacia arriba."""
    izq = to_logo(ORILLA_IZQ, **kw)
    der = to_logo(ORILLA_DER, **kw)[::-1]
    return catmull_rom(izq + der) + " Z"


def paths(**kw):
    return {"lago": lago(**kw)} | {name: catmull_rom(to_logo(pts, **kw)) for name, pts in {
        "sierra": SIERRA, "ladera_izq": LADERA_IZQ, "colina": COLINA_MEDIA,
        "ladera_der": LADERA_DER, "orilla_izq": ORILLA_IZQ, "orilla_der": ORILLA_DER}.items()}


if __name__ == "__main__":
    import json
    print(json.dumps({"normal": paths(), "compacto": paths(width=230, y_at_top=92)}, indent=1))
