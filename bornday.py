"""- Спросить у пользователя год рождения А.С. Пушкина
- Если пользователь ввел верный год спросить у него день рождения
- Если день рождения введен верно вывести 'Верно'
- Если день рождения введен неверно вывести 'Неверный день рождения'
- Если неверно введен год, то сразу вывести 'Неверный год
  рождения', а день рождения не спрашивать
"""

bornYear = "1799"
bornDay = "6 июня"

userAnswerYear = input("Введите год рождения А.С.Пушкина  ")

if userAnswerYear == bornYear:
    userAnswerDay = input("Введите день рождения А.С.Пушкина ")
    if userAnswerDay == bornDay:
        print("Верно")
    else:
        print("Неверный день рождения")
else:
    print("Неверный год рождения")
