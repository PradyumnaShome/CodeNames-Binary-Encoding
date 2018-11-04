from schemas import board, player

BOARD_SIZE = 8

if __name__ == "__main__":
    my_board = board.Board.generate_random_board(BOARD_SIZE)
    print(my_board)

    number = my_board.board_to_number(player.Player.Red)
    print(f"Board to number: {number}\n\n")

    new_board = board.Board.number_to_board(player.Player.Red, number, BOARD_SIZE)
    print(f"{new_board}")
