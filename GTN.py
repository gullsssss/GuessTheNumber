import random

print("Привествуем вас в игре 'Угадай число' чтобы начать введите")
Fn = int(input("От сколько будет идти игра: "))
Sn = int(input("До сколько будет идти игра: "))
at = int(input("Сколько попыток у вас будет попыток: "))
number = random.randint(Fn,Sn)
attempt = 0
while True:
    try:
        guess = int(input("Угадайте число: "))
    except:
        print("Вводите только числа")
        continue
    attempt += 1
    if guess == number:
        print("Поздравляю вы угадали это:",number, "вы потратили", attempt, "попытки")
        con = input("Продолжить?(y/n): ")
        if con != "y":
            print("Игра завершена")
            break
        else:
            Fn = int(input("От сколько будет идти игра: "))
            Sn = int(input("До сколько будет идти игра: "))
            number = random.randint(Fn,Sn)
            attempt = 0
            continue
    if guess > number:
        print("Загаданное число меньше")
    elif guess < number:
        print("Загаданное число больше")
    if attempt == at:
        print("К сожалению вы проиграли было потрачено", at, "попыток")
        con = input("Прололжить?(y/n): ")
        if con != "y":
            break
        else:
            continue      
