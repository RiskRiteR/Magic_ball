from random import *

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.',
      'Как тебя зовут?', sep='\n')

name_user = input()

print(f'Привет, {name_user}!', '', sep='\n')


def is_valid(user_correct_text):
    """
    Проверяет правильность введённых пользователем данных
    в repeat_or_not.
    """
    correct_text = ['y', 'n']
    return correct_text.count(user_correct_text) if True else False


repeat_or_not = 'y'
while repeat_or_not == 'y':
    print('Какой у Вас вопрос?', '', sep='\n')
    question = input()
    print(choice(answers), '', 'Хочешь задать ещё вопрос? (y/n)', sep='\n')
    counter = 0
    while counter == 0:
        repeat_or_not_user = input()
        if is_valid(repeat_or_not_user):
            repeat_or_not = repeat_or_not_user
            counter = 1
        else:
            print('Введено не верное значение! Попробуйте ещё раз!',
                'Введите y/n для нового вопроса или выхода из программы соответственно:', sep='\n')

if repeat_or_not == 'n':
    print('Возвращайся если возникнут вопросы!')