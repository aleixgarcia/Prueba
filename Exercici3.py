def main():


    numeros=list(range(1000))
    l_num=[x if x % 2 == 0 and x % 3 !=0 else -1 for x in numeros ]
    print(numeros)
    print(l_num)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()