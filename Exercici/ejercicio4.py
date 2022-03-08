from functions import *
from literales import *
import csv
"""----------------------EJERCICIO 4-------------------------"""
def nom(nom):
    nom=str(input(NOMBRE))
    return nom

def cognom(cognom):
    cognom = str(input(APELLIDO))
    return cognom

def edat(edat):
    edat = int(input(EDAD))
    return edat

def identificador(nom,cognom,edat):
    ident=nom.upper()[0:2]+'-'+cognom.upper()[0:2]+'-'+str(edat)
    print(ident)
    return ident

def opcio(op):
    op=int(input("Vols introduir més dades?\n\t1.-No\n\t2.-Si"))

def tecnologia(tecn):
    tecn=str(input(MENU))
    return tecn

def filecsv(nom, cognom, edat,tecn, iden):
    with open('C:\\Users\\aleii\dades3.csv', 'a+', encoding='utf-8', newline='') as csvfile:
        fieldnames = ['iden', 'name', 'surname', 'age', 'tecn']
        writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writeCSV.writeheader()
        writeCSV.writerow(usuaris)
    read_file('C:\\Users\\aleii\\dades3.csv')
