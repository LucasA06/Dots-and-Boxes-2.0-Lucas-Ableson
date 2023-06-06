from tkinter import *
import sys
import os
from tkVideoPlayer import TkinterVideo

win = Tk()
win.geometry("610x610")
win.title('Make the Longest Line!!')

dots = []
lines = []

videoplayer = TkinterVideo(master=win, scaled=True)
videoplayer.load(r"lines.mp4")
videoplayer.pack(expand=True, fill="both")
videoplayer.play()

def loop_video():
    videoplayer.play()
    win.after(100, loop_video)

win.after(100, loop_video)

grid_size = 4
grid_range = 3
grid_range2 = 4
line_width = 12
dot_radius = 7
grid_gap = 100

def create_game_window():
    game_win = Toplevel(win)
    game_win.geometry("650x650")
    game_win.title('Make the Longest Line!!')

    c = Canvas(game_win, width=500, height=500, bg="white")
    c.pack()

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
    welcome_label = Label(game_win, text="Click a gap between dots to start the game!!", fg='black',font= (20))
    welcome_label.pack()
    player_label = Label(game_win, text="You are Green", fg="seagreen")
    player_label.pack()
    computer_label = Label(game_win, text="Computer is Red", fg="firebrick")
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
                line = c.create_line(x, y, x, y + grid_gap, width=line_width, fill='white')
                lines.append(line)

        for i in range(grid_size):
            for j in range(grid_size):
                x = 100 + i * grid_gap
                y = 100 + j * grid_gap
                dot = c.create_oval(x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius, fill='black')
                dots.append(dot)

    def main_menu():
        game_win.destroy()
        win.deiconify()

    reset_button = Button(game_win, text="Reset", command=reset_canvas, fg='gold', bg='black')
    reset_button.pack()
    main_menu = Button(game_win, text='Main Menu', command= main_menu, fg='gold', bg='black')
    main_menu.pack()

    c.bind('<Button-1>', click_line)
    game_win.mainloop()

def create_game_window2():
    game_win = Toplevel(win)
    game_win.geometry("610x610")
    game_win.title('Make the Longest Line!!')

    c = Canvas(game_win, width=500, height=500, bg="white")
    c.pack()

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

    welcome_label = Label(game_win, text="Click a gap between dots to start the game!!", fg='black', font=(20))
    welcome_label.pack()
    player1_label = Label(game_win, text="Click to start", fg="black")
    player1_label.pack()

    current_player = 1

    def click_line(event):
        nonlocal current_player
        item = event.widget.find_closest(event.x, event.y)[0]
        color = c.itemcget(item, 'fill')

        if color == 'white':
            if current_player == 1:
                c.itemconfigure(item, fill='firebrick')
                player1_label.config(text="Player 2's Turn (Green)",fg='seagreen')
                current_player = 2
            else:
                c.itemconfigure(item, fill='seagreen')
                player1_label.config(text="Player 1's Turn (Red)",fg='firebrick')
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
                line = c.create_line(x, y, x, y + grid_gap, width=line_width, fill='white')
                lines.append(line)

        for i in range(grid_size):
            for j in range(grid_size):
                x = 100 + i * grid_gap
                y = 100 + j * grid_gap
                dot = c.create_oval(x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius, fill='black')
                dots.append(dot)

    def main_menu():
        game_win.destroy()
        win.deiconify()

    reset_button = Button(game_win, text="Reset", command=reset_canvas, fg='gold', bg='black')
    reset_button.pack()
    main_menu = Button(game_win, text='Main Menu', command= main_menu, fg='gold', bg='black')
    main_menu.pack()

    c.bind('<Button-1>', click_line)
    game_win.mainloop()


def start_game_computer():
    win.withdraw()  # Hide the main window
    create_game_window()

def start_game_two_players():
    win.withdraw()  # Hide the main window
    create_game_window2()

def font_style():
    return ("Helvetica bold", 30)

welcome = Label(win, text="Welcome to Longest Line!!", fg='black', font=font_style())
welcome.place(x=80, y=150)
one_player_button = Button(win, text="Play Against Computer", command=start_game_computer, fg='black', bg='firebrick', font=(20), width=20)
one_player_button.place(x=200, y=380)
two_player_button = Button(win, text="Play Against Friend", command=start_game_two_players, fg='black', bg='seagreen', font=(20), width=20)
two_player_button.place(x=200, y=300)

win.mainloop()
