from tkinter import *
import random

win = Tk()
win.geometry("1960x1080")
win.config(bg='white')
win.title('Make the Longest Line!!')

c = Canvas(win, width=800, height=800, bg="white")
c.pack()

dots = []
lines = []

grid_size = 7
grid_range = 6
grid_range2 = 7
line_width = 12
dot_radius = 7
grid_gap = 100

for i in range(grid_range):
    for j in range(grid_range2):
        x = 100 + i * grid_gap
        y = 100 + j * grid_gap
        line = c.create_line(x, y, x + grid_gap, y, width=line_width, fill='white')
        lines.append(line)
for j in range(grid_range):
    for i in range(grid_range2):
        x = 100 + i * grid_gap
        y = 100 + j * grid_gap
        line = c.create_line(x, y, x, y + grid_gap, width=line_width, fill='white')
        lines.append(line)

for i in range(grid_size):
    for j in range(grid_size):
        x = 100 + i * grid_gap
        y = 100 + j * grid_gap
        dot = c.create_oval(x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius, fill='black')
        dots.append(dot)

# Player labels
welcome_label = Label(win, text="Click a gap between dots to start the game!!", fg='black', bg='white', font=(20))
welcome_label.pack()
player1_label = Label(win, text="Player 1 is Green", fg="seagreen", bg='white')
player1_label.pack()
player2_label = Label(win, text="Player 2 is Red", fg="firebrick", bg='white')
player2_label.pack()

# Variable to track current player
current_player = 1

def player_move(event):
    global current_player

    item = event.widget.find_closest(event.x, event.y)[0]
    color = c.itemcget(item, 'fill')
    if color == 'white':
        if current_player == 1:
            c.itemconfigure(item, fill='seagreen')
            player1_label.config(fg='black')
            player2_label.config(fg='firebrick')
            current_player = 2
        else:
            c.itemconfigure(item, fill='firebrick')
            player1_label.config(fg='seagreen')
            player2_label.config(fg='black')
            current_player = 1


def reset_canvas():
    c.delete("all")
    for i in range(grid_range):
        for j in range(grid_range2):
            x = 100 + i * grid_gap
            y = 100 + j * grid_gap
            line = c.create_line(x, y, x + grid_gap, y, width=line_width, fill='white')
            lines.append(line)
    for j in range(grid_range):
        for i in range(grid_range2):
            x = 100 + i * grid_gap
            y = 100 + j * grid_gap
            line = c.create_line(x, y, x , y+ grid_gap, width=line_width, fill='white')
            lines.append(line)

    for i in range(grid_size):
        for j in range(grid_size):
            x = 100 + i * grid_gap
            y = 100 + j * grid_gap
            dot = c.create_oval(x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius, fill='black')
            dots.append(dot)

reset_button = Button(win, text="Click To Reset", command=reset_canvas, fg='gold',bg='black')
reset_button.pack()

c.bind('<Button-1>', player_move)

win.mainloop()
