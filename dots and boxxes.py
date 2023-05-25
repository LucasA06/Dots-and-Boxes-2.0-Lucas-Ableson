from tkinter import *
import random

win = Tk()
win.geometry("610x610")
win.title('Make the Longest Line!!')

c = Canvas(win, width=500, height=500, bg="white")
c.pack()

dots = []
lines = []

grid_size = 4
grid_range = 3
grid_range2 = 4
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
        line = c.create_line(x, y, x , y+ grid_gap, width=line_width, fill='white')
        lines.append(line)

for i in range(grid_size):
    for j in range(grid_size):
        x = 100 + i * grid_gap
        y = 100 + j * grid_gap
        dot = c.create_oval(x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius, fill='black')
        dots.append(dot)

# Player and computer labels
welcome_label = Label(win, text="Click a gap between dots to start the game!!", fg='black',bg='white',font= (20))
welcome_label.pack()
player_label = Label(win, text="You are Green", fg="seagreen", bg='white')
player_label.pack()
computer_label = Label(win, text="Computer is Red", fg="firebrick",bg='white')
computer_label.pack()


def find_connected_lines(item, color, visited):
    connected = [item]
    queue = [item]

    while queue:
        current = queue.pop(0)
        neighbors = c.find_overlapping(*c.coords(current))

        for neighbor in neighbors:
            if neighbor in lines and neighbor not in visited and c.itemcget(neighbor, 'fill') == color:
                connected.append(neighbor)
                visited.add(neighbor)
                queue.append(neighbor)

    return connected

def computer_move():
    white_lines = [line for line in lines if c.itemcget(line, 'fill') == 'white']
    if white_lines:
        max_length = 0
        best_line = None

        for line in white_lines:
            visited = set()
            connected_lines = find_connected_lines(line, 'seagreen', visited)
            length = len(connected_lines)

            if length > max_length:
                max_length = length
                best_line = line

        if best_line:
            c.itemconfigure(best_line, fill='firebrick')

def click_line(event):
    item = event.widget.find_closest(event.x, event.y)[0]
    color = c.itemcget(item, 'fill')
    if color == 'white':
        c.itemconfigure(item, fill='seagreen')
        computer_move()

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

c.bind('<Button-1>', click_line)
win.mainloop()