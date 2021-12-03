# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():

    reg=int(input("Quants valors vols introduir?"))
    llista_codi = list()
    llista_tlf = list()
    llista_edat= list()
    llista_cntcte= list()


    for x in range(reg):


        nom=str(input("Introdueix el teu nom:"))
        cognom1=str(input("Introdeuix el primer cognom:"))
        cognom2=str(input("Introdueix el segon cognom:"))

        llista_codi.append(cognom1[0:2]+cognom2[0:2]+nom[0:2])

        tlf=int(input("Introdueix el telèfon de contacte:"))
        l_tlf=len(str(tlf))
        while l_tlf<9 or l_tlf>9:
            tlf = int(input("Introdueix el telèfon de contacte de 9 nums:"))
            l_tlf = len(str(tlf))
        llista_tlf.append(tlf)

        edat= int(input("introdueix l'edat de la persona: "))
        while edat<=0:
            edat= int(input("introdueix un altre edat de la persona: "))
        llista_edat.append(edat)

        llista_cntcte.append(bool(input("Si vols que tinguem el teu contacte escriu, sino dona-li al enter:")))

    print("****************************************************")
    print("Codi\t|\tTelèfon\t\t|\t\tEdat\t|\tContacte")
    print("----------------------------------------------------")
    for x in range(reg):
        print(llista_codi[x], "\t|\t", llista_tlf[x], "\t|\t\t", llista_edat[x], "\t|\t", llista_cntcte[x])
    print("****************************************************")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()