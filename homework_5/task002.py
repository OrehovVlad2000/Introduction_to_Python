# Создайте программу для игры с конфетами человек против человека.
#
#  Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется
#  жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний
#  ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
import random

print("Добро пожаловать в игру с конфетами!")
print("Правила игры: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. \nПервый ход "
      "определяется жеребьёвкой. \nЗа один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются "
      "сделавшему последний ход.")
user_1 = input("Введите имя первого игрока: ")
user_2 = input("Введите имя второго игрока: ")
candies = 2021

first_move = random.randint(1, 2)
if first_move == 1:
    print(f"Первым ходит: {user_1}")
    first_user = user_1
    second_user = user_2
else:
    print(f"Первым ходит: {user_2}")
    first_user = user_2
    second_user = user_1
candy_first_user = 0
candy_second_user = 0


def take_candy(player):
    while True:
        value = int(input(f"{player}, введите количество конфет: "))
        if candies >= 28:
            if not (0 < value < 29):
                print("Нельзя взять столько конфет!")
                continue
        else:
            if not (0 < value <= candies):
                print("Нельзя взять столько конфет!")
                continue
        return value


count = 0
while True:
    if count % 2 == 0:
        temp = take_candy(first_user)
        candy_first_user += temp
        candies -= temp
        flag = first_user
    else:
        temp = take_candy(second_user)
        candy_second_user += temp
        candies -= temp
        flag = second_user
    count += 1
    print(f"Осталось: {candies} конфет")
    print(f"{first_user}: {candy_first_user} конфет")
    print(f"{second_user}: {candy_second_user} конфет")
    if candies == 0:
        if flag == first_user:
            candy_first_user += candy_second_user
            candy_second_user = 0
            print(f"Победил: {first_user}! У него {candy_first_user} конфет!")
        else:
            candy_second_user += candy_first_user
            candy_first_user = 0
            print(f"Победил: {second_user}! У него {candy_second_user} конфет!")
        break
