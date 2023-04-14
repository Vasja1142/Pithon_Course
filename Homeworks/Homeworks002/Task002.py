# Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def Truth_table():
    print("U = not (X and Y) or Z")
    print("X", "Y", "Z", "U")
    for X in range(2):
        for Y in range(2):
            for Z in range(2):
                if not (X and Y) or Z:
                    print(X, Y, Z, 1)
                else:
                    print(X, Y, Z, 0)


Truth_table()
