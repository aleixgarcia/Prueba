# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():

    num1=int(input("introdueix el primer num: "))
    num2=int(input("introdueix el segon num: "))
    aux=1

    while num1>num2:
        print("Error!")
        num2=int(input("introdueix un numero major que el primer: "))
    while num1<num2:
        print(num1, end=",")
        num1=aux+num1
    print(num2,end="")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()