from literales import *
from datetime import datetime
import csv
# from s_funciones import *
import os
import pandas as pd
import time


# Funció per demanar el dia
def dia():
    while True:
        d = input(DIA)
        try:
            d = datetime.strptime(d, '%d/%m/%Y').strftime('%d-%m-%Y')
            print(d)
            return d
        except ValueError:
            print("La fecha es incorrecta:", d)


# Funció on l'usuari introdueix totes les dades necessaries
def sentinella(d):
    dies = dict()
    path = input("Quina es la ruta on vols guardar el fitxer?")
    arxiu = 'C:\\Users\\aleii\\activitatPY\\' + d + '.csv'
    d_ant = info_csv(arxiu)

    if d != d_ant:  # Demanem les dades del curs si el dia introduit es diferent a l'anterior
        dies['dia'] = d
        dies['curs'] = input(CURS)
        dies['aula'] = aula()
        dies['nalum'] = input(NALUM)
        dies['nprof'] = input(NPROF)

    else:
        print(f"El dia {d} ja es troba registrat, segueix introduint les dades:")

    fsessio = 1
    while fsessio != '1':
        dies['hora'] = hora()
        dies['CO2'] = input(CO2)
        dies['temp'] = input(TEMP)
        dies['humi'] = input(HUMITAT)
        dies['nomprof'] = input(NOMPROF)
        dies['assig'] = input(ASSIG)
        with open(arxiu, 'a+', newline='') as a:
            fieldnames = ['curs', 'aula', 'nalum', 'nprof', 'dia',
                          'hora', 'CO2', 'temp', 'humi', 'nomprof',
                          'assig', 'pp', 'ps', 'fext', 'fint', 'vent']
            if os.stat(arxiu).st_size == 0:  # Comprovem que si el fitxer existeix, no tingui cap dada,
                # de ser aixi escriurem la capçalera, sino només escivim els registres
                writer = csv.DictWriter(a, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(dies)
            else:
                writer = csv.DictWriter(a, fieldnames=fieldnames)
                writer.writerow(dies)
        fsessio = input(FSESSIO)
        # Validem la resposta de si la classe ha finalitzat o no
        while fsessio != 1 or fsessio != 2:
            fsessio = input(FSESSIO)

    # Demanem el temps de porta principal oberta
    dies['pp'] = input(PP)
    # Demanem si hi ha porta secundaria
    psec = int(input(PSEC))
    # Si la resposta a la pregunta anterior es si (un 1), preguntem quant temps ha estat oberta
    if psec == 1:
        dies['ps'] = input(PS)
    # Preguntem si hi han finestres exteriors
    finestres_ext = int(input(FINESTRES_EXT))
    # Si la resposta a la pregunta anterior es si (un 1), preguntem quant temps han estat obertes
    if finestres_ext == 1:
        dies['fext'] = input(FEXT)
    # Preguntem si hi han finestres interiors
    finestres_int = int(input(FINESTRES_INT))
    # Si la resposta a la pregunta anterior es si (un 1), preguntem quant temps han estat obertes
    if finestres_int == 1:
        dies['fint'] = input(FINT)
    # Preguntem quant de temps hi ha hagut ventilació creuada
    dies['vent'] = input(VENTILACIO)

    # Obrim el fitxer en format lectura per poder comprar les hores introduides,
    # si la ultima es igual a la que es vol introduir no escriu res pq el registre ja s'ha fet abans,
    # pero si es diferent, vol dir que son registres diferents i per tant si s'escriu
    with open(arxiu, 'r') as a:
        readcsv = csv.DictReader(a)
        for row in readcsv:
            hour = row['hora']
        if hour != dies['hora']:
            with open(arxiu, 'a+', newline='') as ar:
                writer = csv.DictWriter(ar, fieldnames=fieldnames)
                writer.writerow(dies)
    # Cridem a la funcio per llegir el csv que s'ha registrat
    read_file(arxiu)


# Funció para leer fitxers
def read_file(file_name):
    try:
        df = pd.read_csv(file_name)
    except FileNotFoundError:
        print(MSG_FIELD_KO)
    else:
        print(MOSTRAR)
        print(df)


def info_csv(arxiu):
    d = 0
    try:
        with open(arxiu, 'r') as csvfile:
            readcsv = csv.DictReader(csvfile)
            for row in readcsv:
                d = row['dia']
    except FileNotFoundError:
        print("Aquest dia encara no es troba registrat, comença!")
    print(d)
    return d


def hora():
    while True:
        h = input(HORA)
        try:
            h = time.strptime(h, "%H:%M")
            return h
        except ValueError:
            print("El format es incorrecte!")


def aula():
    a = 0
    while a < 1 or a > 30:
        a = int(input(AULA))
        if a < 1 or a > 30:
            print("El num de l'aula no es correcte, torna a provar:")
    return a
