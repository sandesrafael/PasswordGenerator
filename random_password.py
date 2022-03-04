from constants import NUM_MIN, NUM_MAX
import random
import string
import menu


class PasswordGenerate:

    def __init__(self, char_min, char_max):
        self.char_min = char_min
        self.char_max = char_max
        
    def char_number(self, min_char, max_char):
        try:
            char_num = int(input("\nHow many characters would you like in your password (Between 12 and 20)? \n"))

            if char_num >= min_char and char_num <= max_char:
                continue_stmt = "continue"
            else:
                print("Please type a value between 12 and 20 characters")
                exit()
        except ValueError:
            print("Invalid value! Please type an integer.")

        return char_num

    def digits_number(self, min_digits, max_digits):
        numbers = string.digits

        try:
            digits_num = int(input("\nHow many numbers would you like in your password  (The minimum is 1)? \n"))
        except ValueError:
            print("Invalid Value!! Please type an integer")
            exit()
        
        if min_digits <= digits_num <= max_digits:

            random_num = ''.join(random.sample(numbers, digits_num))
            return random_num

        elif digits_num < min_digits or digits_num > max_digits:  # Check if the number of symbols is invalid. (less than 1 and greater than 3)
            print("The value must have a min of 1 and a max of 3 digits. \n")
            print("Try Again!!")
            menu.menu()
        # Check if symbols number is greater than 2 or if it's an integer
        else:
            print("Invalid value! Please type an integer.")

    def symbols_generator(self, min_symbols, max_symbols):
        allowed_symbols = ['@', '#', '!', '$', '&', '_']
        choice_symbol_list = []
        symbol_str = ""
        symbol = ""

        try:
            symbols_number = int(input("How many symbols would you like in your password (min = 1 / max = 2)? \n"))
            if min_symbols <= symbols_number <= max_symbols:  # Check if the number of symbols is valid. (greater than 1 and less than 3)
                for i in range(0, symbols_number):
                    symbol = input(
                        f"Choose {i + 1} symbol(s) to use! Allowed [#,!,$,&,@] \n")  # Input the number of symbols
                    choice_symbol_list.append(symbol)  # Add symbols at the list
                # Check if the values are duplicates in the same table
                if len(choice_symbol_list) != len(set(choice_symbol_list)):
                    print("You can't to repeat the symbols!")
                    choice_symbol_list.clear()
                    menu.menu()
                else:
                    continue_stmt = "continue"

                # Checks if the symbols chosen are allowed
                check = all(item in allowed_symbols for item in choice_symbol_list)
                if check is True:
                    continue_stmt = "continue"
                else:
                    print("Invalid Symbol!\n")
                    print("Try Again!!")
                    menu.menu()
            # Check if symbols number is less than 1 and greater than 2
            else:
                print("The value must have a min of 1 and a max of 3 symbols. \n")
                menu.menu()
        except ValueError:
            print("Invalid value! Input an integer.")
            menu.menu()

        # convert list to string using join
        symbol_str = ''.join(choice_symbol_list).replace(" ", "")

        return symbol_str

    def upper_generator(self, min_upper, max_upper):
        choice_upper_list = []
        upper = string.ascii_uppercase
        upper_number = None

        try:
            upper_number = int(input("\nHow many uppercase would you like in your password  (The minimum is 1)? \n"))
        except ValueError:
            print("Invalid value! Type an integer")
            menu.menu()

        if min_upper <= upper_number <= max_upper:  # Check if the number of upper is valid. (greater than 1 and less than 3)
            for i in range(0, upper_number):
                uppers = input(
                    f"Choose {i + 1} uppercase to use! \n").upper()  # Input the number of symbols
                choice_upper_list.append(uppers)  # Add symbols at the list

            # # Checks if the uppercase chosen are allowed
            check = all(item in upper for item in choice_upper_list)
            if check:
                continue_stmt = "continue"
            else:
                print("Invalid Value! Please type allowed values.\n")
                menu.menu()

            # Check if the values are duplicates in the same table
            if len(choice_upper_list) != len(set(choice_upper_list)):
                print("You can't to repeat the uppercase! ")
                print("Try Again")
                choice_upper_list.clear()
                menu()
            else:
                continue_stmt = "continue"

            break_stmt = "break"

        elif upper_number < min_upper or upper_number > max_upper:  # Check if the number of uppercase is invalid. (greater than 1 and less than 3)
            print("The value must have a min of 1 and a max of 3 numbers. \n")
            menu()
        else:
            print("ERROR!!")
            exit()

        # Convert: from list to string
        upper_str = ' '.join(map(str, choice_upper_list)).replace(" ", "")

        return upper_str

    def generate_password(self):
        lower = string.ascii_lowercase # recebe uma string com letras minusculas
        
        char_num = self.char_number(self.char_min, self.char_max)
        digits = self.digits_number(NUM_MIN, NUM_MAX)
        symbols = self.symbols_generator(NUM_MIN, NUM_MAX)
        upper = self.upper_generator(NUM_MIN, NUM_MAX) 


        # Retorna a subtração do char_num(12) em relação ao num(3)    = 9
        lower_num = char_num - ( len(digits) + len(symbols) + len(upper))

        # retorna letras em lowercase de forma aleatoria
        random_lower = ''.join(random.sample(lower, lower_num))
        concat_password = random_lower + digits + symbols + upper
        random_password = ''.join(random.sample(concat_password, len(concat_password)))

        print("\nYour random password is:", random_password)

        return random_password