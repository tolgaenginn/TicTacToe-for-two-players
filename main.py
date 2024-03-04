from player import Player

class Field:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def __str__(self):
        # Create a visual representation of the board
        board_str = "  1 2 3\n"  # Column numbers
        for i, row in enumerate(self.board):
            row_str = f"{i+1} "  # Row number
            for cell in row:
                if cell is None:
                    row_str += ". "  # Empty cell
                else:
                    row_str += f"{cell} "  # X or O
            board_str += row_str + "\n"
        return board_str

def triple(matrix, players):
    # for each player
    for player in players:
        # check each row
        for row in matrix:
            if all(row[i] == player.sign for i in range(len(row))):
                return True, player
        # check each column
        for col in range(3):
            if all(matrix[row][col] == player.sign for row in range(3)):
                return True, player
        #check each diagonal
        if all(matrix[i][i] == player.sign for i in range(3)) or \
                all(matrix[i][2-i] == player.sign for i in range(3)):
            return True, player

    #if none is correct there is no triple present
    return False, None

if __name__ == '__main__':
    field = Field()
    players = [Player(1), Player(2)]

    game_over = False
    turn = 0
    print(field)
    while not game_over and any(None in row for row in field.board):
        curr_player = players[(turn % 2)]
        curr_player.play(field.board)
        print(field)
        game_over, winner = triple(field.board, players)
        turn += 1

    if game_over:
        print(f'{winner} won the game')
    else:
        print("It's a tie")









