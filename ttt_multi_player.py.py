class TicTacToe:
    # initialising the basic attributes
    # initially winner is None and game_running set to True to run the while loop until a win or tie occur.
    def __init__(self) -> None:
        self.board = ["-"] * 9
        self.current_player = "X"
        self.winner = None
        self.game_running = True
    
    def print_board(self):
        for i in range(0,9,3):
            print(" | ".join(self.board[i:i+3]))
            if i < 6:
                print("---------")

    def player_input(self):
        while True:
            try:
                self.position = int(input("enter the position, 1 to 9: "))
                if self.position > 0 and self.position <= 9 and self.board[self.position-1] == "-":
                    self.board[self.position-1] = self.current_player
                    break
                else:
                    print("Oops!! invalid selection. Enter a valid position between 1 and 9")
            except ValueError:
                print("invalid input. Enter a valid position between 1 and 9")    

    def row_check(self):
        valid_combinations = [[0,1,2], [3,4,5], [6,7,8]]
        for combo in valid_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "-":
                self.winner = self.board[combo[0]]
                return True       
    def column_check(self):
        valid_combinations = [[0,3,6], [1,4,7], [2,5,8]]
        for combo in valid_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "-":
                self.winner = self.board[combo[0]]
                return True
    
    def diagonal_check(self):
        valid_combinations = [[0,4,8], [2,4,6]]
        for combo in valid_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "-":
                self.winner = self.board[combo[0]]
                return True

    def tie_check(self):
        if "-" not in self.board:
            return True
        
    def win_check(self):
        if self.diagonal_check() or self.row_check() or self.column_check():
            return True

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "0"
            print("its 'O' turn")
        else:
            self.current_player = "X"
            print("its 'X' turn")    



game = TicTacToe()
game.print_board()
while game.game_running:
    game.player_input()
    game.print_board()
    if game.win_check():
        print(f"the winner is {game.winner}")
        game.game_running = False
    elif game.tie_check():
        print("its a tie!!")
        game.game_running = False
    else:
        game.switch_player()

