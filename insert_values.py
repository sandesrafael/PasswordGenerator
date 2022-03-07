class InputValues:
    def __init__(self) -> None:
        pass

    def input_char(self):
        try:
            char_num = int(input("\nHow many characters would you like in your password (Between 12 and 20)? \n"))
        except ValueError:
            print("Invalid value! Please type an integer.")
            exit()

        return char_num

    def input_digits(self):
        try:
            digits_num = int(input("\nHow many numbers would you like in your password  (The minimum is 1)? \n"))
        except ValueError:
            print("Invalid Value!! Please type an integer")
            exit()
        
        return digits_num

    def input_symbols(self):
        try:
            symbols_num = int(input("How many symbols would you like in your password (min = 1 / max = 2)? \n"))
        except ValueError:
            print("Invalid value! Input an integer.")
            exit()

        return symbols_num

    def input_upper(self):
        try:
            upper_number = int(input("\nHow many uppercase would you like in your password  (The minimum is 1)? \n"))
        except ValueError:
            print("Invalid value! Type an integer")
            exit()

        return upper_number