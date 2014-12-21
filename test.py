from Tkinter import *
import time
import turtle
from IPython import embed

tk = Tk()



canvas = Canvas(width=1000, height=800, bg='grey')
canvas.pack()
tk.title('game')

keypress_counter = 0

def get_pre_image(x):
	return 2-(x%2)

def get_cur_image(x):
	return 2-((get_pre_image(x)+1)%2)

def on_keypress_right(evt):
	global keypress_counter
	keypress_counter = keypress_counter + 1
	pre = get_pre_image(keypress_counter)
	cur = get_cur_image(keypress_counter)	
	
	canvas.itemconfig(pre, state='hidden')
	canvas.itemconfig(cur, state='normal')
	canvas.move(cur, 10,0)
	
	#print '...'


def create_images():
	R1 = PhotoImage(file = 'figure_R1.gif')
	canvas.create_image(0, 768, image = R1, anchor=NW)

	R2 = PhotoImage(file = 'figure_R2.gif')
	canvas.create_image(0, 768, image = R2, anchor=NW, state='hidden')
	return {
		1: R1,
		2: R2,
	}



#-- init keypress
canvas.bind_all('<KeyPress-Right>', on_keypress_right)


images = create_images()

mainloop()

