# Задача 4*. (Необязательная). Создайте игру в крестики-нолики.

def First_players_move(playing_field):
    flag = True
    while flag:
        first_players_move = int(input('Ход первого игрока: '))
        counter = 0
        counter2 = 0
        for i in playing_field:
            for j in range(3):
                counter += 1
                if first_players_move < 1 and first_players_move > 9:
                    print('Пожалуйста введите число от 1 до 9')
                elif counter == first_players_move and i[j] != 0:
                    print("Такой ход невозможен!")
                    break
                elif counter == first_players_move:
                    i.pop(j)
                    i.insert(j, 1)
                    print(playing_field[0])
                    print(playing_field[1])
                    print(playing_field[2])
                    flag = False
                    break
            counter2 += 1

def Second_players_move(playing_field):
    flag = True
    while flag:
        second_players_move = int(input('Ход второго игрока: '))
        counter = 0
        counter2 = 0
        for i in playing_field:
            for j in range(3):
                counter += 1
                if second_players_move < 1 and second_players_move > 9:
                    print('Пожалуйста введите число от 1 до 9')
                elif counter == second_players_move and i[j] != 0:
                    print("Такой ход невозможен!")
                    break
                elif counter == second_players_move:
                    i.pop(j)
                    i.insert(j, 2)
                    print(playing_field[0])
                    print(playing_field[1])
                    print(playing_field[2])
                    flag = False
                    break
            counter2 += 1

def Check(playing_field):
    a = playing_field[0]
    b = playing_field[1]
    c = playing_field[2]
    if  a == [1, 1, 1] or b == [1, 1, 1] or c == [1, 1, 1]:
        return 1
    elif a[0] & b[0] & c[0] == 1:
        return 1
    elif a[1] & b[1] & c[1] == 1:
        return 1
    elif a[2] & b[2] & c[2] == 1:
        return 1
    elif a[0] & b[1] & c[2] == 1:
        return 1
    elif a[2] & b[1] & c[0] == 1:
        return 1
    elif  a == [2, 2, 2] or b == [2, 2, 2] or c == [2, 2, 2]:
        return 2
    elif a[0] & b[0] & c[0] == 2:
        return 2
    elif a[1] & b[1] & c[1] == 2:
        return 2
    elif a[2] & b[2] & c[2] == 2:
        return 2
    elif a[0] & b[1] & c[2] == 2:
        return 2
    elif a[2] & b[1] & c[0] == 2:
        return 2

def Checking():
    Flag = True
    if Check(playing_field) == 1:
        print("Первый игрок выйграл!")
        Flag = False
    elif Check(playing_field) == 2:
        print("Второй игрок выйграл!")
        Flag = False
    return Flag


playing_field = [   [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]]

Flag = True
while Flag:
    First_players_move(playing_field)
    Flag = Checking()
    if Flag == False:
        break
    Second_players_move(playing_field)
    Flag = Checking()