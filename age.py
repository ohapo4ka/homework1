age = int(input("Укажите свой возраст: "))

if age <= 0:
    print("Всё плохо...")
elif age <= 7:
    print("Вы посещаете детский сад")
elif age <= 17:
    print("Вы посещаете школу")
elif age <= 23:
    print("Вы учитесь в ВУЗе")
elif age <= 60:
    print("Вы работаете")
else:
    print("Вы на пенсии (?) Ожидайте смерти")


