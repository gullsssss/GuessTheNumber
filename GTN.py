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
    if guess == number:
        print("Поздравляю вы угадали это:",number)
        con = input("Продолжить?(y/n): ")
        if con != "y":
            print("Игра завершена")
            break
        else:
            number = random.randint(Fn,Sn)
            continue
    if guess > number:
        print("Загаданное число меньше")
        attempt += 1
    elif guess < number:
        print("Загаданное число больше")
        attempt += 1
    if attempt == "3":
        print("К сожалению вы проиграли было потрачено 3 попытки")
        break
        
