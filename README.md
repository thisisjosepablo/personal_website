# Web personal de José Pablo Torres

Web estática construida con [Quarto](https://quarto.org) (probada con Quarto 1.9).

```bash
quarto preview   # servidor local con recarga en caliente
quarto render    # genera la web en _site/
```

## Estructura

| Ruta | Qué contiene |
|------|--------------|
| `_quarto.yml` | Configuración global: navbar, footer, SEO, tema. **Configura `site-url` al publicar.** |
| `index.qmd` | Portada: presentación, actividad reciente, proyectos destacados, áreas y contacto. |
| `projects.qmd` + `projects/<slug>/index.qmd` | Listado y fichas de proyecto. |
| `about.qmd`, `cv.qmd` | Sobre mí (con contacto) y CV web imprimible. |
| `blog.qmd` + `posts/` | Blog (oculto del menú hasta que haya entradas). |
| `biblioteca.qmd` + `data/libros.yml` | Lecturas. |
| `deporte.qmd` + `data/logros.yml` | Marcas y cronología deportiva. |
| `_templates/*.ejs` | Plantillas de listados (tarjetas de proyecto, libros, logros). |
| `_partials/project/title-block.html` | Cabecera de las fichas de proyecto (botones de código/demo). |
| `_includes/` | Metadatos extra del `<head>` y pequeñas mejoras de accesibilidad. |
| `styles/` | Tema SCSS: `common.scss` (componentes) + `light.scss` / `dark.scss` (paletas). |
| `assets/` | Fuentes autoalojadas (OFL), CSS de fuentes e imágenes (avatar, favicon, imagen Open Graph). |

## Tareas habituales

**Añadir un proyecto**: crea `projects/<slug>/index.qmd` con este front matter:

```yaml
---
title: "Nombre"
description: "Una frase: qué hace y para quién."   # aparece en la tarjeta
kind: "Categoría corta"                           # p. ej. "IA generativa"
date: 2026-01-31                                  # se muestra el año
categories: [Python, FastAPI]                     # stack (máx. 4 en la tarjeta)
repo: https://github.com/thisisjosepablo/...
demo: https://...                                 # opcional
featured: true                                    # opcional: sale en la portada
order: 1                                          # orden en los listados
---
```

**Publicar la primera entrada del blog**: sigue los pasos comentados en `blog.qmd`.

**Añadir un libro o un logro deportivo**: edita `data/libros.yml` o `data/logros.yml`. Las descripciones que empiezan por `TODO` no se muestran.

**Actualizar la "Actividad reciente" de la portada**: está escrita a mano en `index.qmd`.

## Pendiente

Busca `TODO` en el repositorio (`grep -rn TODO --include=*.qmd --include=*.yml --include=*.txt .`) para ver los datos que faltan.
