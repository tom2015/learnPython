import time
from Tkinter import *

from IPython import embed

tk = Tk()

c = Canvas(width=800, height=800, bg='grey')
c.pack()
tk.title('game')

def on_key_press_right(evt):
    c.itemconfig(1, state='hidden')
    c.move(1, 15, 0)
    c.move(3, 10,0)
    c.move(2, 5,0)

    c.itemconfig(2, state='normal')
    c.update_idletasks() 
    time.sleep(0.25)

    c.itemconfig(2,state='hidden')
    c.move(2,10,0)

    c.itemconfig(3, state='normal')
    c.update_idletasks()
    
    time.sleep(0.25)
    c.itemconfig(3, state='hidden')
    c.move(3, 5,0)

    c.itemconfig(1,state='normal')


    #c.move(1,10,0)
    


c.bind_all('<KeyPress-Right>', on_key_press_right)

image = PhotoImage(file = 'figure_R1.gif')
c.create_image(80,80, image=image, anchor=NW, state='normal')

image2 = PhotoImage(file = 'figure_Rrun1.gif')
c.create_image(80,80, image=image2, anchor=NW, state='hidden')

image3 = PhotoImage(file = 'figure_Rrun2.gif')
c.create_image(80,80, image=image3, anchor=NW, state='hidden')




mainloop()


