def main():

    llista=list()

    for num in range(1,26):
        if num % 2 == 0:
            llista.append(num*3)
        else:
            llista.append(num / 2)

    print(llista)
    print(llista[18::])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()