from genericpath import exists
from tempfile import mkdtemp
from os import listfiles
from os import path
from os import remove
from os.path import mkdir
from os.path import getsize
from wget import download
from zipfile import ZipFile
from datetime import date

from censo2017 import censo_duckdb_version
from censo2017 import censo_ruta
from censo2017 import censo_desconectar
from censo2017 import censo_eliminar
from censo2017 import censo_conectar
from censo2017 import censo_crear_esquema

def censo_descargar() :
    # search for sql files matching the current duckdb version
    duckdb_current_files = listfiles(censo_ruta(), pattern = 'v' + censo_duckdb_version().replace('\.', '') + '.sql$', fullname = True)

    # if there are existing files matching the current duckdb version, without counting new empty sql files, then do nothing
    if len(duckdb_current_files) > 0 & all(getsize(duckdb_current_files) > 5000000000) :
        print('Ya existe una base de datos con la misma version de DuckDB.')
        print('Si realmente quieres descargarla de nuevo, ejecuta el censo_eliminar() y luego descarga.')
        return True
    
    # if there are no files matching the current duckdb version (excluding new empty sql files), download the latest version
    print('Descargando la base de datos desde GitHub...')
    dir = censo_ruta()
    destdir = mkdtemp()
    # create directory if it doesn't exist
    if not path.exists(dir) :
        mkdir(dir)
    # download file from url to the temp dir
    # TODO: Implement a function that gets the latest release file from GitHub
    download('https://github.com/ropensci/censo2017/releases/download/v0.4/files-for-user-db.zip', destdir + '/files-for-user-db.zip')

    # disconnect and delete old databases (if any)
    print('Borrando las versiones antiguas de la base que pudiera haber...')
    censo_desconectar()
    censo_eliminar(preguntar = False)

    print('Descomprimiendo los archivos necesarios...')
    # unzip the files from destdir
    with ZipFile(destdir + '/files-for-user-db.zip', 'r') as zip_ref :
        zip_ref.extractall(destdir)
    # remove the zip file
    remove(destdir + '/files-for-user-db.zip')
    # list tsv files in destdir
    finp_tsv = listfiles(destdir, pattern = '*.tsv$', fullname = True)

    # Create schema without data
    print('Creando la base de datos...')

    censo_crear_esquema()

    # for each file in destdir, create a table in the database
    for f in finp_tsv :
        ## get the table name from the file name
        table_name = f.split('/')[-1].split('.')[0]
        ## run a copy statement to add contents of the file to the table
        print('Creando la tabla ' + table_name + '...')
        censo_conectar().execute('COPY ' + table_name + ' FROM ' + f + ' DELIMITER \'\t\' NULL \'NA\' CSV HEADER;')

    censo_desconectar()

    # delete the tsv files in destdir
    for f in finp_tsv :
        remove(f)

    # create additional table with duckdb version and system date
    ## create table
    censo_conectar().execute('CREATE TABLE metadatos (version_duckdb VARCHAR, fecha_modificacion DATE);')
    ## insert data
    censo_conectar().execute('INSERT INTO censo_version VALUES (\'' + censo_duckdb_version() + '\',' + date.today() + ');')
    
    # disconnect from the database
    censo_desconectar()

    return(True)
