import random

print("Привествуем вас в игре 'Угадай число' чтобы начать введите")
Fn = int(input("От сколько будет идти игра: "))
Sn = int(input("До сколько будет идти игра: "))
number = random.randint(Fn,Sn)

while True:
    guess = int(input("Угадайте число: "))
    if guess == number:
        print("Поздравляю вы угадали это:",number)
        con = input("Продолжить?(y/n): ")
        if con != "y":
            print("Игра завершена")
            break
        else:
            continue
    if guess > number:
        print("Загаданное число меньше")
    if guess < number:
        print("Загаданное число больше")
        
