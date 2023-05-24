from tkinter import *
import random

win = Tk()
win.geometry("500x500")
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

def computer_move():
    white_lines = [line for line in lines if c.itemcget(line, 'fill') == 'white']
    if white_lines:
        item = random.choice(white_lines)
        c.itemconfigure(item, fill='green')

def click_line(event):
    item = event.widget.find_closest(event.x, event.y)[0]
    color = c.itemcget(item, 'fill')
    if color == 'white':
        c.itemconfigure(item, fill='blue')
        computer_move()

c.bind('<Button-1>', click_line)
c.mainloop()
