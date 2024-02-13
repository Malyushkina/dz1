def newAnswer():
    userAnswer = input("Введите год рождения А.С.Пушкина  ")
    return userAnswer


bornYear = "1799"
currentAnswer = newAnswer()

while currentAnswer != bornYear:
    currentAnswer = newAnswer()

print("Верно")
