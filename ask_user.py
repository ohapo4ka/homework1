def ask_user():
    while True:
        user_answer = input('Как дела? ').lower().strip()        
        if user_answer == 'хорошо':
            break

ask_user()