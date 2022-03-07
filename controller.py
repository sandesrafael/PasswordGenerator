from constants import MIN_CHAR, MAX_CHAR, MIN_NUM, MAX_NUM
import random
import string
from menu import *
from insert_values import InputValues


class PasswordController:
    def __init__(self) -> None:
        pass

    def char_number(self):
        char_num = InputValues.input_char(self)

        print("Valor recebido da função input char:  ", char_num)

        if char_num >= MIN_CHAR and char_num <= MAX_CHAR:
            continue_stmt = "continue"
        else:
            print("Please type a value between 12 and 20 characters")
            Menu.options()

        return char_num

    def digits_generate(self):
        digits_num = InputValues.input_digits(self)
        numbers = string.digits

        if MIN_NUM <= digits_num <= MAX_NUM:
            random_num = ''.join(random.sample(numbers, digits_num))
            return random_num

        # Check if the number of symbols is invalid. (less than 1 and greater than 3)
        elif digits_num < MIN_NUM or digits_num > MAX_NUM:
            print("The value must have a min of 1 and a max of 3 digits. \n")
            print("Try Again!!")
            Menu.options()
        # Check if symbols number is greater than 2 or if it's an integer
        else:
            print("Invalid value! Please type an integer.")

        return digits_num


    def symbols_generate(self):
        symbols_num = InputValues.input_symbols(self)
        allowed_symbols = ['@', '#', '!', '$', '&', '_']
        choice_symbol_list = []
        
        # Check if the number of symbols is valid. (greater than 1 and less than 3)
        if MIN_NUM <= symbols_num <= MAX_NUM:
                for i in range(0, symbols_num):
                    symbol = input(
                        f"Choose {i + 1} symbol(s) to use! Allowed [#,!,$,&,@] \n")  # Input the number of symbols
                    # Add symbols at the list
                    choice_symbol_list.append(symbol)
                # Check if the values are duplicates in the same table
                if len(choice_symbol_list) != len(set(choice_symbol_list)):
                    print("You can't to repeat the symbols!")
                    choice_symbol_list.clear()
                    Menu.options()
                else:
                    continue_stmt = "continue"

                # Checks if the symbols chosen are allowed
                check = all(
                    item in allowed_symbols for item in choice_symbol_list)
                if check is True:
                    continue_stmt = "continue"
                else:
                    print("Invalid Symbol!\n")
                    print("Try Again!!")
                    Menu.options()
            # Check if symbols number is less than 1 and greater than 2
        else:
            print("The value must have a min of 1 and a max of 3 symbols. \n")
            Menu.options()

        # convert list to string using join
        symbol_str = ''.join(choice_symbol_list).replace(" ", "")

        return symbol_str


    def upper_generator(self):
        choice_upper_list = []
        upper = string.ascii_uppercase
        upper_number = InputValues.input_upper(self)

        if MIN_NUM <= upper_number <= MAX_NUM:  # Check if the number of upper is valid. (greater than 1 and less than 3)
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
                Menu.options()

            # Check if the values are duplicates in the same table
            if len(choice_upper_list) != len(set(choice_upper_list)):
                print("You can't to repeat the uppercase! ")
                print("Try Again")
                choice_upper_list.clear()
                Menu.options()
            else:
                continue_stmt = "continue"

            break_stmt = "break"

        elif upper_number < MIN_NUM or upper_number > MAX_NUM:  # Check if the number of uppercase is invalid. (greater than 1 and less than 3)
            print("The value must have a min of 1 and a max of 3 numbers. \n")
            Menu.options()
        else:
            print("ERROR!!")
            exit()

        # Convert: from list to string
        upper_str = ' '.join(map(str, choice_upper_list)).replace(" ", "")

        return upper_str