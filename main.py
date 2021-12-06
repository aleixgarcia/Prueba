# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():

   dict={
       "username":[],
       "department":[],
       "classroom":[]
   }

   num=int(input("Introdueix el num d'usuaris: "))

   for x in range(num):
       user=str(input("Introdueix el nom d'usuari: "))
       dict["username"]=user

       dpt=str(input("Introdueix el nom de departament: "))
       dict["department"]=dpt

       clas=int(input("Introdueix el numero de classe:"))
       while clas<1 or clas>15:
           clas= int(input("Introdueix un num de l'1 al 15:"))
       dict["classroom"]=clas

       for x in range(1):
           print("*************************************************")
           print("USUARI\t\t|\tDEPARTAMENT\t|\t\tCLASSE")
           print("-------------------------------------------------")
           print(dict["username"],dict["department"],dict["classroom"],sep="\t\t|\t\t")
       print("*************************************************")
       dict.clear()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()