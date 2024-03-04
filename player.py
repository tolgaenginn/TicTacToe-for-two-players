
class Player:
    def __init__(self, num):
        self.sign = 'X' if num == 1 else 'O'

    def play(self, board):
        print("Where would you like to place your mark?")

        valid_played = False
        while not valid_played:
            try:
                row = int(input("Row: "))-1
                col = int(input("Column: "))-1
                if board[row][col] == None:
                    board[row][col] = self.sign
                    valid_played = True
                else:
                    print("it is already full")
            except(ValueError, IndexError):
                print("Invalid input")

    def __str__(self):
        return f"Player {self.sign}"


