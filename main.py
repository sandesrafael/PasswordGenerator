from random_password import *


def generate_password():
    char_num = characters_number()
    upper = upper_generator()
    symbol = symbols_generator()
    numbers = digits_generator()

    lower = string.ascii_lowercase
    random_lower = ""

    lower_number = char_num - (len(upper) + len(symbol) + len(numbers))
    random_lower = ''.join(random.sample(lower, lower_number))
    concat_password = upper + symbol + numbers + random_lower

    random_password = ''.join(random.sample(concat_password, len(concat_password)))
    print("\nYour random password is:", random_password)


def menu():
    option = True

    while option:
        print("""\n########### WELCOME TO THE PASSWORD GENERATOR ###########\n
            1 - Generate a new password
            2 - Exit
            """)
        option = input("What would you like to do? ")

        if option == "1":
            generate_password()
            exit()
        elif option == "2":
            print("\n Closing...")
            option = False
            exit()
        else:
            print("\n Not Valid Choice!\n Try again")


if __name__ == '__main__':
    menu()
