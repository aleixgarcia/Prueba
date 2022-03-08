from literales import *
import csv

#Función para leer ficheros
def read_file(file_name):
    try:
        f = open(file_name, 'r')
    except:
        print(MSG_FIELD_KO)
    else:
        print(MOSTRAR)
        print(f.read())
        f.close()

#Función para escribir ficheros
def write_file(file_name):
    f = open(file_name, 'w')
    f.write("Hola")
    f.close()

#Función para añadir a ficheros
def append_file(file_name):
    f = open(file_name, 'a+')
    f.write("Hola")
    print(f.read())
    f.close()

"""----------------------EJERCICIO 1-------------------------"""
#Funcion para pedir el nombre del fichero
def usuari(file_name):
    f = str(input(NOM))
    print(f[-4:])
    if(f[-4:]) != '.csv':
        f= f + '.csv'
    else:
        read_file(f)
    print("Has indicat el nom del fitxer:",f)
    return f

#Funcion para pedir el contenido del fichero
def contingut(f):
        dades= str(input(CONTINGUT))[0:100]
        return dades

#Funcion para introducir el contenido pedido anteriormente
def escribir(f, dades):
    f=open(f, 'w+')
    f.write(dades)
    print(f.read())
    f.close()
