"""Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
Она должна запрашивать у пользователя следующие данные:

1) направление: шифрование или дешифрование;
2) язык алфавита: русский или английский;
3) шаг сдвига (со сдвигом вправо).

Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".
"""

import sys
import time

def working_time(fn: function) -> function:
    def enc_func(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения {fn.__name__}: ", end_time - start_time)
        return result
    return enc_func

def main():

    operation_question = (
        "Введите направление: шифрование или дешифрование. Варианты: enc / dec"
    )
    lang_question = "Введите язык алфавита: русский или английский. Варианты: rus / eng"
    move_question = "Введите шаг сдвига (со сдвигом вправо)"
    text_question = "Введите строку для преобразования"

    operation_dict = {"enc": True, "dec": False}
    language_dict = {
        "rus": {"us_pos": 1040, "ls_pos": 1072, "lenght": 32},
        "eng": {"us_pos": 65, "ls_pos": 97, "lenght": 26},
    }

    print(operation_question)
    opperation = get_correct_reply(check_reply_from_dict, operation_dict)
    print(lang_question)
    lang = get_correct_reply(check_reply_from_dict, language_dict)
    print(move_question)
    move = int(get_correct_reply(check_if_digit))
    print(text_question)
    text = input()

    new_text = ""
    if opperation == "enc":
        new_text = encoder(text, move, language_dict.get(lang))
    elif opperation == "dec":
        new_text = decoder(text, move, language_dict.get(lang))

    print(new_text)
    print("end")


def get_correct_reply(funct: function, dictionary=None) -> str:
    right_message = "Ответ принят"
    wrong_message = "Ответ не верен. Попробуй ещё."
    correct_reply_flag = False
    reply = ""
    while not correct_reply_flag:
        reply = input()
        if is_exit_reply(reply.lower()):
            print("Всего хорошего")
            sys.exit()
        correct_reply_flag = funct(reply, dictionary)
        if correct_reply_flag:
            print(right_message)
        else:
            print(wrong_message)
    return reply

@working_time
def encoder(text: str, move: int, dictionary: dict) -> str:
    new_text = ""
    up_start_pos = dictionary.get("us_pos")
    low_start_pos = dictionary.get("ls_pos")
    lenght = dictionary.get("lenght")
    move = move % lenght
    for char in text:
        if char.isalpha():
            if char.isupper():
                char = get_char_after_move(char, move, up_start_pos, lenght)
            else:
                char = get_char_after_move(char, move, low_start_pos, lenght)
        new_text += char
    return new_text


def get_char_after_move(char: str, move: int, start_pos: int, lenght: int) -> str:
    rel_char_pos = ord(char) - start_pos
    new_rel_pos = rel_char_pos + move
    if new_rel_pos < 0:
        new_rel_pos += lenght
    elif new_rel_pos >= lenght:
        new_rel_pos -= lenght
    new_char_pos = new_rel_pos + start_pos
    return chr(new_char_pos)


def decoder(text: str, move: int, dictionary: dict) -> str:
    return encoder(text, -move, dictionary)


def check_reply_from_dict(reply: str, dictionary: dict) -> bool:
    if reply in dictionary:
        return True
    else:
        return False


def check_if_digit(num: str, *args) -> bool:
    return num.isdigit()


def is_exit_reply(reply: str) -> bool:
    return reply == "exit" or reply == "quit"


if __name__ == "__main__":
    main()


