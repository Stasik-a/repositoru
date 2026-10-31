import random

number = random.randint(1, 100)

while True:
    guess = int(input("Вгадай число від 1 до 100: "))

    if guess == number:
        print("🎉 Ти вгадав!")
        break

    distance = abs(number - guess)

    if distance <= 3:
        print("🔥 Дуже близько!")
    elif distance <= 10:
        print("😊 Близько!")
    else:
        print("🥶 Далеко!")