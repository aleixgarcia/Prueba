# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def main():

   # Exercici 1 --------------------------------
   nums = [x for x in range(0, 31, 2)]
   print(nums)

   # Exercici 2 --------------------------------
   nums = [x for x in range(1, 1001) if x % 8 == 0]
   print(nums)

   # Exercici 3 --------------------------------
   nums = [x for x in range(1, 1001) if '6' in str(x)]
   print(nums)

   # Exercici 4 --------------------------------
   state = 'Practica els problemes de list comprehensions per a ser més Pythonic!'
   v_state = [x for x in state if x in ' ']
   print("Hay", len(v_state), "espacios")

   # Exercici 5 --------------------------------
   state = 'Practica els problemes de list comprehensions per a ser més Pythonic!'
   f_state = [x for x in state if x not in 'aeioué']
   print(f_state)

   # Exercici 6 --------------------------------
   state = 'Practica els problemes de list comprehensions per a ser més Pythonic!'
   p_state = [x for x in state.split() if len(x) < 6]
   print(p_state)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
