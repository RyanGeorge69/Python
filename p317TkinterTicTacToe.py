import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.turn = 1
        self.board = ["-" for _ in range(9)]
        self.buttons = []

        self.status_label = tk.Label(self.root, text="Player O's turn", font=("Arial", 16))
        self.status_label.grid(row=0, column=0, columnspan=3)

        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 24), width=6, height=2,
                            command=lambda i=i: self.click(i))
            btn.grid(row=(i//3)+1, column=i%3)
            self.buttons.append(btn)

    def click(self, index):
        if self.board[index] != "-" or self.turn > 9:
            return

        player = "O" if self.turn % 2 != 0 else "X"
        color = "blue" if player == "O" else "red"

        self.board[index] = player
        self.buttons[index].config(text=player, fg=color)

        if self.check_winner(player):
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            self.turn = 10
            return

        self.turn += 1
        if self.turn == 10:
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            next_player = "O" if self.turn % 2 != 0 else "X"
            self.status_label.config(text=f"Player {next_player}'s turn")

    def check_winner(self, player):
        b = self.board
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for pattern in win_patterns:
            if b[pattern[0]] == b[pattern[1]] == b[pattern[2]] == player:
                for i in pattern:
                    self.buttons[i].config(bg="lightgreen")
                return True
        return False


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
