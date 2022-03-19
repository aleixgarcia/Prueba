import genericpath

from literales import *
from functions import *
from ejercicio2 import *
from ejercicio3 import *
from ejercicio4 import *
from ejercicio5 import *
from ejercicio7 import *
from ejercicio8 import *
from invent import *
import os
from sentinella import *
from datetime import datetime

MITG = "El fitxer existeix, vols sobreescriure'l? \n\ty=Si\n\taltre=No"

def main():
    #Escribo en un fichero (o lo creo)
    #read_file('C:\\Users\\aleii\\prueba\\dades.txt')

    #Leo el fichero (o lo creo)
    #write_file('C:\\Users\\aleii\\dades2.txt')

    #Añado nuevos elementos al fichero (o lo creo)
    #append_file('C:\\Users\\aleii\\dades3.txt')

    #------------------EJERCICIO 2------------------
    #Pedir a usuario los datos para un fichero
    #fitxer = usuari("Demanem nom fitxer")
    #dades = contingut(fitxer)
    #print(dades)
    #escribir('C:\\Users\\aleii\\'+fitxer, dades)

    #----------------EJERCICIO 3--------------------
    #segontext= demanartext(fitxer)
    #afegir('C:\\Users\\aleii\\'+fitxer, segontext)

    #opcio= seleccio("Demanem opcio")
    #print("Has escogido la opcion:",opcio)
    #enviemopcio(opcio)

    #----------------EJERCICIO 4---------------------
    """
    usuaris=dict()
    usuaris['name']=nom("Demanem usuari")
    usuaris['surname']= cognom("Demanem cognom")
    usuaris['age']=edat("Demanem edat")
    usuaris['iden']=identificador(usuaris['name'],usuaris['surname'], usuaris['age'])
    usuaris['tecn']=tecnologia("Demanem tecnologia")
    #filecsv(usuaris['name'],usuaris['surname'],usuaris['age'],usuaris['iden'], usuaris['tecn'])
    with open('C:\\Users\\aleii\dades3.csv', 'a+', encoding='utf-8', newline='') as csvfile:
        fieldnames= ['iden','name','surname','age','tecn']
        writeCSV = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writeCSV.writerow(usuaris)
        read_file('C:\\Users\\aleii\\dades3.csv')

    """
    #----------------EJERCICIO 5---------------------
    #menucsv("Demanem opcio:")

    # ----------------EJERCICIO 7---------------------
    """arxiu=('C:\\Users\\aleii\\bio.csv')
    print("El contingut del fitxer és el següent:")
    read_file(arxiu)
    text = contingut("Demanem contingut")
    filecsv7(arxiu,text)"""


    # ----------------EJERCICIO 8---------------------
    """txt=('C:\\Users\\aleii\\projects.csv')
    filecsv8(txt)"""

    # ----------------EJERCICIO 8(de otra forma)---------------------
    #get_info()

    # ----------------EJERCICIO INVENT---------------------
    #invent()

    #------------------EXAMEN------------------
    #prova1()
    #exercici2()
    #exercici3()
    #prova2()
    #ans = 'y'
    #f = usuari()
    #if(os.path.exists(f) == True):
    #    ans = input(MITG)
    #if(ans == 'y'):
    #    createFile(f)

    #------------------ACTIVITAT PRACTICA-----------------
    d = dia()
    sentinella(d)


if __name__ == '__main__':
    main()