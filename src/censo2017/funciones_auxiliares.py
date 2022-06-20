import duckdb
from os import environ
from os import listdir
from os import remove
from os.path import expanduser
from os.path import exists
from shutil import rmtree

def version_duckdb() :
    return(duckdb.__version__)

def ruta() :
    # read environment variable CENSO2017_DIR
    # if not defined, use default value
    dir = environ.get('CENSO2017_PYTHON_DIR', expanduser('~') + '/.censo2017')
    return(dir)

def archivo_sql() :
    return(ruta() + '/' + 'censo_2017_duckdb_v' + duckdb.__version__.replace('.', '') + '.sql')

def eliminar(preguntar = True) :
    # ask the user, stop if selects anything different from 1
    if (preguntar == True) :
        print('Esto eliminara todas las bases del censo')
        print('1. De acuerdo')
        print('2. Cancelar')
        inp = int(input('Ingresa la opcion 1 o 2: '))
        if inp != 1 :
            return(False)
        
    # remove dir and all its contents
    dir = ruta()

    if exists(dir) :
        for f in listdir(dir) :
            # print(dir + f)
            remove(dir + '/' + f)
    
        rmtree(dir)

    return(True)




