import string
def playable_board():
    playing_board = [[' ', ' ', ' '],
                     [' ', ' ', ' '],
                     [' ', ' ', ' ']]

    row1 = playing_board[2]
    row2 = playing_board[1]
    row3 = playing_board[0]

    game_on = True
    firsts_turn = True
    while game_on and ' ' in row1 or ' ' in row2 or ' ' in row3:
        while firsts_turn:
            player_x = False
            player_o = False
            # while tie == False:

            # WIN CONDITIONS!
            # CONDITION 1
            if 'O' in (row1[0]) and 'O' in (row2[0]) and 'O' in (row3[0]) \
                    or ('O' in row1[0] and 'O' in row1[1] and 'O' in row1[2]) \
                    or ('O' in row1[0] and 'O' in row2[1] and 'O' in row3[2]) \
                    or ('O' in row3[2] and 'O' in row2[2] and 'O' in row1[2]) \
                    or ('O' in row3[0] and 'O' in row3[1] and 'O' in row3[2]) \
                    or ('O' in row3[0] and 'O' in row2[1] and 'O' in row1[2]):

                print('\n' 'Player "O" WINS!\n')
                firsts_turn = False
                game_on = False
                player_o = True
                print(f'\n{playing_board[0]}\n{playing_board[1]}\n{playing_board[2]}')
                if game_on == False:
                    break

            # CONDITION 2
            elif 'X' in (row1[0]) and 'X' in (row2[0]) and 'X' in (row3[0]) \
                    or ('X' in row1[0] and 'X' in row1[1] and 'X' in row1[2]) \
                    or ('X' in row1[0] and 'X' in row2[1] and 'X' in row3[2]) \
                    or ('X' in row3[2] and 'X' in row2[2] and 'X' in row1[2]) \
                    or ('X' in row3[0] and 'X' in row3[1] and 'X' in row3[2]) \
                    or ('X' in row3[0] and 'X' in row2[1] and 'X' in row1[2]):

                print('\n' 'Player "X" WINS!\n')
                firsts_turn = False
                game_on = False
                player_x = True
                print(f'\n{playing_board[0]}\n{playing_board[1]}\n{playing_board[2]}')
                if game_on == False:
                    break
                # CONDITION TIE


            elif ' ' not in row1 and ' ' not in row2 and ' ' not in row3:
                if not player_x and not player_o:
                    firsts_turn = False
                    game_on = False
                return f'ITS A TIE!\n{row3}\n{row2}\n{row1}\n\nGAME ENDED!'
                # elif 'O' not in (row1[0]) and 'O' not in (row2[0]) and 'O' not in (row3[0]) \
                #         or ('O' not in row1[0] and 'O' not in row1[1] and 'O' not in row1[2]) \
                #         or ('O' not in row1[0] and 'O' not in row2[1] and 'O' not in row3[2]) \
                #         or ('O' not in row3[2] and 'O' not in row2[2] and 'O' not in row1[2]) \
                #         or ('O' not in row3[0] and 'O' not in row3[1] and 'O' not in row3[2]) \
                #         or ('O' not in row3[0] and 'O' not in row2[1] and 'O' not in row1[2]) \
                #         and 'X' not in (row1[0]) and 'X' not in (row2[0]) and 'X' not in (row3[0]) \
                #         or ('X' not in row1[0] and 'X' not in row1[1] and 'X' not in row1[2]) \
                #         or ('X' not in row1[0] and 'X' not in row2[1] and 'X' not in row3[2]) \
                #         or ('X' not in row3[2] and 'X' not in row2[2] and 'X' not in row1[2]) \
                #         or ('X' not in row3[0] and 'X' not in row3[1] and 'X' not in row3[2]) \
                #         or ('X' not in row3[0] and 'X' not in row2[1] and 'X' not in row1[2]):
                #
                #     tie = True
                #
                #     print('ITS A TIE!')
                #     print(f'\n{playing_board[0]}\n{playing_board[1]}\n{playing_board[2]}')
                # elif row1[0] == ' ' and row1[1] == ' ' and row1[2] == ' ' and row2[0] == ' ' and row2[] == ' '

            # ACTUAL GAME LOGIC!
            row_placement = input(f'Which row would you like to place your Character?'
                                  f' \n Row3{row3}\n Row2{row2}\n Row1{row1} \nPlayer Input(1, 2, 3): ')
            current_player = input("Whos is the current player, 'X' or 'O'?")
            if not row_placement in ['1', '2', '3']:
                return 'No such row exists!'
            # Placing an X for player 'X' in ROW 1
            elif row_placement == '1':
                index_placement = input(f'Where would you like to place your symbol?(1, 2, 3)\n{row1}:')
                # Placing an 'X' in index position 1-3 at row 1:
                # Validates that a charcter exists in there
                if index_placement == '1' and current_player == 'X' or current_player == 'x':
                    row1[0] = 'X'

                elif index_placement == '1' and current_player == 'O' or current_player == 'o':
                    row1[0] = 'O'

                elif index_placement == '2' and current_player == 'X' or current_player == 'x':
                    row1[1] = 'X'
                if index_placement == '2' and current_player == 'O' or current_player == 'o':
                    row1[1] = 'O'


                elif index_placement == '3' and current_player == 'X' or current_player == 'x':
                    row1[2] = 'X'
                if index_placement == '3' and current_player == 'O' or current_player == 'o':
                    row1[2] = 'O'
                # else:
                #     return "Can't Place Character Please Try Again!"
            # Placing an X for player 'X' in ROW 2
            elif row_placement == '2':
                index_placement = input(f'Where would you like to place your symbol?(1, 2, 3)\n{row2}:')
                # Placing an 'X' in index position 1-3 at row 2:
                if index_placement == '1' and current_player == 'X' or current_player == 'x':
                    row2[0] = 'X'
                if index_placement == '1' and current_player == 'O' or current_player == 'o':
                    row2[0] = 'O'
                # print(row3,'\n',row2,'\n',row1)
                elif index_placement == '2' and current_player == 'X' or current_player == 'x':
                    row2[1] = 'X'
                if index_placement == '2' and current_player == 'O' or current_player == 'o':
                    row2[1] = 'O'

                elif index_placement == '3' and current_player == 'X' or current_player == 'x':
                    row2[2] = 'X'
                if index_placement == '3' and current_player == 'O' or current_player == 'o':
                    row2[2] = 'O'
            # Placing an X for player 'X' in ROW 3
            elif row_placement == '3':
                index_placement = input(f'Where would you like to place your symbol?(1, 2, 3)\n{row3}:')
                # Placing an 'X' in index position 1-3 at row 3
                if index_placement == '1' and current_player == 'X' or current_player == 'x':
                    row3[0] = 'X'
                if index_placement == '1' and current_player == 'O' or current_player == 'o':
                    row3[0] = 'O'
                # print(row3,'\n',row2,'\n',row1)
                elif index_placement == '2' and current_player == 'X' or current_player == 'x':
                    row3[1] = 'X'
                if index_placement == '2' and current_player == 'O' or current_player == 'o':
                    row3[1] = 'O'

                elif index_placement == '3' and current_player == 'X' or current_player == 'x':
                    row3[2] = 'X'
                if index_placement == '3' and current_player == 'O' or current_player == 'o':
                    row3[2] = 'O'


print(playable_board())
