# Web personal · José Pablo Soriano Torres

Web hecha con [Quarto](https://quarto.org) y publicada automáticamente en GitHub Pages:
<https://thisisjosepablo.github.io/>

## Uso diario: la orden `./web`

Todo se hace desde la terminal, en la carpeta de la web:

| Quiero… | Orden |
|---|---|
| Ver la web mientras edito | `./web ver` |
| Escribir una nota | `./web nota "Título" --etiquetas "datos, salud"` |
| Contar una aventura | `./web aventura "Título" --lugar "Segura de la Sierra"` |
| Añadir las fotos de una aventura | meterlas en `_originales/` y `./web fotos aventuras/2026/09-nombre` |
| Añadir un proyecto | `./web proyecto "Nombre"` |
| Añadir un libro | `./web libro` (pregunta los datos) |
| Actualizar trayectoria, formación… | `./web editar trayectoria` (o `formacion`, `publicaciones`, `idiomas`, `reconocimientos`, `libros`) |
| Comprobar que todo compila | `./web comprobar` (con la vista previa cerrada) |
| **Publicar** | `./web publicar "Mensaje opcional"` |

`./web publicar` sube los cambios a GitHub y GitHub compila y publica la web solo (1-2 minutos).
El progreso se ve en la pestaña **Actions** del repositorio.

> **Vista previa:** recoge sola los cambios en páginas `.qmd`, pero **no** los de `_quarto.yml`
> (menú, pie…), `_sistema/` (plantillas, tema) ni los archivos de `datos/`. Si cambias alguno de
> esos, cierra la vista previa (Ctrl+C) y vuelve a lanzar `./web ver`.

## Estructura

Cada sección de la web es una carpeta con **su página, sus datos, sus imágenes y su contenido**.
Lo que empieza por `_` no se publica: es el "motor" de la web o material original.

```
personal_website/
├── web                     ← herramienta para crear contenido y publicar
├── _quarto.yml             ← configuración global: menú, pie, tema, estilos
├── index.qmd               ← Inicio
├── 404.qmd                 ← página de "no encontrada"
│
├── sobre-mi/
│   ├── index.qmd           ← la página (perfil)
│   ├── datos/              ← ✏️ trayectoria.yml · formacion.yml · publicaciones.yml · idiomas.yml · reconocimientos.yml
│   ├── proyectos/          ← ✏️ un proyecto por carpeta: proyectos/<nombre>/index.qmd
│   └── imagenes/           ← imágenes de la sección (portada de la sierra, logos…)
│
├── notas/
│   ├── index.qmd           ← la lista de notas
│   └── <año>/<mes>-<nombre>/index.qmd   ← ✏️ cada nota
│
├── biblioteca/
│   ├── index.qmd           ← la página
│   └── datos/libros.yml    ← ✏️ los libros
│
├── aventuras/
│   ├── index.qmd           ← la lista de aventuras
│   ├── _ejemplo/           ← aventura de referencia (no se publica)
│   └── <año>/<mes>-<nombre>/            ← ✏️ cada aventura
│       ├── index.qmd       ← el texto
│       ├── _originales/    ← tus fotos tal cual (no se publican ni se suben a git)
│       └── fotos/          ← fotos listas para la web (las genera ./web fotos)
│
├── recursos/               ← comunes a toda la web
│   ├── css/                ← estilos, un archivo por sección (base, inicio, sobre-mi…)
│   └── img/                ← logo, favicon, foto de perfil, banner del inicio
│
├── _sistema/               ← motor de la web (rara vez hace falta tocarlo)
│   ├── marca/              ← colores y tipografías (claro.yml, oscuro.yml)
│   ├── tema/               ← ajustes del tema (claro.scss, oscuro.scss)
│   ├── plantillas/         ← cómo se dibujan las listas (libros, notas, aventuras, perfil)
│   ├── parciales/          ← cabecera de notas/aventuras/proyectos (migas de pan)
│   ├── includes/           ← protección del email
│   └── filtros/            ← YouTube en modo privacidad
│
├── _fuentes/               ← originales: fotos en alta calidad, diseño del logo
└── .github/workflows/      ← publicación automática
```

Los ✏️ son los únicos sitios que se editan en el día a día.

## Convenciones

- **Fechas** en los datos: `"AAAA-MM"` (p. ej. `"2024-10"`). Sin `fin`, un puesto cuenta como actual y
  la duración se calcula sola.
- **Carpetas de contenido**: `<año>/<mes>-<nombre-sin-tildes>/`. La orden `./web` las crea así.
- **Fotos**: nunca se suben los originales. `./web fotos` quita el GPS, las gira, corrige el color y las
  comprime a WebP (máx. 1600 px); además añade la galería a la aventura y activa su portada.
- **Vídeos**: `{{< video https://youtu.be/ID >}}` en cualquier página.

## Puesta en marcha (una sola vez)

1. En GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**,
   rama `gh-pages`, carpeta `/ (root)`.
2. En la terminal, una vez: `quarto publish gh-pages` (crea la rama `gh-pages` y el archivo `_publish.yml`).
3. A partir de ahí basta con `./web publicar`.
