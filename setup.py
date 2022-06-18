from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name = "censo2017",
    version = "0.0.1",
    description = "Base de Datos de Facil Acceso del Censo 2017 de Chile (2017 Chilean Census Easy Access Database)",
    long_description = "Provee un acceso conveniente a mas de 17 millones de registros de la base de datos del Censo 2017. Los datos fueron importados desde el DVD oficial del INE usando el Convertidor REDATAM creado por Pablo De Grande. Esta paquete esta documentado intencionalmente en castellano asciificado para que funcione sin problema en diferentes plataformas. (Provides convenient access to more than 17 million records from the Chilean Census 2017 database. The datasets were imported from the official DVD provided by the Chilean National Bureau of Statistics by using the REDATAM converter created by Pablo De Grande and in addition it includes the maps accompanying these datasets.)",
    url = "https://github.com/pachadotdev/censo2017_python",
    author = "Mauricio Vargas Sepulveda (Pacha)",
    author_email="mavargas11@uc.cl",
    classifiers = [
        "Development Status :: 2 - Beta",
        "Intended Audience :: Researchers",
        "Topic :: Sociology :: Social Statistics",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords = "chile,census,duckdb",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    python_requires = ">=3.7, <4",
    install_requires = ["peppercorn", "duckdb", "wget", "datetime", "pandas"],
    extras_require = {
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },
    entry_points = {
        "console_scripts": [
            "sample=sample:main",
        ],
    },
    project_urls = {
        "Bug Reports": "https://github.com/pachadotdev/censo2017_python/issues",
        "Funding": "https://buymeacoffee.com/pacha",
        "Source": "https://github.com/pachadotdev/censo2017_python",
    },
)
