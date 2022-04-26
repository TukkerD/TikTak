# This is the game Tic-Tac-Toe created in python for CSE210.
# Author : Tukker De Hart

def player_x():
    x = input("Numbers 1-6 which one do you pick, 'X'? ")
    return int(x)


def player_o():
    o = input("Numbers 1-6 which one do you pick, 'O'? ")
    return int(o)


def table():
    winner = False
    table_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    test = 'Y'
    while winner == False:
        print_list(table_list)
        x = player_x()
        table_list[x - 1] = 'X'

        if win_test(table_list) == 'X' or win_test(table_list) == 'O':
            winner = True
            print(f'You won, {win_test(table_list)}!!')
            break
        else:
            pass

        print_list(table_list)

        o = player_o()
        table_list[o - 1] = 'O'

        if win_test(table_list) == 'X' or win_test(table_list) == 'O':
            winner = True
            print(f'You won, {win_test(table_list)}!!')
            break
        else:
            pass


def win_test(table_list):
    if table_list[0] == 'X' and table_list[1] == 'X' and table_list[2] == 'X':
        return 'X'
    if table_list[0] == 'O' and table_list[1] == 'O' and table_list[2] == 'O':
        return 'O'
    if table_list[3] == 'X' and table_list[4] == 'X' and table_list[5] == 'X':
        return 'X'
    if table_list[3] == 'O' and table_list[4] == 'O' and table_list[5] == 'O':
        return 'O'
    else:
        return


def print_list(table_list):
    print(f"{table_list[0]} | {table_list[1]} | {table_list[2]}\n"
          "--+---+--\n"
          f"{table_list[3]} | {table_list[4]} | {table_list[5]}\n"
          "--+---+--\n"
          f"{table_list[6]} | {table_list[7]} | {table_list[8]}")


table()