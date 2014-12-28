from Tkinter import *
import random
import time

from IPython import embed


tk = Tk()
c = Canvas(tk, width=500, height=400)
c.pack()
tk.update()


class Ball:
    def __init__(self, canvas, color):
        self.c = c
        self.id = c.create_oval(0,0,15,15, fill=color)
        self.c.move(self.id, 0,400)
        #starts = [-3, -3, -1, 1, 2, 3]
        #random.shuffle(starts)

        self.dx = 2
        self.dy = 0 

        self.canvas_width = self.c.winfo_width()
        self.canvas_height = self.c.winfo_height()

    def draw(self):
        x,y = self.c.coords(self.id)[:2]
        self.dy = 1./50*(x-200)*self.dx
        
        #print x,y
        if y>420:
            self.dy = 1./50*(x-200)*self.dx

        self.c.move(self.id,self.dx,self.dy)



ball = Ball(c,'red')



while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)