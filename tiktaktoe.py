
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
root.geometry("500x600")
root.configure(bg="#222831")



turn = True
count = 0


# Disable all buttons
def DAB():
    for b in buttons:
        b.config(state=DISABLED)

# Function that adds X and O while clicking
def clicked(b):
    global turn, count
    if b["text"] == " " and turn:
        b["text"] = "X"
        b.config(fg="#00adb5")
        turn = False
        count += 1
        whowon()
    elif b["text"] == " " and not turn:
        b["text"] = "O"
        b.config(fg="#ff5722")
        turn = True
        count += 1
        whowon()
#who won
# Game end logic and winner check
winner = False

def whowon():
    global winner, count
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # cols
        (0, 4, 8), (2, 4, 6) # diagonals
    ]
    for a, b, c in win_combos:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != " ":
            winner = True
            for i in (a, b, c):
                buttons[i].config(bg="#393e46")
            DAB()
            messagebox.showinfo("Game Over", f"Player {buttons[a]['text']} wins!")
            replay_btn.config(state=NORMAL)
            return
    if count == 9 and not winner:
        DAB()
        messagebox.showinfo("Game Over", "It's a Draw!")
        replay_btn.config(state=NORMAL)

# UI Frame for title and replay
title_lbl = Label(root, text="Tic Tac Toe", font=("Arial", 24, "bold"), bg="#222831", fg="#00adb5")
title_lbl.pack(pady=20)

board_frame = Frame(root, bg="#222831")
board_frame.pack(pady=10)

# Create buttons in a grid
buttons = []
for r in range(3):
    for c in range(3):
        btn = Button(
            board_frame,
            text=" ",
            font=("Arial", 32, "bold"),
            bg="#eeeeee",
            fg="#222831",
            width=4,
            height=2,
            relief=RIDGE,
            bd=4,
            command=lambda b=len(buttons): clicked(buttons[b])
        )
        btn.grid(row=r, column=c, padx=8, pady=8)
        buttons.append(btn)

# Replay button
def replay():
    global turn, count, winner
    for b in buttons:
        b.config(text=" ", state=NORMAL, bg="#eeeeee", fg="#222831")
    turn = True
    count = 0
    winner = False
    replay_btn.config(state=DISABLED)

replay_btn = Button(root, text="Replay", font=("Arial", 16, "bold"), bg="#00adb5", fg="#222831", command=replay, state=DISABLED)
replay_btn.pack(pady=20)

root.mainloop()