from Tkinter import *


tk = Tk()

canvas = Canvas(width=1000, height=800, bg='grey')
canvas.pack()
tk.title('game')

def Key_Press_R(evt):
    s1 = canvas.itencget(1,'state')
    s2 = canvas.itemcget(2,'state')

    pre,cur = None,None
    if s1 == 'normal':
        pre,cur = 1,2
    else:
        pre,cur = 2,1

    canvas.itemconfig(pre, state = 'hidden')
    canvas.itemconfig(cur, state = 'normal')
    canvas.move(cur, 5,0 )





def create_images():
    rs = []
    for i in range(1,3):
        state = 'normal' if i==1 else 'hidden'
        img = PhotoImage( file = 'figure_R%s.gif'%i)
        img_id = canvas.create_image(0, 768, image=img, anchor=NW, state=state)
        rs.append(img_id)
    return rs
    

 
canvas.bind_all("<KeyPress-Right>", Key_Press_R)




images = create_images()






