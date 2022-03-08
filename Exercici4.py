def main():

    frase=str(input("Introdueix una frase: "))
    l_frase=frase.split()
    j=list()
    for i in l_frase:
        j.append(i[0:2])
    print(j)
    print(j[::-1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()