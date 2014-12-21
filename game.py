from Tkinter import *
import time
import turtle
tk = Tk()

canvas = Canvas(width=1000, height=800, bg='grey')
canvas.pack()
tk.title('game')

def start_game():		
	stick_man_R()
	

def stick_man_R():
	R1 = PhotoImage(file = 'figure_R1.gif')
	R2 = PhotoImage(file = 'figure_R2.gif')
	canvas.create_image(0, 100, image = R1, anchor=NW)

start_game()

mainloop()