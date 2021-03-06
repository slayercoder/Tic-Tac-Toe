from utils.display_board import display_board
from utils.first_chance import first_chance
from utils.make_move import make_move
from utils.check_win import check_win

def run_game(player1_choice, player2_choice):
    board_data = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    match_status = ''
    current_player = first_chance()
    current_player_choice = player1_choice if current_player == 'Player 1' else player2_choice
    positions_filled = 0
    display_board(board_data)
    while True:
        current_player_choice = make_move(current_player, board_data, current_player_choice)
        positions_filled += 1
        display_board(board_data)
        # after this, check if the user has won, if yes break out and print result else continue        
        if check_win(board_data, current_player_choice):
            match_status = 'won by {}'.format(current_player)
            break
        elif not check_win(board_data, current_player_choice) and positions_filled == 9:
            match_status = 'Drawn !!'
            break
        else:
            # toggle player
            current_player = "Player 2" if current_player == 'Player 1' else "Player 1"
            current_player_choice = player1_choice if current_player == 'Player 1' else player2_choice
            continue
    if match_status:
        return match_status