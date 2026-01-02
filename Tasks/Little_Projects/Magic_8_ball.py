import random
"""Описание проекта: магический шар 8 (шар судьбы) — шуточный способ предсказывать будущее. 
Программа должна просить пользователя задать некий вопрос, чтобы случайным образом на него ответить."""

def choise(question):
    responses = ['Даже не думай', 
                 'Мой ответ - нет', 
                 'По моим данным - нет', 
                 'Перспективы не очень хорошие', 
                 'Весьма сомнительно', 
                 'Пока неясно, попробуй снова', 
                 'Спроси позже', 
                 'Лучше не рассказывать', 
                 'Сейчас нельзя предсказать', 
                 'Сконцентрируйся и спроси опять', 
                 'Мне кажется - да', 
                 'Вероятнее всего', 
                 'Хорошие перспективы', 
                 'Знаки говорят - да', 
                 'Да', 
                 'Можешь быть уверен в этом', 
                 'Определённо да', 
                 'Никаких сомнений', 
                 'Предрешено', 
                 'Бесспорно']
    
    random.seed(question) # Один и тот же ответ на тот же вопрос
    rnd = random.randint(0, 19)
    message = responses[rnd]
    
    return message

def is_correct_name(name):
    i_name = str(name)
    flag = True
    if i_name.isdigit() or i_name == '':
        flag = False
    return flag

def is_new_question(answer):
    if answer.lower() == 'да':
        return True
    return False

def main():
    greeting_message = 'Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.'
    name_question = 'Пожалуйста назови свое имя'
    name = ''
    ask_for_question_masseage = 'Задайте ваш вопрос: '

    print(greeting_message)
    print(name_question)

    while not is_correct_name(name):
        name = input()
    print('Привет, {0}'.format(name))
    
    working_flag = True
    while working_flag:
        print(ask_for_question_masseage)
        question = input()
        answer = choise(question)
    
        print('Шар отвечает вам - {0}'.format(answer))
        print()
        print('{0}, Хотите задать ещё один вопрос?'.format(name))

        answer = input()
        working_flag = is_new_question(answer)
    
    print('Возвращайся, если возникнут вопросы!')
        

main()