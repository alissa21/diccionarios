# Librerias a usar:
import csv
from tinydb import TinyDB


# Funcion para cargar los datos de un archivo csv a una base de datos de TinyDB:
def crear(archivo_csv, bdd_tinydb):
    # Usamos csv en el archivo
    with open(archivo_csv) as csvarchivo:
        # leemos el archivo
        entrada = csv.reader(csvarchivo)
        for linea in entrada:
            # Asignamos los 2 valores del archivo que estan separados por coma
            palabra, significado = linea
            # Insertamos un dic con la palabra y el significado en la bdd
            bdd_tinydb.insert({"Palabra": palabra, "Significado": significado})
            # Borramos, para que en la siguiente linea no se repitan los valores
            del palabra, significado