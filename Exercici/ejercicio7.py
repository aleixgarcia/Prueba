import csv
from functions import *

def filecsv7(arxiu):
    with open(arxiu, encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

def filecsv7(arxiu,dades):
    with open(arxiu,'a+', encoding='utf-8', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        writeCSV.writerow(dades)
    read_file(arxiu)