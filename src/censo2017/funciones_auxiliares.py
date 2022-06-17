import duckdb
from os import environ
from os import listfiles
from os import listdir
from os import remove
from os.path import expanduser
from shutil import rmtree

def censo_duckdb_version() :
    return(duckdb.__version__)

def censo_ruta() :
    # read environment variable CENSO2017_DIR
    # if not defined, use default value
    dir = environ.get('CENSO2017_PYTHON_DIR', expanduser('~') + '/.censo2017')
    return(dir)

def censo_conectar() :
    # connect to database
    # this can also write (i.e. when the database is new)
    duckdb.connect(database = censo_ruta() + 'censo_2017_duckdb_v' + duckdb.__version__.replace('\.', '') + '.sql$', readonly = False)
    return(True)
    
def censo_desconectar() :
    # disconnect from database
    censo_conectar().close()
    return(True)

def censo_eliminar(preguntar = False) :
    # ask the user, stop if selects anything different from 1
    if (preguntar) :
        print('Esto eliminara todas las bases del censo')
        print('1. De acuerdo')
        print('2. Cancelar')
        inp = int(input('Ingresa la opcion 1 o 2: '))
        if inp != 1 :
            return(False)
        
    # remove dir and all its contents
    dir = censo_ruta()
    for f in listfiles(dir, fullname = True) :
        remove(f)
    # remove dir if it is empty
    if not listdir(dir, fullname = True) :
        rmtree(dir)

    return(True)




