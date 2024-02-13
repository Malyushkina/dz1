def newAnswer(param):
    if param == "year":
        userAnswer = input("Введите год рождения А.С.Пушкина  ")
    elif param == "date":
        userAnswer = input("Введите дату рождения А.С.Пушкина  ")

    return userAnswer


bornYear = "1799"
bornDay = "6 июня"

currentAnswer = newAnswer("year")

while currentAnswer != bornYear:
    currentAnswer = newAnswer("year")

currentAnswer = newAnswer("date")
while currentAnswer != bornDay:
    currentAnswer = newAnswer("date")

print("Верно")
