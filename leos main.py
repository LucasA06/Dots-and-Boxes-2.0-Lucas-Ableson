import tkinter as tk
from tkinter import *
import random

window = Tk()
window.title("Line Game")
window.geometry('500x500')

canvas_width = 500
canvas_height = 500

c = Canvas(window, width = canvas_width, height = canvas_height, bg='white')
c.pack()

dot_size = 16
dot_spacing = 100
line_thickness = 12 

player_first = True
win_condition = 6

player_max_count = 0
computer_max_count =0


def player_wins():
    print('Player wins!')

def computer_wins():
    print('Game Over. You lose.')


def line_click(event):
    line_id = event.widget.find_closest(event.x, event.y)[0]
    color = c.itemcget(line_id, 'fill')
    if color == 'white':
        c.itemconfig(line_id, fill='crimson')
        computer_turn()


def computer_turn():
    white_lines = [line for line in lines if c.itemcget(line, 'fill') == 'white']
    if white_lines:
        line_id = random.choice(white_lines)
        c.itemconfig(line_id, fill='lightseagreen')  
    

start_x = (canvas_width - (3 * dot_spacing + 4 * dot_size)) // 2
start_y = (canvas_height - (3 * dot_spacing + 4 * dot_size)) // 2

lines = []
for row in range(4):
    for col in range(3):
        x = start_x + col * (dot_size + dot_spacing) + dot_size // 2
        y = start_y + row * (dot_size + dot_spacing) + dot_size // 2
        line=c.create_line(x, y, x + dot_spacing + dot_size, y, fill = "white", width = line_thickness)
        lines.append(line)
        c.tag_bind(line, '<Button-1>', line_click)

for row in range(3):
    for col in range(4):
        x = start_x + col * (dot_size + dot_spacing) + dot_size // 2
        y = start_y + row * (dot_size + dot_spacing) + dot_size // 2
        line=c.create_line(x, y, x, y + dot_spacing + dot_size, fill = "white", width = line_thickness)
        lines.append(line)
        c.tag_bind(line, '<Button-1>', line_click)
        
dots = []
for row in range(4):
    for col in range(4):
        x = start_x + col * (dot_size + dot_spacing)
        y = start_y + row * (dot_size + dot_spacing)
        c.create_oval(x, y, x + dot_size, y + dot_size, fill="black")


c.bind('<Button-1>', line_click)

if player_first == False:
    computer_turn()

window.mainloop()