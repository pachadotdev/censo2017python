import duckdb

from genericpath import exists
from os import listdir
from os import path
from os import remove
from os import mkdir
from os.path import getsize
from wget import download
from zipfile import ZipFile
from datetime import datetime

from censo2017 import archivo_sql
from censo2017 import version_duckdb
from censo2017 import ruta
from censo2017 import eliminar
from censo2017 import crear_esquema

def descargar() :
    # disconnect and delete old databases (if any)
    print('Borrando las versiones antiguas de la base que pudiera haber...')
    if exists(archivo_sql()) :
        duckdb.connect(database = archivo_sql(), read_only = False).close()
    eliminar(preguntar = False)

    # create database directory if it doesn't exist
    dir = ruta()
    if not path.exists(dir) :
        mkdir(dir)

    # search for sql files matching the current duckdb version
    duckdb_current_files = []
    for f in listdir(dir):
        if f.endswith('v' + version_duckdb().replace('\.', '') + '.sql') :
            duckdb_current_files.append(f)

    # if the length of duckdb_current files is larger than 0 and all files are larger than 5MB then return true
    if len(duckdb_current_files) > 0 :
        print('Ya existe una base de datos con la misma version de DuckDB.')
        print('Si realmente quieres descargarla de nuevo, ejecuta el censo_eliminar() y luego descarga.')
        return True

    # if there are no files matching the current duckdb version (excluding new empty sql files), download the latest version
    # download file from url to the temp dir
    # TODO: Implement a function that gets the latest release file from GitHub
    print('Descargando la base de datos desde GitHub...')
    zipfile = 'files-for-user-db.zip'
    download('https://github.com/ropensci/censo2017/releases/download/v0.4/files-for-user-db.zip', dir + '/' + zipfile)

    print('Descomprimiendo los archivos necesarios...')
    # extract zipfile in the same directory
    with ZipFile(dir + '/' + zipfile, 'r') as zip_ref:
        zip_ref.extractall(dir)
    # remove the zip file
    remove(dir + '/' + zipfile)
    # list tsv files in destdir
    finp_tsv = []
    for f in listdir(dir):
        if f.endswith('.tsv') :
            finp_tsv.append(dir + '/' + f)

    # Create schema without data
    print('Creando la base de datos...')
    crear_esquema()

    # connect to the database
    con = duckdb.connect(database = archivo_sql(), read_only = False)
    # for each file in destdir, create a table in the database
    for f in finp_tsv :
        ## get the table name from the file name
        table_name = f.split('/')[-1].split('.')[0]
        ## run a copy statement to add contents of the file to the table
        print('Creando la tabla ' + table_name + '...')
        con.execute('COPY ' + table_name + ' FROM \'' + f + '\' DELIMITER \'\t\' NULL \'NA\' CSV HEADER;')
    # create additional table with duckdb version and system date
    ## create table
    con.execute('CREATE TABLE metadatos (version_duckdb VARCHAR, fecha_modificacion VARCHAR);')
    ## insert data
    con.execute('INSERT INTO metadatos VALUES (\'' + version_duckdb() + '\',' + datetime.now().strftime('%Y-%m-%d') + ');')
    # disconnect from the database
    con.close()

    # delete the tsv files in dir
    for f in finp_tsv :
        remove(f)

    return(True)
