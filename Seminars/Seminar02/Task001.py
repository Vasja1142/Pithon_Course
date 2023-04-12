# Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.
def Task():
    print("Z = not X or Y")
    print("X", "Y", "Z")
    for X in range(2):
        for Y in range(2):
            if not X or Y:
                print(X, Y, 1)
            else:
                print(X, Y, 0)


Task()
