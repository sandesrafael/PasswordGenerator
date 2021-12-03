import random
import string


def characters_number():
    char_number = 0

    try:
        char_number = int(input("\nHow many characters would you like in your password (Between 12 and 20)? \n"))
        if 12 <= char_number <= 20:
            continue_stmt = "continue"
        elif char_number < 12 or char_number > 20:
            print("Please type a value between 12 and 20 characters")
            menu()
    except ValueError:
        print("Invalid value! Please type an integer.")

    return char_number


def upper_generator():
    choice_upper_list = []
    upper = string.ascii_uppercase
    upper_number = None

    try:
        upper_number = int(input("\nHow many uppercase would you like in your password  (The minimum is 1)? \n"))
    except ValueError:
        print("Invalid value! Type an integer")
        menu()

    if 1 <= upper_number <= 3:  # Check if the number of upper is valid. (greater than 1 and less than 3)
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
            menu()

        # Check if the values are duplicates in the same table
        if len(choice_upper_list) != len(set(choice_upper_list)):
            print("You can't to repeat the uppercase! ")
            print("Try Again")
            choice_upper_list.clear()
            menu()
        else:
            continue_stmt = "continue"

        break_stmt = "break"

    elif upper_number < 1 or upper_number > 3:  # Check if the number of uppercase is invalid. (greater than 1 and less than 3)
        print("The value must have a min of 1 and a max of 3 numbers. \n")
        menu()
    else:
        print("ERROR!!")
        exit()

    # Convert from list to string
    upper_str = ' '.join(map(str, choice_upper_list)).replace(" ", "")

    return upper_str


def symbols_generator():
    allowed_symbols = ['@', '#', '!', '$', '&', '_']
    choice_symbol_list = []
    symbol_str = ""

    try:
        symbols_number = int(input("How many symbols would you like in your password (min = 1 / max = 2)? \n"))
        if 1 <= symbols_number <= 3:  # Check if the number of symbols is valid. (greater than 1 and less than 3)
            symbol = ""
            for i in range(0, symbols_number):
                symbol = input(
                    f"Choose {i + 1} symbol(s) to use! Allowed [#,!,$,&,@] \n")  # Input the number of symbols
                choice_symbol_list.append(symbol)  # Add symbols at the list
            # Check if the values are duplicates in the same table
            if len(choice_symbol_list) != len(set(choice_symbol_list)):
                print("You can't to repeat the symbols!")
                choice_symbol_list.clear()
            else:
                continue_stmt = "continue"

            # Checks if the symbols chosen are allowed
            check = all(item in allowed_symbols for item in choice_symbol_list)
            if check is True:
                continue_stmt = "continue"
            else:
                print("Invalid Symbol!\n")
                print("Try Again!!")
                menu()

        # Check if symbols number is less than 1 and greater than 2
        else:
            print("The value must have a min of 1 and a max of 3 symbols. \n")
            menu()
    except ValueError:
        print("Invalid value! Input an integer.")
        menu()

    # convert list to string using join
    symbol_str = ''.join(choice_symbol_list).replace(" ", "")

    return symbol_str


def digits_generator():
    numbers = string.digits
    random_numbers = ""
    digits_number = None

    try:
        digits_number = int(input("\nHow many numbers would you like in your password  (The minimum is 1)? \n"))
    except ValueError:
        print("Invalid Value!! Please type an integer")
        exit()

    if 1 <= digits_number <= 3:
        random_numbers = ''.join(random.sample(numbers, digits_number))
        return random_numbers

    elif digits_number < 1 or digits_number > 3:  # Check if the number of symbols is invalid. (less than 1 and greater than 3)
        print("The value must have a min of 1 and a max of 3 symbols. \n")
        print("Try Again!!")
        digits_generator()

    # Check if symbols number is greater than 2 or if it's an integer
    else:
        print("Invalid value! Please type an integer.")

    return random_numbers
