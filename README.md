# Algortimos y Programacion III - Catedra Suarez

[![Versión de Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://www.python.org/downloads/)
[![Versión de Pelican](https://img.shields.io/badge/Pelican-4.8.0-yellow.svg)](https://docs.getpelican.com/en/latest/index.html#)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-green.svg)](LICENSE)
[![GitHub Pages](https://github.com/alejovillores/algo_3_fiuba/actions/workflows/pages/pages-build-deployment/badge.svg)](https://alejovillores.github.io/algo_3_fiuba/)

## Instalación

Para instalar el proyecto se debe tener una version de `python 3.11`

```bash
pip3 install -r requirements.txt
```

Luego debe realizar un pull de los submodulos (el theme)

```bash
git submodule update --init --recursive --remote
```

Luego podra hacer los pulls del submodulo con el siguiente comando

```bash
git submodule update  --recursive --remote
```

## Uso

Para correr el servidor de desarrollo de debe ejecutar el archivo `StartServer.ps1`, este settea las variables de entorno correspondiente, levanta un servidor local en `http://127.0.0.1:8000`. Para que el reload por cada cambio sea automatico se debe ejecutar `StartServer.ps1 -R` o `StartServer.ps1 --reload`

### Desarrollo

Es recomendable leer la documentacion oficial de [Pelican](https://docs.getpelican.com/en/latest/index.html) para entender mejor como agregar nueva funcionalidad

Para crear una nueva pagina, el archivo debe estar en `/pages`, ésta debe tener un formato de markdown (es posible introducir codigo html). El archivo debe contener una metadata como el siguiente

```markdown
Title: Preguntas Frecuentes (obligatorio)
Slug: fqa (obligatorio)
Authors: Alejo Villores (obligatorio)
Summary: preguntas frecuentes de los alumnos (opcional)
Position: 3 (obligatorio)

### Pagina
```

### CSS

La hoja de estilo depende de un submodulo de github [pelican-theme]("https://github.com/alejovillores/pelican-theme"). Es posible cambiar los estilos, colaborando tambien a a ese repositorio que es a su vez un `fork` de un theme ya realizado por un tercero.

## Contribución

Las contribuciones se deben hacer hacia la rama `main`

1. Haz un fork del proyecto.
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`).
3. Confirma tus cambios (`git commit -m 'Añade una característica increíble'`).
4. Haz push a la rama (`git push origin feature/AmazingFeature`).
5. Abre un Pull Request.

Proximamente, cada pull request lanzará un workflow para subir a gh-pages los nuevos cambios

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Cualquier duda, queja o sugerencia que no se pueda realizar desde el mismo repo, por favor enviar un mail a [avillores@fi.uba.ar](avillores@fi.uba.ar)
