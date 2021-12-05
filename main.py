# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():

    sumaA=0
    sumaS=0
    auxA=0
    auxS=0
    notes=list()

    reg=int(input("Introdueix el num de registres de notes:"))

    for x in range(reg):
        notes.append(int(input("Introdueix la nota de l'alumne:")))
        if notes[x]>=4:
            sumaA=notes[x]+sumaA
            auxA=auxA+1
        else:
            sumaS=notes[x]+sumaS
            auxS=auxS+1
    sumaA = sumaA / auxA
    sumaS = sumaS / auxS
    print("***************************************")
    print("Les notes dels alumnes son: ")
    for x in range(reg-1):
        print(notes[x], end=",")
    print(notes[-1],end="")
    print("\n***************************************")

    print("La mitjana dels aprobats es: ",sumaA)
    print("La mitjana dels suspesos es: ", sumaS)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()