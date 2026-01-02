"""
Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля,
а также на то, какие символы требуется в него включить, а какие исключить.
"""

import random


def main():
    pass_lenght = 0
    digits = "0123456789"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation = "!#$%&*+-=?@^_"
    ambiguous_to_delete = "il1Lo0O"
    chars = ""
    list_of_num_repiles = []
    list_of_bool_replies = []

    numeric_questions = ["Количество паролей для генерации", "Длину одного пароля"]

    bool_questions = [
        "Включать ли цифры 0123456789?",
        "Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?",
        "Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz?",
        "Включать ли символы !#$%&*+-=?@^_?",
        "Исключать ли неоднозначные символы il1Lo0O?",
    ]

    for question in numeric_questions:
        message = ""
        print(question)
        reply_is_correct = False

        while not reply_is_correct:
            reply = input()
            if reply.isdigit() and int(reply) > 0:
                message = "Ответ принят"
                reply_is_correct = True
                list_of_num_repiles.append(int(reply))
            else:
                message = "Ответ не верен. Только цифры больше 0"
                reply_is_correct = False
            print(message)

    for question in bool_questions:

        print(question)
        reply_is_correct = False

        while not reply_is_correct:
            reply = input().lower()
            reply_is_correct = is_reply_yes_no(reply)
            if reply_is_correct:
                message = "Ответ принят"
                if reply == "да" or reply == "yes":
                    list_of_bool_replies.append(True)
                else:
                    list_of_bool_replies.append(False)
            else:
                message = "Ответ неверен - только да/нет или yes/no попробуй ещё"
            print(message)

    if list_of_bool_replies[0]:
        chars += digits
    if list_of_bool_replies[1]:
        chars += lowercase_letters
    if list_of_bool_replies[2]:
        chars += uppercase_letters
    if list_of_bool_replies[3]:
        chars += punctuation
    if list_of_bool_replies[4]:
        for c in ambiguous_to_delete:
            chars = chars.replace(c, "")

    for _ in range(list_of_num_repiles[0]):
        password = generate_password(list_of_num_repiles[1], chars)
        print(password)


def generate_password(lenght: int, chars: str):
    password = ""
    for _ in range(lenght):
        rnd = random.randrange(len(chars))
        password += chars[rnd]
    return password


def is_reply_yes_no(reply: str):
    return reply == "да" or reply == "нет" or reply == "yes" or reply == "no"


if __name__ == "__main__":
    main()
