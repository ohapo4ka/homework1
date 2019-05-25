import ephem
import datetime

planets = {
    'mars': ephem.Mars(),
    'moon': ephem.Moon(),
    'venus': ephem.Venus()
}

def ask_user(dialog_data):
    user_question = input('Планета: ').lower().strip()
    for dialog_q in dialog_data:
        if user_question[:len(dialog_q)] == dialog_q:
            return dialog_q
    return ''

def get_constellation(planet_name):
    time_now = datetime.datetime.now()
    ephem_planet = planets[planet_name]
    ephem_planet.compute(time_now)
    return ephem.constellation(ephem_planet)

while True:
    try:
        user_question = ask_user(planets)
    except KeyboardInterrupt:
        print('Программа: до свидания!')
        break
    if len(user_question) > 0:
        print('Программа:', get_constellation(user_question))
    else:
        print('Программа: ???')