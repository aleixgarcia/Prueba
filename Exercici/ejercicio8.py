from functions import *
import pandas as pd
import csv

def filecsv8(arxiu):
    #with open(arxiu, encoding="utf8") as csvfile:
    #    readCSV = csv.reader(csvfile, delimiter=',')
        count = 0
        suma=0
    df = pd.read_csv(arxiu, header=0)
        #print("La capçalera és: \n", end="")
    for row in readCSV:
        df['preu'] = df['preu'].astype('int64')
            #print(','.join(row))
        count+=1
        #print(df.dtypes)
    print(df)
    print(f"\nEn total son {df.shape[0]} linies")
        print(f"\nLa suma total dels registros son: {df['preu'].sum()}")
