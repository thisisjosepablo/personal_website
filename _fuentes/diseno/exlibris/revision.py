"""Genera ../piezas.html para revisar las piezas del logo en claro/oscuro y a varios tamaños."""
leer = lambda f: open(f).read()
ex, ca, co, fa = [leer(f) for f in ("exlibris-jpst.svg", "cartela-jpst.svg", "cartela-corta.svg", "favicon-j.svg")]
tam = lambda svg, h: svg.replace("<svg ", f'<svg style="height:{h}px;width:auto;display:block" ', 1)
nav = "<em>Inicio · Sobre mí · Proyectos · Blog</em>"
bloque = lambda cls: f'''
<div class="panel {cls}">
  <h3>Ex libris completo</h3>{tam(ex, 260)}
  <h3>Cartela con triángulos</h3>{tam(ca, 70)}{tam(ca, 34)}
  <h3>Cartela corta</h3><div class="fila">{tam(co, 70)}{tam(co, 34)}{tam(co, 22)}</div>
  <h3>Favicon</h3><div class="fila">{tam(fa, 64)}{tam(fa, 32)}{tam(fa, 16)}</div>
  <h3>Navbar</h3>
  <div class="nav">{tam(co, 30)}<span>José Pablo Soriano Torres</span>{nav}</div>
  <div class="nav">{tam(ca, 30)}{nav}</div>
  <div class="nav">{tam(fa, 30)}<span>José Pablo Soriano Torres</span>{nav}</div>
</div>'''
html = f'''<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>Piezas del logo JPST</title>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@600&family=Inter:wght@400;500&display=swap" rel="stylesheet">
<style>
body{{margin:0;padding:2rem 1rem;font-family:Inter,sans-serif;background:#e9e6dc}}
h1{{font-family:Fraunces,serif;text-align:center}} h3{{font:500 .8rem Inter;text-transform:uppercase;letter-spacing:.08em;opacity:.6;margin:1.6rem 0 .6rem}}
.cols{{display:grid;grid-template-columns:repeat(auto-fit,minmax(600px,1fr));gap:1.5rem;max-width:1400px;margin:auto}}
.panel{{padding:1.5rem 2rem 2rem;border-radius:1rem}}
.claro{{background:#f8f6ef;color:#2d6a2e}} .oscuro{{background:#111a10;color:#9fce6f}}
.panel>svg{{margin-bottom:.6rem}} .fila{{display:flex;gap:1.2rem;align-items:flex-end}}
.nav{{display:flex;align-items:center;gap:.8rem;padding:.6rem 1rem;margin-bottom:.6rem;border-bottom:1px solid rgba(128,160,120,.3);white-space:nowrap}}
.nav span{{font:600 1.05rem Fraunces,serif}} .claro .nav span{{color:#1a3017}} .oscuro .nav span{{color:#e3eadb}}
.nav em{{font-style:normal;font-size:.85rem;margin-left:auto;opacity:.75}}
</style></head><body><h1>Piezas del logo · JPST</h1>
<div class="cols">{bloque("claro")}{bloque("oscuro")}</div></body></html>'''
open("../piezas.html", "w").write(html)
