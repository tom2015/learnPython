from Tkinter import *
import time
from IPython import embed

tk = Tk()

c = Canvas(width=800, height=800)
c.pack()
tk.title('game')

Step, Num = 5,7


def on_keypress_right(evt):
    #distance--------------------------
    d = Num*Step
    
    #Run0------------------------------
    c.itemconfig(1,state='hidden')  # hide first image
    
    #move------------------------------
    c.move(1,-d,0)
        
    for i in range(1,Num*2,2):          # skip first image, processing others.    
        c.move(i+1,-(Step*i),0)        # i+1 => second image idx
        c.itemconfig(i+1, state='normal')
        c.update_idletasks()
        time.sleep(0.25)
        c.itemconfig(i+1, state='hidden')
        c.move(i+1,-(d-Step*i) , 0 )
    c.itemconfig(1,state='normal')  # show first image



def on_keypress_left(evt):
    #distance--------------------------
    d = Num*Step
    
    #Run0------------------------------
    c.itemconfig(1,state='hidden')  # hide first image
    
    #move------------------------------
    c.move(1,-d,0)
        
    for i in range(1,Num):          # skip first image, processing others.    
        c.move(i+1,-(Step*i),0)        # i+1 => second image idx
        c.itemconfig(i+1, state='normal')
        c.update_idletasks()
        time.sleep(0.25)
        c.itemconfig(i+1, state='hidden')
        c.move(i+1,-(d-Step*i) , 0 )
    c.itemconfig(1,state='normal')  # show first image

 
    

def create_my_images():
    rs = []
    for i in range(Num):
        img = PhotoImage(file = 'figure_Rrun%s.gif'%(i))
        rs.append(img)
        c.create_image(80,80, image=img, anchor=NW, state='hidden')
        img2 = PhotoImage(file = 'figure_Lrun%s.gif'%(i))
        rs.append(img2)
        c.create_image(80,80, image=img2, anchor=NW, state='hidden')       
        c.itemconfig(1,state='normal')    
    return rs









c.bind_all('<KeyPress-Right>', on_keypress_right)
c.bind_all('<KeyPress-Left>', on_keypress_left)





images = create_my_images()
mainloop()

