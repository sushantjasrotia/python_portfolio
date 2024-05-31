def sum(a, b, c):
    return a + b + c

def Board(x_state, y_state):
    zero = 'X' if x_state[0] else ('O' if y_state[0] else 0)
    one = 'X' if x_state[1] else ('O' if y_state[1] else 1)
    two = 'X' if x_state[2] else ('O' if y_state[2] else 2)
    three = 'X' if x_state[3] else ('O' if y_state[3] else 3)
    four = 'X' if x_state[4] else ('O' if y_state[4] else 4)
    five = 'X' if x_state[5] else ('O' if y_state[5] else 5)
    six = 'X' if x_state[6] else ('O' if y_state[6] else 6)
    seven = 'X' if x_state[7] else ('O' if y_state[7] else 7)
    eight = 'X' if x_state[8] else ('O' if y_state[8] else 8)

    print(f"  {zero}  |  {one}  |  {two}  ")
    print(f"-----|-----|-----")
    print(f"  {three}  |  {four}  |  {five}  ")
    print(f"-----|-----|-----")
    print(f"  {six}  |  {seven}  |  {eight}  ")
    print(f"-----|-----|-----")


def checkWins(x_state, y_state):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
             [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        if(sum(x_state[win[0]], x_state[win[1]], x_state[win[2]]) == 3):
            print("X won the match")
            return 1

        if (sum(y_state[win[0]], y_state[win[1]], y_state[win[2]]) == 3):
            print("O won the match")
            return 0

    return -1


x_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
y_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]

turn = 1 # 1 for x and 0 for O
print("Welcome to Tic Tac Toe")

while True:
    Board(x_state, y_state)
    if(turn == 1):
        print("This is  X Turn ")
        value = int(input("Please enter value form 0 - 9 (where you to place your X): "))
        x_state[value] = 0
    else:
        print("This is  Y Turn ")
        value = int(input("Please enter value form 0 - 9 (where you to place your O): "))
        y_state[value] = 0
        

    a = checkWins(x_state,y_state)
    if(a != -1):
        Board(x_state,y_state)
        print("match over")

        break


    turn = 1-turn


