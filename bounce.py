from Tkinter import *
import random
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [10, -3, -5, 9, 4, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        #self.score = 0


    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if self.hit_paddle(pos) == True:
            self.y = -3
            #self.score +=1
            #print self.score

        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if (pos[0] <= 0) or (pos[2] >= self.canvas_width):
            self.x = -self.x
        
    
    def my_hit(self):
        pos = self.canvas.coords(self.id)
        return self.hit_paddle(pos)
        

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            #if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
        return False

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        
    def turn_left(self, evt):
        self.x = -5
        
    def turn_right(self, evt):
        self.x = 5
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
     
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'red')



score = 0

while 1:    
    
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    else:
        print 'gameover'
        break
    
    if ball.my_hit():
        score = score+1
        print 'your score:%s '% score

    tk.update_idletasks()
    tk.update()
    time.sleep(0.02)
    
