import csv
from functions import *
def filecsv7(arxiu,dades):
    with open(arxiu,'a+', encoding='utf-8', newline='') as csvfile:
        writeCSV = csv.writer(csvfile, delimiter=',')
        writeCSV.writerow(dades)
    read_file(arxiu)