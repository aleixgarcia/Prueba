from functions import *
from literales import *
"""----------------------EJERCICIO 2-------------------------"""
def demanartext(file_name):
    segontext= str(input(CONTINGUT))[0:100]
    return segontext

def afegir(f,segontext):
    f=open(f, 'a+')
    f.write(segontext)
    print(f.read())
    f.close()