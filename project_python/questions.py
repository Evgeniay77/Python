questions = ('Какой язык мы учим?', 'Какой тип данных имеет целая переменная?', 'Какой тип данных имеет вещественная переменная?', 'Какой тип данных имеет логическая переменная?', 'Какой тип данных имеет символьная переменная?')
answers = ('Python', 'Integer', 'Float', 'Bool', 'String')
i = 0
count_answers = 0
while i < len(questions):
    user_answers = input('{}...'.format(questions[i]))
    if user_answers.capitalize() == answers[i]:
        count_answers = count_answers + 1
    i += 1
print('Было задано {i} вопросов. Правильных ответов - {count_answers}!'.format(i = i, count_answers = count_answers))
