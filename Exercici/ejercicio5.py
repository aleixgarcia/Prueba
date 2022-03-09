from functions import *
from literales import *
"""----------------------EJERCICIO 5-------------------------"""

def menucsv(opcio):
    opciocsv=int(input(MENUCSV))
    match opciocsv:
        case 1:
            filename = usuari(LLEGIR)
            llegircsv(filename)
        case 2:
            filename=usuari(LLEGIR)
            dades=contingut(filename)
            afegircsv(filename,dades)

def llegircsv(file_name):
    with open('C:\\Users\\aleii\\'+file_name, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        line_count = 0
        print("La capçalera és: ", end="")
        for row in readCSV:
            print(','.join(row))

def afegircsv(file_name,dades):
    with open('C:\\Users\\aleii\\'+file_name, 'a', encoding='utf-8', newline='') as csvfile:
        writeCSV = csv.writer(csvfile)
        writeCSV.writerow(dades)
    read_file('C:\\Users\\aleii\\'+file_name)