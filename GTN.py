import random

print("Привествуем вас в игре 'Угадай число' чтобы начать введите")
Fn = int(input("От сколько будет идти игра: "))
Sn = int(input("До сколько будет идти игра: "))
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
            number = random.randint(Fn,Sn)
            attempt = 0
            continue
    if guess > number:
        print("Загаданное число меньше")
    elif guess < number:
        print("Загаданное число больше")
    if attempt == 3:
        print("К сожалению вы проиграли было потрачено 3 попытки")
        break
        
