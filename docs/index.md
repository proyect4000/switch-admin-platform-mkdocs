# Switch Admin Platform

Esta documentación reúne el código fuente del proyecto y una explicación anotada archivo por archivo.

## Qué incluye

- Backend en FastAPI
- Frontend en Vue 3
- PostgreSQL con Docker Compose
- Autenticación JWT
- Consola SSH web
- Discovery de puertos y vecinos
- Backups de configuración
- Tareas programadas
- Topología de red

## Documentación automática con MkDocs

El proyecto incluye un archivo `mkdocs.yml` y páginas Markdown generadas para que puedas construir un sitio HTML con:

```bash
pip install mkdocs
mkdocs serve
```

Para generar el sitio estático:

```bash
mkdocs build
```

El contenido generado se publicará en la carpeta `site/`.
