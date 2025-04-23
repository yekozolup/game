from random import randint

def start():
    randNum = randint(1, 10)
    countStep = 0

    print(f"Введіть число від 1 до 10:")

    while countStep < 3:
        countStep += 1
        userNum = int(input())
        if userNum == randNum:
            print(f"Ви ввели правильне число!")
            print(f"Вітаємо Вас!")
            break
        elif countStep == 3:
            print(f"Ви програли :(")
        else:
            print(f"Ви не вгадали :(")
            print(f"У вас ще є {3 - countStep} спрб. Введіть число від 1 до 10:")
    else:
        print(f"Задане число - {randNum}")

print(f"Вітаємо в грі Guess Number! Ви маєте 3 спроби на вгадування числа.")
isPlay = "y"
while isPlay == "Y" or isPlay=="y":
    start()
    print(f"Чи хочете ви пограти ще? (Y/N)")
    isPlay = input()
print(f"Бувайте! Чекаємо Вас знову!")