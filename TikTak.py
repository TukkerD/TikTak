# This is the game Tic-Tac-Toe created in python for CSE210.
# Author : Tukker De Hart

# This function asks and tracks the 'X' players placement on the board.
def player_x():
    # We ask the player 'O' what spot on the board they want to choose then return that place when
    # it's called upon in a different function.
    x = input("Numbers 1-6 which one do you pick, 'X'? ")
    return int(x)


# This function asks and tracks the 'O' players placement on the board.
def player_o():
    # We ask the player 'O' what spot on the board they want to choose then return that place when
    # it's called upon in a different function.
    o = input("Numbers 1-6 which one do you pick, 'O'? ")
    return int(o)


# This is where a majority of the checks happen and where the table is asked to render.
# We check to see if a winner is declared, then if not it runs a loop asking for placement for the players
# and places them on the board via a list.
def table():
    winner = False
    table_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while winner == False:
        # Here it calls the function print_list to print the list with the list
        # as the argument because its fluid.
        print_list(table_list)

        # We ask for 'X' to play and then -1 to their response to
        # correctly pick the list item to change to 'X'
        x = player_x()
        table_list[x - 1] = 'X'

        # Here we check for the win condition. 3 across or diagonal to win.
        # If those conditions are met it tells the player and exits the loop!
        if win_test(table_list) == 'X' or win_test(table_list) == 'O':
            winner = True
            print_list(table_list)
            print(f'You won, {win_test(table_list)}!!')
            break

        # If the conditions are not met it'll just move on.
        else:
            pass

        # Just like above we print the list and when 'O' selects a spot it is replaced with 'O'.
        print_list(table_list)
        o = player_o()
        table_list[o - 1] = 'O'

        # We then check again to see if a player won.
        # We check twice to make sure a player didn't win then it keeps playing for another turn.
        if win_test(table_list) == 'X' or win_test(table_list) == 'O':
            winner = True
            print_list(table_list)
            print(f'You won, {win_test(table_list)}!!')
            break
        else:
            pass


# When win_test is called it goes through a bunch of if statements to see if the list has the X's or O's
# In a winning order.
def win_test(table_list):
    # These check the rows to see if there are 3 in a row.
    if table_list[0] == 'X' and table_list[1] == 'X' and table_list[2] == 'X':
        return 'X'
    if table_list[0] == 'O' and table_list[1] == 'O' and table_list[2] == 'O':
        return 'O'
    if table_list[3] == 'X' and table_list[4] == 'X' and table_list[5] == 'X':
        return 'X'
    if table_list[3] == 'O' and table_list[4] == 'O' and table_list[5] == 'O':
        return 'O'
    if table_list[6] == 'X' and table_list[7] == 'X' and table_list[8] == 'X':
        return 'X'
    if table_list[6] == 'O' and table_list[7] == 'O' and table_list[8] == 'O':
        return 'O'
    # These check the columns to see if there are 3 in a row.
    if table_list[0] == 'X' and table_list[3] == 'X' and table_list[6] == 'X':
        return 'X'
    if table_list[0] == 'O' and table_list[3] == 'O' and table_list[8] == 'O':
        return 'O'
    if table_list[1] == 'X' and table_list[4] == 'X' and table_list[7] == 'X':
        return 'X'
    if table_list[1] == 'O' and table_list[4] == 'O' and table_list[7] == 'O':
        return 'O'
    if table_list[2] == 'X' and table_list[5] == 'X' and table_list[8] == 'X':
        return 'X'
    if table_list[2] == 'O' and table_list[5] == 'O' and table_list[8] == 'O':
        return 'O'
    # These check the diagonals to see if there are 3 in a diagonal.
    if table_list[0] == 'X' and table_list[4] == 'X' and table_list[8] == 'X':
        return 'X'
    if table_list[0] == 'O' and table_list[4] == 'O' and table_list[8] == 'O':
        return 'O'
    if table_list[2] == 'X' and table_list[4] == 'X' and table_list[6] == 'X':
        return 'X'
    if table_list[2] == 'O' and table_list[4] == 'O' and table_list[6] == 'O':
        return 'O'
    else:
        return


# When called it prints the list to show the most up-to-date board info.
def print_list(table_list):
    print('')
    print(f"{table_list[0]} | {table_list[1]} | {table_list[2]}\n"
          "--+---+--\n"
          f"{table_list[3]} | {table_list[4]} | {table_list[5]}\n"
          "--+---+--\n"
          f"{table_list[6]} | {table_list[7]} | {table_list[8]}")


def main():
    table()


if __name__ == '__main__':
    main()
