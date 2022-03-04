from constants import MIN_CHAR, MAX_CHAR
import random_password
from main import *


def menu():
    print("\n########### WELCOME TO THE PASSWORD GENERATOR ###########\n")
    password = random_password.PasswordGenerate(MIN_CHAR, MAX_CHAR)

    option = True
    while option:
        print("""
            1 - Generate a new password
            2 - Exit
            """)
        option = input("What would you like to do? ")

        if option == "1":
            password.generate_password()
            exit()
        elif option == "2":
            print("\n Closing...")
            option = False
            exit()
        else:
            print("\n Not Valid Choice!\n Try again")