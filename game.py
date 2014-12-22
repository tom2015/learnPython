from Tkinter import *
import time
import turtle
from IPython import embed

tk = Tk()



canvas = Canvas(width=1000, height=800, bg='grey')
canvas.pack()
tk.title('game')

s1 = canvas.itemcget(1,'state')
s2 = canvas.itemcget(2,'state')
pre,cur = None,None
canvas.itemconfig(pre, state = 'hidden')
canvas.itemconfig(cur, state = 'normal')

def on_keypress_right(evt):   

    #pre,cur = None,None
    if s1 == 'normal':
        pre,cur = 1,2
    else:
        pre,cur = 2,1
    #canvas.move(cur, 10, 0 )
    #canvas.itemconfig(pre, state = 'hidden')
    #canvas.move(cur, 10, 0 )
    #canvas.itemconfig(cur, state = 'normal')
    canvas.move(cur, 10, 0 )

def on_keypress_space(evt):
    if s1 == 'normal':
        pre,cur = 1,2
    else:
        pre,cur = 2,1
    canvas.move(cur, 10, -5)
    


def on_keypress_left(evt):
    if s1 == 'normal':
        pre,cur = 1,2
    else:
        pre,cur = 2,1
    canvas.move(cur, -10, 0)

        



def create_images():
	R1 = PhotoImage(file = 'figure_R1.gif')
	canvas.create_image(0, 768, image = R1, anchor=NW)

	R2 = PhotoImage(file = 'figure_R2.gif')
	canvas.create_image(0, 768, image = R2, anchor=NW, state='hidden')
	return {
		1: R1,
		2: R2,
	}




canvas.bind_all('<KeyPress-Right>', on_keypress_right)
canvas.bind_all('<KeyPress-space>', on_keypress_space)
canvas.bind_all('<KeyPress-Left>', on_keypress_left)


images = create_images()

mainloop()