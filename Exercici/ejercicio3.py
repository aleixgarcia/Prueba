from functions import *
from literales import *
"""----------------------EJERCICIO 3-------------------------"""
def seleccio(opcio):
    print("+-----------------------------------------------------------------+")
    print("Benvingut al programa de selecció en fitxers, indica l'opció a fer:")
    print("+-----------------------------------------------------------------+")
    opcio=int(input("|\t1.-Crear un fitxer on demanem el seu nom \n|\t2.-Mostrar el contingut d'unt fitxer\n|\t3.-Modificar el contingut d'un fitxer demanant el nom \n|\t4.-Sortir\n"))
    return opcio

def enviemopcio(opcio):
    match opcio:
        case 1:
            file=usuari(FITXER)
            dades=contingut(file)
            escribir(file,dades)
            read_file(file)
        case 2:
            file=usuari(FITXER)
            read_file(file)
        case 3:
            file = usuari(FITXER)
            dades=contingut(file)
            escribir(file,dades)
            read_file(file)
        case _:
            print("Sortim!")
