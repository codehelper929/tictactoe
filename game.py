import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text=" ", font=('Arial', 40), width=5, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.status_label = tk.Label(self.root, text="Player X's turn", font=('Arial', 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"Player {winner} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None

    def is_board_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
        self.status_label.config(text="Player X's turn")

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.root.mainloop()