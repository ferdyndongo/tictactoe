# write your code here
s = "_________"
move_X = True
move_O = not move_X


def print_grid():
    print("---------")
    print(f"| {s[0]} {s[1]} {s[2]} |".replace("_", " "))
    print(f"| {s[3]} {s[4]} {s[5]} |".replace("_", " "))
    print(f"| {s[6]} {s[7]} {s[8]} |".replace("_", " "))
    print("---------")


rows = [[s[i] for i in range(3)], [s[i] for i in range(3, 6)], [s[i] for i in range(6, 9)]]
columns = [[s[i] for i in range(0, 9, 3)], [s[i] for i in range(1, 9, 3)], [s[i] for i in range(2, 9, 3)]]
diagonal = [s[i] for i in range(2, 8, 2)]


def x_win():
    return 3 in [r.count('X') for r in rows] or 3 in [c.count('X') for c in columns] or diagonal.count('X') == 3


def o_win():
    return 3 in [r.count('O') for r in rows] or 3 in [c.count('O') for c in columns] or diagonal.count('O') == 3


def empty_cell():
    return "_" in s or " " in s


def impossible():
    return (x_win() and o_win()) or (abs(s.count('X') - s.count('O')) >= 2)


def game_state():
    if not x_win() and not o_win() and empty_cell() and not impossible():
        return True
    elif not x_win() and not o_win() and not empty_cell():
        print("Draw")
        return False
    elif impossible():
        print("Impossible")
        return False
    elif x_win():
        print("X wins")
        return False
    elif o_win():
        print("O wins")
        return False


def check_input():
    if not x.isdigit() or not y.isdigit():
        print("You should enter numbers!")
        return False
    elif int(x) > 3 or int(y) > 3:
        print("Coordinates should be from 1 to 3!")
        return False
    elif rows[int(x) - 1][int(y) - 1] == "X" or rows[int(x) - 1][int(y) - 1] == "O":
        print("This cell is occupied! Choose another one!")
        return False
    else:
        return True


print_grid()

while game_state():
    x, y = input("Enter the coordinates:").split()
    while not check_input():
        x, y = input("Enter the coordinates:").split()
    if move_X:
        rows[int(x) - 1][int(y) - 1] = "X"
        s = [r for row in rows for r in row]
        columns = [[s[i] for i in range(0, 9, 3)], [s[i] for i in range(1, 9, 3)], [s[i] for i in range(2, 9, 3)]]
        diagonal = [s[i] for i in range(2, 8, 2)]
        move_X = False
    else:
        rows[int(x) - 1][int(y) - 1] = "O"
        s = [r for row in rows for r in row]
        columns = [[s[i] for i in range(0, 9, 3)], [s[i] for i in range(1, 9, 3)], [s[i] for i in range(2, 9, 3)]]
        diagonal = [s[i] for i in range(2, 8, 2)]
        move_X = True
    print_grid()
