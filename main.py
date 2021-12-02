# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    nom=str(input("introdueix el teu nom: "))
    cognom1=str(input("Introdueix el primer cognom: "))
    cognom2=str(input("Introdueix el segon cognom: "))

    print(cognom1[0:2]+cognom2[0:2]+nom[0:2])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


