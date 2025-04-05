import tkinter as tk
from tkinter import messagebox

# Game logic functions
def if_game_over(red, blue):
    return red == 0 or blue == 0

def evaluate(red, blue):
    return 2 * red + 3 * blue

def best_move(red, blue):
    best_val = float('-inf')
    best = None
    for count in [1, 2]:
        for color in ['red', 'blue']:
            r, b = red, blue
            if color == 'red' and red >= count:
                r -= count
            elif color == 'blue' and blue >= count:
                b -= count
            else:
                continue
            val = evaluate(r, b)
            if val > best_val:
                best_val = val
                best = (count, color)
    return best

# Main game class
class RedBlueNimGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Red-Blue Nim Game")
        self.root.geometry("400x300")

        self.red = 5
        self.blue = 5
        self.turn = 'Human'  # Alternate with 'Computer'

        self.status = tk.StringVar()
        self.status.set("Your turn. Choose a move.")

        self.create_widgets()
        self.update_labels()

    def create_widgets(self):
        tk.Label(self.root, text="Red Marbles:").grid(row=0, column=0)
        self.red_label = tk.Label(self.root, text="0")
        self.red_label.grid(row=0, column=1)

        tk.Label(self.root, text="Blue Marbles:").grid(row=1, column=0)
        self.blue_label = tk.Label(self.root, text="0")
        self.blue_label.grid(row=1, column=1)

        tk.Label(self.root, text="Remove Marble(s):").grid(row=2, column=0)
        self.count_var = tk.StringVar(self.root)
        self.count_var.set("1")
        tk.OptionMenu(self.root, self.count_var, "1", "2").grid(row=2, column=1)

        tk.Label(self.root, text="Color:").grid(row=3, column=0)
        self.color_var = tk.StringVar(self.root)
        self.color_var.set("red")
        tk.OptionMenu(self.root, self.color_var, "red", "blue").grid(row=3, column=1)

        tk.Button(self.root, text="Make Move", command=self.player_move).grid(row=4, column=0, columnspan=2, pady=10)

        self.status_label = tk.Label(self.root, textvariable=self.status, fg="blue")
        self.status_label.grid(row=5, column=0, columnspan=2)

    def update_labels(self):
        self.red_label.config(text=str(self.red))
        self.blue_label.config(text=str(self.blue))

    def player_move(self):
        if self.turn != 'Human':
            return

        try:
            count = int(self.count_var.get())
            color = self.color_var.get()
            if color == 'red' and self.red >= count:
                self.red -= count
            elif color == 'blue' and self.blue >= count:
                self.blue -= count
            else:
                messagebox.showerror("Invalid Move", "Not enough marbles of selected color.")
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Enter a valid number.")
            return

        self.update_labels()
        self.check_game_over('Human')
        self.turn = 'Computer'
        self.root.after(1000, self.computer_move)

    def computer_move(self):
        if self.turn != 'Computer':
            return

        move = best_move(self.red, self.blue)
        if move is None:
            messagebox.showinfo("Game Over", "Computer has no valid moves. You win!")
            self.root.quit()
            return

        count, color = move
        if color == 'red':
            self.red -= count
        else:
            self.blue -= count

        self.status.set(f"Computer removes {count} {color} marble(s). Your turn.")
        self.update_labels()
        self.check_game_over('Computer')
        self.turn = 'Human'

    def check_game_over(self, last_player):
        if if_game_over(self.red, self.blue):
            winner = 'You' if last_player == 'Human' else 'Computer'
            messagebox.showinfo("Game Over", f"{winner} win(s)!")
            self.root.quit()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = RedBlueNimGame(root)
    root.mainloop()