from controller import PasswordController
import string
import random


class GeneratePassword:
    def __init__(self) -> None:
        pass

    def password(self):
        pswdcontroller = PasswordController()

        lower = string.ascii_lowercase  # recebe uma string com letras minusculas
        char_num = pswdcontroller.char_number()
        digits_num = pswdcontroller.digits_generate()
        symbols_num = pswdcontroller.symbols_generate()
        upper_num = pswdcontroller.upper_generator()

        # Retorna a subtração do char_num(12) em relação ao num(3)    = 9
        lower_num = char_num - \
            (len(digits_num) + len(symbols_num) + len(upper_num))

        # retorna letras em lowercase de forma aleatoria
        random_lower = ''.join(random.sample(lower, lower_num))
        concat_password = random_lower + digits_num + symbols_num + upper_num
        random_password = ''.join(random.sample(
            concat_password, len(concat_password)))
        print("\nYour random password is:", random_password)

        return random_password
