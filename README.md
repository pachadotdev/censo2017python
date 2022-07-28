# Censo 2017 (Paquete Python)

<!-- badges: start -->

![Python Logo](https://www.python.org/static/community_logos/python-logo.png "Sample inline image")
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4277761.svg)](https://doi.org/10.5281/zenodo.4277761)
[![Buy Me a
Coffee](https://img.shields.io/badge/buymeacoffee-pacha-yellow)](https://www.buymeacoffee.com/pacha?via=github)
<!-- badges: end -->

# Acerca de

Provee un acceso conveniente a mas de 17 millones de registros de la
base de datos del Censo 2017. Los datos fueron importados desde el DVD
oficial del INE usando el [Convertidor
REDATAM](https://github.com/discontinuos/redatam-converter/) creado por
Pablo De Grande y ademas se proporcionan los mapas que acompanian a
estos datos. Estos mismos datos en DVD posteriormente quedaron
disponibles en las [Bases de Datos del
INE](https://www.ine.cl/estadisticas/sociales/censos-de-poblacion-y-vivienda/poblacion-y-vivienda).

Despues de la primera llamada a `import censo2017` es necesario
descargar la base de datos usando `censo_descargar()`.

Este software es una adaptacion del paquete original de R censo2017. Para hacer el port me base 
en [Python Sample Project](https://github.com/pypa/sampleproject).

# Publico objetivo

Estudiantes, academicos e investigadores que necesiten un acceso
conveniente a datos censales directamente en Python o Jupyer Notebook.

# Requerimientos de instalacion

Esta libreria necesita 3.5 GB libres para la crear la base de datos
localmente. Una vez creada la base, esta ocupa 1.0 GB en disco.

# Instalacion

## Directamente desde GitHub

Se puede usar cualquiera de las siguientes opciones desde la linea de comandos

```bash
pip install git+https://github.com/pachadotdev/censo2017python.git#egg=censo2017
```

```bash
git clone git@github.com:pachadotdev/censo2017python.git
cd censo2017python
python setup.py install --user
```

# Valor agregado sobre los archivos SHP y REDATAM del INE

Esta version de la base de datos del Censo 2017 presenta algunas
diferencias respecto de la original que se obtiene en DVD y corresponde
a una version DuckDB derivada a partir de los Microdatos del Censo 2017
en formato DVD.

La modificacion sobre los archivos originales, que incluyen geometrias
detalladas disponibles en [Cartografias
Censo2017](https://github.com/ropensci/censo2017-cartografias),
consistio en unir todos los archivos SHP regionales en una unica tabla
por nivel (e.g en lugar de proveer `R01_mapa_comunas`, …,
`R15_mapa_comunas` combine las 15 regiones en una unica tabla
`mapa_comunas`).

Los cambios concretos respecto de la base original son los siguientes:

-   Nombres de columna en formato “tidy” (e.g. `comuna_ref_id` en lugar
    de `COMUNA_REF_ID`).
-   Agregue los nombres de las unidades geograficas (e.g. se incluye
    `nom_comuna` en la tabla `comunas` para facilitar los filtros).
-   Aniadi la variable `geocodigo` a la tabla de `zonas`. Esto facilita
    mucho las uniones con las tablas de mapas en SQL.
-   Tambien inclui las observaciones 16054 to 16060 en la variable
    `zonaloc_ref_id`. Esto se debio a que era necesario para crear una
    llave foranea desde la tabla `mapa_zonas` (ver repositorio
    [Cartografias
    Censo2017](https://github.com/ropensci/censo2017-cartografias)) y
    vincular el `geocodigo` (no todas las zonas del mapa estan presentes
    en los datos del Censo).

Ademas de los datos del Censo, inclui la descripcion de las variables en
formato tabla (y no en XML como se obtiene del DVD). La ventaja de esto
es poder consultar rapidamente lo que significan los codigos de
variables y su etiquetado, por ejemplo como se explica en 
[demo.ipynbn](https://github.com/pachadotdev/censo2017_python/blob/main/demo.ipynb)

# Cita este trabajo

Si usas `censo2017` en trabajos academicos u otro tipo de publicacion
por favor usa la siguiente cita:

    Mauricio Vargas (2022). censo2017: Base de Datos de Facil Acceso del Censo
      2017 de Chile (2017 Chilean Census Easy Access Database). Python package version
      0.0.1. https://github.com/pachadotdev/censo2017_python

Entrada para BibTeX:

    @Manual{,
      title = {censo2017: Base de Datos de F\'acil Acceso del Censo 2017 de Chile
    (2017 Chilean Census Easy Access Database)},
      author = {Mauricio Vargas},
      year = {2022},
      note = {Python package version 0.0.1},
      url = {https://github.com/pachadotdev/censo2017_python},
      doi = {10.5281/zenodo.4277761}
    }

# Agradecimientos

Muchas gracias a Juan Correa por su asesoria como geografo experto.

# Aportes

Si quieres donar para aportar al desarrollo de este y mas paquetes Open
Source, puedes hacerlo en [Buy Me a
Coffee](https://www.buymeacoffee.com/pacha/).
