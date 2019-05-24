dialog_data = {
    'слыш': 'A?',
    'как дела': 'Хорошо!',
    'что делаешь': 'Интерпретируюсь.',
    'как жизнь': 'Всё тлён...'
}

def ask_user(dialog_data):
    user_question = input('Пользователь: ').lower().strip()
    for dialog_q in dialog_data:
        if user_question[:len(dialog_q)] == dialog_q:
            return dialog_q
    return ''

while True:
    user_question = ask_user(dialog_data)
    if len(user_question) > 0:
        print('Программа:', dialog_data[user_question])
    else:
        print('Программа: Чё?')