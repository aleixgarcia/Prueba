# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():

    reg=int(input("Quants valors vols introduir?"))
    llista_codi = ["codi"]
    llista_tlf = ["tlf"]
    llista_edat=["edat"]
    llista_cntcte=["cntcte"]
    x=1

    for x in range(0,reg):
        codi = x + 1
        llista_codi.append(codi)

        tlf = int(input("Introdueix el num de telefon de la persona :"))
        llista_tlf.append(tlf)

        edat = int(input("introdueix l'edat de la persona: "))
        llista_edat.append(edat)

        cntcte = bool(input("Si vols que tinguem el teu contacte escriu, sino dona-li al enter:"))
        llista_cntcte.append(cntcte)

    print("***********************************************")
    print("Codi\t|\tTelèfon\t\t|\tEdat\t\t|\tContacte")
    for x in range(0, reg):
        print("\t", llista_codi[x+1], "\t|\t", llista_tlf[x+1], "\t|\t\t", llista_edat[x+1], "\t|\t", llista_cntcte[x+1])
    print("***********************************************")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


