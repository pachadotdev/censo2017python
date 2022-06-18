import duckdb

from censo2017 import archivo_sql

def crear_esquema() :
    # connect to database
    con = duckdb.connect(database = archivo_sql(), read_only = False)

    # create schema

    ## drop table comunas if it exists
    con.execute('DROP TABLE IF EXISTS comunas')
    ## send query to create table comunas
    con.execute("""CREATE TABLE comunas (
        comuna_ref_id INTEGER NOT NULL,
        provincia_ref_id INTEGER NULL,
        idcomuna VARCHAR NULL,
        redcoden VARCHAR(5) NOT NULL, 
        nom_comuna VARCHAR NULL);""")

    ## drop table hogares if it exists
    con.execute('DROP TABLE IF EXISTS hogares')
    ## send query to create table hogares
    con.execute("""CREATE TABLE hogares (
        hogar_ref_id INTEGER NOT NULL,
        vivienda_ref_id INTEGER NULL,
        nhogar INTEGER NULL,
        tipo_hogar INTEGER NULL,
        ncu_yern_nuer INTEGER NULL,
        n_herm_cun INTEGER NULL,
        nuc_herm_cun INTEGER NULL,
        num_sueg_pad_abu INTEGER NULL,
        nuc_pad_sueg_abu INTEGER NULL,
        num_otros INTEGER NULL,
        nuc_otros INTEGER NULL,
        num_no_par INTEGER NULL,
        nuc_no_par INTEGER NULL,
        tot_nucleos INTEGER NULL);""")

    ## drop table personas if it exists
    con.execute('DROP TABLE IF EXISTS personas')
    ## send query to create table personas
    con.execute("""CREATE TABLE personas (
        persona_ref_id DOUBLE NULL,
        hogar_ref_id INTEGER NULL,
        personan INTEGER NULL,
        p07 INTEGER NULL,
        p08 INTEGER NULL,
        p09 INTEGER NULL,
        p10 INTEGER NULL,
        p10comuna INTEGER NULL,
        p10pais INTEGER NULL,
        p10pais_grupo INTEGER NULL,
        p11 INTEGER NULL,
        p11comuna INTEGER NULL,
        p11pais INTEGER NULL,
        p11pais_grupo INTEGER NULL,
        p12 INTEGER NULL,
        p12comuna INTEGER NULL,
        p12pais INTEGER NULL,
        p12pais_grupo INTEGER NULL,
        p12a_llegada INTEGER NULL,
        p12a_tramo INTEGER NULL,
        p13 INTEGER NULL,
        p14 INTEGER NULL,
        p15 INTEGER NULL,
        p15a INTEGER NULL,
        p16 INTEGER NULL,
        p16a INTEGER NULL,
        p16a_otro INTEGER NULL,
        p16a_grupo INTEGER NULL,
        p17 INTEGER NULL,
        p18 VARCHAR NULL,
        p19 INTEGER NULL,
        p20 INTEGER NULL,
        p21m INTEGER NULL,
        p21a INTEGER NULL,
        escolaridad INTEGER NULL,
        rec_parentesco INTEGER NULL);""")

    ## drop table provincias if it exists
    con.execute('DROP TABLE IF EXISTS provincias')
    ## send query to create table provincias
    con.execute("""CREATE TABLE provincias (
        provincia_ref_id INTEGER NULL,
        region_ref_id INTEGER NULL,
        idprovincia INTEGER NULL,
        redcoden VARCHAR(3) NOT NULL,
        nom_provincia VARCHAR NULL);""")

    ## drop table regiones if it exists
    con.execute('DROP TABLE IF EXISTS regiones')
    ## send query to create table regiones
    con.execute("""CREATE TABLE regiones (
        region_ref_id INTEGER NOT NULL,
        censo_ref_id INTEGER NULL,
        idregion VARCHAR NULL,
        redcoden VARCHAR(2) NOT NULL,
        nom_region VARCHAR NULL);""")

    ## drop table viviendas if it exists
    con.execute('DROP TABLE IF EXISTS viviendas')
    ## send query to create table viviendas
    con.execute("""CREATE TABLE viviendas (
        vivienda_ref_id INTEGER NOT NULL,
        zonaloc_ref_id INTEGER NULL,
        nviv INTEGER NULL,
        p01 INTEGER NULL,
        p02 INTEGER NULL,
        p03a INTEGER NULL,
        p03b INTEGER NULL,
        p03c INTEGER NULL,
        p04 INTEGER NULL,
        p05 INTEGER NULL,
        cant_hog INTEGER NULL,
        cant_per INTEGER NULL,
        ind_hacin DOUBLE NULL,
        ind_hacin_rec INTEGER NULL,
        ind_material INTEGER NULL);""")

    ## drop table metadatos if it exists
    con.execute('DROP TABLE IF EXISTS metadatos')

    ## drop table variables if it exists
    con.execute('DROP TABLE IF EXISTS variables')
    ## send query to create table variables
    con.execute("""CREATE TABLE variables (
        tabla VARCHAR NULL,
        variable VARCHAR NULL,
        descripcion VARCHAR NULL,
        tipo VARCHAR NULL,
        rango VARCHAR NULL);""")

    ## drop table variables_codificacion if it exists
    con.execute('DROP TABLE IF EXISTS variables_codificacion')
    ## send query to create table variables_codificacion
    con.execute("""CREATE TABLE variables_codificacion (
        tabla VARCHAR NULL,
        variable VARCHAR NULL,
        valor INTEGER NULL,
        descripcion VARCHAR NULL);""")

    ## drop table zonas if it exists
    con.execute('DROP TABLE IF EXISTS zonas')
    ## send query to create table zonas
    con.execute("""CREATE TABLE zonas (
        zonaloc_ref_id INTEGER NOT NULL,
        geocodigo VARCHAR NOT NULL,
        observacion VARCHAR NULL);""")

    ## create indexes
    con.execute('CREATE UNIQUE INDEX hogares_hogar_ref_id ON hogares (hogar_ref_id);')
    con.execute('CREATE UNIQUE INDEX viviendas_vivienda_ref_id ON viviendas (vivienda_ref_id);')
    con.execute('CREATE UNIQUE INDEX zonas_zonaloc_ref_id ON zonas (zonaloc_ref_id);')
    con.execute('CREATE UNIQUE INDEX zonas_geocodigo ON zonas (geocodigo);')

    con.close()

    return(True)
    