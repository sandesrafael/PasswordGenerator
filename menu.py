from  password_generator import *
from main import *


class Menu:
    def __init__(self) -> None:
        pass

    def options(self):
        print("\n########### WELCOME TO THE PASSWORD GENERATOR ###########\n")

        option = True
        while option:
            print("""
                1 - Generate a new password
                2 - Exit
                """)
            option = input("What would you like to do? ")

            if option == "1":
                GeneratePassword.password(self)
                exit()
            elif option == "2":
                print("\n Closing...")
                option = False
                exit()
            else:
                print("\n Not Valid Choice!\n Try again")