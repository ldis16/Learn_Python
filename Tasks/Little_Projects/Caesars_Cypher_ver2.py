"""Описание проекта: требуется написать программу, способную шифровать и дешифровать текст в соответствии с алгоритмом Цезаря.
Она должна запрашивать у пользователя следующие данные:

1) направление: шифрование или дешифрование;
2) язык алфавита: русский или английский;
3) шаг сдвига (со сдвигом вправо).

Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).

Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.

Примечание 3. Сохраните регистр символов. Например, текст: "Умом Россию не понять" при сдвиге на одну позицию вправо будет преобразован в: "Фнпн Спттйя ож рпоауэ".
"""
from Modules import working_time

def main():

    question_0 = "Введите текст для обработки"
    question_1_replies = ["ecn", "dec", "b_dec"]
    question_1 = (
        "Введите направление: шифрование, дешифрование или полный перебор. Команды: "
        + " / ".join(question_1_replies)
    )
    question_2_replies = {
        "rus": "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
        "eng": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    }
    question_2 = (
        "Введите язык алфавита: русский или английский: Команды: "
        + " / ".join(question_2_replies)
    )
    question_3 = "Введите число шаг сдвига (со сдвигом вправо)"

    print(question_0)
    text = input()
    opperation = ask_and_wait_for_reply_from_list(question_1, question_1_replies)
    language_pack = question_2_replies.get(
        ask_and_wait_for_reply_from_list(question_2, question_2_replies)
    )
    step = int(ask_and_wait_for_reply_from_list(question_3))

    switch = {"enc" : decoding(text, language_pack, -step), 
              "dec" : decoding(text, language_pack, step), 
              "b_dec" : "\n".join(brute_decoding(text, language_pack))}
    
    result = switch.get(opperation)
    print(result)


def brute_decoding(text: str, language_pack: str) -> list:
    result = []
    for i in range(1, len(language_pack)):
        result.append(decoding(text, language_pack, i) + "  | step: " + str(i))
    return result
@working_time
def decoding(text: str, language_pack: str, step: int) -> str:
    u_lang = language_pack.upper()
    l_lang = language_pack.lower()
    lang_lenght = len(language_pack)
    step = step % lang_lenght
    new_text = ""
    for c in text:
        if c in u_lang:
            cur_pos = u_lang.index(c)
            new_pos = (cur_pos + step) % lang_lenght
            c = u_lang[new_pos]
        elif c in l_lang:
            cur_pos = l_lang.index(c)
            new_pos = (cur_pos + step) % lang_lenght
            c = l_lang[new_pos]
        new_text += c
    return new_text


def ask_and_wait_for_reply_from_list(question: str, correct_replies=None) -> str:
    correct_reply = False
    reply = ""
    while not correct_reply:
        reply = input(question + "\n")
        if correct_replies == None:
            correct_reply = reply.isdigit()
        else:
            correct_reply = reply.lower() in correct_replies
        if correct_reply:
            print("Ответ принят")
        else:
            print("Неверно, попробуйте ещё")
    return reply


if __name__ == "__main__":
    main()
