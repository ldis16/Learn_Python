import random
import sys

default_minimum = 1
default_maximum = 100
greeting_message = "Добро пожаловать в числовую угадайку. Для выхода напишите - Exit"


def is_valid(arg, minimum, maximum=sys.maxsize):
    return arg.isdigit() and minimum <= int(arg) <= maximum


def get_answer(guess, hide_num):
    message = ""
    flag = False

    if int(guess) < hide_num:
        message = "Ваше число меньше загаданного, попробуйте еще разок"
    elif int(guess) > hide_num:
        message = "Ваше число больше загаданного, попробуйте еще разок"
    else:
        message = "Вы угадали, поздравляем!"
        flag = True

    return message, flag


def check_exit(arg):
    return arg.lower() == "exit"


def main(minimum, maximum):
    exit_game_flag = False

    while not exit_game_flag:

        guessed_flag = False
        hide_num = random.randint(minimum, maximum)
        counter = 0
        maximum_set_flag = False
        start_message = "Установите большее значение или нажмите Enter для занчения по умолчанию. По умолчанию - 100"
        new_game_message = "Новая игра!"
        fillers = "*" * ((len(start_message) - len(new_game_message)) // 2)

        print(greeting_message)
        print(fillers + new_game_message + fillers)
        print(start_message)

        while not maximum_set_flag and not exit_game_flag:
            message = ""
            num = input()
            if check_exit(num):
                exit_game_flag = True
            elif num == "":
                maximum_set_flag = True
            elif not is_valid(num, minimum):
                message = (
                    "А может быть все-таки введем целое число большее от {0}?".format(
                        minimum
                    )
                )
            else:
                maximum = int(num)
                maximum_set_flag = True
        if maximum_set_flag:
            hide_num = random.randint(minimum, maximum)
            message = "Загаданно число от {0} до {1}".format(minimum, maximum)
            print(message)

        while not guessed_flag and not exit_game_flag:

            guess = input()

            if check_exit(guess):
                exit_game_flag = True
                break
            elif not is_valid(guess, minimum, maximum):
                message = "А может быть все-таки введем целое число от 1 до 100?"
            else:
                counter += 1
                message, guessed_flag = get_answer(guess, hide_num)
            print(message)

        print("Количество попыток - {0}".format(counter))

        # exit_game_flag = True

    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")


main(default_minimum, default_maximum)
